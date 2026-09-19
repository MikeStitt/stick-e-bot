#!/usr/bin/env python3
"""The walls a face dump can measure exactly, for the tabs whose briefs ask.

    uv run python .../scripts/c_walls.py

A wall between two curved faces that share a centre or an axis is their radius
gap, measured rather than estimated. Four briefs ask for the thinnest wall in a
part, and the socket's is the one with a number against it: 1.72 mm, from the
collar's outside to the cavity.

**`src/stickbot/measure_walls.py` cannot read today's `bodydetails`.** It filters
on `CYLINDER` and `SPHERE` where the route now answers `cylinder` and `sphere`,
and it reads each vector as a `{x, y, z}` map where the route now answers a list.
It reports *pairs found: 0* on every tab and then raises on the empty minimum.
That is a defect in a shared tool, so it is named here and not edited.
"""

from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

SCRATCH = Path("/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-stick-e-bot"
               "/c3730b06-661a-42fb-887a-a5f90835fc73/scratchpad")
MM = 1000.0
NEAR = 1e-4     # millimetres; nearer than this is the same centre or axis


def curved(dump):
    out = []
    for body in dump.get("bodies", []):
        for f in body.get("faces", []):
            s = f.get("surface", {})
            if s.get("type") not in ("cylinder", "sphere", "cone", "torus"):
                continue
            out.append({"id": f["id"], "body": body["id"], "type": s["type"],
                        "radius": (s.get("radius") or 0) * MM,
                        "origin": [v * MM for v in (s.get("origin") or [0, 0, 0])],
                        "axis": [round(v, 6) for v in (s.get("axis") or [0, 0, 0])]})
    return out


def same_place(a, b):
    """Concentric spheres, or a cylinder whose axis runs through a sphere's centre."""
    if a["type"] == b["type"] == "sphere":
        return all(abs(a["origin"][i] - b["origin"][i]) < NEAR for i in range(3))
    sph = a if a["type"] == "sphere" else (b if b["type"] == "sphere" else None)
    cyl = b if sph is a else a
    if sph is None or cyl["type"] != "cylinder":
        return False
    d = [sph["origin"][i] - cyl["origin"][i] for i in range(3)]
    along = sum(d[i] * cyl["axis"][i] for i in range(3))
    off = sum((d[i] - along * cyl["axis"][i]) ** 2 for i in range(3)) ** 0.5
    return off < NEAR


def main() -> int:
    for tab in ("ball and socket", "head", "foot", "gripper"):
        path = SCRATCH / f"raw-{tab.replace(' ', '-')}.json"
        if not path.exists():
            print(f"  {tab:<16} no dump at {path.name}")
            continue
        fs = curved(json.loads(path.read_text()))
        walls = []
        for a, b in itertools.combinations(fs, 2):
            if same_place(a, b):
                gap = round(abs(a["radius"] - b["radius"]), 4)
                if gap > NEAR:
                    walls.append((gap, a["id"], a["type"], b["id"], b["type"]))
        walls.sort()
        print(f"  {tab:<16} {len(fs):>2} curved faces, {len(walls)} measurable walls")
        for w in walls[:4]:
            print(f"       {w[0]:>8} mm   {w[2]} {w[1]} to {w[4]} {w[3]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
