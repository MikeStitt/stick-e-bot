"""B3 — where a radius at 96 is a coincidence between two different rules."""
import json, sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
A = json.load(open(D + "b2_raw.json")); B = json.load(open(D + "b3_raw_120.json"))
MM = 1000.0
def cyls(rec):
    out = []
    for body in rec["bodydetails"]["bodies"]:
        for f in body["faces"]:
            s = f.get("surface") or {}
            if s.get("type") == "cylinder":
                out.append((round(s["radius"] * MM, 4),
                            tuple(round(v * MM, 2) for v in s["origin"]),
                            tuple(round(v, 3) for v in s["axis"]),
                            round(f.get("area", 0) * MM * MM, 2)))
    return sorted(out)
for name in A:
    a, b = cyls(A[name]), cyls(B[name])
    ra = sorted({x[0] for x in a}); rb = sorted({x[0] for x in b})
    print(f"{name}:")
    print(f"   96 {ra}")
    print(f"  120 {rb}")
    print(f"      counts 96 {len(a)}  120 {len(b)}")
