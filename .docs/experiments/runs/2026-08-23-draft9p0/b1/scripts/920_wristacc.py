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
    gui.name_feature(page, "wrist end"); page.wait_for_timeout(800)
    gui.tick(page); page.wait_for_timeout(4500)
    print(gui.tree(page))
    print("bbox", common.bbox(page, api, s["did"], s["wid"], s["ll_eid"]))
    for pt in api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['ll_eid']}")["body"]:
        print(pt["name"], common.volume(page, api, s["did"], s["wid"], s["ll_eid"], pt["partId"]))
