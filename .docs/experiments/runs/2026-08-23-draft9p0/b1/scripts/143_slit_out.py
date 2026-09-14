import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    # prove both picks before spending them on the tool
    gui.pick(page, (923, 750), "y axis")
    gui.pick(page, (1087, 515), "outer short edge", add=True)
    gui.clear(page)
    gui.dimension(page, [(923, 750), (1087, 515)], (1030, 800), "#slit_out")
    page.screenshot(path=D + "bs28.png")
