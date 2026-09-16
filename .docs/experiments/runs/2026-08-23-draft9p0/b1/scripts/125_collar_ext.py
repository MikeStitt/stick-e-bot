import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.name_feature(page, "collar profile")
    gui.tick(page); page.wait_for_timeout(1500)
    gui.clear(page)
    gui.search_tool(page, "Extrude")
    x, y = gui.row(page, "collar profile")
    page.mouse.click(x, y); page.wait_for_timeout(1500)
    print("labels:", [l[0] for l in gui.labels(page)])
    el = gui.number_fields(page)[0]
    el.click(); el.fill("#grip"); el.press("Tab"); page.wait_for_timeout(2000)
    print("depth:", el.input_value())
    sx, sy = gui.at(page, "Second end position")
    page.mouse.click(sx, sy); page.wait_for_timeout(2000)
    fs = gui.number_fields(page)
    print("fields:", [f.input_value() for f in fs])
    page.screenshot(path=D + "bs15.png", clip={"x": 246, "y": 76, "width": 320, "height": 500})
