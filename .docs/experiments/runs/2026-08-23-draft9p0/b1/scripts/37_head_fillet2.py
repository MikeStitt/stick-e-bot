import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.pick(page, (997, 378), "back arch edge", add=True)
    print("field:", [l for l in gui.labels(page) if "of head" in l[0]])
    el = gui.number_fields(page)[0]
    gui.set_field(page, el, "12 mm")
    print("radius:", el.input_value())
    page.screenshot(path="hd11.png")
