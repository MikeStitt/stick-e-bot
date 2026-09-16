import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    page.keyboard.press("Shift+7"); page.wait_for_timeout(2200)
    gui.fit(page); page.wait_for_timeout(2000)
    sc = gui.px_per_mm(page)
    sc = sc[0] if isinstance(sc, tuple) else sc
    print("px/mm after fit", round(sc, 3))
    for nm, xyz in [("origin",(0,0,0)), ("axis",(0,0,-100.4)),
                    ("pA",(0,8.8,-100.4)), ("pB",(0,-8.8,-100.4)), ("tip",(0,0,-112.4))]:
        print(nm, [round(v) for v in gui.project(page, *xyz)])
    page.screenshot(path=D+"ub21.png")
