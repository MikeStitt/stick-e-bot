"""B3 — the torso's studs, and the two bosses that do not follow."""
import json
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
MM = 1000.0
for tag, path in (("96", "b2_raw.json"), ("120", "b3_raw_120.json")):
    rec = json.load(open(D + path))["body"]
    print(f"--- torso at {tag}")
    for body in rec["bodydetails"]["bodies"]:
        for f in body["faces"]:
            s = f.get("surface") or {}
            if s.get("type") in ("cylinder", "sphere"):
                o = [round(v * MM, 2) for v in s["origin"]]
                ax = [round(v, 2) for v in s.get("axis", [0, 0, 0])]
                print(f"  {s['type'][:3]} r={round(s['radius']*MM,3):7}  at {o}  axis {ax}")
