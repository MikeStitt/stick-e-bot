import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for spot, what in [((1300, 522), "x axis"), ((1040, 508), "far long side"),
                       ((1040, 537), "near long side")]:
        gui.clear(page)
        gui.pick(page, spot, what)
    gui.clear(page)
    gui.dimension(page, [(1300, 522), (1040, 508)], (1200, 400), "#slit / 2")
    page.screenshot(path=D + "bs29.png")
