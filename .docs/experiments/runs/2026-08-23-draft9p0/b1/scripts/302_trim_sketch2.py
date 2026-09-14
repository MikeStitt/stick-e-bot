import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(158, 234)         # Front plane row
    page.wait_for_timeout(1000)
    page.mouse.click(155, 58)          # Sketch
    page.wait_for_timeout(3500)
    for r in gui.labels(page):
        print(r)
    page.keyboard.press("Shift+1")
    page.wait_for_timeout(2500)
    scale, cam = gui.px_per_mm(page)
    print("scale", scale)
    print("origin", gui.project(page, 0, 0, 0, cam=cam))
    print("z48", gui.project(page, 0, 0, 48, cam=cam))
    print("x68z64", gui.project(page, 68, 0, 64, cam=cam))
    page.screenshot(path=D + "tj53.png")
