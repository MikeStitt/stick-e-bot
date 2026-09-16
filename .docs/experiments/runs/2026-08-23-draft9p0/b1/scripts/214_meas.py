import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    fs = common.faces(page, api, s['did'], s['wid'], s['head_eid'], "JqD")
    zs = []
    for f in fs:
        su = f["surface"]; t = su["type"]
        lo = round(f["box"]["minCorner"][2]*1000, 4); hi = round(f["box"]["maxCorner"][2]*1000, 4)
        zs += [lo, hi]
        ex = ""
        if t == "cylinder": ex = "r=%.4f" % (su["radius"]*1000)
        elif t == "sphere": ex = "r=%.4f c=(%.3f,%.3f,%.3f)" % (su["radius"]*1000, *[v*1000 for v in su["origin"]])
        elif t == "plane": ex = "n=(%.2f,%.2f,%.2f)" % tuple(su["normal"])
        print("%-9s z %9.4f .. %9.4f  area %10.4f  %s" % (t, lo, hi, f["area"]*1e6, ex))
    print("SPAN", min(zs), max(zs))
    print("volume", common.volume(page, api, s['did'], s['wid'], s['head_eid'], "JqD"))
