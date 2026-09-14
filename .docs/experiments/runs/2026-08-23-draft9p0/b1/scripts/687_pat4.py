import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(343, 227); page.wait_for_timeout(900)
    common.scroll_tree(page, -25)
    page.mouse.click(*common.jrow(page, "axis for circular patterns")); page.wait_for_timeout(1500)
    for r in gui.labels(page):
        print(r)
