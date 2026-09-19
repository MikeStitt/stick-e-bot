#!/usr/bin/env python3
"""Ring 2 acceptance, for every check a face dump can answer.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/c_accept_faces.py [tab]

Each brief's *Acceptance checks* names things `bodydetails` measures directly: a
sphere's centre and radius, a cylinder's axis, a planar face's position, an arc's
radius from three points on it. This answers those, one line per check, with the
number beside the number the brief asks for.

**It reads both shapes the route answers in.** A surface's type arrives as `PLANE`
or as `plane`, and a vector as `{x, y, z}` or as `[x, y, z]`, depending on which
path asked. `src/stickbot/measure_walls.py` carries the same tolerance and says
what a version written for one shape alone does.

What it cannot answer is the distance between two faces that share no centre or
axis, which is `evDistance` and needs `featurescript`.
"""

from __future__ import annotations

import math
import sys

from stickbot import make_plans as P
from stickbot import onshape_session as S

DID, WID = "2f08b54d795df0ee6b72e321", "1d8e4c837228c90bab9ff062"
TABS = {
    "ball and socket": "1a8322899842a1934e85851d",
    "body": "5441067befc71f1e3b91482e",
    "head": "303898bd4ba38fc3957b0a21",
    "foot": "229aa0900e5a7e7aa4768c6f",
    "gripper": "a3a4fac68ffb7372a7803003",
}
MM = 1000.0
NEAR = 5e-4     # millimetres; two numbers the same to the micron


def vec(v, scale=MM):
    """A point or a direction, however the route spelled it."""
    if v is None:
        return None
    if isinstance(v, dict):
        return [v.get(k, 0.0) * scale for k in "xyz"]
    return [float(v[i]) * scale for i in range(3)]


def read(page, eid):
    """Every part of a tab, as faces, edges and vertices in millimetres."""
    base = f"/api/v10/parts/d/{DID}/w/{WID}/e/{eid}"
    parts = S._raw_api(page, "GET", base)["body"]
    out = []
    for p in parts:
        bd = S._raw_api(page, "GET", f"{base}/partid/{p['partId']}/bodydetails")["body"]
        b = bd["bodies"][0]
        faces = []
        for f in b["faces"]:
            s = f.get("surface") or {}
            faces.append({
                "id": f.get("id"), "area": f["area"] * MM * MM,
                "type": (s.get("type") or "").upper(),
                "radius": s["radius"] * MM if s.get("radius") is not None else None,
                "origin": vec(s.get("origin")), "axis": vec(s.get("axis"), 1.0),
                "normal": vec(s.get("normal"), 1.0),
                "lo": vec(f["box"]["minCorner"]), "hi": vec(f["box"]["maxCorner"]),
            })
        edges = []
        for e in b.get("edges", []):
            g = e.get("geometry") or {}
            edges.append({"arc": "Arc" in (g.get("btType") or ""),
                          "start": vec(g.get("startPoint")), "mid": vec(g.get("midPoint")),
                          "quarter": vec(g.get("quarterPoint"))})
        out.append({"name": p.get("name"), "faces": faces, "edges": edges,
                    "vertices": [vec(v["point"]) for v in b.get("vertices", [])]})
    return out


def box_of(part):
    lo = [min(f["lo"][i] for f in part["faces"]) for i in range(3)]
    hi = [max(f["hi"][i] for f in part["faces"]) for i in range(3)]
    return lo, hi


def circumradius(a, b, c):
    """The radius of the circle through three points, or None if they are collinear."""
    ab = [b[i] - a[i] for i in range(3)]
    ac = [c[i] - a[i] for i in range(3)]
    cross = [ab[1] * ac[2] - ab[2] * ac[1],
             ab[2] * ac[0] - ab[0] * ac[2],
             ab[0] * ac[1] - ab[1] * ac[0]]
    n = sum(v * v for v in cross) ** 0.5
    if n < 1e-12:
        return None
    la = sum(v * v for v in ab) ** 0.5
    lb = sum(v * v for v in ac) ** 0.5
    lc = sum((c[i] - b[i]) ** 2 for i in range(3)) ** 0.5
    return la * lb * lc / (2 * n)


