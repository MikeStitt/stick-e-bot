import sys, collections
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api

s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    common.delete_row(page, gui, "Chamfer 1")
    print("tree:", gui.tree(page))
    gui.clear(page)
    gui.search_tool(page, "Chamfer")
    gui.pick(page, (846, 621), "bottom front edge")
    print("field:", [l[0] for l in gui.labels(page) if " of " in l[0]])
    el = gui.number_fields(page)[0]
    gui.set_field(page, el, "6 mm")
    page.wait_for_timeout(2500)
    page.screenshot(path="hd26.png")
