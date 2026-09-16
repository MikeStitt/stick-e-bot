"""Talking to Onshape through the signed-in browser.

There is no API key here. Everything runs against a headed Chromium that the user
signed in to by hand, reached over the Chrome DevTools Protocol. REST calls are
issued with ``fetch`` *inside* the logged-in page so they are same-origin and carry
the session cookies, which is exactly how Onshape's own web client talks to ``/api``.

See ../browser-access.md and ../onshape-api.md for the background.
"""

from __future__ import annotations

import copy
import json
import re
import time
from dataclasses import dataclass

from playwright.sync_api import Page, sync_playwright

# The agent's own browser. 9222 is the browser a person signed in to and is sitting
# in front of, and it is reached by naming it, never by defaulting to it.
CDP_URL = "http://127.0.0.1:9223"
ONSHAPE = "https://cad.onshape.com"

# Sketch geometry is in meters; dialog values are expressions like "3 in".
IN = 0.0254
MM = 0.001

# The Front plane's geometryId. Verified; Top and Right were never checked.
FRONT_PLANE = "JCC"


class NotSignedIn(RuntimeError):
    pass


class RateLimited(RuntimeError):
    """Onshape said 429 and waiting is not the answer.

    Carries what the response said so the caller can decide rather than guess:
    ``retry_after`` in seconds, ``remaining`` from ``x-rate-limit-remaining``, and
    the ``path`` that was refused. ``retry_after`` is None when the response did
    not say, which is the tell for the burst block rather than a spent quota.
    """

    def __init__(self, message: str, *, path: str, retry_after=None, remaining=None):
        super().__init__(message)
        self.path = path
        self.retry_after = retry_after
        self.remaining = remaining


@dataclass
class Doc:
    """Where a Part Studio lives."""

    did: str
    wid: str
    eid: str

    @property
    def url(self) -> str:
        return f"{ONSHAPE}/documents/{self.did}/w/{self.wid}/e/{self.eid}"

    @property
    def path(self) -> str:
        return f"d/{self.did}/w/{self.wid}/e/{self.eid}"


def connect(playwright):
    """Attach to the already-running browser, on a CAD tab.

    Which tab matters: every REST call is a `fetch` from inside the page, so it is
    same-origin against whatever that page is. Grabbing the last tab blindly means a
    Learning Center tab or a docs tab silently becomes the API host, and the calls
    hang or 404 with nothing pointing at the cause.

    Which browser matters as much. This attaches to `CDP_URL`, which is 9223, the
    agent's browser. A caller that wants the signed-in browser on 9222 sets `CDP_URL`
    itself; nothing reaches a person's session by leaving a default alone.
    """
    browser = playwright.chromium.connect_over_cdp(CDP_URL)
    ctx = browser.contexts[0]
    for page in ctx.pages:
        if page.url.startswith(ONSHAPE):
            return browser, ctx, page
    page = ctx.new_page()
    page.goto(f"{ONSHAPE}/documents", wait_until="domcontentloaded")
    page.wait_for_timeout(4000)
    return browser, ctx, page


# Bounded on purpose. An unbounded backoff turns a rate limit into something
# indistinguishable from a hang, which is a worse failure than a clear error.
RATE_LIMIT_WAITS = (5, 15, 30, 60)


def limit_from(headers) -> tuple:
    """What a 429's headers say, as ``(retry_after_seconds, remaining)``.

    ``retry-after`` is the whole difference between the two kinds of 429. A burst of
    feature writes earns a block measured in seconds; a spent daily quota answers with
    a number in the tens of thousands that counts down against the clock, so no ladder
    of retries reaches the end of it. Either value may be absent.
    """
    got = {str(k).lower(): v for k, v in dict(headers or {}).items()}
    try:
        retry_after = float(got["retry-after"])
    except (KeyError, TypeError, ValueError):
        retry_after = None
    return retry_after, got.get("x-rate-limit-remaining")


