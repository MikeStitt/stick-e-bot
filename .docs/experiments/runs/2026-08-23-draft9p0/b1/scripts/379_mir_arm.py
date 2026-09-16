import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page); page.wait_for_timeout(600)
    # pre-select the two studs, then arm Mirror
    page.mouse.move(1026, 550); page.wait_for_timeout(700)
    page.mouse.click(1026, 550); page.wait_for_timeout(900)
    page.keyboard.down("Shift")
    page.mouse.move(982, 722); page.wait_for_timeout(700)
    page.mouse.click(982, 722); page.wait_for_timeout(900)
    page.keyboard.up("Shift")
    page.wait_for_timeout(600)
    page.screenshot(path=D + "tj95.png")
    gui.search_tool(page, "Mirror"); page.wait_for_timeout(2200)
    for r in gui.labels(page):
        print(r)
