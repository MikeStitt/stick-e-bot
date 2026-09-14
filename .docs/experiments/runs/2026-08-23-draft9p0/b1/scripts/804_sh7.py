import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_screen as screen
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    page.mouse.move(*screen.CENTER)
    page.keyboard.press("Shift+5"); page.wait_for_timeout(2500)
    gui.fit(page); page.wait_for_timeout(1200)
    sc, cam = gui.zoom_to(page, 22.0)
    o = tuple(round(v) for v in gui.project(page, 0, 0, 55.4, cam=cam))
    print("axis px", o)
    gui.search_tool(page, "Mate connector"); page.wait_for_timeout(2500)
    page.mouse.move(*o); page.wait_for_timeout(1400)
    page.mouse.click(*o); page.wait_for_timeout(1800)
    for r in gui.labels(page):
        if r[1] < 500: print(r)
    page.screenshot(path=D+"ua63.png")
