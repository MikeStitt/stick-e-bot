import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
F = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/frames/"
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.no_banner(page); gui.still(page)
    gui.frame(page, F+"cad.parts.hinge.blade.axle_sketch.png")
    gui.tick(page); page.wait_for_timeout(3000)
    common.scroll_tree(page, -20)
    x, y = common.jrow(page, "Sketch 2")
    gui.rename_row(page, "Sketch 2", "stub axle outline")
    page.wait_for_timeout(2000)
    for n, fid, st in common.features(page, api, s["did"], s["wid"], s["hinge_eid"])[-4:]:
        print(n, st)
