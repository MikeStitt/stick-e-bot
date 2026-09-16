import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
import onshape_screen as screen

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    s = common.load()
    gui.tick(page); page.wait_for_timeout(3000)
    common.scroll_tree(page, -25)
    gui.rename_row(page, "Mate connector 1", "blade to robot connector")
    page.wait_for_timeout(1500)
    page.mouse.click(140, 880); page.keyboard.press("Escape"); page.wait_for_timeout(800)
    print("selected", screen.selected(gui.probe(page)))
    fs = common.features(page, api, s["did"], s["wid"], s["hinge_eid"])
    print(len(fs))
    for n, f, st in fs[20:]:
        print(" ", repr(n), st)
