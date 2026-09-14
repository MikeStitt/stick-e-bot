import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    gui.dimension(page, [(922, 158), (923, 405)], (1230, 260), "#bump_r")
    gui.clear(page)
    page.mouse.move(1450, 900); page.wait_for_timeout(500)
    page.screenshot(path=D+"tl94.png")
