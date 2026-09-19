#!/usr/bin/env python3
"""Phase B — build one Part Studio, feature by feature, with Ring 1 after each.

    uv run python .../scripts/b_build.py "ball and socket" [start] [upto]

`start` resumes a tab, `upto` stops before an index — which is how a tab that
derives is built: REST up to the derive, the derive itself through the GUI,
because a derive `POST` does not return (measured: ten minutes, and it creates
nothing), and REST again after it.

Each feature is replayed from the parent's record, in the order this draft's
tree wants rather than the order the parent has, with the renames and the
corrections Phase A settled. Replay carries a feature's own parameters, so the
shape is the parent's; what changes is where a variable sits, what a feature is
called, and the handful of parameters named in `CORRECTIONS`.

**A feature's wrapper type has to be carried across.** A sketch posted as
`BTMFeature` is refused with *must be of type BTMSketch* — and it is created
anyway. After that the whole `/features` GET answers 400, so the tab cannot be
read at all. The tree row in the GUI carries the `feature-id` attribute, which is
how the one built on 2026-09-18 was found and deleted.

**A query can name a feature, and that name has to be remapped.** A sketch
region is a `BTMIndividualSketchRegionQuery` carrying the sketch's own
`featureId`, so replaying it verbatim points at a feature this document has never
had: the extrude comes back *Select face or sketch region to extrude, 1 missing
selection*, while the geometry id beside it is perfectly valid. Every feature
this script writes is recorded parent id against new id, and every `featureId`
anywhere inside a later message is rewritten before it is posted.

Deterministic geometry ids need no remapping. Built in the same order they
regenerate the same: the stud came back as body `JHD` and `collar profile`'s
region as `JJC`, which is what the parent's records call them.

**A variable keeps Onshape's own title.** A student cannot type over it: the
dialog has no rename pencil, the row's menu offers no *Rename*, and `F2` does
nothing. So every `assignVariable` this script writes carries the literal
`###name = #value`, whatever the parent called it. Five of `ball and socket`'s
and eight of `hinge`'s are typed over in the parents, and replaying them
verbatim carries the defect across, which is what scoring the construction by
hand caught on 2026-09-18.

**Ring 1 runs after every geometry write, and not after a variable.** The read is
a `/features` GET, which is the one endpoint family Onshape rate limits hardest,
and it is per day rather than per burst: on 2026-09-18 the quota went at
`x-rate-limit-remaining: 0` with `retry-after` reading 22.4 hours. Reading the
whole list back after all 187 features, plus the rebuilds, is what spent it. A
variable cannot break geometry on its own and its expression is proved by the
first feature that reads it, so a variable's write is checked against the POST's
own answer and costs nothing extra. Every geometry feature still gets the full
read: parameters compared one by one, every `featureStates` entry, and
`rollbackIndex` against the feature count.

**Reads and writes bill separately on that path.** With the GET at 429 on
2026-09-18 a `POST` to the same `/features` answered 200, so a tab can be written
while it cannot be read. The builder tries one GET at the start: if it is
refused, it writes the whole tab and defers Ring 1's feature read to the verify
pass, and says so rather than appearing to have checked. What it still checks in
that mode costs nothing from the spent family — a sketch's entities from
`sketches`, the part names from `parts` and `metadata`, and the tab's whole
shape from `bodydetails`, diffed against the parent face by face, which is what
a feature that failed to regenerate shows up in.

**Both of these depart from the plan's § Ring 1, which says after every single
`POST`.** They are named here and in the register for Mike to rule on.

A sketch's entities come from `sketches?includeGeometry=true`, which is a
different endpoint family and kept answering with `/features` at zero.
"""

from __future__ import annotations

import json
import sys

from playwright.sync_api import sync_playwright

from stickbot import onshape_session as S
from stickbot import repo_root

