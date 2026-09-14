import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    s = common.load()
    gui.tick(page); page.wait_for_timeout(3000)
    print([(n, st) for n, f, st in common.features(page, api, s["did"], s["wid"], s["hinge_eid"])[-2:]])
    page.keyboard.press("Shift+4"); page.wait_for_timeout(1500)
    gui.fit(page); page.wait_for_timeout(1200)
    sc, cam = gui.zoom_to(page, 8.0)
    P = lambda x, y, z: tuple(round(v) for v in gui.project(page, x, y, z, cam))
    print("scale", round(sc,3), {"top": P(0,0,45), "y6": P(0,6,45), "O": P(0,0,0)})
    page.mouse.move(1450, 900); page.wait_for_timeout(500)
    page.screenshot(path=D+"tm06.png")
