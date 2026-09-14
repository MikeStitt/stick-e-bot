import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(451, 93)          # cancel Sketch 1
    page.wait_for_timeout(2500)
    common.delete_row(page, gui, "New folder (0)")
    page.wait_for_timeout(1500)
    page.mouse.wheel(0, -1200)         # scroll the feature tree up
    page.wait_for_timeout(800)
    print(gui.tree(page))
    print("Front row", gui.row(page, "Front"))
    page.screenshot(path=D + "tj52.png")
