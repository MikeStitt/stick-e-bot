import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.zoom_to(page, 12.0, at_px=(923, 387)); page.wait_for_timeout(1800)
    scale, cam = gui.px_per_mm(page)
    q = gui.project(page, 0, 0, 48, cam=cam)
    print("scale", scale, "neck", q)
    page.mouse.move(round(q[0]), round(q[1])); page.wait_for_timeout(1200)
    page.screenshot(path=D + "tj89.png")