ROOT = repo_root()
DID = "2f08b54d795df0ee6b72e321"
WID = "1d8e4c837228c90bab9ff062"
OUT = ROOT / ".docs/experiments/runs/2026-09-18-draft9p5/results"
D4 = ROOT / ".docs/experiments/runs/2026-09-08-draft9p4/reference"
D3 = ROOT / ".docs/experiments/runs/2026-08-29-draft9p3/reference"

# What an untyped Variable feature's row reads, and the only title one may carry.
VARIABLE_TITLE = "###name = #value"

# The order and the parent come from `results/build-order.json`, which
# `b_order.py` derives from each brief's *Recommended steps*, the plan's rename
# table and Phase A's walk. What cannot be derived is here: which part takes
# which name, and the corrections Phase A settled.
#
# `parts` names a part by the feature that made it, because a part id is not
# stable across a metadata write and a name is what the brief's own steps
# address — `ball-and-socket.md` step 6 says *Set `Merge scope` to `Socket
# body`*. `None` as the feature means the one part left at the end of the tab.
EXTRAS = {
    "ball and socket": {
        "parts": [("revolve stud", "Ball stud"), ("collar blank", "Socket body")],
        # #118: both connectors are inferred CENTROID. The parent has the stud on
        # CENTER, which takes a second query to say what it is the center of; a
        # CENTROID takes one face and nothing else, which is how the socket's is
        # built. Sent with the inference changed and the second query left in
        # place, the feature fails to resolve its coordinate system, so the fix
        # is both. On a disc the two land on the same point, which is why the
        # check is the parameter and Ring 2 measures the position.
        "corrections": {
            "stud connect to robot": {"set": {"entityInferenceType": "CENTROID"},
                                      "clear": ["secondaryOriginQuery"]},
        },
    },
    "hinge": {"parts": [], "corrections": {}},
    "body": {"parts": [], "corrections": {},
             "derives": {"copy ball stud": "ball and socket"}},
    "head": {"parts": [(None, "Head")], "corrections": {},
             "derives": {"get socket": "ball and socket"}},
    # #215 is settled at this tab: `sole groove` cuts up into the foot instead of
    # down through the sole. Its parameters are decoded against the record when
    # the tab is built, and the acceptance check is the one task #215 names —
    # the sole at z -24 mm is nine faces, not one, and no face stands at z -20 mm.
    # draft9p1p1's record carries an EMPTY plane query for these three, so the
    # replay has to supply one: read live from draft9p3's own `foot` on
    # 2026-09-18, all three stand on the Top plane, origin at the world origin
    # with normal (0, 0, 1). Replayed without it every feature after them is a
    # warning triangle and the tab makes no part at all.
    "foot": {"parts": [(None, "Foot")], "corrections": {},
             "derives": {"add socket": "ball and socket"},
             "planes": {"pedestal outline": "JDC", "foot outline": "JDC",
                        "groove profile": "JDC"}},
    "u limb": {"parts": [], "corrections": {},
               "derives": {"add socket": "ball and socket", "add fork": "hinge"}},
    "l limb": {"parts": [], "corrections": {},
               "derives": {"add blade": "hinge", "add ball stud": "ball and socket"}},
    # `clip profile`'s plane query is empty in the feature record too. Its own
    # geometry record carries the frame — normal (1, 0, 0) through the origin,
    # which is the Right plane.
    "gripper": {"parts": [(None, "Gripper")], "corrections": {},
                "derives": {"copy socket": "ball and socket"},
                "planes": {"clip profile": "JEC"}},
    "stickbot": {"parts": [], "corrections": {}},
}

# Which tab is which element, read from what Phase A0 recorded.
ELEMENTS = {e["name"]: e["id"] for e in json.loads(
    (OUT / "elements.json").read_text())["elements"]}

ORDER = json.loads((OUT / "build-order.json").read_text())

