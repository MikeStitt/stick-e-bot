import sys, json
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    common.scroll_tree(page, 25)
    hit = common.jrow(page, "Front")
    print("Front row", hit)
    page.mouse.click(*hit); page.wait_for_timeout(900)
    page.mouse.click(155, 58); page.wait_for_timeout(4500)
    page.keyboard.press("Shift+1"); page.wait_for_timeout(1200)
    gui.fit(page); page.wait_for_timeout(1000)
    s, cam = gui.zoom_to(page, 30.0)
    P = lambda x, z: tuple(round(v) for v in gui.project(page, x, 0, z, cam))
    pts = {"O": P(0,0), "R": P(2,0), "Q": P(1.4142,1.4142)}
    print("scale", round(s,3), pts)
    json.dump({"cam": cam, "pts": {k: list(v) for k,v in pts.items()}}, open(D+"cam_stub.json","w"))
    page.screenshot(path=D+"tl21.png")
