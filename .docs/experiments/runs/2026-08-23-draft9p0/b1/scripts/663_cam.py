import sys, json
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    s, cam = gui.px_per_mm(page), None
    print("px_per_mm", s)
    import onshape_gui
    cam = page.evaluate("() => window.__cam") if False else None
    sc, cam = gui.zoom_to(page, 11.67)
    P = lambda x, z: tuple(round(v) for v in gui.project(page, x, 0, z, cam))
    print("scale", round(sc,3), {"O": P(0,0), "bump": P(0, 9.6), "top": P(0,21)})
    json.dump({"cam": cam}, open(D+"cam_bump.json","w"))
    page.screenshot(path=D+"tl87.png")