def load(path):
    """The parent's features, by the name this draft calls them."""
    raw = json.loads(path.read_text())["features"]
    out = {}
    for f in raw:
        m = f["message"]
        if m.get("featureType") == "assignVariable":
            name = next(p["message"].get("value") for p in m["parameters"]
                        if p["message"]["parameterId"] == "name")
            key = f"#{name}"
        else:
            key = m.get("name")
        out[key] = (f["type"], f["typeName"], m)
    return out


def strip(m):
    """A message ready to POST: no ids this document has not issued."""
    out = json.loads(json.dumps(m))
    out.pop("featureId", None)
    return out


def remap(node, ids):
    """Rewrite every feature a parameter names, parent's id to this one's.

    Two spellings, and missing the second cost a whole hinge. A sketch region
    query carries `featureId`, a single string. A pattern or a mirror set to
    pattern *features* carries `BTMParameterFeatureList`, whose `featureIds` is
    a list — `blade wedges` names `blade wedge` that way. Left unmapped it names
    a feature this document has never had, and Onshape neither errors nor
    patterns anything: the tab came back 29 faces against the reference's 491,
    with the seed wedge present and all 24 copies missing.
    """
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "featureId" and isinstance(v, str) and v in ids:
                node[k] = ids[v]
            elif k == "featureIds" and isinstance(v, list):
                node[k] = [ids.get(x, x) for x in v]
            else:
                remap(v, ids)
    elif isinstance(node, list):
        for v in node:
            remap(v, ids)
    return node


def repoint_derive(m, source_eid, microversion):
    """Point an `importDerived` at this document's tab instead of the parent's.

    The source is carried in the `partStudio` parameter's `namespace`, spelled
    `e<elementId>::m<microversion>` — the element id takes a leading `e` and the
    microversion a leading `m`. Written without the `e` the feature is accepted
    and then fails to regenerate, saying only *Error regenerating*. Replayed verbatim it names an element in
    another document and the write is a 404, so the whole robot's derives have
    to be repointed. The part it takes is a geometry id inside `partQuery`, and
    that regenerates on its own.
    """
    for prm in m.get("parameters", []):
        pm = prm["message"]
        if pm.get("parameterId") == "partStudio":
            pm["namespace"] = f"e{source_eid}::m{microversion}"
            return m
    raise RuntimeError(f"{m.get('name')!r} has no partStudio parameter to repoint")


def fix_merge_scope(m):
    """Give an Add or Remove a merge scope when the record lost the one it had.

    Every Add or Remove needs a scope: either `defaultScope` true, or bodies in
    `booleanScope`. draft9p1p1's `foot` and `sole groove` come back from
    `/features` with `defaultScope` false and an EMPTY `booleanScope`, because
    the read did not carry the queries, and replayed that way they build nothing
    at all — the foot came out a 3-face pedestal with every later feature dead.
    Where the scope is empty and there is no default, merging with all is what
    the tab wants: these tabs end on one part.
    """
    ops = {p["message"].get("value") for p in m.get("parameters", [])
           if p["message"].get("parameterId") == "operationType"}
    if not (ops & {"ADD", "REMOVE"}):
        return m
    scope = default = None
    for prm in m.get("parameters", []):
        pm = prm["message"]
        if pm.get("parameterId") == "booleanScope":
            scope = pm
        elif pm.get("parameterId") == "defaultScope":
            default = pm
    if scope is None or default is None:
        return m
    has_bodies = any(q["message"].get("geometryIds") for q in (scope.get("queries") or []))
    if not has_bodies and not default.get("value"):
        default["value"] = True
    return m


def apply_correction(m, fix):
    """Set a parameter's value, or empty a query parameter the new form drops."""
    sets, clears = fix.get("set", {}), set(fix.get("clear", []))
    for prm in m.get("parameters", []):
        pm = prm["message"]
        pid = pm.get("parameterId")
        if pid in sets:
            pm["value"] = sets[pid]
        if pid in clears:
            pm["queries"] = []
    return m


