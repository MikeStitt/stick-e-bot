"""Phase C — every part's curved faces and every planar cut face, out of c1-raw.json."""
import sys, json, collections
RAW = "/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/runs/2026-08-25-draft9p1/c/c1-raw.json"
d = json.load(open(RAW))
want = sys.argv[1:] or list(d["studios"])
for name in want:
    rec = d["studios"][name]
    byid = {p["partId"]: p.get("name", p["partId"]) for p in rec["parts"]}
    print("=" * 78)
    print(name)
    for bd in rec["bodydetails"]["bodies"]:
        print(f"--- {byid.get(bd['id'], bd['id'])}   ({len(bd['faces'])} faces)")
        curved = collections.Counter()
        planes = collections.defaultdict(float)
        other = collections.Counter()
        for f in bd["faces"]:
            s = f.get("surface", {}) or {}
            t = s.get("type"); a = f.get("area", 0) * 1e6
            if t == "plane":
                n = tuple(round(v, 4) for v in s.get("normal", []))
                o = [round(v * 1000, 4) for v in s.get("origin", [])]
                off = round(sum(n[i] * o[i] for i in range(3)), 4)
                planes[(n, off)] += a
            elif t in ("cylinder", "cone", "sphere", "torus"):
                key = (t, round(s.get("radius", 0) * 1000, 4),
                       tuple(round(v, 3) for v in s.get("axis", [])),
                       tuple(round(v * 1000, 3) for v in s.get("origin", [])))
                curved[key] += 1
            else:
                other[t] += 1
        for (t, r, ax, o), n in sorted(curved.items(), key=lambda kv: (kv[0][0], -kv[0][1])):
            print(f"    {t:8s} r {r:8.4f}  axis {str(list(ax)):22s} at {list(o)}  x{n}")
        if other: print("    other surfaces:", dict(other))
        print("    planes, by normal and signed offset (mm), with total area (mm^2):")
        for (n, off), a in sorted(planes.items(), key=lambda kv: (kv[0][0], kv[0][1])):
            print(f"      n {str(list(n)):26s} off {off:10.4f}   area {a:10.3f}")
