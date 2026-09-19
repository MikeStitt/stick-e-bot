#!/usr/bin/env python3
"""The thinnest wall in a part, taken analytically off the face dump.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/c_thinnest_wall.py [tab]

Four briefs ask for the thinnest wall anywhere in a part. The usual instrument is
`evDistance` through `featurescript`, which shares its quota with the feature
writes. But `bodydetails` gives each face's surface exactly: a plane's point and
normal, a cylinder's axis and radius, a sphere's centre and radius. Between two
such surfaces the distance is arithmetic, not search, and it is exact.

**Wall or gap is decided by the outward normals, not by the size of the number.**
A face's outward normal is its stored normal when `orientation` is true and the
opposite when it is false; the head's front face and back face both store `-y`
and only the flag tells them apart. If the second surface lies on the material
side of the first, the two bound a wall; if they face each other across air, the
number is a slit or a mouth, which is what the briefs say to separate out.

**What it does not reach**: two curved faces that are neither coaxial nor
concentric, and any pair where the closest approach is at an edge rather than
across the surfaces. Those still want `evDistance`. Every pair it does reach is
exact, and each is reported with the faces it came from so it can be recognised.
"""

from __future__ import annotations

import itertools
import math
import sys
from collections import defaultdict

from stickbot import onshape_session as api

DID, WID = "2f08b54d795df0ee6b72e321", "1d8e4c837228c90bab9ff062"
TABS = {"ball and socket": "1a8322899842a1934e85851d",
        "body": "5441067befc71f1e3b91482e",
        "head": "303898bd4ba38fc3957b0a21",
        "foot": "229aa0900e5a7e7aa4768c6f",
        "gripper": "a3a4fac68ffb7372a7803003"}
MM = 1000.0
NEAR = 1e-4          # millimetres
SPAN = 0.05          # how far a pair may miss each other's extent and still count


def vec(v, scale=MM):
    if v is None:
        return None
    if isinstance(v, dict):
        return [v.get(k, 0.0) * scale for k in "xyz"]
    return [float(v[i]) * scale for i in range(3)]


def sub(a, b):
    return [a[i] - b[i] for i in range(3)]


def dot(a, b):
    return sum(a[i] * b[i] for i in range(3))


def read(page, eid):
    base = f"/api/v10/parts/d/{DID}/w/{WID}/e/{eid}"
    out = []
    for p in api._raw_api(page, "GET", base)["body"]:
        bd = api._raw_api(page, "GET", f"{base}/partid/{p['partId']}/bodydetails")["body"]
        b = bd["bodies"][0]
        faces, touching = [], defaultdict(set)
        for f in b["faces"]:
            s = f.get("surface") or {}
            sign = 1.0 if f.get("orientation", True) else -1.0
            n = vec(s.get("normal"), 1.0)
            faces.append({
                "id": f["id"], "type": (s.get("type") or "").upper(),
                "radius": s["radius"] * MM if s.get("radius") is not None else None,
                "origin": vec(s.get("origin")), "axis": vec(s.get("axis"), 1.0),
                "out": [v * sign for v in n] if n else None,
                "solid_inside": f.get("orientation", True),
                "lo": vec(f["box"]["minCorner"]), "hi": vec(f["box"]["maxCorner"]),
            })
            for loop in f.get("loops", []):
                for ce in loop.get("coedges", []):
                    touching[ce["edgeId"]].add(f["id"])
        adjacent = set()
        for fids in touching.values():
            for a, c in itertools.combinations(sorted(fids), 2):
                adjacent.add((a, c))
        out.append({"name": p.get("name"), "faces": faces, "adjacent": adjacent})
    return out


def reaches(a, b, u, d):
    """Is the measured distance the distance between these faces, or between their
    surfaces carried on past where the faces end?

    The head's domed top is a cylinder of radius 36 whose axis lies 36 below the
    underside, so the two surfaces are tangent and the arithmetic says 0.0000 mm
    while the faces are at opposite ends of the part. Their boxes are 36 apart
    along the measurement, and that is what catches it.
    """
    if u is None:
        return True
    sep = 0.0
    for i in range(3):
        if abs(u[i]) < 0.2:
            continue
        sep = max(sep, a["lo"][i] - b["hi"][i], b["lo"][i] - a["hi"][i])
    return sep <= d + SPAN


def side_by_side(a, b, u):
    """Do the two faces lie across from each other, rather than merely parallel?

    Only the axes across the measurement matter. Two slit walls 1.6 mm apart have
    boxes that do not meet along the measurement, which is the whole point, so
    testing every axis rejects exactly the pairs worth measuring.
    """
    for i in range(3):
        if u is not None and abs(u[i]) > 0.2:
            continue                       # this axis is the measurement, not across it
        if a["lo"][i] - SPAN > b["hi"][i] or b["lo"][i] - SPAN > a["hi"][i]:
            return False
    return True