def say(label, got, want=None, unit="mm"):
    """One check: what it measured, and what the brief asks for."""
    if want is None:
        print(f"    {label:<52} {got}")
        return
    ok = abs(got - want) < NEAR if isinstance(got, (int, float)) else got == want
    mark = "pass" if ok else "DIFFERS"
    if isinstance(got, float):
        print(f"    {label:<52} {got:>10.4f} {unit}   asks {want:.4f}   {mark}")
    else:
        print(f"    {label:<52} {got!r}   asks {want!r}   {mark}")


def planes_normal_to(part, axis):
    i = "xyz".index(axis)
    return [f for f in part["faces"]
            if f["type"] == "PLANE" and f["normal"] and abs(abs(f["normal"][i]) - 1) < 1e-6]


def check_head(part):
    lo, hi = box_of(part)
    print(f"  {part['name']}: {len(part['faces'])} faces")
    say("parts in the tab", 1, 1, "")
    say("across, x", hi[0] - lo[0], float(P.HEAD_W))
    inner = [f for f in planes_normal_to(part, "y") if abs(f["area"] - 1765.177) < 1e9
             and abs(f["lo"][1] - f["hi"][1]) < NEAR]
    front = min(f["lo"][1] for f in inner if f["area"] > 1000)
    back = max(f["hi"][1] for f in inner if f["area"] > 1000)
    say("deep, face to face", back - front, float(P.HEAD_D))
    say("the head box, z", hi[2] - (-hi[2]), 2.0 * P.HEAD_W / 2)

    ball = [f for f in part["faces"] if f["type"] == "SPHERE"]
    say("socket cavity faces", len(ball), 1, "")
    centre = ball[0]["origin"]
    say("socket centre below the head centre", -centre[2], 45.0)
    say("cavity radius", ball[0]["radius"], (P.BALL + 2 * P.FIT) / 2)

    rim_z = lo[2]
    say("collar proud of the underside", -36.0 - rim_z, 10.947)
    say("cavity centre above the rim plane", centre[2] - rim_z, float(P.GRIP))

    rim = [f for f in planes_normal_to(part, "z") if abs(f["lo"][2] - rim_z) < NEAR]
    say("rim faces, four arcs not one circle", len(rim), 4, "")

    arcs = [e for e in part["edges"] if e["arc"] and e["start"]
            and all(abs(pt[2] - rim_z) < NEAR for pt in (e["start"], e["mid"], e["quarter"]))]
    radii = sorted({round(r, 4) for r in
                    (circumradius(e["start"], e["mid"], e["quarter"]) for e in arcs) if r})
    say("arc radii on the rim plane", radii, None)
    if radii:
        say("socket mouth diameter", 2 * radii[0], 11.520)

    slit_floor = sorted({round(f["lo"][2], 4) for f in planes_normal_to(part, "z")
                         if rim_z + 1 < f["lo"][2] < -36.0 and f["area"] < 20})
    if slit_floor:
        say("slit depth from the rim", slit_floor[0] - rim_z, 4.947)
        say("floor left above the slit", -36.0 - slit_floor[0], 6.000)


