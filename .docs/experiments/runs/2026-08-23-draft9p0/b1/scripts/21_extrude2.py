import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    x, y = gui.at(page, "Symmetric")
    print("Symmetric at", x, y)
    page.mouse.click(x, y)
    page.wait_for_timeout(1200)
    fields = gui.number_fields(page)
    for f in fields:
        print("field:", f)
    page.screenshot(path="ex2.png", clip={"x": 246, "y": 76, "width": 230, "height": 380})
