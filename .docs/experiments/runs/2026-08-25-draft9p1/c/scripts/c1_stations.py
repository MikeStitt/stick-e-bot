"""The joint stations as the assembly actually places them, against make_plans.py."""
import json, sys
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge/instructions/robot-guide")
import make_plans as M

RAW = json.loads(open("/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/"
                      "runs/2026-08-25-draft9p1/c/c1-raw.json").read())
asm = RAW["assembly"]
root = asm["rootAssembly"]
names = {i["id"]: i["name"] for i in root["instances"]}
print("occurrences (mm), rotation block:")
for o in sorted(root["occurrences"], key=lambda o: names.get(o["path"][-1], "")):
    t = o["transform"]
    rot = [round(t[i], 6) for i in (0, 1, 2, 4, 5, 6, 8, 9, 10)]
    pos = [round(t[i] * 1000, 4) for i in (3, 7, 11)]
    ident = rot == [1, 0, 0, 0, 1, 0, 0, 0, 1]
    print(f"  {names.get(o['path'][-1], o['path'][-1]):14s} {str(pos):32s} "
          f"{'identity' if ident else rot}")

bb = RAW["assembly_bbox"]
lo = [round(bb[k] * 1000, 4) for k in ("lowX", "lowY", "lowZ")]
hi = [round(bb[k] * 1000, 4) for k in ("highX", "highY", "highZ")]
print(f"\nassembly box  x {lo[0]} … {hi[0]}   y {lo[1]} … {hi[1]}   z {lo[2]} … {hi[2]}")
print(f"height {hi[2] - lo[2]}   source HEIGHT {M.HEIGHT}")
print(f"top    {hi[2]}   source HEAD_T {M.HEAD_T}")
print(f"sole   {lo[2]}   source SOLE_Z {M.SOLE_Z}")
print(f"span x {hi[0] - lo[0]}   depth y {hi[1] - lo[1]}")
for n in ("NECK_Z", "HIP_Z", "KNEE_Z", "ANKLE_Z", "SOLE_Z", "SH_X", "SH_Z", "LEG_X",
          "FOOT_X", "LIMB_CENTER", "HEAD_RIM", "HEAD_B"):
    print(f"  {n:12s} {getattr(M, n)}")
