import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    print("tree:", gui.tree(page))
    gui.search_tool(page, "Variable")
    page.wait_for_timeout(1500)
    print("labels:", gui.labels(page))
    inputs = page.locator("#feature-dialog input")
    print("inputs:", inputs.count())
    for i in range(inputs.count()):
        el = inputs.nth(i)
        print(" ", i, el.get_attribute("class"), repr(el.input_value()))
    page.screenshot(path=D + "bs3.png", clip={"x": 246, "y": 76, "width": 320, "height": 300})
