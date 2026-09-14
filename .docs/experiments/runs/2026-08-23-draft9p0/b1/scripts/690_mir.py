import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_screen as screen

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    common.scroll_tree(page, -25)
    gui.rename_row(page, "Circular pattern 1", "24 bumps")
    page.wait_for_timeout(1500)
    page.mouse.click(140, 880); page.keyboard.press("Escape"); page.wait_for_timeout(800)
    common.scroll_tree(page, -25)
    x, y = common.jrow(page, "Part 1")
    page.mouse.click(x, y, button="right"); page.wait_for_timeout(1500)
    hit = common.menu_item(page, "Show")
    print("show at", hit)
    page.mouse.click(*hit); page.wait_for_timeout(2000)
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    gui.clear(page)
    print("selected", screen.selected(gui.probe(page)))
    gui.search_tool(page, "Mirror", settle=2500); page.wait_for_timeout(1200)
    for r in gui.labels(page):
        print(r)
