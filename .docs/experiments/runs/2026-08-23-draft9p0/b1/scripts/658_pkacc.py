import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
import onshape_screen as screen

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    s = common.load()
    gui.tick(page)
    page.wait_for_timeout(3500)
    common.scroll_tree(page, -25)
    gui.rename_row(page, "Sketch 1", "pocket axle sketch")
    page.wait_for_timeout(1500)
    page.mouse.click(140, 880); page.keyboard.press("Escape")
    page.wait_for_timeout(800)
    print("selected", screen.selected(gui.probe(page)))
    print([n for n, f, st in common.features(page, api, s["did"], s["wid"], s["hinge_eid"])[-2:]])
    common.scroll_tree(page, -25)
    page.mouse.click(*common.jrow(page, "pocket axle sketch"))
    page.wait_for_timeout(1000)
    gui.search_tool(page, "Extrude", settle=2500)
    page.wait_for_timeout(1000)
    page.mouse.click(365, 149)          # Remove
    page.wait_for_timeout(1500)
    for r in gui.labels(page):
        print(r)