# Longer than this and no build step can usefully wait it out, so the advice stops
# being "wait" and becomes "go a different way". It is a threshold on the advice, not
# a claim about which limiter answered.
CHANGE_THE_ROUTE_AFTER = 600.0


def rate_limit_message(path: str, retry_after, remaining, waited: float, now: float) -> str:
    """What to say about a 429, given what the response said. Pure; ``now`` is passed in."""
    head = f"Onshape is rate limiting {path}"
    if retry_after is None:
        return (
            f"{head} and did not say for how long, after waiting {waited:g}s.\n"
            "With no retry-after the length is unknown. Stop calling this endpoint "
            "entirely, do something else for a few minutes, then make one request — "
            "continued polling keeps the bucket empty."
        )
    back = time.strftime("%H:%M on %a %d %b", time.localtime(now + retry_after))
    scale = f"{retry_after / 3600:.1f} hours" if retry_after >= 3600 else f"{retry_after:g}s"
    said = f"{head} for another {scale}, until about {back} (x-rate-limit-remaining: {remaining})."
    if retry_after < CHANGE_THE_ROUTE_AFTER:
        return (
            f"{said}\nThat is longer than this client waits, having already waited "
            f"{waited:g}s of a {sum(RATE_LIMIT_WAITS)}s budget. Stop calling, leave it "
            "alone for that long, then make one request."
        )
    return (
        f"{said}\nNothing this client does shortens that: retry-after counts down "
        "against the clock rather than resetting when you stop asking.\n"
        "Change the route rather than the delay. The limit is per endpoint family, so "
        "with /features spent, bodydetails, parts, boundingboxes, assemblies and "
        "variables have each kept answering, and the GUI is not rate limited at all. "
        "See .claude/skills/onshape/SKILL.md, 'Read what a refusal says before waiting on it'."
    )


def api(page: Page, method: str, path: str, payload=None) -> dict:
    """One REST call, backing off only when backing off can work.

    Onshape's **429** has two modes and they take different answers. A burst of feature
    writes earns a block that clears in a minute or two of silence. A spent daily quota
    on one endpoint does not clear that day at all: on 2026-08-27 `.../features` answered
    `retry-after: 67201` beside `x-rate-limit-remaining: 0`. The response says which, so
    this reads it rather than assuming, and raises `RateLimited` the moment the server
    asks for longer than the ladder can wait. Both the limit and the quota are per
    endpoint family, so a raise here says nothing about the rest of the API.

    Left unhandled a 429 does not look like rate limiting at all — a delete quietly does
    nothing, a feature list comes back with no `features` key, and the next thing to
    touch the GUI fails somewhere unrelated.

    The rate to build at, rather than the rate to retry at, is the real fix: see
    `pace()`.
    """
    budget = float(sum(RATE_LIMIT_WAITS))
    waited = 0.0
    for wait in RATE_LIMIT_WAITS:
        res = _raw_api(page, method, path, payload)
        if res.get("status") != 429:
            return res
        retry_after, remaining = limit_from(res.get("headers"))
        pause = wait if retry_after is None else retry_after
        if waited + pause > budget:
            raise RateLimited(
                rate_limit_message(path, retry_after, remaining, waited, time.time()),
                path=path,
                retry_after=retry_after,
                remaining=remaining,
            )
        print(
            f"    rate limited on {path.rsplit('/', 1)[-1]}; waiting {pause:g}s",
            flush=True,
        )
        page.wait_for_timeout(int(pause * 1000))
        waited += pause
    res = _raw_api(page, method, path, payload)
    if res.get("status") == 429:
        retry_after, remaining = limit_from(res.get("headers"))
        raise RateLimited(
            rate_limit_message(path, retry_after, remaining, waited, time.time()),
            path=path,
            retry_after=retry_after,
            remaining=remaining,
        )
    return res


def pace(page: Page, ms: int = 350) -> None:
    """A breath between feature writes, so the 429 never arrives in the first place."""
    page.wait_for_timeout(ms)


