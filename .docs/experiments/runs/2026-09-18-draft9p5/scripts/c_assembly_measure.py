#!/usr/bin/env python3
"""The robot's own dimensions, measured in the assembly rather than reasoned about.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/c_assembly_measure.py

An occurrence carries a 4 x 4 row-major transform and a part carries every vertex
as a point, so a point in assembly space is the part's point through its
occurrence's transform. That is the whole method, and it needs none of the
endpoints a feature write shares a quota with.

It reports the standing height, each foot's centre and the gap between them, and
how far the grippers reach down the thigh.
"""

from __future__ import annotations

import sys

from stickbot import make_plans as P
from stickbot import onshape_session as S

DID, WID = "2f08b54d795df0ee6b72e321", "1d8e4c837228c90bab9ff062"
ASM = "c81b630354bd0739d788a42d"
MM = 1000.0


def vec(v, scale=MM):
    if v is None:
        return None
    if isinstance(v, dict):
        return [v.get(k, 0.0) * scale for k in "xyz"]
    return [float(v[i]) * scale for i in range(3)]


def through(t, p):
    """A point in millimetres through a row-major 4 x 4 whose offsets are in metres."""
    return [t[0] * p[0] + t[1] * p[1] + t[2] * p[2] + t[3] * MM,
            t[4] * p[0] + t[5] * p[1] + t[6] * p[2] + t[7] * MM,
            t[8] * p[0] + t[9] * p[1] + t[10] * p[2] + t[11] * MM]


def part_points(page, eid):
    """Every vertex of every part of a Part Studio, keyed by part id."""
    base = f"/api/v10/parts/d/{DID}/w/{WID}/e/{eid}"
    got = {}
    for p in S._raw_api(page, "GET", base)["body"]:
        bd = S._raw_api(page, "GET", f"{base}/partid/{p['partId']}/bodydetails")["body"]
        b = bd["bodies"][0]
        got[p["partId"]] = {"name": p.get("name"),
                            "points": [vec(v["point"]) for v in b.get("vertices", [])]
                                      + [vec(f["box"]["minCorner"]) for f in b["faces"]]
                                      + [vec(f["box"]["maxCorner"]) for f in b["faces"]]}
    return got


def main() -> int:
    with S.sync_playwright() as pw:
        browser, ctx, page = S.connect(pw)
        asm = S._raw_api(page, "GET", f"/api/assemblies/d/{DID}/w/{WID}/e/{ASM}")["body"]
        root = asm["rootAssembly"]
        inst = {i["id"]: i for i in root["instances"]}

        studios, placed = {}, []
        for occ in root["occurrences"]:
            i = inst.get(occ["path"][-1])
            if not i or i.get("type") != "Part":
                continue
            eid = i["elementId"]
            if eid not in studios:
                studios[eid] = part_points(page, eid)
            part = studios[eid].get(i.get("partId"))
            if not part:
                continue
            pts = [through(occ["transform"], p) for p in part["points"]]
            placed.append((i.get("name") or part["name"], pts))

        if not placed:
            print("no placed parts; nothing to measure")
            return 1

        every = [p for _n, pts in placed for p in pts]
        lo = [min(p[i] for p in every) for i in range(3)]
        hi = [max(p[i] for p in every) for i in range(3)]
        print(f"  the robot, in the assembly: x {lo[0]:.3f}..{hi[0]:.3f}"
              f"   y {lo[1]:.3f}..{hi[1]:.3f}   z {lo[2]:.3f}..{hi[2]:.3f}")
        print(f"  standing height, sole to the top of the head: {hi[2] - lo[2]:.3f} mm"
              f"   make_plans HEIGHT {float(P.HEIGHT):.3f} mm")

        feet = [(n, pts) for n, pts in placed if n.lower().startswith("foot")]
        for n, pts in feet:
            fl = [min(p[i] for p in pts) for i in range(3)]
            fh = [max(p[i] for p in pts) for i in range(3)]
            print(f"  {n:<12} x {fl[0]:>8.3f}..{fh[0]:<8.3f}"
                  f"  centre x {(fl[0] + fh[0]) / 2:>7.3f}   sole z {fl[2]:.3f}")
        if len(feet) == 2:
            a, b = (sorted(feet, key=lambda f: min(p[0] for p in f[1])))
            gap = min(p[0] for p in b[1]) - max(p[0] for p in a[1])
            print(f"  gap between the feet: {gap:.3f} mm")

        grips = [(n, pts) for n, pts in placed if "grip" in n.lower()]
        thighs = [(n, pts) for n, pts in placed if n.lower().startswith("upper limb")]
        if grips and thighs:
            legs = sorted(thighs, key=lambda t: min(p[2] for p in t[1]))[:2]
            for n, pts in legs:
                zl, zh = min(p[2] for p in pts), max(p[2] for p in pts)
                print(f"  {n:<14} z {zl:.3f}..{zh:.3f}   middle {(zl + zh) / 2:.3f}")
            low = min(min(p[2] for p in pts) for _n, pts in grips)
            mid = sum((min(p[2] for p in pts) + max(p[2] for p in pts)) / 2
                      for _n, pts in legs) / len(legs)
            print(f"  the grippers reach to z {low:.3f}, mid-thigh is z {mid:.3f},"
                  f" so they reach {mid - low:.3f} mm past it")
    return 0


if __name__ == "__main__":
    sys.exit(main())
