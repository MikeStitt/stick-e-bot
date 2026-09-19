#!/usr/bin/env python3
"""Which sketches should stand on a face, derived from the records.

    uv run python .../scripts/a_sketch_moves.py

Phase A found 22 of 28 sketches on a stock plane. That count alone does not say
which are wrong: a sketch on the plane its part is symmetric about is right, and
there is often no face there at all. What gives a wrong one away is its extrude:
a `startOffset` whose distance names a dimension the geometry already fixes —
`blade wedge` offsetting by `#blade / 2` to reach the blade's own face — is the
arithmetic the ruling is about.

So this reports, per tab, every sketch standing on a stock plane together with
what its extrude does: symmetric about the plane, offset by an expression, or
neither. The ones with an offset are the candidates; the symmetric ones are the
sketches that need the plane.

Nothing here talks to Onshape.
"""

from __future__ import annotations

import json
import sys

from stickbot import repo_root

ROOT = repo_root()
D4 = ROOT / ".docs/experiments/runs/2026-09-08-draft9p4/reference"
D3 = ROOT / ".docs/experiments/runs/2026-08-29-draft9p3/reference"
OUT = ROOT / ".docs/experiments/runs/2026-09-18-draft9p5/results"

TABS = [("ball and socket", D4 / "ball-and-socket.features.json"),
        ("hinge", D4 / "hinge.features.json"),
        ("body", D3 / "body.features.json"),
        ("head", D3 / "head.features.json"),
        ("foot", D3 / "foot.features.json"),
        ("u limb", D4 / "u-limb.features.json"),
        ("l limb", D4 / "l-limb.features.json"),
        ("gripper", D3 / "gripper.features.json")]

CONSUMES = {"extrude", "revolve"}


def param(m, pid):
    for prm in m.get("parameters", []):
        if prm["message"].get("parameterId") == pid:
            return prm["message"]
    return None


def main() -> int:
    planes = json.loads((OUT / "sketch-planes.json").read_text())
    report = ["# Phase A — which sketches should stand on a face\n",
              "Written by [`../scripts/a_sketch_moves.py`](../scripts/a_sketch_moves.py).",
              "A sketch on a stock plane is wrong when its extrude offsets its start by an",
              "expression that names a dimension the geometry already fixes; it is right when the",
              "extrude is symmetric about that plane, because then the plane is what places it.\n"]
    candidates = 0
    for tab, path in TABS:
        feats = [f["message"] for f in json.loads(path.read_text())["features"]]
        by_sketch = {}
        for m in feats:
            if m.get("featureType") not in CONSUMES:
                continue
            ents = param(m, "entities")
            for q in (ents or {}).get("queries") or []:
                fid = q["message"].get("featureId")
                if fid:
                    by_sketch.setdefault(fid, []).append(m)
        sketch_id = {m.get("name"): m.get("featureId") for m in feats
                     if m.get("featureType") == "newSketch"}
        rows = []
        for row in planes.get(tab, []):
            if row["stands_on"] == "face of the model":
                continue
            users = by_sketch.get(sketch_id.get(row["sketch"]), [])
            verdict, detail = "no extrude names it", ""
            for u in users:
                sym = (param(u, "symmetric") or {}).get("value")
                start = (param(u, "startOffset") or {}).get("value")
                dist = (param(u, "startOffsetDistance") or {}).get("expression")
                if start:
                    verdict = "**offsets its start**"
                    detail = f"`{u.get('name')}` by `{dist}`"
                elif sym:
                    verdict = "symmetric about the plane"
                    detail = f"`{u.get('name')}`"
                else:
                    verdict = "neither"
                    detail = f"`{u.get('name')}`"
            rows.append((row["sketch"], row["stands_on"], row["had_a_face"], verdict, detail))
        if not rows:
            continue
        report.append(f"## `{tab}`\n")
        report.append("| Sketch | Stands on | What its extrude does |")
        report.append("| ------ | --------- | --------------------- |")
        for name, on, _had, verdict, detail in rows:
            report.append(f"| `{name}` | {on} | {verdict} {detail} |")
        report.append("")
        candidates += sum(1 for r in rows if "offsets" in r[3])
    report.insert(5, f"**{candidates} sketches offset their start**, and those are the ones to "
                     f"move.\n")
    (OUT / "sketch-moves.md").write_text("\n".join(report) + "\n")
    print(f"wrote {OUT / 'sketch-moves.md'}")
    print(f"{candidates} sketches offset their start")
    return 0


if __name__ == "__main__":
    sys.exit(main())
