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
    # delete the bad shoulder end
    x, y = common.jrow(page, "shoulder end")
    page.mouse.click(x, y, button="right"); page.wait_for_timeout(2200)
    page.mouse.click(*common.menu2(page, "Delete")); page.wait_for_timeout(3000)
    gui.clear(page)
    ox, oy = common.jrow(page, "Origin")
    page.mouse.move(ox, oy); page.wait_for_timeout(700)
    page.mouse.click(219, oy); page.wait_for_timeout(1200)
    print("tree", gui.tree(page)[:8])
    page.screenshot(path=D+"ua62.png")
