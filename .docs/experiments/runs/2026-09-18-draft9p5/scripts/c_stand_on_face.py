#!/usr/bin/env python3
"""Stand a sketch on the face it belongs on, and drop the arithmetic that placed it.

    uv run python .../scripts/c_stand_on_face.py "hinge" "blade wedge outline"

The ruling is that a sketch stands on a face of the robot and on a stock plane
only where it needs a center the model has no face at. `blade wedge outline` and
`ear wedge outline` are the hinge's two that fail it: each is drawn on the Front
plane and its extrude carries a start offset — `#blade / 2` and `#seat / 2` —
which is arithmetic reproducing the position of a face the model already has.
Standing the sketch on that face and dropping the offset makes the wedge follow
the face if the blade's thickness ever changes.

Each move is one update to the sketch and one to its extrude, and then the shape
is read and diffed against the parent: the wedge ring must come out where it was.

Reverts with `--revert`, which puts the parent's own parameters back.
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

# sketch -> the face it stands on, the extrude it drives, and what that extrude
# offset by. The face id is a deterministic id, checked against the tab's own
# `bodydetails` before it is used.
MOVES = {
    "hinge": {
        "blade wedge outline": {"face": "R+DC", "extrude": "blade wedge",
                                "was": "#blade / 2"},
        # The seat face's own normal points out of the fork, so with the offset
        # gone the extrude has to run the other way to grow the wedge proud of
        # it rather than into it. Sent without the flip the ring vanished and the
        # tab came back 270 faces against 510.
        "ear wedge outline": {"face": "SMGyH", "extrude": "ear wedge",
                              "was": "#seat / 2", "flip": True},
    },
}
PARENT = {"hinge": ROOT / ".docs/experiments/runs/2026-09-08-draft9p4/reference/hinge.features.json"}


def parent_features(tab):
    raw = json.loads(PARENT[tab].read_text())["features"]
    return {f["message"].get("name"): f for f in raw}


def plane_query(face_id):
    return [{"type": 138, "typeName": "BTMIndividualQuery",
             "message": {"geometryIds": [face_id], "hasUserCode": False}}]


def set_param(m, pid, **kv):
    for prm in m.get("parameters", []):
        pm = prm["message"]
        if pm.get("parameterId") == pid:
            pm.update(kv)
            return True
    return False


def face_exists(page, doc, face_id):
    body = S.api(page, "GET", f"/api/partstudios/{doc.path}/bodydetails")["body"]
    for b in body["bodies"]:
        for f in b["faces"]:
            if f["id"] == face_id:
                s = f["surface"]
                return {"body": b["id"], "type": s["type"],
                        "origin": [round(v * 1000, 4) for v in s.get("origin", [])],
                        "area": round(f["area"] * 1e6, 3)}
    return None


def main(tab, sketch, revert=False) -> int:
    move = MOVES[tab][sketch]
    rec = json.loads((OUT / f"{tab.replace(' ', '-')}.ring1.json").read_text())
    ids = {r["step"]: r["featureId"] for r in rec["features"]}
    # The record keys on this draft's names; MOVES keys on the parent's, because
    # that is where the message is read from. `ear wedge outline` is built as
    # `fork prong wedge outline`.
    order = json.loads((OUT / "build-order.json").read_text())[tab]["order"]
    new_name = {o["parent"]: (o["name"] or o["parent"]) for o in order}
    ids = {parent: ids[new] for parent, new in new_name.items() if new in ids}
    parent = parent_features(tab)
    doc = S.Doc(DID, WID, ELEMENTS[tab])

    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        where = face_exists(page, doc, move["face"])
        if where is None and not revert:
            raise RuntimeError(f"face {move['face']} is not in `{tab}`")
        print(f"face {move['face']}: {where}")

        sk = json.loads(json.dumps(parent[sketch]))
        if not revert:
            if not set_param(sk["message"], "sketchPlane", queries=plane_query(move["face"])):
                raise RuntimeError("no sketchPlane parameter")
        sk["message"].pop("featureId", None)
        S.update_feature(page, doc, ids[sketch], sk)
        print(f"{sketch}: plane -> "
              f"{'the parent’s' if revert else move['face']}")
        S.pace(page)

        ex = json.loads(json.dumps(parent[move["extrude"]]))
        if not revert:
            set_param(ex["message"], "startOffset", value=False)
            if move.get("flip"):
                for prm in ex["message"]["parameters"]:
                    pm = prm["message"]
                    if pm.get("parameterId") == "oppositeDirection":
                        pm["value"] = not pm.get("value", False)
        ex["message"].pop("featureId", None)
        S.update_feature(page, doc, ids[move["extrude"]], ex)
        print(f"{move['extrude']}: start offset "
              f"{'restored to ' + move['was'] if revert else 'dropped, was ' + move['was']}")
        S.pace(page)
        browser.close()
    return 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--revert"]
    sys.exit(main(args[0], args[1], "--revert" in sys.argv))
