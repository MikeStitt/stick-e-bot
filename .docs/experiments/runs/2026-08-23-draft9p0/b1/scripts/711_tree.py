import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
F = D + "frames/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    common.scroll_tree(page, -25)
    x, y = common.jrow(page, "blade")
    page.mouse.click(x, y, button="right"); page.wait_for_timeout(1500)
    page.mouse.click(*common.menu_item(page, "Show")); page.wait_for_timeout(2000)
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    gui.clear(page)
    gui.frame(page, F + "cad.parts.hinge.tree.png",
              clip={"x": 40, "y": 60, "width": 250, "height": 880})
