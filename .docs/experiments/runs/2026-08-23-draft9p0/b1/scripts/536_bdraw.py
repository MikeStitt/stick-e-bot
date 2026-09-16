import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
O, A, B, C, Dd = (922,524), (1054,463), (791,463), (791,764), (1054,764)
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.search_tool(page, "Center point arc")
    for spot in (O, A, B):
        page.mouse.move(*spot); page.wait_for_timeout(600)
        page.mouse.click(*spot); page.wait_for_timeout(800)
    page.keyboard.press("Escape"); page.wait_for_timeout(700)
    gui.search_tool(page, "Line")
    for spot in (B, C, Dd, A):
        page.mouse.move(*spot); page.wait_for_timeout(600)
        page.mouse.click(*spot); page.wait_for_timeout(800)
    page.keyboard.press("Escape"); page.wait_for_timeout(500)
    page.keyboard.press("Escape"); page.wait_for_timeout(800)
    page.screenshot(path=D+"tl05.png")
