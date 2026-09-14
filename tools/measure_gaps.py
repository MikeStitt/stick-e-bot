"""The closure: how close does any face come to any other face, over the whole part.

measure_walls.py is exact but only sees concentric curved pairs, and measure_planes.py only
sees parallel planes. Neither can look at a slit's flat cut face against the cavity sphere, and
neither can touch the two OTHER faces, which `bodydetails` describes with no geometry at all.

`GET .../tessellatedfaces` answers 200 while `POST .../featurescript` is throttled, and it returns
real triangles for every face including the OTHER ones. Their vertices, run through a spatial grid,
give the closest approach between every pair of faces that do not already share an edge. That is
not the same thing as a wall — a slit's two sides are 0.8 apart and that is a cut, not plastic —
so this reports the pairs and their surface types, and the reading is done by hand against the
material-side test in measure_planes.py.

Distances are sampled at vertices, so a reported gap can overstate the true minimum by up to about
one triangle edge. Tessellation is requested at a 0.0002 m chord tolerance to keep that small.

usage: measure_gaps.py <bodydetails.json> <tess.json> [limit_mm]
"""
import json, sys, math, collections

BD = json.loads(open(sys.argv[1]).read())
TS = json.loads(open(sys.argv[2]).read())
LIMIT = float(sys.argv[3]) if len(sys.argv) > 3 else 1.25
CELL = LIMIT

kind, edges = {}, {}
for body in BD.get("bodies", []):
    for f in body.get("faces", []):
        kind[f["id"]] = f["surface"]["type"]
        edges[f["id"]] = {c["edgeId"] for l in f.get("loops", []) for c in l.get("coedges", [])}

pts = []
for body in TS.get("bodies", []):
    for f in body.get("faces", []):
        fid, seen = f["id"], set()
        for facet in f.get("facets", []):
            for v in facet.get("vertices", []):
                k = (round(v.get("x", 0.0) * 1e5), round(v.get("y", 0.0) * 1e5),
                     round(v.get("z", 0.0) * 1e5))
                if k in seen:
                    continue
                seen.add(k)
                pts.append((fid, v.get("x", 0.0) * 1000, v.get("y", 0.0) * 1000,
                            v.get("z", 0.0) * 1000))
print(f"faces {len(kind)}   sampled points {len(pts)}")

grid = collections.defaultdict(list)
for i, (fid, x, y, z) in enumerate(pts):
    grid[(int(math.floor(x / CELL)), int(math.floor(y / CELL)),
          int(math.floor(z / CELL)))].append(i)

best = {}
NB = [(a, b, c) for a in (-1, 0, 1) for b in (-1, 0, 1) for c in (-1, 0, 1)]
for cell, idxs in grid.items():
    near = []
    for d in NB:
        near.extend(grid.get((cell[0] + d[0], cell[1] + d[1], cell[2] + d[2]), ()))
    for i in idxs:
        fa, xa, ya, za = pts[i]
        ea = edges[fa]
        for j in near:
            fb, xb, yb, zb = pts[j]
            if fb == fa or ea & edges[fb]:
                continue
            key = (fa, fb) if fa < fb else (fb, fa)
            d2 = (xa - xb) ** 2 + (ya - yb) ** 2 + (za - zb) ** 2
            if d2 < best.get(key, (LIMIT * LIMIT, None))[0]:
                best[key] = (d2, ((xa + xb) / 2, (ya + yb) / 2, (za + zb) / 2))

rows = sorted((math.sqrt(v[0]), k, v[1]) for k, v in best.items())
print(f"non-adjacent face pairs closer than {LIMIT} mm: {len(rows)}\n")
for d, (a, b), mid in rows:
    print(f"  {d:7.4f} mm   {kind[a]:8s} {a:6s}  vs  {kind[b]:8s} {b}")
json.dump([{"gap": d, "a": a, "b": b, "ka": kind[a], "kb": kind[b], "mid": mid}
           for d, (a, b), mid in rows], open("gaps.json", "w"))
