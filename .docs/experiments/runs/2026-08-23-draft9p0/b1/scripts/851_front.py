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
    page.keyboard.press("Shift+1"); page.wait_for_timeout(2200)
    gui.fit(page); page.wait_for_timeout(1800)
    sc, cam = gui.zoom_to(page, 26.0, at_px=gui.project(page, 0, 0, -100.4))
    page.wait_for_timeout(1500)
    a = [round(v) for v in gui.project(page, 0, 0, -100.4, cam)]
    print("px/mm", round(sc,3), "axis", a)
    page.screenshot(path=D+"ub23.png", clip={"x": a[0]-220, "y": a[1]-220, "width": 440, "height": 440})