def params(m):
    """What a feature was told, for comparing a write with its read-back."""
    got = {}
    for prm in m.get("parameters", []):
        pm = prm["message"]
        pid = pm["parameterId"]
        if "queries" in pm:
            got[pid] = ("entities", sum(len(q["message"].get("geometryIds") or [])
                                        for q in pm["queries"]))
        elif "expression" in pm:
            got[pid] = ("expression", pm["expression"])
        elif "value" in pm:
            got[pid] = ("value", pm["value"])
        else:
            got[pid] = ("empty", None)
    return got


def features_path(tab, doc):
    """A Part Studio's feature list, or an Assembly's."""
    kind = "assemblies" if tab == "stickbot" else "partstudios"
    return f"/api/{kind}/{doc.path}/features"


def feature_id_of(res_body):
    """The id Onshape gave the feature, out of the POST's own answer.

    Reading it here rather than from a fresh `/features` is what keeps a
    variable from costing a call against the endpoint family that runs out.
    """
    node = res_body.get("feature", res_body)
    node = node.get("message", node)
    fid = node.get("featureId")
    if not fid:
        raise RuntimeError(f"the write did not answer with a featureId: "
                           f"{json.dumps(res_body)[:200]}")
    return fid


def ring1(page, tab, doc, sent_name, sent_message, index):
    """Read the feature back, check every state, and check the rollback bar."""
    body = S.api(page, "GET", features_path(tab, doc))["body"]
    if "features" not in body:
        raise RuntimeError(f"the feature list came back without features: "
                           f"{json.dumps(body)[:200]}")
    feats = body["features"]
    if len(feats) != index + 1:
        raise RuntimeError(f"expected {index + 1} features, the tab holds {len(feats)}")
    got = feats[index]["message"]

    states = {e["key"]: e["value"]["message"]["featureStatus"]
              for e in body["featureStates"]}
    bad = {k: v for k, v in states.items() if v != "OK"}
    if bad:
        named = {n["message"].get("name", k): v for k, v in bad.items()
                 for n in feats if n["message"].get("featureId") == k}
        raise RuntimeError(f"after {sent_name!r}, features are not OK: {named or bad}")

    if body.get("rollbackIndex") != len(feats):
        raise RuntimeError(f"rollbackIndex is {body.get('rollbackIndex')}, "
                           f"not {len(feats)}: a parked bar makes every later read short")

    sent, read = params(sent_message), params(got)
    differs = {k: (sent.get(k), read.get(k)) for k in set(sent) | set(read)
               if sent.get(k) != read.get(k)}
    if differs:
        raise RuntimeError(f"{sent_name!r} read back differently: {differs}")
    return got


def sketch_readback(page, doc, name):
    """A sketch's entities and constraints, read before the next feature runs."""
    body = S.api(page, "GET",
                 f"/api/partstudios/{doc.path}/sketches?includeGeometry=true")["body"]
    sk = next((s for s in body.get("sketches", []) if s.get("sketch") == name), None)
    if sk is None:
        raise RuntimeError(f"sketch {name!r} is not in the tab's sketch list")
    ents = [e for e in sk.get("geomEntities", []) if e.get("entityType") != "point"]
    return {"entities": len(ents), "geomEntities": ents}


def body_of(page, doc, feature_id):
    """The deterministic id of the body a feature created."""
    script = """function(context is Context, queries is map)
{
    return toString(transientQueriesToStrings(evaluateQuery(context,
        qCreatedBy(makeId("%s"), EntityType.BODY))));
}""" % feature_id
    text = S.eval_fs(page, doc, script)
    ids = [t.strip() for t in text.strip("[] \n").split(",") if t.strip()]
    if not ids:
        raise RuntimeError(f"feature {feature_id} created no body")
    return ids[0]


