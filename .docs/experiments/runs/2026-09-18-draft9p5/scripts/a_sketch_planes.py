#!/usr/bin/env python3
"""Phase A — what each sketch stands on, face or stock plane.

The ruling is that a sketch stands on a face of the robot, and on a stock plane
only where the sketch needs the torso's center. A record answers this once the
`sketchPlane` query's geometry ids can be told apart, and they can: the default
planes' ids were evaluated in draft9p5's own empty `ball and socket` tab on
2026-09-18 with `transientQueriesToStrings(qCreatedBy(makeId("Front")))` and its
two siblings, which is where the families below come from. `JCC` agreeing with
the Front plane id `onshape_session.py` already carried is the cross-check.

Anything outside those families is a face or an edge of the model.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/a_sketch_planes.py
"""

from __future__ import annotations

import json
import sys

from stickbot import repo_root

ROOT = repo_root()
D4 = ROOT / ".docs/experiments/runs/2026-09-08-draft9p4/reference"
D3 = ROOT / ".docs/experiments/runs/2026-08-29-draft9p3/reference"
OUT = ROOT / ".docs/experiments/runs/2026-09-18-draft9p5/results"

TABS = [
    ("ball and socket", D4 / "ball-and-socket.features.json"),
    ("hinge", D4 / "hinge.features.json"),
    ("body", D3 / "body.features.json"),
    ("head", D3 / "head.features.json"),
    ("foot", D3 / "foot.features.json"),
    ("u limb", D4 / "u-limb.features.json"),
    ("l limb", D4 / "l-limb.features.json"),
    ("gripper", D3 / "gripper.features.json"),
]

# Measured, not recalled. Each default plane owns a family of ids: the plane
# itself and the edges and vertices of the rectangle drawn for it.
STOCK = {
    "Top": {"ID", "JDE", "JDI", "JDM", "JDB", "JDF", "JDJ", "JDN", "JDC", "JDD"},
    "Front": {"IC", "JCE", "JCI", "JCM", "JCB", "JCF", "JCJ", "JCN", "JCC", "JCD"},
    "Right": {"IE", "JEE", "JEI", "JEM", "JEB", "JEF", "JEJ", "JEN", "JEC", "JED"},
    "Origin": {"IB", "JBD"},
}


def stands_on(ids):
    """What a sketch plane's geometry ids are: a stock plane, or the model."""
    if not ids:
        return "no query"
    names = set()
    for gid in ids:
        hit = [n for n, family in STOCK.items() if gid in family]
        names.add(hit[0] if hit else "model")
    if names == {"model"}:
        return "face of the model"
    if "model" in names:
        return "mixed: " + ", ".join(sorted(names))
    return " and ".join(sorted(names)) + " plane"


# A feature that puts solid in the tab, so a later sketch has a face to stand on.
MAKES_GEOMETRY = {"extrude", "revolve", "importDerived", "sweep", "loft", "thicken",
                  "fill", "boolean", "mirror", "linearPattern", "circularPattern"}


def sketch_planes(path):
    doc = json.loads(path.read_text())
    out, solid = [], False
    for f in doc["features"]:
        m = f["message"]
        if m.get("featureType") in MAKES_GEOMETRY:
            solid = True
        if m.get("featureType") != "newSketch":
            continue
        ids = []
        for prm in m.get("parameters", []):
            pm = prm["message"]
            if pm.get("parameterId") != "sketchPlane":
                continue
            for q in pm.get("queries") or []:
                ids.extend(q["message"].get("geometryIds") or [])
        out.append((m.get("name") or "(unnamed)", ids, stands_on(ids), solid))
    return out


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    report = ["# Phase A — what each sketch stands on\n",
              "Written by [`../scripts/a_sketch_planes.py`](../scripts/a_sketch_planes.py) on",
              "2026-09-18, from the parents' records. A sketch on a stock plane needs a reason",
              "written beside it or a face to move to; the ruling allows a plane where the sketch",
              "needs the torso's center.\n"]
    counts = {}
    data = {}
    for tab, path in TABS:
        rows = sketch_planes(path)
        data[tab] = [{"sketch": n, "ids": ids, "stands_on": v, "had_a_face": s}
                     for n, ids, v, s in rows]
        on_plane = [r for r in rows if r[2] != "face of the model"]
        chose = [r for r in on_plane if r[3]]
        counts[tab] = (len(rows), len(on_plane), len(chose))
        report.append(f"## `{tab}`\n")
        report.append(f"{len(rows)} sketches, {len(on_plane)} of them on a stock plane, "
                      f"{len(chose)} of those with a face already in the tab to stand on.\n")
        report.append("| Sketch | Stands on | A face existed | Geometry ids |")
        report.append("| ------ | --------- | -------------- | ------------ |")
        for name, ids, verdict, had in rows:
            mark = "yes" if had else "no, it is the tab's first"
            report.append(f"| `{name}` | {verdict} | {mark} | `{', '.join(ids) or 'none'}` |")
        report.append("")
    total = sum(c[0] for c in counts.values())
    on_plane = sum(c[1] for c in counts.values())
    chose = sum(c[2] for c in counts.values())
    report.insert(4, f"Across the eight tabs: {total} sketches, {on_plane} on a stock plane, "
                     f"and {chose} of those stand on a plane with a face already in the tab.\n")
    (OUT / "sketch-planes.md").write_text("\n".join(report) + "\n")
    (OUT / "sketch-planes.json").write_text(json.dumps(data, indent=2) + "\n")
    print(f"wrote {OUT / 'sketch-planes.md'}")
    for tab, (n, k, c) in counts.items():
        print(f"  {tab:<16} {n:>2} sketches, {k:>2} on a stock plane, {c:>2} with a face to hand")
    print(f"  {'total':<16} {total:>2} sketches, {on_plane:>2} on a stock plane, "
          f"{chose:>2} with a face to hand")
    return 0


if __name__ == "__main__":
    sys.exit(main())
