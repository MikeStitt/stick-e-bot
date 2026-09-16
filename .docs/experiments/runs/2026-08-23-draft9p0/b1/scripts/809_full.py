import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.fit(page); page.wait_for_timeout(1800)
    sc, cam = gui.zoom_to(page, 7.0)
    page.wait_for_timeout(1200)
    print("px_per_mm", round(sc, 3))
    print("ctr", gui.project(page, 0, 0, 55.4, cam))
    print("z0 ", gui.project(page, 0, 0, 0.0, cam))
    print("hinge", gui.project(page, 0, 0, -45.0, cam))
    page.screenshot(path=D+"ua72.png")
