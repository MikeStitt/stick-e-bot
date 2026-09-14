import sys, collections
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api

def mm(v): return round(v * 1000, 4)

s = common.load(); did, wid, eid = s["did"], s["wid"], s["bs_eid"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    r = api.api(page, "GET", f"/api/parts/d/{did}/w/{wid}/e/{eid}/partid/JKD/bodydetails")
    body = common._one(r["body"]["bodies"])
    print("=== faces, z extent ===")
    for f in body["faces"]:
        b = f["box"]; su = f["surface"]
        lo, hi = mm(b["minCorner"][2]), mm(b["maxCorner"][2])
        extra = f"r={mm(su['radius'])}" if "radius" in su else ""
        print(f"  {su['type']:9s} z {lo:>8} .. {hi:<8} area {round(f['area']*1e6,3):>9} {extra}")
    print("=== circular edges ===")
    seen = collections.Counter()
    for e in body["edges"]:
        c = e.get("curve", {})
        if c.get("type") != "circle":
            continue
        seen[(mm(c["radius"]), mm(c["origin"][2]))] += 1
    for (rad, z), n in sorted(seen.items()):
        print(f"  radius {rad:>8}  at z {z:>8}   x{n}")
