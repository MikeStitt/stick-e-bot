import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.tick(page); page.wait_for_timeout(4000)
    gui.rename_row(page, "Boolean 1", "combine parts"); page.wait_for_timeout(1500)
    s = common.load()
    parts = api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['foot_eid']}")["body"]
    for pt in parts:
        print(pt["name"], pt["partId"], common.volume(page, api, s["did"], s["wid"], s["foot_eid"], pt["partId"]))
    print(common.bbox(page, api, s["did"], s["wid"], s["foot_eid"]))
    print([r for r in gui.tree(page)][-4:])
