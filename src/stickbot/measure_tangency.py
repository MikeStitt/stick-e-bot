"""Tangent or creased, at every edge in the part.

The head's brief asks that the profile be tangent throughout - no crease where an arc meets a
Looking at a render only shows that no crease is visible, which is not the same claim. This takes
it off the geometry: two faces meeting tangentially share a normal along their common edge, so for
every pair of faces that share an edgeId, compare the facet normals on either side at the vertices
they have in common. Zero degrees is tangent, anything else is a crease of that many degrees.

Tessellation normals are facet normals, so on a curved face they lag the true surface by up to the
angle tolerance the tessellation was asked for — 0.02 rad, about 1.15 deg. Treat anything under a
couple of degrees as tangent and read the exact figure off bodydetails instead.

usage: measure_tangency.py <bodydetails.json> <tess.json>
"""
import json, sys, math, collections

BD = json.loads(open(sys.argv[1]).read())
TS = json.loads(open(sys.argv[2]).read())

kind, edges = {}, {}
for body in BD.get("bodies", []):
    for f in body.get("faces", []):
        kind[f["id"]] = f["surface"]["type"]
        edges[f["id"]] = {c["edgeId"] for l in f.get("loops", []) for c in l.get("coedges", [])}

at = collections.defaultdict(lambda: collections.defaultdict(list))
for body in TS.get("bodies", []):
    for f in body.get("faces", []):
        fid = f["id"]
        for facet in f.get("facets", []):
            n = facet.get("normal", {})
            n = (n.get("x", 0.0), n.get("y", 0.0), n.get("z", 0.0))
            for v in facet.get("vertices", []):
                k = (round(v.get("x", 0.0) * 1e5), round(v.get("y", 0.0) * 1e5),
                     round(v.get("z", 0.0) * 1e5))
                at[fid][k].append(n)


def mean_unit(ns):
    s = [sum(n[i] for n in ns) for i in range(3)]
    m = math.sqrt(sum(c * c for c in s))
    return [c / m for c in s] if m > 1e-9 else None


rows = []
for a, b in ((a, b) for a in kind for b in kind if a < b):
    if not (edges[a] & edges[b]):
        continue
    shared = set(at[a]) & set(at[b])
    if not shared:
        continue
    worst = 0.0
    for k in shared:
        na, nb = mean_unit(at[a][k]), mean_unit(at[b][k])
        if not na or not nb:
            continue
        d = max(-1.0, min(1.0, sum(x * y for x, y in zip(na, nb))))
        worst = max(worst, math.degrees(math.acos(d)))
    rows.append((worst, a, b, len(shared)))

TOL = 2.0
tangent = [r for r in rows if r[0] <= TOL]
creased = [r for r in rows if r[0] > TOL]
print(f"adjacent face pairs: {len(rows)}   tangent (<={TOL} deg): {len(tangent)}   "
      f"creased: {len(creased)}\n")
for w, a, b, n in sorted(creased, reverse=True):
    print(f"  crease {w:7.2f} deg   {kind[a]:8s} {a:6s} vs {kind[b]:8s} {b:6s}  ({n} shared pts)")
print()
for w, a, b, n in sorted(tangent, reverse=True):
    print(f"  tangent {w:6.2f} deg   {kind[a]:8s} {a:6s} vs {kind[b]:8s} {b:6s}  ({n} shared pts)")
