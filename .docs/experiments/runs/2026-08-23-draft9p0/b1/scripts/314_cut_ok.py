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
    page.keyboard.press("Tab")
    page.wait_for_timeout(1200)
    gui.tick(page)
    page.wait_for_timeout(3500)
    gui.rename_row(page, "Extrude 1", "trim shoulder cut")
    page.wait_for_timeout(2000)
    for n, i, st in common.features(page, api, s["did"], s["wid"], s["ps_eid"]):
        print(f"{st:8} {n}")
    print(common.bbox(page, api, s["did"], s["wid"], s["ps_eid"]))
    page.screenshot(path=D + "tj61.png")
