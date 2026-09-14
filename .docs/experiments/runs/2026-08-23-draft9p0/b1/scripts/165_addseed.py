import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.move(1400, 800); page.wait_for_timeout(500)
    print("cursor", gui.cursor(page))
    page.screenshot(path=D + "bs43.png")
    gui.pick(page, (871, 545), "left short edge", add=True)
    gui.pick(page, (1198, 545), "right short edge", add=True)
    page.screenshot(path=D + "bs44.png")
