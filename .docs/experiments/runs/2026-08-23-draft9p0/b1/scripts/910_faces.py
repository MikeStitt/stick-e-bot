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
    fs = common.faces(page, api, s["did"], s["wid"], s["ll_eid"], "RADD")
    for f in fs:
        srf = f.get("surface", {})
        t = srf.get("type")
        if t == "sphere":
            print("SPHERE", f["id"], srf.get("radius"), srf.get("origin"))
        elif t == "cylinder" and abs(srf.get("radius", 0) - 2.0) < 0.01:
            print("STUB CYL", f["id"], srf.get("radius"), srf.get("origin"), srf.get("axis"), f.get("area"))
        elif t == "plane":
            o = srf.get("origin"); n = srf.get("normal")
            if n and abs(abs(n[1]) - 1.0) < 1e-6 and f.get("area", 0) < 20:
                print("STUB DISC", f["id"], o, n, f.get("area"))
