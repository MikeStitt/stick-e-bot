import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"

def axis_filled(page):
    return not any(r[0] == "Axis" for r in gui.labels(page))

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.move(1300, 800)
    page.keyboard.press("Shift+7")
    page.wait_for_timeout(2500)
    gui.still(page)
    page.mouse.click(342, 208)
    page.wait_for_timeout(600)
    page.screenshot(path=D + "hs15.png")
    scale, cam = gui.px_per_mm(page)
    print("scale", scale)
    for pt in [(0,-30,-36), (30,0,-36), (0,0,-36), (0,0,36)]:
        print(pt, tuple(round(v) for v in gui.project(page, *pt, cam=cam)))
