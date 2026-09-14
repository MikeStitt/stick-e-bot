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
    for n, f, st in common.features(page, api, did, wid, eid):
        if st != "OK":
            print("BAD", n, st)
    page.mouse.click(180, 984)
    page.wait_for_timeout(8000)
    page.mouse.click(51, 209)   # chevron on torso <1>
    page.wait_for_timeout(2000)
    for r in gui.tree(page):
        print(r)
    page.screenshot(path=D+"tk33.png")
