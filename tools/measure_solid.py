"""Wall or void, decided by the mesh rather than by argument.

measure_gaps.py finds how close any two faces come, and where. That distance is only a *wall* if
is between them; the slit's two sides are 0.8 apart and that is a cut. The midpoint of the closest
approach answers it: inside the solid means wall, outside means gap.

The tessellation is the whole closed boundary of the part, so inside/outside is a ray cast — fire
a ray from the midpoint and count crossings, odd is inside. Rays go up and down and must agree, and
each is nudged off the axes so it does not graze a shared edge and count it twice.

usage: measure_solid.py <tess.json> <gaps.json> [limit_mm]
"""
import json, sys, collections

TS = json.loads(open(sys.argv[1]).read())
NEAR = json.loads(open(sys.argv[2]).read())
LIMIT = float(sys.argv[3]) if len(sys.argv) > 3 else 1.25

tris = []
for body in TS.get("bodies", []):
    for f in body.get("faces", []):
        for facet in f.get("facets", []):
            v = facet.get("vertices", [])
            if len(v) != 3:
                continue
            tris.append(tuple((p.get("x", 0.0) * 1000, p.get("y", 0.0) * 1000,
                               p.get("z", 0.0) * 1000) for p in v))
print(f"triangles: {len(tris)}")

CELL = 2.0
grid = collections.defaultdict(list)
for i, t in enumerate(tris):
    xs, ys = [p[0] for p in t], [p[1] for p in t]
    for cx in range(int(min(xs) // CELL), int(max(xs) // CELL) + 1):
        for cy in range(int(min(ys) // CELL), int(max(ys) // CELL) + 1):
            grid[(cx, cy)].append(i)


def crossings(p, up):
    """Count triangles the vertical ray from p crosses, using 2D point-in-triangle in XY."""
    px, py, pz = p
    n = 0
    for i in grid.get((int(px // CELL), int(py // CELL)), ()):
        (ax, ay, az), (bx, by, bz), (cx, cy, cz) = tris[i]
        d = (by - ay) * (cx - ax) - (bx - ax) * (cy - ay)
        if abs(d) < 1e-12:
            continue
        u = ((by - ay) * (px - ax) - (bx - ax) * (py - ay)) / d
        v = ((ay - cy) * (px - ax) - (ax - cx) * (py - ay)) / d
        if u < 0 or v < 0 or u + v > 1:
            continue
        z = az + u * (cz - az) + v * (bz - az)
        if (z > pz) if up else (z < pz):
            n += 1
    return n


def is_inside(p):
    votes = []
    for dx, dy in ((0.0031, 0.0017), (-0.0023, 0.0041), (0.0043, -0.0029)):
        q = (p[0] + dx, p[1] + dy, p[2])
        up, dn = crossings(q, True) % 2, crossings(q, False) % 2
        if up == dn:
            votes.append(up)
    return (sum(votes) * 2 > len(votes)) if votes else None


walls, voids, unsure = [], [], []
for r in NEAR:
    if r["gap"] >= LIMIT:
        continue
    verdict = is_inside(r["mid"])
    (walls if verdict else voids if verdict is False else unsure).append(r)

print(f"pairs tested: {len(walls) + len(voids) + len(unsure)}   "
      f"walls {len(walls)}   voids {len(voids)}   undecided {len(unsure)}\n")
for label, rows in (("WALL", walls), ("undecided", unsure)):
    seen = set()
    for r in sorted(rows, key=lambda r: r["gap"]):
        k = (round(r["gap"], 4), r["ka"], r["kb"])
        if k in seen:
            continue
        seen.add(k)
        m = [round(c, 3) for c in r["mid"]]
        print(f"  {label:9s} {r['gap']:7.4f} mm  {r['ka']:8s} {r['a']:6s} vs "
              f"{r['kb']:8s} {r['b']:6s}  at {m}")
if walls:
    print(f"\nthinnest wall anywhere: {min(r['gap'] for r in walls):.4f} mm")
print(f"closest void (a cut, not plastic): {min((r['gap'] for r in voids), default=None)}")
