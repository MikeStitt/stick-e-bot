"""Thinnest concentric wall, per PART — a pair spanning two parts is a clearance, not a wall."""
import json, pathlib
D = pathlib.Path("/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/"
                 "c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
raw = json.load(open(D / "b2_raw.json")); MM = 1000.0

def surfaces(body):
    for f in body.get("faces", []):
        s = f["surface"]
        if s["type"] == "cylinder":
            yield ("cyl", tuple(round(v * MM, 3) for v in s["origin"]),
                   tuple(round(abs(v), 4) for v in s["axis"]), round(s["radius"] * MM, 4))
        elif s["type"] == "sphere":
            yield ("sph", tuple(round(v * MM, 3) for v in s["origin"]),
                   None, round(s["radius"] * MM, 4))

def concentric(a, b):
    if a[3] == b[3]:
        return False
    if a[0] == b[0] == "cyl":
        if a[2] != b[2]:
            return False
        d = [a[1][k] - b[1][k] for k in range(3)]
        return sum(abs(d[k]) for k in range(3) if a[2][k] < 0.5) < 1e-3
    if a[0] == b[0] == "sph":
        return a[1] == b[1]
    cyl, sph = (a, b) if a[0] == "cyl" else (b, a)
    d = [sph[1][k] - cyl[1][k] for k in range(3)]
    return sum(abs(d[k]) for k in range(3) if cyl[2][k] < 0.5) < 1e-3

print(f"{'studio':16s} {'part':14s} {'thinnest':>9s}  between")
for name, rec in raw.items():
    ids = {p["partId"]: p["name"] for p in rec["parts"]}
    for body in rec["bodydetails"]["bodies"]:
        surf = list(surfaces(body))
        walls = set()
        for i in range(len(surf)):
            for j in range(i + 1, len(surf)):
                if concentric(surf[i], surf[j]):
                    walls.add((round(abs(surf[i][3] - surf[j][3]), 3),
                               surf[i][0], surf[i][3], surf[j][0], surf[j][3]))
        pname = ids.get(body.get("id"), body.get("id", "?"))
        if walls:
            w = sorted(walls)[0]
            print(f"{name:16s} {str(pname)[:14]:14s} {w[0]:9.3f}  "
                  f"{w[1]} r{w[2]} / {w[3]} r{w[4]}   ({len(walls)} pair(s))")
        else:
            print(f"{name:16s} {str(pname)[:14]:14s} {'—':>9s}  no concentric pair")
