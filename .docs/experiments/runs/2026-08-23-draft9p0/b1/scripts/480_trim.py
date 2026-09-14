import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    gui.search_tool(page, "Trim")
    page.screenshot(path=D+"tk71.png")
    for spot in ((842, 467), (987, 626)):
        page.mouse.move(*spot); page.wait_for_timeout(700)
        page.mouse.click(*spot); page.wait_for_timeout(1200)
    page.keyboard.press("Escape"); page.wait_for_timeout(800)
    page.screenshot(path=D+"tk72.png")
