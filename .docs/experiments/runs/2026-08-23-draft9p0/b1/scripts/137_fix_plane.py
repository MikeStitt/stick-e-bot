import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for l in gui.labels(page):
        if l[0] == "Top plane":
            page.mouse.click(l[1] + 97, l[2]); page.wait_for_timeout(1000)
    print("after clear:", [l[0] for l in gui.labels(page)])
    page.mouse.move(1030, 481); page.wait_for_timeout(500)
    page.mouse.click(1030, 481); page.wait_for_timeout(2000)
    print("labels:", [l[0] for l in gui.labels(page)])
    page.screenshot(path=D + "bs24.png")
