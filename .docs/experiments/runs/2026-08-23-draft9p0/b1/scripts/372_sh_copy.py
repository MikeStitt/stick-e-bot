import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page); page.wait_for_timeout(600)
    gui.search_tool(page, "Transform"); page.wait_for_timeout(2200)
    page.mouse.click(336, 157); page.wait_for_timeout(1200)
    page.mouse.click(351, 266); page.wait_for_timeout(1800)
    # entities: the first Ball stud row (the neck one)
    rows = [r for r in gui.labels(page)]
    x, y = gui.row(page, "Ball stud")
    print("row", x, y)
    page.mouse.click(x, y); page.wait_for_timeout(1500)
    page.mouse.click(356, 208); page.wait_for_timeout(900)
    page.mouse.move(923, 387); page.wait_for_timeout(900)
    page.mouse.click(923, 387); page.wait_for_timeout(1800)
    for r in gui.labels(page):
        print(r)
