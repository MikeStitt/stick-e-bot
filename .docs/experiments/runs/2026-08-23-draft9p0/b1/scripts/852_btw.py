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
    gui.search_tool(page, "Mate connector"); page.wait_for_timeout(2500)
    page.mouse.click(336, 121); page.wait_for_timeout(2000)
    page.screenshot(path=D+"ub24.png", clip={"x": 240, "y": 80, "width": 300, "height": 260})
    for t in ("Between entities", "Mid plane", "On entity"):
        print(t, common.menu2(page, t))
