"""The flat half of the wall search: parallel planes that actually have material between them.

measure_walls.py covers curved walls, where shell leaves a concentric pair. This covers the flat
Spacing alone does not make a wall: two planes 0.3 apart are a wall only if the solid lies between
them. bodydetails says which side that is. Each face carries `orientation`, and its surface carries
`isOrientedWithFace`; multiply the two into the surface normal and you get the face's outward
normal, which points away from material. So plane A at offset dA with outward normal +n has
material below dA, plane B with outward normal -n has material above dB, and the pair encloses a
wall of dA - dB only when dB < dA. Any other arrangement is a void.
"""
import json, sys, itertools

DUMP = json.loads(open(sys.argv[1]).read())


def vec(v, scale=1.0):
    return tuple(v.get(k, 0.0) * scale for k in "xyz")


planes = []
for body in DUMP.get("bodies", []):
    for f in body.get("faces", []):
        s = f.get("surface", {})
        if s.get("type") != "PLANE":
            continue
        sign = (1 if f.get("orientation") else -1) * (1 if s.get("isOrientedWithFace") else -1)
        n = tuple(round(c * sign, 6) for c in vec(s.get("normal", {})))
        o = vec(s.get("origin", {}), 1000)
        offset = round(sum(x * y for x, y in zip(o, n)), 4)
        planes.append((n, offset, round(f.get("area", 0) * 1e6, 3)))

print(f"planar faces: {len(planes)}")
walls, voids = {}, {}
for a, b in itertools.combinations(planes, 2):
    dot = sum(x * y for x, y in zip(a[0], b[0]))
    if abs(dot + 1) > 1e-6:          # opposed normals -> candidate wall
        if abs(dot - 1) < 1e-6:      # same-facing -> a step, never a wall
            continue
        continue
    hi, lo = (a, b) if a[0] > b[0] else (b, a)
    # measure along hi's outward normal: material runs from -lo[1] up to hi[1]
    t = round(hi[1] + lo[1], 4)
    (walls if t > 1e-6 else voids)[abs(t)] = (hi[0], hi[2], lo[2])

for label, table in (("wall", walls), ("void", voids)):
    for gap in sorted(table)[:8]:
        n, aa, ab = table[gap]
        print(f"  {label} {gap:8.4f}  outward {n}  areas {aa} / {ab} mm^2")
if walls:
    print(f"\nthinnest flat wall: {min(walls):.4f} mm")