def _raw_api(page: Page, method: str, path: str, payload=None) -> dict:
    """One REST call, made from inside the page.

    Cookie auth alone is read-only: writes come back 401 unless the XSRF-TOKEN
    cookie is echoed back as an X-XSRF-TOKEN header.

    The response headers come back with the body. They are what tells a burst block
    from a spent quota, and a client that drops them cannot tell the difference — see
    `api()`. The fetch is same-origin, so every header is readable.
    """
    return page.evaluate(
        """async ([method, path, payload]) => {
            const headers = {Accept: 'application/json;charset=UTF-8; qs=0.09'};
            if (payload !== null) headers['Content-Type'] = 'application/json';
            const xsrf = document.cookie.match(/(?:^|;\\s*)XSRF-TOKEN=([^;]+)/);
            if (xsrf) headers['X-XSRF-TOKEN'] = decodeURIComponent(xsrf[1]);
            const res = await fetch(path, {
                method, headers, credentials: 'include',
                body: payload === null ? undefined : JSON.stringify(payload),
            });
            const got = {};
            res.headers.forEach((v, k) => { got[k] = v; });
            const text = await res.text();
            let body;
            try { body = JSON.parse(text); } catch { body = text.slice(0, 800); }
            return {status: res.status, ok: res.ok, headers: got, body};
        }""",
        [method, path, payload],
    )


def require_signed_in(page: Page) -> str:
    """Return the signed-in user's name, or explain how to fix it.

    ``/api/users/sessioninfo`` answers 200 with a body when there is a session and
    204 with nothing when there is not, so an empty body is the tell.
    """
    if not page.url.startswith(ONSHAPE):
        page.goto(f"{ONSHAPE}/documents", wait_until="domcontentloaded")
        page.wait_for_timeout(4000)
    res = api(page, "GET", "/api/users/sessioninfo")
    body = res.get("body")
    if not isinstance(body, dict) or not body.get("id"):
        raise NotSignedIn(
            # Not CDP_URL: this takes a page, and browser.py hands it one from 9222.
            "No Onshape session in the browser this page came from.\n"
            "The agent's browser on 9223 borrows its session at launch and the borrow dies "
            "with the process, so restart `uv run python tools/agent_browser.py` to borrow "
            "again.\n"
            "If the signed-in browser on 9222 is the one logged out, run "
            "`uv run python tools/browser.py --signin`, which types the account email and "
            "lets Chrome's saved credential fill the password; if Chrome has nothing saved, "
            "sign in by hand once in that window so it can offer to save it.\n"
            "No password is ever handled by this tooling."
        )
    return body.get("name") or body["id"]


# --------------------------------------------------------------------------
# Feature JSON. The BTM* type numbers are not guessable; they were read back off
# features built in the GUI. See ../onshape-api.md.
# --------------------------------------------------------------------------


def feature_spec(page: Page, doc: Doc, feature_type: str) -> dict:
    """Every parameter a feature type takes, by id, with its enum's name.

    Read-only, and the answer to "what is this parameter called". Guessing costs a 400 with
    a body the CSP headers push out of view; `/featurespecs` says it outright. Two that a
    guess gets wrong: an extrude's starting offset is `startOffset` and `startOffsetDistance`
    with enum `StartOffsetType`, not `hasOffset`, which is the *end* offset; and a variable's
    `mode` takes `VariableMode`, not `VariableAssignmentMode`.

    The whole response is a dozen megabytes covering 97 feature types, so this pulls one.
    """
    res = api(page, "GET", f"/api/partstudios/{doc.path}/featurespecs")
    for spec in res["body"]["featureSpecs"]:
        m = spec.get("message", spec)
        if m.get("featureType") != feature_type:
            continue
        out = {}
        for p in m.get("parameters") or []:
            pm = p.get("message", p)
            out[pm["parameterId"]] = {
                "type": p.get("typeName", "").replace("BTParameterSpec", ""),
                "enumName": pm.get("enumName"),
                "options": [o.get("message", {}).get("value") if isinstance(o, dict) else o
                            for o in (pm.get("options") or [])],
            }
        return out
    raise RuntimeError(f"no feature type named {feature_type}")


