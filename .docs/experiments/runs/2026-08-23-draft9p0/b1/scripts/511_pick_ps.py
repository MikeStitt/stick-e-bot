import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(368, 148); page.wait_for_timeout(2500)
    hit = common.menu_item(page, "ball and socket")
    print("ball and socket at", hit)
    page.screenshot(path=D+"tk91.png")
    if hit:
        page.mouse.click(*hit); page.wait_for_timeout(2500)
        page.screenshot(path=D+"tk92.png")
        for r in gui.labels(page):
            if r[2] < 600 and r[1] < 900:
                print(r)
