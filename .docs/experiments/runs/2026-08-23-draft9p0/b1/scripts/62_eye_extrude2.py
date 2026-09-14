import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api

s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    # clear the wrong pick
    for l in gui.labels(page):
        if l[0] == "Face of head body":
            page.mouse.click(l[1] + 97, l[2]); page.wait_for_timeout(800)
    print("after clear:", [l[0] for l in gui.labels(page) if " of " in l[0]])
    x, y = gui.row(page, "eye profile")
    page.mouse.click(x, y); page.wait_for_timeout(1200)
    print("field:", [l[0] for l in gui.labels(page) if " of " in l[0] or l[0] == "eye profile"])
    page.screenshot(path="ey6.png", clip={"x": 246, "y": 76, "width": 240, "height": 400})
