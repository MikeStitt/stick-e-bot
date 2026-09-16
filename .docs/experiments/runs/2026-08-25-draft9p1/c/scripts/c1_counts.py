import json
from collections import Counter
RAW = json.loads(open("/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/"
                      "runs/2026-08-25-draft9p1/c/c1-raw.json").read())
for name in ("hinge", "u limb", "l limb", "foot", "head"):
    for body in RAW["studios"][name]["bodydetails"].get("bodies", []):
        c = Counter()
        for f in body.get("faces", []):
            s = f.get("surface", {})
            t = s.get("type")
            r = s.get("radius")
            c[(t, round(r * 1000, 4) if r else None)] += 1
        print(f"--- {name} {body.get('id')}")
        for k, v in sorted(c.items(), key=lambda kv: -kv[1])[:8]:
            print(f"    {k[0]:10s} r={k[1]}  ×{v}")
