import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(307, 178); page.wait_for_timeout(2000)     # Between entities
    for r in gui.labels(page):
        if r[2] < 400: print(r)
    # pick the -Y stub end disc, off centre
    page.mouse.move(966, 420); page.wait_for_timeout(900)
    page.mouse.click(966, 420); page.wait_for_timeout(2500)
    print("--- after pick 1")
    for r in gui.labels(page):
        if r[2] < 400: print(r)
    page.screenshot(path=D+"la22.png")
