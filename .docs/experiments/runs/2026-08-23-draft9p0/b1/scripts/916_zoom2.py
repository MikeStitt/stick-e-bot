import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    sc, cam = gui.zoom_to(page, 40.0, at_px=(923, 446)); page.wait_for_timeout(1500)
    at = gui.project(page, 1.2, 6.6, 0.8, cam)
    print("px/mm", sc, "pick", at)
    page.mouse.move(int(at[0]), int(at[1])); page.wait_for_timeout(1200)
    page.screenshot(path=D+"la24.png")
