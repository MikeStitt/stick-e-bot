import sys, json
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    sc, cam = gui.zoom_to(page, 11.67)
    P = lambda x, z: tuple(round(v) for v in gui.project(page, x, 0, z, cam))
    print("scale", round(sc,3), {"O": P(0,0), "z16": P(0,16), "z21": P(0,21)})
    json.dump({"cam": cam}, open(D+"cam_bump.json","w"))
    page.mouse.move(1450, 900); page.wait_for_timeout(500)
    page.screenshot(path=D+"tl92.png")
