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
    # confirm the two picks land before arming Dimension
    gui.pick(page, (923, 520), "origin point")
    gui.pick(page, (895, 348), "the chord")
    page.screenshot(path=D+"tl65.png")
