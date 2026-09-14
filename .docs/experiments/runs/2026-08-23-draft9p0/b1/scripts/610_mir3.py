import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    common.scroll_tree(page, -25)
    page.mouse.click(356, 154)                     # Features to mirror
    page.wait_for_timeout(800)
    for nm in ("click lock valley", "round valley rim", "24 valleys"):
        x, y = common.jrow(page, nm)
        page.mouse.click(x, y); page.wait_for_timeout(1100)
    page.wait_for_timeout(1200)
    for r in gui.labels(page):
        if r[1] < 500 and r[2] < 400:
            print(r)
    page.screenshot(path=D+"tl53.png")
