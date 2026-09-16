import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for f in common.faces(page, api, s["did"], s["wid"], s["ul_eid"], "JaD"):
        su = f.get("surface", {})
        if su.get("type") == "cylinder" and abs(su.get("radius", 0) - 0.0022) < 1e-9:
            b = f["box"]
            print(f["id"], "y", [round(b["minCorner"][1]*1000,2), round(b["maxCorner"][1]*1000,2)],
                  "x", [round(b["minCorner"][0]*1000,2), round(b["maxCorner"][0]*1000,2)],
                  "z", [round(b["minCorner"][2]*1000,2), round(b["maxCorner"][2]*1000,2)],
                  "axis", su["axis"])