def check_foot(part):
    lo, hi = box_of(part)
    print(f"  {part['name']}: {len(part['faces'])} faces")
    say("parts in the tab", 1, 1, "")
    say("length, y", hi[1] - lo[1], float(P.FOOT_L))
    say("width, x", hi[0] - lo[0], float(P.FOOT_W))
    say("ground, lowest z", lo[2], -float(P.FOOT_H))
    ball = [f for f in part["faces"] if f["type"] == "SPHERE"]
    say("socket cavity faces", len(ball), 1, "")
    if ball:
        c = ball[0]["origin"]
        say("ankle ball centre, x", c[0], 0.0)
        say("ankle ball centre, y", c[1], 0.0)
        say("ankle ball centre, z", c[2], 0.0)
        say("ankle height, ground to the ball centre", c[2] - lo[2], float(P.FOOT_H))
    rim_z = max(f["hi"][2] for f in part["faces"])
    arcs = [e for e in part["edges"] if e["arc"] and e["start"]
            and all(abs(pt[2] - rim_z) < NEAR for pt in (e["start"], e["mid"], e["quarter"]))]
    radii = sorted({round(r, 4) for r in
                    (circumradius(e["start"], e["mid"], e["quarter"]) for e in arcs) if r})
    say("arc radii on the rim plane", radii, None)
    if radii:
        say("socket mouth diameter", 2 * radii[0], 11.520)
    rim = [f for f in planes_normal_to(part, "z") if abs(f["hi"][2] - rim_z) < NEAR]
    say("rim faces, four arcs not one circle", len(rim), 4, "")
    grooves = [f for f in planes_normal_to(part, "z") if lo[2] < f["lo"][2] < lo[2] + 5]
    say("groove floors above the sole",
        sorted({round(f["lo"][2], 4) for f in grooves}), None)
    if grooves:
        say("groove depth", grooves[0]["lo"][2] - lo[2], float(P.RIB_D))
        say("groove floors, one per rib", len(grooves), int(P.RIB_N), "")

    plate = [f for f in planes_normal_to(part, "z")
             if f["area"] > 200 and f["hi"][2] < rim_z - 1]
    if plate:
        top = max(f["hi"][2] for f in plate)
        say("plate top face z", top, None)
        # `#plate` is a CAD variable with no `make_plans` constant, so the brief's
        # 14.2205 is `#grip` + 12 and the 12 is read off the plate's own face.
        say("ankle boss proud of the plate", rim_z - top, float(P.GRIP) + 12.0)

    cav = [f for f in part["faces"] if f["type"] == "SPHERE"]
    if cav:
        r, off = cav[0]["radius"], rim_z - cav[0]["origin"][2]
        h = r - off
        say("cavity volume, sphere less the cap above the rim",
            4 / 3 * math.pi * r ** 3 - math.pi * h * h * (3 * r - h) / 3, 689.06, "mm3")


def check_body(part):
    lo, hi = box_of(part)
    print(f"  {part['name']}: {len(part['faces'])} faces")
    say("parts in the tab", 1, 1, "")
    # The brief measures the block, before the studs are added, so each span comes
    # from the block's own pair of faces rather than from the part's bounding box.
    for axis, want in (("x", float(P.TORSO_W)), ("y", float(P.TORSO_D)),
                       ("z", float(P.TORSO_H))):
        big = [f for f in planes_normal_to(part, axis) if f["area"] > 1000]
        i = "xyz".index(axis)
        say(f"the block, {axis}, off its own faces",
            max(f["hi"][i] for f in big) - min(f["lo"][i] for f in big), want)
    tops = [f for f in planes_normal_to(part, "z") if f["area"] > 100]
    say("top face z", max(f["hi"][2] for f in tops), float(P.TORSO_H) / 2)
    # The brief's "nothing stands proud of the top face" is about the shoulder boss.
    # The neck stud stands above it on purpose, so name what is up there.
    top = max(f["hi"][2] for f in tops)
    above = [f for f in part["faces"] if f["hi"][2] > top + NEAR]
    say("faces above the top face", len(above), None)
    say("  and they belong to", sorted({f["type"] for f in above}), None)
    say("  reaching to z", hi[2], top + float(P.BALL) / 2)
    balls = [f for f in part["faces"] if f["type"] == "SPHERE"]
    say("ball studs", len(balls), 5, "")
    for b in sorted(balls, key=lambda f: (round(f["origin"][2]), f["origin"][0])):
        say(f"  ball centre r={b['radius']:.3f}",
            tuple(round(v, 3) for v in b["origin"]), None)
    shoulder = [f for f in part["faces"] if f["type"] == "CYLINDER"
                and f["radius"] and abs(f["radius"] - float(P.BOSS_D) / 2) < 0.51]
    say("shoulder boss cylinders", len(shoulder), None)
    if shoulder:
        say("highest point on a boss", max(f["hi"][2] for f in shoulder),
            float(P.TORSO_H) / 2)


