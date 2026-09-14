import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.name_feature(page, "head profile")
    gui.tick(page)
    print("tree:", gui.tree(page))

    gui.clear(page)
    gui.search_tool(page, "Extrude")
    gui.pick(page, (923, 600), "the head region")
    print([l for l in gui.labels(page) if l[0] in ("New", "Add", "Symmetric")])
    x, y = gui.at(page, "Symmetric")
    page.mouse.click(x, y); page.wait_for_timeout(1000)
    el = gui.number_fields(page)[0]
    gui.set_field(page, el, "60 mm")
    print("depth:", el.input_value())
    gui.name_feature(page, "head body")
    page.screenshot(path="hd8.png", clip={"x": 246, "y": 76, "width": 230, "height": 380})
