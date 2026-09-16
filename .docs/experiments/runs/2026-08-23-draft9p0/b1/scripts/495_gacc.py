import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.frame(page, D + "frames/cad.parts.foot.groove_sketch.png")
    gui.tick(page); page.wait_for_timeout(2500)
    gui.rename_row(page, "Sketch 1", "groove profile"); page.wait_for_timeout(1200)
    gui.clear(page)
    x, y = gui.row(page, "groove profile")
    page.mouse.click(x, y); page.wait_for_timeout(900)
    gui.search_tool(page, "Extrude")
    page.wait_for_timeout(1500)
    page.mouse.click(366, 149); page.wait_for_timeout(1500)   # Remove
    for r in gui.labels(page):
        if r[2] < 480 and r[1] < 480:
            print(r)
