#!/usr/bin/env python3
"""Name a built tab's parts, after the feature that made each one.

    uv run python .../scripts/c_name_parts.py "hinge"

The names are the briefs' own: `ball-and-socket.md` says `Ball stud` and
`Socket body`, `hinge.md` line 40 says *the two parts are named `fork` and
`blade`*, `torso.md` line 150 says *Name it `Torso`*, and `head.md`, `foot.md`
and `gripper.md` each say `Head`, `Foot` and `Gripper`. They are not decoration:
`ball-and-socket.md` step 6 tells the reader to set `Merge scope` to `Socket
body`, so a tab whose parts are `Part 1` and `Part 2` cannot be followed.

A part is found by the feature that created its body, over `featurescript`, and
the part list is fetched again before each write because a part id is not stable
across a metadata write. None of this touches `/features`.
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
ELEMENTS = {e["name"]: e["id"] for e in json.loads(
    (OUT / "elements.json").read_text())["elements"]}

# tab -> (the feature that makes the body, the name the brief gives it).
# `None` means the one part the tab is left with.
NAMES = {
    "ball and socket": [("revolve stud", "Ball stud"), ("collar blank", "Socket body")],
    "hinge": [("blade blank", "blade"), ("fork blank", "fork")],
    "body": [(None, "Torso")],
    "head": [(None, "Head")],
    "foot": [(None, "Foot")],
    "gripper": [(None, "Gripper")],
    # `limbs.md` says only *name the part for the limb it is*; the brief's own
    # words for them are *the upper limb* and *the lower limb*.
    "u limb": [(None, "upper limb")],
    "l limb": [(None, "lower limb")],
}


def body_of(page, doc, feature_id):
    script = """function(context is Context, queries is map)
{
    return toString(transientQueriesToStrings(evaluateQuery(context,
        qCreatedBy(makeId("%s"), EntityType.BODY))));
}""" % feature_id
    ids = [t.strip() for t in S.eval_fs(page, doc, script).strip("[] \n").split(",")
           if t.strip()]
    if not ids:
        raise RuntimeError(f"feature {feature_id} created no body")
    return ids[0]


def main(tab: str) -> int:
    wanted = NAMES[tab]
    # A name that is `None` means the one part left, and needs no record at all.
    path = OUT / f"{tab.replace(' ', '-')}.ring1.json"
    if path.exists():
        rec = json.loads(path.read_text())
        ids = {(r.get("step") or r.get("name")): r["featureId"] for r in rec["features"]}
    elif all(fn is None for fn, _ in wanted):
        ids = {}
    else:
        raise RuntimeError(f"{path} is missing and {tab!r} names parts by feature")
    doc = S.Doc(DID, WID, ELEMENTS[tab])
    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        for feature_name, part_name in wanted:
            parts = S.api(page, "GET", f"/api/parts/{doc.path}")["body"]
            if feature_name is None:
                if len(parts) != 1:
                    raise RuntimeError(f"{part_name!r} names the one part left and "
                                       f"`{tab}` holds {len(parts)}")
                part = parts[0]
            else:
                bid = body_of(page, doc, ids[feature_name])
                part = next((q for q in parts if q["partId"] == bid), None)
                if part is None:
                    raise RuntimeError(f"no part {bid} for {feature_name!r}")
            meta = S.api(page, "GET", f"/api/metadata/{doc.path}/p/{part['partId']}")["body"]
            prop = next(x for x in meta["properties"] if x["name"] == "Name")
            res = S.api(page, "POST", f"/api/metadata/{doc.path}/p/{part['partId']}",
                        {"properties": [{"propertyId": prop["propertyId"],
                                         "value": part_name}]})
            # A name that is already right answers NOTHING_TO_UPDATE, which is a
            # success: the part carries the name asked for.
            if not res["ok"] or res["body"].get("status") not in (
                    "SUCCEEDED", "NOTHING_TO_UPDATE"):
                raise RuntimeError(f"could not name {part['partId']}: {res['status']}")
            print(f"  {part['partId']} <- {part_name!r}"
                  + (f"  (made by `{feature_name}`)" if feature_name else ""))
            S.pace(page)
        got = {x["partId"]: x.get("name")
               for x in S.api(page, "GET", f"/api/parts/{doc.path}")["body"]}
        print(f"read back: {got}")
        if sorted(v for v in got.values() if v) != sorted(n for _, n in wanted):
            raise RuntimeError(f"parts read back as {got}")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
