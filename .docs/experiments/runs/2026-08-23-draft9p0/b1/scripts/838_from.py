import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    x, y = gui.row(page, "add fork")
    print("add fork row", x, y)
    page.mouse.click(50, y); page.wait_for_timeout(2000)      # caret
    print(gui.tree(page))
    page.mouse.click(356, 208); page.wait_for_timeout(1200)
    cx, cy = gui.row(page, "fork to robot connector")
    print("connector row", cx, cy)
    page.mouse.click(cx, cy); page.wait_for_timeout(2500)
    for r in gui.labels(page):
        if r[2] < 500: print(r)
