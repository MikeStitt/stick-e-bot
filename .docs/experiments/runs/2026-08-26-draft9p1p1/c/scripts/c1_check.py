"""Phase C — judge c1-raw.json offline, against what A1, A2, A3 and A4 claim.

Reads nothing from the network. Every number printed here comes out of the one fetch
c1_read.py made, so the checking can be rerun and argued with without touching Onshape.
"""
import json, math, sys

RAW = ("/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/runs/"
       "2026-08-26-draft9p1p1/c/c1-raw.json")


def mm(v):
    return round(v * 1000, 4)


def box(b):
    return {k: mm(v) for k, v in b.items() if isinstance(v, (int, float))}


d = json.load(open(RAW))
S = d["studios"]

print("=" * 78)
print("the variable table")
print("=" * 78)
for table in d.get("variables") or []:
    for v in table.get("variables", []):
        print(f"  {v['name']:12s} {v['expression']}")

print()
print("=" * 78)
print("every part's bounding box, in its own Part Studio")
print("=" * 78)
for name, rec in S.items():
    for prt in rec["parts"]:
        b = box(rec["partboxes"][prt["partId"]])
        print(f"  {name:16s} {prt['name']:14s} "
              f"x {b['lowX']:9.4f}..{b['highX']:9.4f} ({b['highX'] - b['lowX']:8.4f})  "
              f"y {b['lowY']:9.4f}..{b['highY']:9.4f} ({b['highY'] - b['lowY']:8.4f})  "
              f"z {b['lowZ']:9.4f}..{b['highZ']:9.4f} ({b['highZ'] - b['lowZ']:8.4f})")

print()
print("=" * 78)
print("A1 — the slit is a slot: no face at r 5.0 bounds the cut")
print("=" * 78)
bd = S["ball and socket"]["bodydetails"]
for body in bd["bodies"]:
    print(f"  body {body.get('id')}")
    for f in body["faces"]:
        s = f["surface"]
        t = s["type"]
        a = mm(mm(f.get("area", 0)))
        if t == "cylinder":
            o = s["origin"]
            print(f"    cyl    r {mm(s['radius']):8.4f}  o({mm(o[0]):8.4f},{mm(o[1]):8.4f},"
                  f"{mm(o[2]):8.4f})  area {a:10.4f}")
        elif t == "sphere":
            o = s["origin"]
            print(f"    sphere r {mm(s['radius']):8.4f}  o({mm(o[0]):8.4f},{mm(o[1]):8.4f},"
                  f"{mm(o[2]):8.4f})  area {a:10.4f}")
        elif t == "plane":
            o, n = s["origin"], s["normal"]
            print(f"    plane  n({n[0]:5.2f},{n[1]:5.2f},{n[2]:5.2f})  "
                  f"o({mm(o[0]):8.4f},{mm(o[1]):8.4f},{mm(o[2]):8.4f})  area {a:10.4f}")
        else:
            print(f"    {t:6s} area {a:10.4f}")

radii = sorted({mm(f["surface"]["radius"]) for b in bd["bodies"] for f in b["faces"]
                if f["surface"]["type"] in ("cylinder", "sphere")})
print(f"\n  every curved radius in the tab: {radii}")
print(f"  a face at r 5.0 present: {'YES — A1 FAILED' if 5.0 in radii else 'no'}")

# the cavity's radius at the slit floor, against the profile's inner edge
tbl = {v["name"]: v["expression"] for t in (d.get("variables") or [])
       for v in t.get("variables", [])}
print(f"\n  #ball {tbl.get('ball')}   #fit {tbl.get('fit')}   #collar {tbl.get('collar')}")
BALL, FIT, SLIT_IN = 12.0, 0.08, 5.0
floor = -BALL / 4
r_cav = math.sqrt((BALL / 2 + FIT) ** 2 - floor ** 2)
r_cav0 = math.sqrt((BALL / 2) ** 2 - floor ** 2)
print(f"  at the floor z {floor:.4f}: cavity r {r_cav:.4f} at #fit 0.08, "
      f"{r_cav0:.4f} at #fit 0, against the profile's inner edge {SLIT_IN}")
print(f"  margin {r_cav - SLIT_IN:.4f} / {r_cav0 - SLIT_IN:.4f} — "
      f"{'slot' if r_cav0 > SLIT_IN else 'POCKET'}")

print()
print("=" * 78)
print("A3 — the gripper's clip top is one flat square face, 18 both ways")
print("=" * 78)
g = S["gripper"]
for prt in g["parts"]:
    b = box(g["partboxes"][prt["partId"]])
    print(f"  {prt['name']}  x {b['highX'] - b['lowX']:.4f}  y {b['highY'] - b['lowY']:.4f}  "
          f"z {b['lowZ']:.4f}..{b['highZ']:.4f}")
for body in g["bodydetails"]["bodies"]:
    for f in body["faces"]:
        s = f["surface"]
        a = mm(mm(f.get("area", 0)))
        if s["type"] == "plane":
            o, n = s["origin"], s["normal"]
            print(f"    plane  n({n[0]:5.2f},{n[1]:5.2f},{n[2]:5.2f})  "
                  f"z {mm(o[2]):9.4f}  area {a:10.4f}")
        elif s["type"] == "cylinder":
            o, ax = s["origin"], s["axis"]
            print(f"    cyl    r {mm(s['radius']):8.4f} ax({ax[0]:5.2f},{ax[1]:5.2f},"
                  f"{ax[2]:5.2f})  o z {mm(o[2]):9.4f}  area {a:10.4f}")

print()
print("=" * 78)
print("the assembly — height, stations, and the feet")
print("=" * 78)
ab = box(d["assembly_bbox"])
print(f"  bounding box  x {ab['lowX']:.4f}..{ab['highX']:.4f}   "
      f"y {ab['lowY']:.4f}..{ab['highY']:.4f}   z {ab['lowZ']:.4f}..{ab['highZ']:.4f}")
print(f"  standing height {ab['highZ'] - ab['lowZ']:.4f}")

root = d["assembly"]["rootAssembly"]
names = {i["id"]: i["name"] for i in root["instances"]}
print(f"  {len(root['instances'])} instances, "
      f"{len(root.get('features', []))} mate features")
for occ in sorted(root["occurrences"], key=lambda o: o["transform"][11]):
    t = occ["transform"]
    path = occ["path"][-1]
    print(f"    {names.get(path, path):14s} "
          f"x {mm(t[3]):10.4f}  y {mm(t[7]):10.4f}  z {mm(t[11]):10.4f}")
