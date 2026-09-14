import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
def mm(v): return round(v*1000, 4)
s = common.load(); did, wid, eid = s["did"], s["wid"], s["bs_eid"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for pid in ("JHD", "JKD"):
        r = api.api(page, "GET", f"/api/parts/d/{did}/w/{wid}/e/{eid}/partid/{pid}/bodydetails")
        b = common._one(r["body"]["bodies"])
        print("===", pid)
        for f in b["faces"]:
            su = f["surface"]
            if su["type"] != "plane":
                continue
            box = f["box"]
            print(f"  plane z {mm(box['minCorner'][2])}..{mm(box['maxCorner'][2])}"
                  f"  x {mm(box['minCorner'][0])}..{mm(box['maxCorner'][0])}"
                  f"  area {round(f['area']*1e6,3)}  loops {[l['type'] for l in f['loops']]}")
    bb = api.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/boundingboxes")["body"]
    print({k: round(v*1000,3) for k, v in bb.items() if k[0] in "lh"})
