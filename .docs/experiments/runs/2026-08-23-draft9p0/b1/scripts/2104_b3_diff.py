"""B3 — what moved when #torsoH went 96 -> 120."""
import json, sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
A = json.load(open(D + sys.argv[1]))
B = json.load(open(D + sys.argv[2]))
MM = 1000.0

def boxes(rec):
    out = {}
    for prt in rec["parts"]:
        b = rec["partboxes"][prt["partId"]]
        out[prt["name"]] = [round(b[k] * MM, 3) for k in
                            ("lowX", "lowY", "lowZ", "highX", "highY", "highZ")]
    return out

def radii(rec):
    out = {}
    for body in rec["bodydetails"]["bodies"]:
        for f in body["faces"]:
            s = f.get("surface") or {}
            if s.get("type") in ("cylinder", "sphere"):
                out.setdefault(round(s["radius"] * MM, 3), 0)
                out[round(s["radius"] * MM, 3)] += 1
    return out

print(f"{'studio / part':22} {'96 mm':>34}   {'120 mm':>34}")
for name in A:
    ba, bb = boxes(A[name]), boxes(B[name])
    for prt in sorted(set(ba) | set(bb)):
        va, vb = ba.get(prt), bb.get(prt)
        mark = "  " if va == vb else "->"
        f = lambda v: "gone" if v is None else " ".join(f"{x:7.2f}" for x in v)
        print(f"{name[:12]:12} {prt[:9]:9} {f(va)}  {mark} {f(vb)}")
print()
for name in A:
    ra, rb = radii(A[name]), radii(B[name])
    keys = sorted(set(ra) | set(rb))
    print(f"{name:16} 96: " + ", ".join(f"{k}x{ra[k]}" for k in keys if k in ra))
    print(f"{'':16}120: " + ", ".join(f"{k}x{rb[k]}" for k in keys if k in rb))
