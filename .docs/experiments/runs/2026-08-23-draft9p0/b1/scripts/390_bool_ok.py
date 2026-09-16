import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load(); did, wid, eid = s["did"], s["wid"], s["ps_eid"]
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.tick(page)
    page.wait_for_timeout(4000)
    gui.rename_row(page, "Boolean 1", "add neck to body")
    page.wait_for_timeout(2500)
    r = api.api(page, "GET", f"/api/parts/d/{did}/w/{wid}/e/{eid}")
    for part in r["body"]:
        print(part["partId"], part["name"])
    print(common.bbox(page, api, did, wid, eid))
    page.screenshot(path=D+"tk05.png")
