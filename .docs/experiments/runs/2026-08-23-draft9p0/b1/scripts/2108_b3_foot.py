"""B3 — the face the foot gained at z -7.4 when #torsoH went to 120."""
import json
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
MM = 1000.0
for tag, path in (("96", "b2_raw.json"), ("120", "b3_raw_120.json")):
    rec = json.load(open(D + path))["foot"]
    print(f"--- foot at {tag}")
    for body in rec["bodydetails"]["bodies"]:
        for f in body["faces"]:
            s = f.get("surface") or {}
            t = s.get("type")
            a = round(f.get("area", 0) * MM * MM, 3)
            if t == "plane" and abs(abs(s["normal"][2]) - 1) < 1e-9:
                print(f"  plane z={round(s['origin'][2]*MM,3):8}  area {a:10}")
            elif t in ("cylinder", "sphere"):
                o = [round(v * MM, 2) for v in s["origin"]]
                print(f"  {t[:3]} r={round(s['radius']*MM,3):7}  at {o}  area {a:10}")