def q_geom(*geometry_ids):
    return {
        "type": 138,
        "typeName": "BTMIndividualQuery",
        "message": {"geometryIds": list(geometry_ids), "hasUserCode": False},
    }


def query_list(parameter_id, *queries):
    return {
        "type": 148,
        "typeName": "BTMParameterQueryList",
        "message": {"parameterId": parameter_id, "queries": list(queries)},
    }


def line(entity_id, x1, y1, x2, y2):
    dx, dy = (x2 - x1) * IN, (y2 - y1) * IN
    length = (dx * dx + dy * dy) ** 0.5
    return {
        "type": 155,
        "typeName": "BTMSketchCurveSegment",
        "message": {
            "entityId": entity_id,
            "startPointId": f"{entity_id}.start",
            "endPointId": f"{entity_id}.end",
            "startParam": 0,
            "endParam": length,
            "isConstruction": False,
            "geometry": {
                "type": 117,
                "typeName": "BTCurveGeometryLine",
                "message": {
                    "pntX": x1 * IN,
                    "pntY": y1 * IN,
                    "dirX": dx / length,
                    "dirY": dy / length,
                },
            },
        },
    }


def rect(prefix, x1, y1, x2, y2):
    """Four segments, counter-clockwise, forming an axis-aligned rectangle."""
    return [
        line(f"{prefix}a", x1, y1, x2, y1),
        line(f"{prefix}b", x2, y1, x2, y2),
        line(f"{prefix}c", x2, y2, x1, y2),
        line(f"{prefix}d", x1, y2, x1, y1),
    ]


def circle(entity_id, cx, cy, r):
    return {
        "type": 4,
        "typeName": "BTMSketchCurve",
        "message": {
            "entityId": entity_id,
            "isConstruction": False,
            "geometry": {
                "type": 115,
                "typeName": "BTCurveGeometryCircle",
                "message": {
                    "radius": r * IN,
                    "xCenter": cx * IN,
                    "yCenter": cy * IN,
                    "xDir": 1,
                    "yDir": 0,
                    "clockwise": False,
                },
            },
        },
    }


def arc(entity_id, cx, cy, r, a0, a1):
    """A circular arc. startParam/endParam are radians from the sketch's +x axis."""
    return {
        "type": 155,
        "typeName": "BTMSketchCurveSegment",
        "message": {
            "entityId": entity_id,
            "startPointId": f"{entity_id}.start",
            "endPointId": f"{entity_id}.end",
            "startParam": a0,
            "endParam": a1,
            "isConstruction": False,
            "geometry": {
                "type": 115,
                "typeName": "BTCurveGeometryCircle",
                "message": {
                    "radius": r * IN,
                    "xCenter": cx * IN,
                    "yCenter": cy * IN,
                    "xDir": 1,
                    "yDir": 0,
                    "clockwise": False,
                },
            },
        },
    }


def enum_param(parameter_id, enum_name, value):
    return {
        "type": 145,
        "typeName": "BTMParameterEnum",
        "message": {"parameterId": parameter_id, "enumName": enum_name, "value": value},
    }


def bool_param(parameter_id, value):
    return {
        "type": 144,
        "typeName": "BTMParameterBoolean",
        "message": {"parameterId": parameter_id, "value": value},
    }


def qty(parameter_id, expression):
    return {
        "type": 147,
        "typeName": "BTMParameterQuantity",
        "message": {"parameterId": parameter_id, "expression": expression},
    }


def q_sketch_regions(feature_id):
    """Every closed region of a sketch — what the GUI writes for "Faces of Sketch N"."""
    return {
        "type": 140,
        "typeName": "BTMIndividualSketchRegionQuery",
        "message": {"featureId": feature_id, "filterInnerLoops": True},
    }


