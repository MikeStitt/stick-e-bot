import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    a = gui.row(page, "Socket body"); b = gui.row(page, "Part 2"); c = gui.row(page, "fork")
    print(a, b, c)
    page.mouse.click(*a); page.wait_for_timeout(700)
    page.keyboard.down("Shift")
    page.mouse.click(*b); page.wait_for_timeout(500)
    page.mouse.click(*c); page.wait_for_timeout(500)
    page.keyboard.up("Shift"); page.wait_for_timeout(900)
    gui.search_tool(page, "Boolean"); page.wait_for_timeout(3000)
    for r in gui.labels(page):
        if r[2] < 500: print(r)
    page.screenshot(path=D+"ub18.png")
