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
    page.keyboard.press("Shift+6"); page.wait_for_timeout(2000)   # Bottom
    gui.fit(page); page.wait_for_timeout(1500)
    sc, cam = gui.zoom_to(page, 22.0)
    page.wait_for_timeout(1200)
    print("px/mm", round(sc, 3))
    at = gui.project(page, 5.0, 0.0, -7.4, cam)
    print("pick at", at)
    n = gui.pick(page, (int(at[0]), int(at[1])), "collar bottom face")
    print("picked", n)
    page.screenshot(path=D+"ub01.png")
