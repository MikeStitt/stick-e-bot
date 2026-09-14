import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.move(353, 984); page.wait_for_timeout(400)
    page.mouse.down(); page.wait_for_timeout(500)
    for x in (450, 550, 650, 750, 820, 850):
        page.mouse.move(x, 984); page.wait_for_timeout(250)
    page.mouse.up(); page.wait_for_timeout(2500)
    page.screenshot(path=D + "bs2.png", clip={"x": 0, "y": 960, "width": 1300, "height": 40})
