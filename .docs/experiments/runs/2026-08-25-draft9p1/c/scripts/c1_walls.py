"""Thinnest wall per part: two faces on the same axis line differ only in radius, and that
gap IS the wall. Cylinders count as coaxial when their axes are parallel and their origins
lie on the same line; a sphere counts when its centre sits on that line."""
import json, itertools

RAW = json.loads(open("/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/"
                      "runs/2026-08-25-draft9p1/c/c1-raw.json").read())


def vec(v, s=1.0):
    if isinstance(v, dict):
        return tuple(v.get(k, 0.0) * s for k in "xyz")
    if isinstance(v, (list, tuple)) and len(v) == 3:
        return tuple(float(x) * s for x in v)
    return (0.0, 0.0, 0.0)


def sub(a, b):
    return tuple(a[i] - b[i] for i in range(3))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def norm(a):
    return sum(x * x for x in a) ** 0.5


def coaxial(a, b):
    ta, ra, oa, xa = a
    tb, rb, ob, xb = b
    d = sub(oa, ob)
    if ta == "sphere" and tb == "sphere":
        return norm(d) < 1e-6
    ax = xb if ta == "sphere" else xa
    if ta != "sphere" and tb != "sphere" and norm(cross(xa, xb)) > 1e-6:
        return False
    return norm(cross(d, ax)) < 1e-6


for name, studio in RAW["studios"].items():
    for body in studio["bodydetails"].get("bodies", []):
        faces, seen = [], set()
        for f in body.get("faces", []):
            s = f.get("surface", {})
            if s.get("type") not in ("cylinder", "sphere", "cone", "torus"):
                continue
            r = s.get("radius")
            if r is None:
                continue
            k = (s["type"], round(r * 1000, 4),
                 tuple(round(v, 4) for v in vec(s.get("origin"), 1000)),
                 tuple(round(v, 4) for v in vec(s.get("axis"))))
            if k in seen:
                continue
            seen.add(k)
            faces.append(k)
        pairs, done = [], set()
        for a, b in itertools.combinations(faces, 2):
            gap = round(abs(a[1] - b[1]), 4)
            if gap < 1e-6 or not coaxial(a, b):
                continue
            key = tuple(sorted([(a[0], a[1]), (b[0], b[1])]))
            if key in done:
                continue
            done.add(key)
            pairs.append((gap, a, b))
        pairs.sort()
        print(f"--- {name}")
        for gap, a, b in pairs[:5]:
            print(f"    wall {gap:8.4f}  {a[0][:4]} r={a[1]:<9} vs {b[0][:4]} r={b[1]:<9}"
                  f"  at {a[2]} / {b[2]}")
        if not pairs:
            print("    no coaxial pair")
