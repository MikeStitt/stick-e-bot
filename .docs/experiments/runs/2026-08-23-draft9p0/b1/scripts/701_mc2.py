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
    gui.search_tool(page, "Mate connector", settle=2500)
    page.wait_for_timeout(1200)
    for r in gui.labels(page):
        print(r)
    page.mouse.move(923, 523); page.wait_for_timeout(900)
    page.mouse.click(923, 523); page.wait_for_timeout(1800)
    for r in gui.labels(page):
        print(">", r)
    page.screenshot(path=D+"tm04.png")
