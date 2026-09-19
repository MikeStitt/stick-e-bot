#!/usr/bin/env python3
"""Phase A — confirm the six open numbers against the parents' records.

Each is either already right in the parent, and draft9p5 carries it, or it is a
correction draft9p5 makes. Nothing here talks to Onshape.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/a_open_numbers.py
"""

from __future__ import annotations

import json
import sys

from stickbot import repo_root

ROOT = repo_root()
D4 = ROOT / ".docs/experiments/runs/2026-09-08-draft9p4/reference"
D3 = ROOT / ".docs/experiments/runs/2026-08-29-draft9p3/reference"


def features(path):
    return [f["message"] for f in json.loads(path.read_text())["features"]]


def param(m, pid):
    for prm in m.get("parameters", []):
        pm = prm["message"]
        if pm.get("parameterId") == pid:
            return pm
    return None


def named(ms, name):
    return next((m for m in ms if m.get("name") == name), None)


def variable(ms, want):
    for m in ms:
        if m.get("featureType") != "assignVariable":
            continue
        n = param(m, "name")
        if n and n.get("value") == want:
            v = param(m, "value")
            return v.get("expression") if v else None
    return None


def main() -> int:
    out = []

    # #wall, in the Variable Studio.
    studio = features(D4 / "robot-sizes.features.json")
    wall = variable(studio, "wall")
    out.append(("`#wall` reads `#torsoH * 3 / 160`", f"`{wall}`",
                wall == "#torsoH * 3 / 160"))

    # #118 — both of ball and socket's connectors infer CENTROID.
    bs = features(D4 / "ball-and-socket.features.json")
    infer = {}
    for m in bs:
        if m.get("featureType") != "mateConnector":
            continue
        p = param(m, "entityInferenceType")
        infer[m.get("name")] = p.get("value") if p else None
    ok118 = set(infer.values()) == {"CENTROID"}
    out.append(("#118 both connectors infer CENTROID", json.dumps(infer), ok118))

    # #125 — torso shoulder profile stands on a projected edge, not a stock plane.
    body = features(D3 / "body.features.json")
    tsp = named(body, "torso shoulder profile")
    ids = []
    if tsp:
        p = param(tsp, "sketchPlane")
        for q in (p.get("queries") if p else []) or []:
            ids.extend(q["message"].get("geometryIds") or [])
    STOCK = {"JCC", "JDC", "JEC", "IC", "ID", "IE", "IB", "JBD"}
    ok125 = bool(ids) and not (set(ids) & STOCK)
    out.append(("#125 `torso shoulder profile` stands on the model",
                f"plane query `{', '.join(ids) or 'none'}`", ok125))

    # #142 — the blade's robot connector, on axis and at the blade's end face.
    hinge = features(D4 / "hinge.features.json")
    blade = named(hinge, "blade to robot connector")
    origin = None
    if blade:
        for pid in ("originQuery", "originType"):
            pass
        oq = param(blade, "originQuery")
        origin = "query of %d entities" % sum(
            len(q["message"].get("geometryIds") or []) for q in (oq.get("queries") or [])
        ) if oq else None
    out.append(("#142 `blade to robot connector` exists in the parent",
                f"{'present' if blade else 'missing'}, origin {origin}", blade is not None))

    # #168 — l limb's limb section is cut onto the blade's root face.
    ll = features(D4 / "l-limb.features.json")
    sk = next((m for m in ll if m.get("featureType") == "newSketch"), None)
    ids = []
    if sk:
        p = param(sk, "sketchPlane")
        for q in (p.get("queries") if p else []) or []:
            ids.extend(q["message"].get("geometryIds") or [])
    ok168 = bool(ids) and not (set(ids) & STOCK)
    ext = next((m for m in ll if m.get("featureType") == "extrude"), None)
    start = param(ext, "startOffset") if ext else None
    start_expr = start.get("expression") if start else None
    out.append(("#168 `l limb`'s sketch is on the model, not the Top plane",
                f"plane query `{', '.join(ids) or 'none'}`, start offset `{start_expr}`", ok168))

    # #215 — sole groove, still pending; the parent carries the defect.
    foot = features(D3 / "foot.features.json")
    groove = named(foot, "sole groove")
    depth = param(groove, "depth") if groove else None
    opp = param(groove, "oppositeDirection") if groove else None
    so = param(groove, "startOffset") if groove else None
    soo = param(groove, "startOffsetOppositeDirection") if groove else None
    out.append(("#215 `sole groove` is the one draft9p5 must build right",
                f"depth `{depth and depth.get('expression')}`, "
                f"opposite `{opp and opp.get('value')}`, "
                f"start offset `{so and so.get('expression')}`, "
                f"start opposite `{soo and soo.get('value')}`", None))

    width = max(len(a) for a, _, _ in out)
    for what, saw, ok in out:
        mark = "carried" if ok else ("draft9p5 fixes it" if ok is False else "see below")
        print(f"{what:<{width}}  {mark}")
        print(f"{'':<{width}}  saw: {saw}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
