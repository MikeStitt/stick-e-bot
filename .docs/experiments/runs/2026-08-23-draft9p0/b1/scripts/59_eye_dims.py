import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    gui.dimension(page, [(1081, 425)], (1270, 300), "20")
    gui.clear(page)
    gui.dimension(page, [(923, 880), (1020, 425)], (990, 900), "16")
    page.screenshot(path="ey3.png")
