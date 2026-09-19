#!/usr/bin/env python3
"""How close a Ø24 arm comes to the torso, across the shoulder's whole swing.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/c_arm_clearance.py

[`torso.md`](../../../build-briefs/torso.md) asks for it and says why: *this is the
check the 26 mm stud length exists to pass, and it is the only one here that can
fail while every dimension measures correctly.*

The shoulder stud's axis and its ball's centre both come off the torso's own face
dump. The arm is a cylinder of `#limbD` across, running `#limbCenter` from the
ball's centre to the elbow's, and the ball lets it lie anywhere in a cone of
`BALL_SWING` about the stud's axis. The torso is its own block; the Ø16 boss is
left out because it is coaxial with the stud, which is what
[`torso.md`](../../../build-briefs/torso.md) says makes it free.

Clearance is the distance from the arm's axis to the block, less the arm's radius,
taken at the closest point along the arm and over the whole cone.
"""

from __future__ import annotations

import math
import sys

from stickbot import make_plans as P
from stickbot import onshape_session as api

DID, WID = "2f08b54d795df0ee6b72e321", "1d8e4c837228c90bab9ff062"
BODY = "5441067befc71f1e3b91482e"
MM = 1000.0
ALONG = 97          # samples down the arm
TILT = 0.25         # degrees
SPIN = 2.0          # degrees


def vec(v, scale=MM):
    if v is None:
        return None
    if isinstance(v, dict):
        return [v.get(k, 0.0) * scale for k in "xyz"]
    return [float(v[i]) * scale for i in range(3)]


def unit(v):
    n = math.sqrt(sum(c * c for c in v))
    return [c / n for c in v]


def outside(p, half):
    """Distance from a point to a box centred on the origin, zero if it is inside."""
    d = [abs(p[i]) - half[i] for i in range(3)]
    out = [max(0.0, c) for c in d]
    if all(c <= 0 for c in d):
        return -min(-c for c in d)
    return math.sqrt(sum(c * c for c in out))


def clearance(ball, axis, half, radius, length):
    """The least distance from the arm's surface to the block, along its whole length."""
    least = None
    for i in range(ALONG):
        t = length * i / (ALONG - 1)
        p = [ball[j] + axis[j] * t for j in range(3)]
        d = outside(p, half) - radius
        least = d if least is None else min(least, d)
    return least


