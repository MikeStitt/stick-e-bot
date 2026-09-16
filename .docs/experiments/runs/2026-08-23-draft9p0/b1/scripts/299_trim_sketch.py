import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    page.wait_for_timeout(500)
    x, y = gui.row(page, "Front")
    page.mouse.click(x, y)
    page.wait_for_timeout(900)
    page.mouse.click(155, 58)          # Sketch
    page.wait_for_timeout(3000)
    page.keyboard.press("Shift+1")     # Front view
    page.wait_for_timeout(2500)
    gui.fit(page)
    page.wait_for_timeout(2000)
    scale, cam = gui.px_per_mm(page)
    print("scale", scale)
    print(gui.project(page, 0, 0, 0, cam=cam), gui.project(page, 0, 0, 48, cam=cam))
    page.screenshot(path=D + "tj51.png")
