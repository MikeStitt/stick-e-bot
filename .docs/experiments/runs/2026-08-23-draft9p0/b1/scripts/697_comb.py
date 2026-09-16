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
    gui.rename_row(page, "Extrude 1", "fork arm")
    page.wait_for_timeout(1500)
    page.mouse.click(140, 880); page.keyboard.press("Escape"); page.wait_for_timeout(800)
    print("selected", screen.selected(gui.probe(page)))
    gui.search_tool(page, "Boolean", settle=2500); page.wait_for_timeout(1200)
    for r in gui.labels(page):
        print(r)
