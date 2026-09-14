import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

C = (1180, 277)
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    common.scroll_tree(page, 25)
    page.mouse.click(*common.jrow(page, "Front")); page.wait_for_timeout(900)
    page.mouse.click(155, 58); page.wait_for_timeout(4500)
    page.keyboard.press("Shift+1"); page.wait_for_timeout(1400)
    gui.search_tool(page, "Circle")
    for spot in (C, (C[0]+25, C[1])):
        page.mouse.move(*spot); page.wait_for_timeout(700)
        page.mouse.click(*spot); page.wait_for_timeout(900)
    page.keyboard.press("Escape"); page.wait_for_timeout(700)
    gui.dimension(page, [(C[0]+25, C[1])], (1300, 180), "#bump_d")
    gui.clear(page)
    page.screenshot(path=D+"tl85.png")
