import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    x, y = gui.row(page, "Part 2")
    page.mouse.click(x, y, button="right"); page.wait_for_timeout(1400)
    page.mouse.click(*common.menu_item(page, "Rename")); page.wait_for_timeout(1000)
    page.keyboard.press("Meta+a"); page.keyboard.type("shoulder boss")
    page.keyboard.press("Enter"); page.wait_for_timeout(2000)
    scale, cam = gui.px_per_mm(page)
    q = gui.project(page, 44.3390, -4.8145, 27.2218, cam=cam)
    print(scale, q)
    page.screenshot(path=D + "tj45.png", clip={"x": round(q[0])-150, "y": round(q[1])-150, "width": 300, "height": 300})
