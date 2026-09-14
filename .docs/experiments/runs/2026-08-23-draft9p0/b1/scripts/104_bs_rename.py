import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    hit = common.menu_item(page, "Part Studio 1")
    print("tab at", hit)
    page.mouse.click(hit[0], hit[1], button="right"); page.wait_for_timeout(1500)
    r = common.menu_item(page, "Rename")
    page.mouse.click(*r); page.wait_for_timeout(1500)
    page.keyboard.press("Meta+a"); page.wait_for_timeout(300)
    page.keyboard.type("ball and socket", delay=50); page.wait_for_timeout(400)
    page.keyboard.press("Enter"); page.wait_for_timeout(2500)
    page.screenshot(path=D + "bs1.png", clip={"x": 0, "y": 960, "width": 1300, "height": 40})
