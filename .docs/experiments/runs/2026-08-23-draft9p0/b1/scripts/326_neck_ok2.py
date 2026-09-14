import sys, json
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api

s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.tick(page)
    page.wait_for_timeout(3000)
    t = gui.tree(page)
    print(t[-5:])
    cand = [n for n in t if n.startswith("Sketch")]
    if cand:
        gui.rename_row(page, cand[-1], "neck connector location")
        page.wait_for_timeout(2000)
    print(gui.tree(page)[-5:])
