import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    x, y = gui.at(page, "Remove")
    page.mouse.click(x, y); page.wait_for_timeout(1500)
    el = gui.number_fields(page)[0]
    el.click(); page.wait_for_timeout(300)
    el.fill("3 mm"); el.press("Tab"); page.wait_for_timeout(1800)
    print("depth:", el.input_value())
    sx, sy = gui.at(page, "Starting offset")
    page.mouse.click(sx, sy); page.wait_for_timeout(1800)
    print("labels:", gui.labels(page))
    fields = gui.number_fields(page)
    print("fields:", [f.input_value() for f in fields])
    page.screenshot(path=D + "mo15.png", clip={"x": 246, "y": 76, "width": 240, "height": 500})
