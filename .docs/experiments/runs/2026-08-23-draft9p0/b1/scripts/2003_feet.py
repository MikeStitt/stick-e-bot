"""Is the 34.6 mm foot depth real, or is it a tilted foot?"""
import sys, json, math
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_session as osx
from playwright.sync_api import sync_playwright
st = json.load(open(D + "state.json"))
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up()
    d = osx.api(page, "GET",
        f"/api/assemblies/d/{st['did']}/w/{st['wid']}/e/{st['asm_eid']}"
        "?includeMateFeatures=true")
    r = d["body"]["rootAssembly"]
    for inst in r["instances"]:
        if "Foot" not in inst["name"]:
            continue
        occ = [o for o in r["occurrences"] if inst["id"] in o["path"]]
        for o in occ:
            t = o["transform"]          # 4x4, row major, meters in the last column
            R = [t[0:3], t[4:7], t[8:11]]
            pos = [t[3] * 1000, t[7] * 1000, t[11] * 1000]
            # the part's own z axis, in assembly space
            zax = [R[0][2], R[1][2], R[2][2]]
            tilt = math.degrees(math.acos(max(-1, min(1, zax[2]))))
            print(f"{inst['name']:10s} origin z {pos[2]:9.2f}   "
                  f"part z-axis {[round(v,3) for v in zax]}   tilt {tilt:6.2f}°")
