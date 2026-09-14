import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    common.open_feature(page, gui, "shoulder end")
    page.mouse.click(256, 231)          # tick Move
    page.wait_for_timeout(2000)
    for r in gui.labels(page):
        if r[1] < 700 and r[2] < 500:
            print(r)
    page.screenshot(path=D+"ua73.png", clip={"x": 240, "y": 80, "width": 260, "height": 560})