def extrude(name, sketch_feature_id, op, depth, symmetric=False, opposite=False):
    params = [
        enum_param("bodyType", "ExtendedToolBodyType", "SOLID"),
        enum_param("operationType", "NewBodyOperationType", op),
        query_list("entities", q_sketch_regions(sketch_feature_id)),
        enum_param("endBound", "BoundingType", "BLIND"),
        qty("depth", depth),
    ]
    if symmetric:
        params.append(bool_param("symmetric", True))
    if opposite:
        params.append(bool_param("oppositeDirection", True))
    # Add and Remove need a merge scope, or the feature fails with "No merge scope
    # selected" — sometimes not until an unrelated edit triggers a rebuild.
    if op != "NEW":
        params.append(bool_param("defaultScope", True))
    return {
        "type": 134,
        "typeName": "BTMFeature",
        "message": {"featureType": "extrude", "name": name, "suppressed": False, "parameters": params},
    }


def revolve(name, sketch_feature_id, axis_geometry_id, op):
    params = [
        enum_param("bodyType", "ExtendedToolBodyType", "SOLID"),
        enum_param("operationType", "NewBodyOperationType", op),
        query_list("entities", q_sketch_regions(sketch_feature_id)),
        query_list("axis", q_geom(axis_geometry_id)),
        bool_param("fullRevolve", True),
    ]
    if op != "NEW":
        params.append(bool_param("defaultScope", True))
    return {
        "type": 134,
        "typeName": "BTMFeature",
        "message": {"featureType": "revolve", "name": name, "suppressed": False, "parameters": params},
    }


def fillet(name, edge_geometry_ids, radius):
    return {
        "type": 134,
        "typeName": "BTMFeature",
        "message": {
            "featureType": "fillet",
            "name": name,
            "suppressed": False,
            "parameters": [
                enum_param("filletType", "FilletType", "EDGE"),
                query_list("entities", q_geom(*edge_geometry_ids)),
                enum_param("crossSection", "FilletCrossSection", "CIRCULAR"),
                qty("radius", radius),
            ],
        },
    }


def sketch(name, plane_id, entities, constraints=None):
    return {
        "type": 151,
        "typeName": "BTMSketch",
        "message": {
            "featureType": "newSketch",
            "name": name,
            "suppressed": False,
            "entities": entities,
            "constraints": constraints or [],
            "parameters": [query_list("sketchPlane", q_geom(plane_id))],
        },
    }


def new_document(page: Page, name: str) -> Doc:
    res = api(page, "POST", "/api/documents", {"name": name, "isPublic": False})
    if not res["ok"]:
        raise RuntimeError(f"could not create document: {res}")
    body = res["body"]
    did = body["id"]
    wid = body["defaultWorkspace"]["id"]
    els = api(page, "GET", f"/api/documents/d/{did}/w/{wid}/elements")["body"]
    eid = next(e["id"] for e in els if e["elementType"] == "PARTSTUDIO")
    return Doc(did, wid, eid)


def find_document(page: Page, name: str) -> Doc | None:
    """Reuse a capture document from a previous run rather than littering."""
    res = api(page, "GET", f"/api/documents?q={name}&filter=0&limit=20")
    if not res["ok"]:
        return None
    for item in res["body"].get("items", []):
        if item["name"] != name:
            continue
        did = item["id"]
        wid = item["defaultWorkspace"]["id"]
        els = api(page, "GET", f"/api/documents/d/{did}/w/{wid}/elements")["body"]
        eid = next(e["id"] for e in els if e["elementType"] == "PARTSTUDIO")
        return Doc(did, wid, eid)
    return None


def features(page: Page, doc: Doc) -> list[dict]:
    res = api(page, "GET", f"/api/partstudios/{doc.path}/features")
    body = res.get("body")
    if not isinstance(body, dict) or "features" not in body:
        raise RuntimeError(f"feature list unavailable: {json.dumps(res)[:300]}")
    return body["features"]


