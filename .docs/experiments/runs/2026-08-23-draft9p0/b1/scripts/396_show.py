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
    gui.clear(page)
    page.mouse.move(140, 400)
    for _ in range(10):
        page.mouse.wheel(0, -300); page.wait_for_timeout(120)
    page.wait_for_timeout(1000)
    x, y = gui.row(page, "neck connector on torso")
    print("row", x, y)
    page.mouse.move(x, y); page.wait_for_timeout(700)
    page.mouse.click(219, y); page.wait_for_timeout(1800)
    page.screenshot(path=D+"tk14.png")
    for n, f, st in common.features(page, api, did, wid, eid):
        if st != "OK":
            print("BAD", n, st)
    print("features listed")