def main() -> int:
    with api.sync_playwright() as pw:
        browser, ctx, page = api.connect(pw)
        base = f"/api/v10/parts/d/{DID}/w/{WID}/e/{BODY}"
        pid = api._raw_api(page, "GET", base)["body"][0]["partId"]
        bd = api._raw_api(page, "GET", f"{base}/partid/{pid}/bodydetails")["body"]
    faces = []
    for f in bd["bodies"][0]["faces"]:
        s = f.get("surface") or {}
        faces.append({"type": (s.get("type") or "").upper(),
                      "radius": s["radius"] * MM if s.get("radius") is not None else None,
                      "origin": vec(s.get("origin")), "axis": vec(s.get("axis"), 1.0),
                      "lo": vec(f["box"]["minCorner"]), "hi": vec(f["box"]["maxCorner"])})

    half = [float(P.TORSO_W) / 2, float(P.TORSO_D) / 2, float(P.TORSO_H) / 2]
    ball = max((f for f in faces if f["type"] == "SPHERE"),
               key=lambda f: f["origin"][0])["origin"]
    boss = max((f for f in faces if f["type"] == "CYLINDER" and f["radius"]
                and abs(f["radius"] - float(P.BOSS_D) / 2) < 1e-6),
               key=lambda f: f["origin"][0])
    stud = unit([ball[i] - boss["origin"][i] for i in range(3)])
    print(f"  torso block half-sizes {half}")
    print(f"  shoulder ball centre   {[round(v, 4) for v in ball]}")
    print(f"  stud root              {[round(v, 4) for v in boss['origin']]}")
    print(f"  stud axis, outward     {[round(v, 4) for v in stud]}")
    print(f"  arm Ø{float(P.LIMB):g} running {float(P.LIMB_CENTER):g} to the elbow,"
          f" swing ±{float(P.BALL_SWING):.4f} deg")

    # Two directions across the stud axis, to spin the tilt around it.
    ref = [0.0, 0.0, 1.0] if abs(stud[2]) < 0.9 else [1.0, 0.0, 0.0]
    e1 = unit([ref[1] * stud[2] - ref[2] * stud[1],
               ref[2] * stud[0] - ref[0] * stud[2],
               ref[0] * stud[1] - ref[1] * stud[0]])
    e2 = unit([stud[1] * e1[2] - stud[2] * e1[1],
               stud[2] * e1[0] - stud[0] * e1[2],
               stud[0] * e1[1] - stud[1] * e1[0]])

    radius, length = float(P.LIMB) / 2, float(P.LIMB_CENTER)
    zero = clearance(ball, stud, half, radius, length)
    print(f"\n  at the zero pose, arm along the stud: {zero:+.4f} mm")

    worst, at, first_touch = None, None, None
    deg = 0.0
    while deg <= float(P.BALL_SWING) + 1e-9:
        t = math.radians(deg)
        hit_here = None
        spin = 0.0
        while spin < 360.0:
            s = math.radians(spin)
            axis = unit([stud[i] * math.cos(t)
                         + (e1[i] * math.cos(s) + e2[i] * math.sin(s)) * math.sin(t)
                         for i in range(3)])
            c = clearance(ball, axis, half, radius, length)
            if worst is None or c < worst:
                worst, at = c, (deg, spin)
            if c <= 0 and (hit_here is None or c < hit_here):
                hit_here = c
            spin += SPIN
        if hit_here is not None and first_touch is None:
            first_touch = deg
        deg += TILT

    print(f"  least clearance over the cone: {worst:+.4f} mm,"
          f" at {at[0]:.2f} deg of tilt and {at[1]:.0f} deg round")
    if first_touch is None:
        print("  the arm never reaches the torso inside the cone")
        return 0

    # The coarse sweep brackets the first contact; narrow it where it matters.
    lo, hi = first_touch - TILT, first_touch
    for _ in range(40):
        mid = (lo + hi) / 2
        m = math.radians(mid)
        touched = False
        spin = 0.0
        while spin < 360.0:
            s = math.radians(spin)
            axis = unit([stud[i] * math.cos(m)
                         + (e1[i] * math.cos(s) + e2[i] * math.sin(s)) * math.sin(m)
                         for i in range(3)])
            if clearance(ball, axis, half, radius, length) <= 0:
                touched = True
                break
            spin += 0.5
        lo, hi = (lo, mid) if touched else (mid, hi)
    print(f"  contact begins at {hi:.4f} deg of tilt,"
          f" against the {float(P.BALL_SWING):.4f} deg the joint allows,"
          f" so {float(P.BALL_SWING) - hi:.4f} deg past it")

    # Where it lands: the arm point closest to the block at that first contact,
    # and which of the block's faces is the one it reaches.
    m = math.radians(hi)
    best = None
    spin = 0.0
    while spin < 360.0:
        s = math.radians(spin)
        axis = unit([stud[i] * math.cos(m)
                     + (e1[i] * math.cos(s) + e2[i] * math.sin(s)) * math.sin(m)
                     for i in range(3)])
        for i in range(ALONG):
            tt = length * i / (ALONG - 1)
            pt = [ball[j] + axis[j] * tt for j in range(3)]
            d = outside(pt, half) - radius
            if best is None or d < best[0]:
                best = (d, pt, spin, tt)
    
        spin += 0.5
    d, pt, spin, tt = best
    # More than one gap positive means the arm reaches an edge, not a face flat on.
    gaps = [abs(pt[i]) - half[i] for i in range(3)]
    names = {0: "side", 1: "front or back", 2: "top or bottom"}
    on = [i for i in range(3) if gaps[i] > 1e-6]
    where = ", ".join(f"{'+' if pt[i] > 0 else '-'}{'xyz'[i]} {names[i]}"
                      f" (out by {gaps[i]:.2f})" for i in sorted(on, key=lambda i: -gaps[i]))
    kind = "face" if len(on) == 1 else "edge" if len(on) == 2 else "corner"
    print(f"  it lands on the torso's {where}, so a {kind}")
    print(f"  the arm's axis is then at ({pt[0]:.2f}, {pt[1]:.2f}, {pt[2]:.2f}),"
          f" {tt:.1f} mm down the arm, {spin:.0f} deg round the cone")
    return 0


if __name__ == "__main__":
    sys.exit(main())