def feature_states(page: Page, doc: Doc) -> dict[str, str]:
    """featureStates is an ARRAY of {key, value} pairs, not a map.

    Reading it as a map yields '?' for every feature, which is how a broken check
    once got mistaken for a passing one. See ../verification-lessons.md.
    """
    body = api(page, "GET", f"/api/partstudios/{doc.path}/features")["body"]
    return {e["key"]: e["value"]["message"]["featureStatus"] for e in body["featureStates"]}


def add_feature(page: Page, doc: Doc, feature: dict) -> dict:
    res = api(page, "POST", f"/api/partstudios/{doc.path}/features", {"feature": feature})
    if not res["ok"]:
        raise RuntimeError(f"feature rejected: {json.dumps(res)[:600]}")
    return res["body"]


def delete_feature(page: Page, doc: Doc, feature_id: str) -> None:
    res = api(page, "DELETE", f"/api/partstudios/{doc.path}/features/featureid/{feature_id}")
    if not res["ok"]:
        raise RuntimeError(f"could not delete {feature_id}: {json.dumps(res)[:300]}")


def update_feature(page: Page, doc: Doc, feature_id: str, feature: dict) -> dict:
    """Replace one feature in place, keeping its id and its place in the tree.

    Deleting and re-adding cannot do this. A re-added feature lands at the end of the tree,
    after everything that already referenced it, and a variable that lands after its readers
    is a variable nothing can read. Changing a driving dimension is what this is for.
    """
    feature = copy.deepcopy(feature)
    feature["message"]["featureId"] = feature_id
    res = api(page, "POST", f"/api/partstudios/{doc.path}/features/featureid/{feature_id}",
              {"feature": feature})
    if not res["ok"]:
        raise RuntimeError(f"could not update {feature_id}: {json.dumps(res)[:600]}")
    return res["body"]


def eval_fs(page: Page, doc: Doc, script: str) -> str:
    """Evaluate FeatureScript against the model and return its string result.

    Returning a string keeps the parsing trivial — the alternative is walking
    Onshape's BTFS value tree for the sake of six numbers.
    """
    res = api(page, "POST", f"/api/partstudios/{doc.path}/featurescript", {"script": script})
    if not res["ok"]:
        raise RuntimeError(f"featurescript call failed: {json.dumps(res)[:400]}")
    body = res["body"]
    for notice in body.get("notices") or []:
        msg = notice.get("message", {})
        if msg.get("level") == "ERROR":
            raise RuntimeError(f"featurescript error: {msg.get('message')}")
    return (body.get("result") or {}).get("message", {}).get("value", "")


BBOX_SCRIPT = """function(context is Context, queries is map)
{
    var s = "";
    var i = 0;
    for (var b in evaluateQuery(context, qBodyType(qEverything(EntityType.BODY), BodyType.SOLID)))
    {
        var bb = evBox3d(context, { "topology" : b });
        s = s ~ "part" ~ toString(i) ~ " min=" ~ toString(bb.minCorner / inch)
              ~ " max=" ~ toString(bb.maxCorner / inch) ~ "\\n";
        i += 1;
    }
    return s;
}"""


def solid_boxes(page: Page, doc: Doc) -> list[tuple[list[float], list[float]]]:
    """Bounding boxes of every solid body, in inches.

    A status code says a feature regenerated. This says the shape is the right
    size, which is a different question and the one that matters.
    """
    text = eval_fs(page, doc, BBOX_SCRIPT)
    out = []
    for row in text.strip().splitlines():
        nums = [float(n) for n in re.findall(r"-?\d+\.?\d*(?:e-?\d+)?", row.split("min=")[1])]
        out.append((nums[0:3], nums[3:6]))
    return out


__all__ = [
    "CDP_URL",
    "Doc",
    "FRONT_PLANE",
    "IN",
    "NotSignedIn",
    "ONSHAPE",
    "add_feature",
    "api",
    "connect",
    "delete_feature",
    "feature_states",
    "features",
    "find_document",
    "new_document",
    "q_geom",
    "query_list",
    "rect",
    "require_signed_in",
    "sketch",
    "sync_playwright",
]
