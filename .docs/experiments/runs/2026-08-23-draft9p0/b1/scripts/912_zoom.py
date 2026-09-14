import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.fit(page); page.wait_for_timeout(1500)
    sc, cam = gui.px_per_mm(page)
    at = gui.project(page, 0.0, 0.0, 0.0, cam)
    print("fit px/mm", sc, "origin", at)
    sc, cam = gui.zoom_to(page, 40.0, at_px=(int(at[0]), int(at[1]))); page.wait_for_timeout(1500)
    print("px/mm", sc, "origin", gui.project(page, 0.0, 0.0, 0.0, cam))
    print("pick", gui.project(page, 1.2, 0.0, 0.8, cam))
    page.screenshot(path=D+"la20.png")
