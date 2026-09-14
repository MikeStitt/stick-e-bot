import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
O, R, Q = (921,525), (981,525), (964,482)
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.search_tool(page, "Circle")
    for spot in (O, R):
        page.mouse.move(*spot); page.wait_for_timeout(700)
        page.mouse.click(*spot); page.wait_for_timeout(900)
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    page.keyboard.press("Escape"); page.wait_for_timeout(800)
    gui.clear(page)
    gui.dimension(page, [Q], (1150, 380), "#stub")
    gui.clear(page)
    page.screenshot(path=D+"tl22.png")
