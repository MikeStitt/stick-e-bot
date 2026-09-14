import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.tick(page)
    page.wait_for_timeout(3000)
    gui.rename_row(page, "Mirror 1", "mirror shoulder")
    page.wait_for_timeout(2000)
    print(gui.tree(page))
    print(common.bbox(page, api, s["did"], s["wid"], s["ps_eid"]))
    r = api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['ps_eid']}")
    for pt in r["body"]:
        print(pt["partId"], pt["name"])