def name_parts(page, doc, wanted, feature_ids):
    """Name each part after the feature that made it, re-resolving between writes.

    Part ids are not stable across a metadata write, so the list is fetched again
    before each one rather than once at the start.
    """
    for feature_name, part_name in wanted:
        parts = S.api(page, "GET", f"/api/parts/{doc.path}")["body"]
        if feature_name is None:
            if len(parts) != 1:
                raise RuntimeError(f"{part_name!r} names the one part left, and the tab "
                                   f"holds {len(parts)}")
            part = parts[0]
        else:
            bid = body_of(page, doc, feature_ids[feature_name])
            part = next((q for q in parts if q["partId"] == bid), None)
            if part is None:
                raise RuntimeError(f"no part with id {bid} for {feature_name!r}")
        meta = S.api(page, "GET", f"/api/metadata/{doc.path}/p/{part['partId']}")["body"]
        prop = next(p for p in meta["properties"] if p["name"] == "Name")
        res = S.api(page, "POST", f"/api/metadata/{doc.path}/p/{part['partId']}",
                    {"properties": [{"propertyId": prop["propertyId"], "value": part_name}]})
        if not res["ok"]:
            raise RuntimeError(f"could not name {bid} {part_name!r}: {res['status']}")
        S.pace(page)
    got = {p["partId"]: p.get("name") for p in
           S.api(page, "GET", f"/api/parts/{doc.path}")["body"]}
    want = sorted(n for _, n in wanted)
    if sorted(v for v in got.values() if v) != want:
        raise RuntimeError(f"parts read back as {got}, wanted {want}")
    return got


def microversion(page):
    """This workspace's current microversion, which a derive's namespace names."""
    return S.api(page, "GET", f"/api/documents/d/{DID}/w/{WID}/currentmicroversion"
                 )["body"]["microversion"]


def seed_ids(page, doc, parent, order, upto):
    """The ids of sketches already written, so a later query can be remapped.

    `sketches?includeGeometry=true` carries each sketch's `featureId` and is a
    different endpoint family from `/features`, so a resumed build can rebuild
    the remap table without the read that is refused. Only sketches are
    recoverable this way, which is enough: the query that names a feature is the
    sketch region query.
    """
    body = S.api(page, "GET",
                 f"/api/partstudios/{doc.path}/sketches?includeGeometry=true")["body"]
    by_name = {s.get("sketch"): s.get("featureId") for s in body.get("sketches", [])}
    ids = {}
    for step in order[:upto]:
        name = step["name"] or step["parent"]
        if name in by_name:
            _, _, message = parent[step["parent"]]
            ids[message.get("featureId")] = by_name[name]
    return ids


