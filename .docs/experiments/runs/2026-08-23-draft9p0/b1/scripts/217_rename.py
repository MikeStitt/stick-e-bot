import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    x, y = gui.row(page, "Transform 1")
    page.mouse.click(x, y, button="right"); page.wait_for_timeout(1400)
    hit = common.menu_item(page, "Rename")
    print("rename at", hit)
    page.mouse.click(*hit); page.wait_for_timeout(1200)
    page.keyboard.press("Meta+a")
    page.keyboard.type("drop socket to neck")
    page.keyboard.press("Enter"); page.wait_for_timeout(2000)
    for row in gui.labels(page):
        print(row)