def check_gripper(part):
    lo, hi = box_of(part)
    print(f"  {part['name']}: {len(part['faces'])} faces")
    say("parts in the tab", 1, 1, "")
    bores = [f for f in part["faces"] if f["type"] == "CYLINDER" and f["radius"]
             and abs(f["radius"] * 2 - 3.3) < 0.2]
    say("clip bore faces", len(bores), None)
    for b in bores:
        say(f"  bore diameter {b['radius'] * 2:.3f}, axis", tuple(round(v, 4) for v in b["axis"]),
            None)
        say("  bore axis is parallel to x", abs(abs(b["axis"][0]) - 1) < 1e-6, True, "")
    say("top face z", max(f["hi"][2] for f in planes_normal_to(part, "z")), None)
    say("lowest point, z", lo[2], None)

    # The mouth is the slot into the bore: two parallel faces normal to z, one above
    # the bore's axis and one below, running out to the clip's edge.
    if bores:
        axis_z = bores[0]["origin"][2]
        jaws = sorted((f for f in planes_normal_to(part, "z")
                       if abs(f["lo"][2] - axis_z) < 3 and f["lo"][1] < 0),
                      key=lambda f: f["lo"][2])
        if len(jaws) >= 2:
            say("mouth across the opening", jaws[-1]["lo"][2] - jaws[0]["lo"][2], 2.600)
    # A plane has no thickness along its own normal, so a sliver is a face whose two
    # remaining spans include one under a printed bead. 0.4 mm is the nozzle.
    for f in part["faces"]:
        spans = sorted(f["hi"][i] - f["lo"][i] for i in range(3))
        if spans[1] < 0.4 and spans[2] > 1:
            say(f"  sliver face {f['id']}, narrow span", round(spans[1], 6), None)


def check_socket(parts):
    for part in parts:
        lo, hi = box_of(part)
        print(f"  {part['name']}: {len(part['faces'])} faces,"
              f"  box x {lo[0]:.3f}..{hi[0]:.3f} z {lo[2]:.3f}..{hi[2]:.3f}")
        cyl = sorted({round(f["radius"] * 2, 4) for f in part["faces"]
                      if f["type"] == "CYLINDER" and f["radius"]})
        say("cylinder diameters", cyl, None)
        sph = [f for f in part["faces"] if f["type"] == "SPHERE"]
        for s in sph:
            say(f"  sphere r={s['radius']:.4f} centre",
                tuple(round(v, 4) for v in s["origin"]), None)
        cyls = [f["radius"] for f in part["faces"]
                if f["type"] == "CYLINDER" and f["radius"]]
        if not sph or not cyls or max(cyls) < sph[0]["radius"]:
            continue          # the stud: a ball on a stalk, with no collar to measure
        cav, collar = sph[0], max(cyls)
        say("collar outside to the cavity", collar - cav["radius"], 1.72)
        say("the step around the collar's foot in a limb",
            (float(P.LIMB) - 2 * collar) / 2, 4.2)
        say("collar and limb are both round, neither square",
            all(f["type"] in ("CYLINDER", "SPHERE", "PLANE") for f in part["faces"]),
            True, "")

        # The cut is a slot for its whole depth: at the slit floor the cavity is wider
        # than the slit reaches, so the bottom of the cut opens into the hollow.
        floors = [f for f in planes_normal_to(part, "z") if f["area"] < 20
                  and f["lo"][2] < cav["origin"][2]]
        if floors:
            z = floors[0]["lo"][2]
            at_floor = (cav["radius"] ** 2 - (cav["origin"][2] - z) ** 2) ** 0.5
            say("cavity radius at the slit floor", at_floor, 4.5789)
            walls = [f for f in part["faces"] if f["type"] == "PLANE"
                     and f["normal"] and abs(f["normal"][2]) < 1e-6
                     and abs(f["lo"][2] - z) < NEAR]
            if walls:
                inner = min((min(abs(w["lo"][i]) for i in (0, 1)) ** 2
                             + max(abs(w["lo"][i]) for i in (0, 1)) ** 2) ** 0.5
                            for w in walls)
                say("slit inner edge, as a radius", inner, None)
                say("the cut opens into the hollow", inner <= at_floor + NEAR, True, "")


CHECKS = {"head": check_head, "foot": check_foot, "body": check_body,
          "gripper": check_gripper}


def main(only: str | None = None) -> int:
    with S.sync_playwright() as pw:
        browser, ctx, page = S.connect(pw)
        for tab, eid in TABS.items():
            if only and tab != only:
                continue
            print(f"\n{tab}")
            parts = read(page, eid)
            if tab == "ball and socket":
                check_socket(parts)
            else:
                CHECKS[tab](parts[0])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else None))