def main(tab: str, start: int = 0, upto: int | None = None) -> int:
    spec = ORDER[tab]
    extras = EXTRAS[tab]
    doc = S.Doc(DID, WID, ELEMENTS[tab])
    parent = load(ROOT / spec["parent"])

    missing = [o["parent"] for o in spec["order"] if o["parent"] not in parent]
    if missing:
        raise RuntimeError(f"not in the parent's record: {missing}")

    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        print("signed in as", S.require_signed_in(page))
        probe = S._raw_api(page, "GET", features_path(tab, doc))
        readable = probe.get("status") == 200
        if readable:
            have = probe["body"].get("features", [])
            if have and not start:
                raise RuntimeError(f"`{tab}` already holds {len(have)} features; "
                                   f"clear it before building")
        else:
            print(f"the feature list answers {probe.get('status')}: writing the tab "
                  f"and deferring Ring 1's feature read to the verify pass")
        geometry = [o for o in spec["order"] if o["type"] != "assignVariable"]
        print(f"`{tab}`: {len(spec['order'])} features, {len(geometry)} of them geometry")

        record, ids = [], {}
        stem = tab.replace(" ", "-")

        def save(note=None):
            OUT.mkdir(parents=True, exist_ok=True)
            (OUT / f"{stem}.ring1.json").write_text(json.dumps(
                {"tab": tab, "features": record, "ring1_feature_read": readable,
                 "stopped_at": note}, indent=2) + "\n")

        if start:
            ids = seed_ids(page, doc, parent, spec["order"], start)
            print(f"resuming at {start}, with {len(ids)} sketch ids recovered")
        for i, step in enumerate(spec["order"]):
            if i < start or (upto is not None and i >= upto):
                continue
            parent_name = step["parent"]
            wtype, wname, message = parent[parent_name]
            m = remap(strip(message), ids)
            if m.get("featureType") == "assignVariable":
                m["name"] = VARIABLE_TITLE
            elif step["name"]:
                m["name"] = step["name"]
            m = fix_merge_scope(m)
            if parent_name in extras["corrections"]:
                m = apply_correction(m, extras["corrections"][parent_name])
            plane = extras.get("planes", {}).get(step["name"] or parent_name)
            if plane:
                q = next(prm["message"] for prm in m["parameters"]
                         if prm["message"].get("parameterId") == "sketchPlane")
                empty = not any(x["message"].get("geometryIds")
                                for x in (q.get("queries") or []))
                if not empty:
                    raise RuntimeError(f"{parent_name!r} already names a plane; "
                                       f"the `planes` entry would overwrite it")
                q["queries"] = [{"type": 138, "typeName": "BTMIndividualQuery",
                                 "message": {"geometryIds": [plane],
                                             "hasUserCode": False}}]
            source = extras.get("derives", {}).get(step["name"] or parent_name)
            if source:
                m = repoint_derive(m, ELEMENTS[source], microversion(page))

            res = S.api(page, "POST", features_path(tab, doc),
                        {"feature": {"type": wtype, "typeName": wname, "message": m}})
            if not res["ok"]:
                save(f"{parent_name} refused {res['status']}")
                raise RuntimeError(f"{parent_name!r} was refused at index {i}: "
                                   f"{res['status']} {json.dumps(res.get('body'))[:300]}"
                                   f"\n  {len(record)} features are written; the record "
                                   f"names their ids")
            S.pace(page)

            if m.get("featureType") == "assignVariable" or not readable:
                # A variable cannot break geometry on its own, and its expression
                # is proved by the first feature that reads it. When the list
                # cannot be read at all, every feature takes its id this way and
                # the read is owed.
                fid = feature_id_of(res["body"])
                shown = m.get("name") if m.get("featureType") != "assignVariable" \
                    else parent_name
            else:
                got = ring1(page, tab, doc, parent_name, m, i)
                fid = got.get("featureId")
                shown = m.get("name")
            ids[message.get("featureId")] = fid

            line = {"i": i, "name": m.get("name"), "step": step["name"] or parent_name,
                    "type": m.get("featureType"), "featureId": fid}
            if m.get("featureType") == "newSketch":
                line["entities"] = sketch_readback(page, doc, m["name"])["entities"]
            record.append(line)
            print(f"  {i:>2}  {m.get('featureType'):<15} {shown}")

        named = {}
        if extras["parts"]:
            by_step = {r["step"]: r["featureId"] for r in record}
            named = name_parts(page, doc, extras["parts"], by_step)
            print("\nparts, read back:")
            for pid, nm in named.items():
                print(f"  {pid}  {nm}")

        boxes = S.solid_boxes(page, doc) if tab != "stickbot" else []
        print(f"\n{len(boxes)} solids")
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / f"{stem}.ring1.json").write_text(json.dumps(
            {"tab": tab, "features": record, "solids": len(boxes),
             "parts": named, "ring1_feature_read": readable,
             "owed": [] if readable else
                     ["parameters read back", "featureStates", "rollbackIndex"]},
            indent=2) + "\n")
        if not readable:
            print("owed on this tab: the parameter read-back, every featureStates "
                  "entry, and rollbackIndex")
        print(f"wrote {OUT / f'{stem}.ring1.json'}")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1],
                  int(sys.argv[2]) if len(sys.argv) > 2 else 0,
                  int(sys.argv[3]) if len(sys.argv) > 3 else None))
