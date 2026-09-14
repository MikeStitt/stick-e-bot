import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.name_feature(page, "eye profile")
    gui.tick(page)
    print("tree:", gui.tree(page))
    gui.clear(page)
    gui.search_tool(page, "Extrude")
    gui.pick(page, (1020, 425), "the eye disc")
    print("labels:", [l for l in gui.labels(page) if l[0] in
                      ("New", "Add", "Remove", "Symmetric") or " of " in l[0]])
    page.screenshot(path="ey5.png", clip={"x": 246, "y": 76, "width": 240, "height": 400})
