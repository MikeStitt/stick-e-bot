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
    common.scroll_tree(page, -25)
    gui.search_tool(page, "Extrude")
    page.wait_for_timeout(3000)
    page.mouse.click(312, 149)          # Add
    page.wait_for_timeout(1200)
    page.mouse.click(356, 182)          # query
    page.wait_for_timeout(800)
    x, y = common.jrow(page, "blade rod outline")
    page.mouse.click(x, y); page.wait_for_timeout(3000)
    page.mouse.click(276, 313)          # Starting offset
    page.wait_for_timeout(2500)
    for r in gui.labels(page):
        if r[1] < 500 and r[2] < 560:
            print(r)
    page.screenshot(path=D+"tl58.png")
