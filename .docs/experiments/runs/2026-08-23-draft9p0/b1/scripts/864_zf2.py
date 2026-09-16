import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.fit(page); page.wait_for_timeout(1800)
    sc, cam = gui.zoom_to(page, 11.0, at_px=gui.project(page, 0, 0, -100.4))
    page.wait_for_timeout(1500)
    print("px/mm", round(sc,3))
    pts = {}
    for nm, xyz in [("axis",(0,0,-100.4)), ("neg12",(0,-12,-100.4)), ("pos12",(0,12,-100.4))]:
        pts[nm] = [round(v) for v in gui.project(page, *xyz, cam)]
        print(nm, pts[nm])
    a = pts["axis"]
    page.screenshot(path=D+"ub32.png", clip={"x": max(0,a[0]-330), "y": max(0,a[1]-260), "width": 660, "height": 460})
