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
    print("faces", len(fs))
    zs = []
    for f in fs:
        surf = f["surface"]
        t = surf["type"]
        b = f["box"]
        lo, hi = round(b["lowZ"]*1000, 4), round(b["highZ"]*1000, 4)
        zs += [lo, hi]
        extra = ""
        if t == "cylinder": extra = "r=%.4f" % (surf["radius"]*1000)
        if t == "sphere":
            extra = "r=%.4f  c=(%.3f,%.3f,%.3f)" % (surf["radius"]*1000,
                surf["origin"][0]*1000, surf["origin"][1]*1000, surf["origin"][2]*1000)
        if t == "plane":
            extra = "n=(%.2f,%.2f,%.2f)" % tuple(surf["normal"])
        print("%-9s z %9.4f .. %9.4f  area %10.4f  %s" % (t, lo, hi, f["area"]*1e6, extra))
    print("socket z span", min(zs), max(zs))
    print("volume", common.volume(page, api, s['did'], s['wid'], s['head_eid'], "JqD"))
