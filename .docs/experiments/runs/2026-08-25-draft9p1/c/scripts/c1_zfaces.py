"""Every planar face whose normal is z, by the z it sits at, with total area."""
import json
from collections import defaultdict

RAW = json.loads(open("/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/"
                      "runs/2026-08-25-draft9p1/c/c1-raw.json").read())

for name, studio in RAW["studios"].items():
    for body in studio["bodydetails"].get("bodies", []):
        zs = defaultdict(float)
        for f in body.get("faces", []):
            s = f.get("surface", {})
            if s.get("type") != "plane":
                continue
            n = [round(v, 4) for v in s.get("normal", [])]
            if abs(abs(n[2]) - 1) > 1e-6:
                continue
            o = [v * 1000 for v in s.get("origin", [])]
            zs[round(o[2], 4)] += f.get("area", 0.0) * 1e6
        print(f"--- {name}  ({body.get('id')})")
        for z in sorted(zs):
            print(f"    z {z:10.4f}   area {zs[z]:10.3f}")
