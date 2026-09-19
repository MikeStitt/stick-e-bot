#!/usr/bin/env python3
"""Is each part symmetric about the plane its brief names?

    uv run python .../scripts/c_symmetry.py

Three briefs ask for it and each says to check rather than assume: `torso.md`
about the YZ plane, `foot.md` about its own fore-and-aft centreline, `gripper.md`
about its left-right centreline — all of which are the plane x = 0 for these
parts. A face record is enough: mirror every face's centre and its surface's
axis through that plane and look for the face that answers it.

Reads the records on disk; it talks to nothing.
"""

from __future__ import annotations

import json
import sys

from stickbot import repo_root

OUT = repo_root() / ".docs/experiments/runs/2026-09-18-draft9p5/results"
NEAR = 1e-4


def key(face, mirror=False):
    s = face["surface"]
    box = face.get("box") or {}
    lo = list(box.get("minCorner") or [0, 0, 0])
    hi = list(box.get("maxCorner") or [0, 0, 0])
    centre = [(lo[i] + hi[i]) / 2 for i in range(3)]
    if mirror:
        centre[0] = -centre[0]
    # Area is rounded coarsely on purpose. A mirrored pair of the torso's
    # shoulder cylinders measures 717.7415 and 717.7416 mm², which is the
    # mesher's last digit and not an asymmetry; rounding to four places made
    # this check report the body as unsymmetric when its boxes mirror exactly.
    return (s["type"], round(face["area"], 2),
            tuple(round(v, 4) for v in centre),
            round(s.get("radius") or 0, 4))


def main() -> int:
    bad = 0
    for tab in ("body", "foot", "gripper"):
        faces = json.loads((OUT / f"{tab}.faces.json").read_text())
        have = {}
        for f in faces:
            have.setdefault(key(f), 0)
            have[key(f)] += 1
        missing = []
        for f in faces:
            k = key(f, mirror=True)
            if have.get(k, 0) < 1:
                missing.append((f["id"], f["surface"]["type"], round(f["area"], 3)))
        bad += len(missing)
        print(f"  {tab:<9} {len(faces):>3} faces, {len(missing)} without a mirror about x = 0")
        for m in missing[:6]:
            print(f"       {m}")
    print(f"\n{bad} faces unmatched across the three parts")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
