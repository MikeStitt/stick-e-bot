import sys, json
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui
from playwright.sync_api import sync_playwright
s = common.load(); did, wid = s["did"], s["wid"]
TABS = [("hinge", s["hinge_eid"]), ("l limb", s["ll_eid"])]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up(); page.keyboard.press("Escape"); page.wait_for_timeout(600)
    page.set_default_navigation_timeout(180000)
    for name, eid in TABS:
        page.goto(f"https://cad.onshape.com/documents/{did}/w/{wid}/e/{eid}",
                  wait_until="domcontentloaded")
        page.wait_for_timeout(25000)
        t = gui.tree(page)
        if len(t) < 6:
            page.wait_for_timeout(20000); t = gui.tree(page)
        print(f"\n=== {name}"); print(json.dumps(t))
