import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_screen as screen

O = (923, 389)
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    common.scroll_tree(page, -25)
    gui.rename_row(page, "Extrude 1", "trim fork to arm")
    page.wait_for_timeout(1500)
    page.mouse.click(140, 880); page.keyboard.press("Escape")
    page.wait_for_timeout(800)
    print("selected", screen.selected(gui.probe(page)))
    common.scroll_tree(page, 25)
    page.mouse.click(*common.jrow(page, "Front")); page.wait_for_timeout(900)
    page.mouse.click(155, 58); page.wait_for_timeout(4500)
    page.keyboard.press("Shift+1"); page.wait_for_timeout(1400)
    gui.search_tool(page, "Circle")
    for spot in (O, (963, 389)):
        page.mouse.move(*spot); page.wait_for_timeout(800)
        page.mouse.click(*spot); page.wait_for_timeout(900)
    page.keyboard.press("Escape"); page.wait_for_timeout(700)
    gui.dimension(page, [(963, 389)], (1250, 200), "#pocket_d")
    gui.clear(page)
    page.screenshot(path=D+"tl82.png")
