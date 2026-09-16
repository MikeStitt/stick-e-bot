import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(336, 175)               # type dropdown
    page.wait_for_timeout(1200)
    hit = common.menu_item(page, "Transform by mate connectors")
    print("hit", hit)
    page.mouse.click(*hit)
    page.wait_for_timeout(1800)
    for row in gui.labels(page):
        print(row)
    page.mouse.click(50, 547)                 # expand "get socket"
    page.wait_for_timeout(1200)
    print(gui.tree(page))
    page.screenshot(path=D + "hs16.png")
