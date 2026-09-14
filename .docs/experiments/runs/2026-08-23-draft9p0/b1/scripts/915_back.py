import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.move(900, 700); page.wait_for_timeout(400)
    page.keyboard.press("Shift+2"); page.wait_for_timeout(2500)   # Back
    sc, cam = gui.px_per_mm(page)
    o = gui.project(page, 0.0, 0.0, 0.0, cam)
    print("px/mm", sc, "origin", o)
    at = gui.project(page, 1.2, 6.6, 0.8, cam)
    print("pick", at)
    page.screenshot(path=D+"la23.png")
