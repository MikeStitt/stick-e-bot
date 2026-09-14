"""Phase C — part bounding boxes out of c1-raw.json, against make_plans.py."""
import sys, json
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge/instructions/robot-guide")
import make_plans as M
RAW = "/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/runs/2026-08-25-draft9p1/c/c1-raw.json"
d = json.load(open(RAW))
print(f"{'studio':16s} {'part':14s} {'x':>18s} {'y':>18s} {'z':>18s}")
for name, rec in d["studios"].items():
    byid = {p["partId"]: p.get("name", p["partId"]) for p in rec["parts"]}
    for pid, bb in rec["partboxes"].items():
        f = lambda k: round(bb[k] * 1000, 4)
        print(f"  {name:14s} {byid.get(pid, pid):14s}"
              f" {f('lowX'):8.3f}…{f('highX'):<9.3f}"
              f" {f('lowY'):8.3f}…{f('highY'):<9.3f}"
              f" {f('lowZ'):8.3f}…{f('highZ'):<9.3f}")
print()
print("make_plans:")
for k in ("TORSO_W","TORSO_H","TORSO_D","HEAD_W","HEAD_H","HEAD_D","LIMB","LIMB_CENTER",
          "GRIPPER_L","FOOT_H","FOOT_L","FOOT_W","BALL","STALK","FIT","CAVITY","MOUTH","GRIP",
          "COLLAR_WALL","COLLAR_R","COLLAR_L","SLIT_W","CLIP_R","CLIP_BORE","CLIP_MOUTH","CLIP_W",
          "BLADE","GAP","SLOT","EAR","STUB","STUB_PROUD","BORE_D","NOSE","BLADE_OUT","SLOT_DEEP",
          "TEETH_RI","TEETH_R","BUMP_R","BUMP_D","TOOTH_PROUD","VALLEY_D","VALLEY_DEEP","STEP",
          "STAND","BOSS_D","SHOULDER_L","SHOULDER_DROP","SHOULDER_EL","SHOULDER_AZ",
          "HIP_Z","NECK_Z","KNEE_Z","ANKLE_Z","SOLE_Z","HEAD_RIM","HEAD_B","HEAD_T","HEIGHT",
          "LEG_X","FOOT_X","SH_X","SH_Z","RIB_W","RIB_D","RIB_STEP","RIB_N","RIB_0",
          "EYE_X","EYE_UP","EYE_RX","EYE_RY","HEAD_ROUND","MOUTH_W","MOUTH_H","MOUTH_DN"):
    v = getattr(M, k, None)
    print(f"  {k:14s} {v}")
