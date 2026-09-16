import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_screen as screen

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.search_tool(page, "Center point rectangle")
    ox, oy = 923, 523
    page.mouse.move(ox, oy); page.wait_for_timeout(600)
    page.mouse.click(ox, oy); page.wait_for_timeout(600)
    page.mouse.move(ox + 250, oy - 320); page.wait_for_timeout(600)
    page.mouse.click(ox + 250, oy - 320); page.wait_for_timeout(1200)
    page.keyboard.press("Escape"); page.wait_for_timeout(800)
    page.screenshot(path="sk2.png")
