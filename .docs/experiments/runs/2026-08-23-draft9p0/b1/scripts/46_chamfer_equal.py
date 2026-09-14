import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    if page.locator("#feature-dialog").count():
        page.mouse.click(451, 93); page.wait_for_timeout(1800)
    gui.clear(page)
    gui.search_tool(page, "Chamfer")
    gui.pick(page, (923, 520), "the underside")
    print("field:", [l[0] for l in gui.labels(page) if " of " in l[0]])
    x, y = gui.at(page, "Distance and angle")
    page.mouse.click(x, y); page.wait_for_timeout(1000)
    page.screenshot(path="hd20.png", clip={"x": 246, "y": 76, "width": 260, "height": 400})
