"""March a line through the part and print where the plastic starts and stops.

The verdict in measure_solid.py is unreliable when the closest approach lands exactly on the
what happens when two faces both run out at the same edge. This settles those by walking a line and
reporting the solid runs along it: a 0.4 mm answer that is 1.2 mm deep is a narrow land on a normal
wall, and a 0.4 mm answer that is 0.4 mm deep is a thin wall.

usage: measure_line.py <tess.json> x,y,z dx,dy,dz [span_mm] [step_mm]
"""
import json, sys, collections

TS = json.loads(open(sys.argv[1]).read())
p0 = [float(v) for v in sys.argv[2].split(",")]
d = [float(v) for v in sys.argv[3].split(",")]
SPAN = float(sys.argv[4]) if len(sys.argv) > 4 else 3.0
STEP = float(sys.argv[5]) if len(sys.argv) > 5 else 0.02

tris = []
for body in TS.get("bodies", []):
    for f in body.get("faces", []):
        for facet in f.get("facets", []):
            v = facet.get("vertices", [])
            if len(v) == 3:
                tris.append(tuple((p.get("x", 0.0) * 1000, p.get("y", 0.0) * 1000,
                                   p.get("z", 0.0) * 1000) for p in v))

CELL = 2.0
grid = collections.defaultdict(list)
for i, t in enumerate(tris):
    xs, ys = [p[0] for p in t], [p[1] for p in t]
    for cx in range(int(min(xs) // CELL), int(max(xs) // CELL) + 1):
        for cy in range(int(min(ys) // CELL), int(max(ys) // CELL) + 1):
            grid[(cx, cy)].append(i)


def crossings(p, up):
    px, py, pz = p
    n = 0
    for i in grid.get((int(px // CELL), int(py // CELL)), ()):
        (ax, ay, az), (bx, by, bz), (cx, cy, cz) = tris[i]
        det = (by - ay) * (cx - ax) - (bx - ax) * (cy - ay)
        if abs(det) < 1e-12:
            continue
        u = ((by - ay) * (px - ax) - (bx - ax) * (py - ay)) / det
        v = ((ay - cy) * (px - ax) - (ax - cx) * (py - ay)) / det
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
    return bool(votes) and sum(votes) * 2 > len(votes)


n = sum(c * c for c in d) ** 0.5
d = [c / n for c in d]
print(f"triangles {len(tris)};  from {p0} along {[round(c, 4) for c in d]}, +-{SPAN} mm\n")

runs, start, t = [], None, -SPAN
while t <= SPAN + 1e-9:
    ins = is_inside([p0[i] + d[i] * t for i in range(3)])
    if ins and start is None:
        start = t
    elif not ins and start is not None:
        runs.append((start, t - STEP))
        start = None
    t = round(t + STEP, 6)
if start is not None:
    runs.append((start, SPAN))

for a, b in runs:
    print(f"  solid from t={a:+.3f} to t={b:+.3f}   thickness {b - a + STEP:.3f} mm")
if not runs:
    print("  no solid anywhere on this line")
