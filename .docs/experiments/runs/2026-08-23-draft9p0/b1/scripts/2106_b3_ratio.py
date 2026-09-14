"""B3 — which extents followed 96 -> 120 and by how much."""
import json
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
A = json.load(open(D + "b2_raw.json")); B = json.load(open(D + "b3_raw_120.json"))
MM = 1000.0
def boxes(rec):
    out = {}
    for prt in rec["parts"]:
        b = rec["partboxes"][prt["partId"]]
        out[prt["name"]] = [round(b[k] * MM, 3) for k in
                            ("lowX","lowY","lowZ","highX","highY","highZ")]
    return out
print(f"{'part':12} {'axis':4} {'96':>9} {'120':>9} {'x':>7}")
for name in A:
    ba, bb = boxes(A[name]), boxes(B[name])
    for prt in ba:
        for i, ax in enumerate("XYZ"):
            ea = ba[prt][i+3] - ba[prt][i]
            eb = bb[prt][i+3] - bb[prt][i]
            r = eb / ea if ea else 0
            flag = "" if abs(r - 1.25) < 1e-6 else ("  same" if abs(r-1) < 1e-9 else "  <<<")
            print(f"{prt[:12]:12} {ax:4} {ea:9.3f} {eb:9.3f} {r:7.4f}{flag}")
def planes(rec):
    zs = set()
    for body in rec["bodydetails"]["bodies"]:
        for f in body["faces"]:
            s = f.get("surface") or {}
            if s.get("type") == "plane" and abs(abs(s["normal"][2]) - 1) < 1e-6:
                zs.add(round(s["origin"][2] * MM, 3))
    return sorted(zs)
print()
for name in A:
    print(f"{name:16} 96: {planes(A[name])}")
    print(f"{'':16}120: {planes(B[name])}")
