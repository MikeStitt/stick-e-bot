"""Every wall the face dump can measure exactly: coaxial or concentric pairs.

A shell offsets each face inward, so a shelled surface and its offset share an origin and an axis
and differ only in radius. That radius gap IS the wall, measured, not estimated. This finds every
such pair. It does not find a wall between two faces that are not concentric — that needs
evDistance, which is what `POST .../featurescript` is for.
"""
import json, sys, itertools

DUMP = json.loads(open(sys.argv[1]).read())


def vec(v, scale=1.0):
    if not isinstance(v, dict):
        return (0.0, 0.0, 0.0)
    return tuple(round(v.get(k, 0.0) * scale, 3) for k in "xyz")


faces = []
for body in DUMP.get("bodies", []):
    for f in body.get("faces", []):
        s = f.get("surface", {})
        if s.get("type") not in ("CYLINDER", "SPHERE", "CONE", "TORUS"):
            continue
        r = s.get("radius")
        if r is None:
            continue
        faces.append((s["type"], round(r * 1000, 4), vec(s.get("origin"), 1000),
                      vec(s.get("axis"))))

seen, pairs = set(), []
for a, b in itertools.combinations(faces, 2):
    if a[2] != b[2] or a[3] != b[3]:
        continue
    gap = round(abs(a[1] - b[1]), 4)
    if gap < 1e-6:
        continue
    key = (a[0], b[0], a[1], b[1], a[2])
    if key in seen:
        continue
    seen.add(key)
    pairs.append((gap, a[0], a[1], b[0], b[1], a[2]))

for gap, ta, ra, tb, rb, o in sorted(pairs):
    print(f"  wall {gap:7.4f}   {ta:8s} r={ra:<8} vs {tb:8s} r={rb:<8} at {o}")
print(f"\npairs found: {len(pairs)}")
print(f"thinnest coaxial/concentric wall: {min(p[0] for p in pairs):.4f} mm")
