import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.zoom_to(page, 25.0)
    page.wait_for_timeout(1500)
    scale, cam = gui.px_per_mm(page)
    cx, cy = gui.project(page, 0, 0, -47, cam=cam)
    edge = gui.project(page, 5.7689, 0, -47, cam=cam)
    print("scale", scale, "centre", cx, cy, "mouth edge", edge)
    page.screenshot(path=D + "hs28.png")
