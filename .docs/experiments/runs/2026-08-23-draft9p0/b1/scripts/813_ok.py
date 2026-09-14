import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.tick(page); page.wait_for_timeout(4000)
    gui.clear(page)
    page.keyboard.press("Shift+1"); page.wait_for_timeout(1800)
    gui.fit(page); page.wait_for_timeout(1500)
    sc, cam = gui.zoom_to(page, 7.0)
    page.wait_for_timeout(1200)
    ctr = gui.project(page, 0, 0, 55.4, cam)
    print("px/mm", round(sc, 3), "ball centre px", ctr, "mouth", gui.project(page,0,0,59,cam))
    x, y = int(ctr[0]), int(ctr[1])
    page.screenshot(path=D+"ua75.png", clip={"x": x-110, "y": y-90, "width": 220, "height": 180})
