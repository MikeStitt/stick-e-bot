#!/usr/bin/env python3
"""How far the head tilts on its neck before it touches the torso, and on what.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/c_neck_tilt.py

[`head.md`](../../../build-briefs/head.md) leaves this open: *the two-flat-plates
model gives 21.8 deg and is wrong, because the head's underside is 6 mm deeper
fore-and-aft than the torso's top face and its corners swing past that face
rather than onto it. Drive the joint in the assembly, report the angle, and name
the face that stopped it.*

Driving it in the GUI would pose the assembly. This turns the head about the neck
ball instead and finds the angle at which one of its own points first enters the
torso, which is the same question asked of the geometry both parts already have.
Every point comes from `bodydetails`, so nothing here is estimated.

**It is a lower bound on the clearance and an upper bound on the swing.** Only
the head's vertices are tested, so a contact that happens along an edge between
two vertices is found late, by however much the edge bows. The head's underside
is flat and its corners are where it reaches, so for this part the vertices are
the contact.
"""

from __future__ import annotations

import math
import sys

from stickbot import make_plans as P
from stickbot import onshape_session as api

DID, WID = "2f08b54d795df0ee6b72e321", "1d8e4c837228c90bab9ff062"
HEAD, BODY = "303898bd4ba38fc3957b0a21", "5441067befc71f1e3b91482e"
MM = 1000.0
STEP = 0.005        # degrees
LIMIT = 60.0        # degrees; past this the joint is not what stops it


def vec(v, scale=MM):
    if v is None:
        return None
    if isinstance(v, dict):
        return [v.get(k, 0.0) * scale for k in "xyz"]
    return [float(v[i]) * scale for i in range(3)]


def part(page, eid):
    base = f"/api/v10/parts/d/{DID}/w/{WID}/e/{eid}"
    p = api._raw_api(page, "GET", base)["body"][0]
    bd = api._raw_api(page, "GET", f"{base}/partid/{p['partId']}/bodydetails")["body"]
    b = bd["bodies"][0]
    faces = []
    for f in b["faces"]:
        s = f.get("surface") or {}
        sign = 1.0 if f.get("orientation", True) else -1.0
        n = vec(s.get("normal"), 1.0)
        faces.append({"id": f["id"], "type": (s.get("type") or "").upper(),
                      "origin": vec(s.get("origin")) or [0.0, 0.0, 0.0],
                      "out": [v * sign for v in n] if n else None,
                      "radius": s["radius"] * MM if s.get("radius") is not None else None,
                      "lo": vec(f["box"]["minCorner"]), "hi": vec(f["box"]["maxCorner"])})
    return {"name": p.get("name"), "faces": faces,
            "points": [vec(v["point"]) for v in b.get("vertices", [])]}


def turn(p, axis, deg):
    """A point turned about the origin, by degrees, about x or y."""
    a = math.radians(deg)
    c, s = math.cos(a), math.sin(a)
    x, y, z = p
    if axis == "x":
        return [x, y * c - z * s, y * s + z * c]
    return [x * c + z * s, y, -x * s + z * c]


def torso_walls(body):
    """The torso's block as six outward planes: one per axis direction, the largest.

    The part also carries two 45 degree planes where the shoulder boss is trimmed,
    and those are not walls of the block; taking the largest face per direction
    leaves them out.
    """
    want = [(0, +1), (0, -1), (1, +1), (1, -1), (2, +1), (2, -1)]
    walls = []
    for i, s in want:
        faces = [f for f in body["faces"]
                 if f["type"] == "PLANE" and f["out"]
                 and abs(f["out"][i] - s) < 1e-6
                 and all(abs(f["out"][j]) < 1e-6 for j in range(3) if j != i)]
        if not faces:
            continue
        walls.append(max(faces, key=lambda f: max(
            (f["hi"][a] - f["lo"][a]) * (f["hi"][b] - f["lo"][b])
            for a in range(3) for b in range(3) if a < b)))
    return walls


def inside(pt, walls, slack=0.0):
    """Is the point inside every one of the block's outward planes?"""
    for w in walls:
        if sum((pt[i] - w["origin"][i]) * w["out"][i] for i in range(3)) > -slack:
            return False, None
    return True, None


def first_touch(head_pts, walls, pivot, axis, sense):
    """The angle at which a head point first enters the torso block, and which point."""
    rel = [[p[i] - pivot[i] for i in range(3)] for p in head_pts]
    deg = 0.0
    while deg <= LIMIT:
        for r in rel:
            t = turn(r, axis, sense * deg)
            world = [t[i] + pivot[i] for i in range(3)]
            hit, _ = inside(world, walls)
            if hit:
                return deg, world
        deg += STEP
    return None, None


def main() -> int:
    with api.sync_playwright() as pw:
        browser, ctx, page = api.connect(pw)
        head, body = part(page, HEAD), part(page, BODY)

    socket = next(f for f in head["faces"] if f["type"] == "SPHERE")
    print(f"  head socket centre, in the head's own frame: "
          f"{[round(v, 4) for v in socket['origin']]}")
    neck = [0.0, 0.0, float(P.NECK_Z)]
    print(f"  neck ball, in the torso's frame: {neck}")
    shift = [neck[i] - socket["origin"][i] for i in range(3)]
    placed = [[p[i] + shift[i] for i in range(3)] for p in head["points"]]
    print(f"  the head placed on it: {len(placed)} points,"
          f" lowest z {min(p[2] for p in placed):.3f}")

    walls = torso_walls(body)
    print(f"  the torso block, as outward planes: {len(walls)}")
    for w in sorted(walls, key=lambda w: w["out"]):
        print(f"      {w['id']:<6} out=({w['out'][0]:+.0f},{w['out'][1]:+.0f},{w['out'][2]:+.0f})"
              f"  through {[round(v, 3) for v in w['origin']]}")

    for axis, sense, name in (("x", +1, "nod forward"), ("x", -1, "nod back"),
                              ("y", +1, "tilt right"), ("y", -1, "tilt left")):
        deg, where = first_touch(placed, walls, neck, axis, sense)
        if deg is None:
            print(f"  {name:<12} clears the torso to {LIMIT:g} deg")
            continue
        # At a corner two or three walls are equally close, so name them all
        # rather than picking one: an edge is what stopped it, not a face.
        on = [w for w in walls
              if abs(sum((where[i] - w["origin"][i]) * w["out"][i] for i in range(3))) < 1e-3]
        which = ", ".join(f"{w['id']}"
                          f" out=({w['out'][0]:+.0f},{w['out'][1]:+.0f},{w['out'][2]:+.0f})"
                          for w in on) or "inside, between walls"
        kind = {1: "face", 2: "edge", 3: "corner"}.get(len(on), "?")
        governs = ("the joint stops first" if float(P.BALL_SWING) < deg
                   else "the torso stops first")
        print(f"  {name:<12} reaches the torso at {deg:7.3f} deg, at"
              f" ({where[0]:.2f}, {where[1]:.2f}, {where[2]:.2f}), on the {kind}: {which}")
        print(f"               against BALL_SWING {float(P.BALL_SWING):.4f} deg, so {governs}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
