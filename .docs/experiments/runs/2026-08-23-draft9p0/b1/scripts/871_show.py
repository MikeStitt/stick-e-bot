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
    for n in ["Origin", "socket connect to robot", "fork to robot connector"]:
        x, y = gui.row(page, n)
        page.mouse.click(x, y, button="right"); page.wait_for_timeout(1800)
        hit = common.menu2(page, "Show")
        print(n, "->", hit)
        if hit:
            page.mouse.click(*hit)
        else:
            page.keyboard.press("Escape")
        page.wait_for_timeout(1800)
    gui.clear(page)
    page.screenshot(path=D+"ub37.png")
