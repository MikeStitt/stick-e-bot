import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(140, 696); page.wait_for_timeout(600)
    page.keyboard.down("Shift"); page.mouse.click(140, 722); page.keyboard.up("Shift")
    page.wait_for_timeout(900)
    gui.search_tool(page, "Boolean")
    page.wait_for_timeout(1200)
    for row in gui.labels(page): print(row)
    page.screenshot(path=D + "hs23.png")
