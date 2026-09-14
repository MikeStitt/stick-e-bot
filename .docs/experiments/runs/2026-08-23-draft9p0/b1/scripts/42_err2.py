import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    x, y = gui.row(page, "Chamfer 1")
    print("row", x, y)
    page.mouse.move(x, y); page.wait_for_timeout(2000)
    page.screenshot(path="hd16.png", clip={"x": 0, "y": y - 60, "width": 900, "height": 200})
