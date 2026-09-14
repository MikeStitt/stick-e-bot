import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
L = [((838, 425), (796, 719)), ((1008, 425), (1050, 719))]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for a, b in L:
        gui.search_tool(page, "Line")
        for spot in (a, b):
            page.mouse.move(*spot); page.wait_for_timeout(600)
            page.mouse.click(*spot); page.wait_for_timeout(800)
        page.keyboard.press("Escape"); page.wait_for_timeout(500)
        page.keyboard.press("Escape"); page.wait_for_timeout(500)
    page.screenshot(path=D+"tk69.png")
