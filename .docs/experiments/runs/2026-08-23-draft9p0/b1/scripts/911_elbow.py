import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    page.mouse.move(900, 600); page.wait_for_timeout(300)
    page.keyboard.press("Shift+1"); page.wait_for_timeout(2000)   # Front
    gui.fit(page); page.wait_for_timeout(1500)
    sc, cam = gui.zoom_to(page, 40.0, at_px=None); page.wait_for_timeout(1500)
    print("px/mm", sc)
    print("origin px", gui.project(page, 0.0, 0.0, 0.0, cam))
    print("stub off px", gui.project(page, 1.2, 0.0, 0.8, cam))
    page.screenshot(path=D+"la19.png")
