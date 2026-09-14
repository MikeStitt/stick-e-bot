import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.keyboard.press("Escape"); page.wait_for_timeout(500)
    gui.zoom_to(page, 7.0); page.wait_for_timeout(1500)
    scale, cam = gui.px_per_mm(page)
    lo = gui.project(page, 36, 0, 36, cam=cam)
    hi = gui.project(page, 36, 0, 44, cam=cam)
    ax = gui.project(page, -46, 0, 0, cam=cam)
    print(scale, lo, hi, ax)
    lo = (round(lo[0]), round(lo[1])); hi = (round(hi[0]), round(hi[1])); ax = (round(ax[0]), round(ax[1]))
    gui.dimension(page, [lo, ax], (1400, 460), "#torsoH / 2 - #shoulder_drop")
    page.wait_for_timeout(1000)
    page.screenshot(path=D + "tj06.png")