def direction(a, b):
    """The unit vector the measurement is taken along, where there is a single one."""
    if a["type"] == "PLANE" and a["out"]:
        return a["out"]
    if b["type"] == "PLANE" and b["out"]:
        return b["out"]
    return None


def measure(a, b):
    """Distance between two surfaces, and whether material lies between them.

    Returns (distance, verdict, how) or None where the pair is not one of the
    analytic cases.
    """
    ta, tb = a["type"], b["type"]
    if ta == "PLANE" and tb == "PLANE":
        if a["out"] is None or b["out"] is None:
            return None
        if abs(abs(dot(a["out"], b["out"])) - 1) > 1e-6:
            return None                      # not parallel, so no slab between them
        s = dot(sub(b["origin"], a["origin"]), a["out"])
        if abs(s) < NEAR:
            return None                      # the same plane
        t = dot(sub(a["origin"], b["origin"]), b["out"])
        verdict = "wall" if s < 0 and t < 0 else ("gap" if s > 0 and t > 0 else "offset")
        return abs(s), verdict, "plane to plane"
    plane, curved = ((a, b) if ta == "PLANE" else (b, a)) if "PLANE" in (ta, tb) else (None, None)
    if plane is not None and curved["type"] in ("CYLINDER", "SPHERE") and plane["out"]:
        d = dot(sub(curved["origin"], plane["origin"]), plane["out"])
        if curved["type"] == "CYLINDER":
            if abs(dot(curved["axis"], plane["out"])) > 1e-6:
                return None                  # the axis runs into the plane, not along it
        gap = abs(d) - curved["radius"]
        if gap < -NEAR:
            return None                      # the surface crosses the plane
        verdict = "wall" if d < 0 else "gap"
        return abs(gap), verdict, f"plane to {curved['type'].lower()}"
    if {ta, tb} <= {"CYLINDER", "SPHERE"}:
        if ta == tb == "CYLINDER":
            if abs(abs(dot(a["axis"], b["axis"])) - 1) > 1e-6:
                return None
            off = sub(b["origin"], a["origin"])
            along = dot(off, a["axis"])
            perp = math.sqrt(max(0.0, dot(off, off) - along * along))
            if perp > NEAR:
                return None                  # not coaxial
        else:
            centre = a["origin"] if ta == "SPHERE" else b["origin"]
            other = b if ta == "SPHERE" else a
            if other["type"] == "CYLINDER":
                off = sub(centre, other["origin"])
                along = dot(off, other["axis"])
                perp = math.sqrt(max(0.0, dot(off, off) - along * along))
                if perp > NEAR:
                    return None
            elif any(abs(a["origin"][i] - b["origin"][i]) > NEAR for i in range(3)):
                return None
        d = abs(a["radius"] - b["radius"])
        if d < NEAR:
            return None
        inner, outer = (a, b) if a["radius"] < b["radius"] else (b, a)
        # Material lies between them when the inner surface is a cavity, which
        # `orientation` false marks, and the outer one is the part's outside.
        between = (not inner["solid_inside"]) and outer["solid_inside"]
        return d, "wall" if between else "not a wall", "coaxial or concentric"
    return None


def main(only: str | None = None) -> int:
    with api.sync_playwright() as pw:
        browser, ctx, page = api.connect(pw)
        for tab, eid in TABS.items():
            if only and tab != only:
                continue
            print(f"\n{tab}")
            for part in read(page, eid):
                got = []
                for a, b in itertools.combinations(part["faces"], 2):
                    if tuple(sorted((a["id"], b["id"]))) in part["adjacent"]:
                        continue
                    m = measure(a, b)
                    u = direction(a, b)
                    if m and side_by_side(a, b, u) and reaches(a, b, u, m[0]):
                        got.append((m[0], m[1], m[2], a["id"], a["type"], b["id"], b["type"]))
                got.sort()
                # A distance of zero is two surfaces touching, which is a tangency
                # rather than a wall; the collar meeting the clip body is one.
                touching = [g for g in got if g[0] < NEAR]
                walls = [g for g in got if g[1] == "wall" and g[0] >= NEAR]
                print(f"  {part['name']}: {len(part['faces'])} faces,"
                      f" {len(got)} measurable pairs, {len(walls)} of them walls")
                for g in got[:8]:
                    print(f"      {g[0]:8.4f} mm  {g[1]:<6} {g[2]:<22}"
                          f" {g[4]} {g[3]} to {g[6]} {g[5]}")
                if touching:
                    print(f"      {len(touching)} tangency at 0.0000 mm:"
                          + ", ".join(f" {g[4]} {g[3]} to {g[6]} {g[5]}" for g in touching[:4]))
                if walls:
                    print(f"    thinnest wall: {walls[0][0]:.4f} mm"
                          f"  ({walls[0][4]} {walls[0][3]} to {walls[0][6]} {walls[0][5]})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else None))
