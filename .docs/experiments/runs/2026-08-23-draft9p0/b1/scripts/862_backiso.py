import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.move(900, 500)
    page.keyboard.press("Shift+7"); page.wait_for_timeout(2500)
    page.mouse.click(1441, 166); page.wait_for_timeout(2500)
    page.mouse.click(1441, 166); page.wait_for_timeout(2500)
    gui.fit(page); page.wait_for_timeout(2000)
    sc = gui.px_per_mm(page); sc = sc[0] if isinstance(sc, tuple) else sc
    print("px/mm", round(sc,3))
    for nm, xyz in [("axis",(0,0,-100.4)), ("neg12",(0,-12,-100.4)), ("pos12",(0,12,-100.4))]:
        print(nm, [round(v) for v in gui.project(page, *xyz)])
    page.screenshot(path=D+"ub30.png")
