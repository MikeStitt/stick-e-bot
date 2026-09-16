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
    page.keyboard.press("Shift+7"); page.wait_for_timeout(2200)
    gui.fit(page); page.wait_for_timeout(1500)
    sc, cam = gui.zoom_to(page, 14.0, at_px=gui.project(page, 0, 0, -100.4))
    page.wait_for_timeout(1500)
    print("px/mm", round(sc,3))
    for nm, xyz in [("axis", (0,0,-100.4)), ("pocketA", (0,5.6,-100.4)), ("pocketB", (0,-5.6,-100.4))]:
        print(nm, gui.project(page, *xyz, cam))
    page.screenshot(path=D+"ub20.png")
