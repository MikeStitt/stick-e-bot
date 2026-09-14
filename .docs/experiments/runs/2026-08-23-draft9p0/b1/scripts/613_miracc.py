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
    gui.tick(page); page.wait_for_timeout(7000)
    print(common.features(page, api, s["did"], s["wid"], s["hinge_eid"])[-1])
    print("vol", common.volume(page, api, s["did"], s["wid"], s["hinge_eid"], "JHD"))
    fs = common.faces(page, api, s["did"], s["wid"], s["hinge_eid"], "JHD")
    for lvl in (-4.1, 4.1):
        n = len([f for f in fs if f["surface"]["type"] == "plane"
                 and abs(f["surface"]["origin"][1]*1000 - lvl) < 1e-6])
        print(f"valley floors at y={lvl}: {n}")
    print(common.bbox(page, api, s["did"], s["wid"], s["hinge_eid"]))
