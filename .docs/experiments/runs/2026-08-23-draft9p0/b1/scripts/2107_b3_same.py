"""B3 — after the restore, is the model bit-for-bit what B2 read?"""
import json
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
A = json.load(open(D + "b2_raw.json")); C = json.load(open(D + "b3_raw_96.json"))
MM = 1000.0
def sig(rec):
    """Everything geometric, with the ids that change on every regen left out."""
    out = {"boxes": {}, "radii": {}, "planes": {}, "volumes": {}}
    for prt in rec["parts"]:
        b = rec["partboxes"][prt["partId"]]
        out["boxes"][prt["name"]] = [round(b[k] * MM, 6) for k in
                                     ("lowX","lowY","lowZ","highX","highY","highZ")]
    for body in rec["bodydetails"]["bodies"]:
        for f in body["faces"]:
            s = f.get("surface") or {}
            if s.get("type") in ("cylinder", "sphere"):
                k = round(s["radius"] * MM, 6)
                out["radii"][k] = out["radii"].get(k, 0) + 1
            if s.get("type") == "plane" and abs(abs(s["normal"][2]) - 1) < 1e-9:
                k = round(s["origin"][2] * MM, 6)
                out["planes"][k] = out["planes"].get(k, 0) + 1
            out["volumes"][round(f.get("area", 0) * MM * MM, 4)] = 1
    return out
bad = 0
for name in A:
    sa, sc = sig(A[name]), sig(C[name])
    for key in ("boxes", "radii", "planes", "volumes"):
        if sa[key] != sc[key]:
            bad += 1
            print(f"{name}: {key} differs")
            for k in sorted(set(sa[key]) | set(sc[key]), key=str):
                if sa[key].get(k) != sc[key].get(k):
                    print(f"    {k!r}: 96 was {sa[key].get(k)}, back is {sc[key].get(k)}")
print("identical" if not bad else f"{bad} differences")
