"""Every wall the face dump can measure exactly: coaxial or concentric pairs.

    uv run --project . python src/stickbot/measure_walls.py <bodydetails.json>

A shell offsets each face inward, so a shelled surface and its offset share an origin and an axis
and differ only in radius. That radius gap IS the wall, measured, not estimated. This finds every
such pair. It does not find a wall between two faces that are not concentric — that needs
evDistance, which is what `POST .../featurescript` is for.

**Read both shapes `bodydetails` has answered in.** It named surfaces `CYLINDER` and gave each
vector as an `{x, y, z}` map; it now names them `cylinder` and gives a list. Written for the first
only, this filtered every face out, printed `pairs found: 0` on a sound model and then raised on
the minimum of an empty sequence — a silent wrong answer followed by a crash that pointed at the
wrong line. Both shapes are accepted here and a dump with no pair says so plainly.
"""
import json, sys, itertools

DUMP = json.loads(open(sys.argv[1]).read())


def vec(v, scale=1.0):
    """A point or a direction, however the route spelled it."""
    if isinstance(v, dict):
        return tuple(round(v.get(k, 0.0) * scale, 3) for k in "xyz")
    if isinstance(v, (list, tuple)) and len(v) >= 3:
        return tuple(round(float(v[i]) * scale, 3) for i in range(3))
    return (0.0, 0.0, 0.0)


faces = []
for body in DUMP.get("bodies", []):
    for f in body.get("faces", []):
        s = f.get("surface", {})
        if (s.get("type") or "").upper() not in ("CYLINDER", "SPHERE", "CONE", "TORUS"):
            continue
        r = s.get("radius")
        if r is None:
            continue
        faces.append((s["type"].upper(), round(r * 1000, 4), vec(s.get("origin"), 1000),
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
print(f"\npairs found: {len(pairs)}   from {len(faces)} curved faces")
if pairs:
    print(f"thinnest coaxial/concentric wall: {min(p[0] for p in pairs):.4f} mm")
else:
    print("no coaxial or concentric pair in this dump, so no wall it can measure exactly")
