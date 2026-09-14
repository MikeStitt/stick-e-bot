import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    el = gui.number_fields(page)[0]
    gui.set_field(page, el, "#torsoD")
    print("depth reads:", el.input_value())
    gui.name_feature(page, "torso block")
    gui.tick(page)
    print("tree:", gui.tree(page))
    page.screenshot(path="ex3.png")
