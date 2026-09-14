import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

O = (923, 389)
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.dimension(page, [O, (762, 470)], (660, 720), "#nose + 2 mm")
    gui.dimension(page, [O, (1086, 470)], (1180, 720), "#nose + 2 mm")
    gui.clear(page)
    page.screenshot(path=D+"tl78.png")
