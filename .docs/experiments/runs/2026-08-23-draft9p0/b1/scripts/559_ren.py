import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    common.scroll_tree(page, -25)
    print("row", common.jrow(page, "Sketch 1"))
    gui.rename_row(page, "Sketch 1", "stub axle outline")
    page.wait_for_timeout(2000)
    for n, fid, st in common.features(page, api, s["did"], s["wid"], s["hinge_eid"])[-2:]:
        print(repr(n), st)
