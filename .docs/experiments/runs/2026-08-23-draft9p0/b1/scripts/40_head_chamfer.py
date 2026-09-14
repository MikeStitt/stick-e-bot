import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    gui.search_tool(page, "Chamfer")
    print("labels:", gui.labels(page))
    gui.pick(page, (923, 520), "the underside")
    print("field:", [l for l in gui.labels(page) if " of " in l[0]])
    el = gui.number_fields(page)[0]
    gui.set_field(page, el, "6 mm")
    print("distance:", el.input_value())
    page.screenshot(path="hd14.png")
