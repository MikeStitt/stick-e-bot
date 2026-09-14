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
    gui.dimension(page, [(923, 249)], (1230, 240), "2 * #nose")
    gui.dimension(page, [O, (775, 323)], (640, 300), "#slot / 2")
    gui.dimension(page, [O, (800, 552)], (640, 620), "#nose + 2")
    gui.clear(page)
    page.screenshot(path=D+"tl73.png")
