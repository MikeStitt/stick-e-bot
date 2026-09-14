"""B2 — check the read-back against make_plans.py. Reads b2_raw.json only."""
import json, math, collections, importlib.util, pathlib

D = pathlib.Path("/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/"
                 "c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
MP = "/Users/mikestitt/projects/first/2027/sponge/instructions/robot-guide/make_plans.py"

spec = importlib.util.spec_from_file_location("mp", MP)
mp = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(mp)
except BaseException:
    pass

raw = json.load(open(D / "b2_raw.json"))
MM = 1000.0

def r3(x):
    return round(x * MM, 3)

def faces(rec):
    for b in rec["bodydetails"].get("bodies", []):
        for f in b.get("faces", []):
            yield b.get("id"), f

print("=" * 96)
print("B2 — the model read back, against make_plans.py")
print("=" * 96)

# ---------------------------------------------------------------- bounding boxes
print("\n## Part bounding boxes (mm)\n")
print(f"{'studio':16s} {'part':16s} {'x':>18s} {'y':>18s} {'z':>18s}")
for name, rec in raw.items():
    for prt in rec["parts"]:
        bb = rec["partboxes"].get(prt["partId"])
        if not bb:
            continue
        f = lambda a, b: f"{r3(bb[a]):8.2f}…{r3(bb[b]):<8.2f}"
        print(f"{name:16s} {prt['name'][:16]:16s} "
              f"{f('lowX','highX'):>18s} {f('lowY','highY'):>18s} {f('lowZ','highZ'):>18s}")

# ---------------------------------------------------------------- radii census
print("\n## Every distinct cylinder and sphere radius, per studio (mm)\n")
for name, rec in raw.items():
    cyl, sph = collections.Counter(), collections.Counter()
    for _, f in faces(rec):
        s = f["surface"]
        if s["type"] == "cylinder":
            cyl[round(s["radius"] * MM, 3)] += 1
        elif s["type"] == "sphere":
            sph[round(s["radius"] * MM, 3)] += 1
    parts = []
    if cyl:
        parts.append("cyl " + ", ".join(f"r{k}×{v}" for k, v in sorted(cyl.items())))
    if sph:
        parts.append("sph " + ", ".join(f"r{k}×{v}" for k, v in sorted(sph.items())))
    print(f"  {name:16s} {'; '.join(parts) or '—'}")

# ---------------------------------------------------------------- named checks
print("\n## Named checks\n")
CHECKS = [
    ("collar outside radius", "ball and socket", "cyl", mp.COLLAR_R),
    ("cavity radius",         "ball and socket", "sph", mp.CAVITY),
    ("ball radius",           "ball and socket", "sph", mp.BALL / 2),
    ("limb radius, u limb",   "u limb",          "cyl", mp.LIMB / 2),
    ("limb radius, l limb",   "l limb",          "cyl", mp.LIMB / 2),
]
for label, studio, kind, want in CHECKS:
    got = set()
    for _, f in faces(raw[studio]):
        s = f["surface"]
        if (kind == "cyl" and s["type"] == "cylinder") or (kind == "sph" and s["type"] == "sphere"):
            got.add(round(s["radius"] * MM, 3))
    hit = any(abs(g - want) < 0.005 for g in got)
    print(f"  {'OK ' if hit else '** ':3s} {label:24s} want {want:8.3f}   found {sorted(got)}")

# the mouth: the socket's opening, MOUTH across
want = mp.MOUTH / 2
got = sorted({round(f["surface"]["radius"] * MM, 3)
              for _, f in faces(raw["ball and socket"]) if f["surface"]["type"] == "cylinder"})
print(f"  {'** ' if not any(abs(g-want)<0.005 for g in got) else 'OK '} "
      f"{'mouth radius':24s} want {want:8.3f}   found {got}")

# ---------------------------------------------------------------- cut-face z
print("\n## Distinct z of every planar face whose normal is along Z (mm)\n")
for name, rec in raw.items():
    zs = set()
    for _, f in faces(rec):
        s = f["surface"]
        if s["type"] != "plane":
            continue
        n = s["normal"]
        if abs(abs(n[2]) - 1) < 1e-6 and abs(n[0]) < 1e-6 and abs(n[1]) < 1e-6:
            zs.add(round(s["origin"][2] * MM, 3))
    print(f"  {name:16s} {sorted(zs)}")

# ---------------------------------------------------------------- thinnest wall
print("\n## Thinnest wall, concentric cylinder pairs only (mm)\n")
for name, rec in raw.items():
    groups = collections.defaultdict(set)
    for _, f in faces(rec):
        s = f["surface"]
        if s["type"] != "cylinder":
            continue
        key = (tuple(round(v, 6) for v in s["origin"]),
               tuple(round(abs(v), 6) for v in s["axis"]))
        groups[key].add(round(s["radius"] * MM, 4))
    walls = []
    for key, rs in groups.items():
        rs = sorted(rs)
        for a, b in zip(rs, rs[1:]):
            walls.append((round(b - a, 3), a, b))
    walls.sort()
    if walls:
        w, a, b = walls[0]
        print(f"  {name:16s} thinnest {w:6.3f}  between r{a} and r{b}   "
              f"({len(walls)} concentric pair(s))")
    else:
        print(f"  {name:16s} no concentric cylinder pair")

print("\nNote: the concentric test is blind to flat-against-curved and plane-against-plane.")
