import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
F = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/frames/"
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    common.scroll_tree(page, -25)
    gui.rename_row(page, "Fillet 1", "round valley rim")
    page.wait_for_timeout(2000)
    print(common.features(page, api, s["did"], s["wid"], s["hinge_eid"])[-1])
    gui.clear(page)
    page.mouse.move(872, 445); page.wait_for_timeout(400)
    s2, cam = gui.zoom_to(page, 160.0, at_px=(872, 445))
    px = tuple(round(v) for v in gui.project(page, 0, -5, 9.6, cam))
    print("scale", round(s2,3), "valley", px)
    page.mouse.move(1450, 900); page.wait_for_timeout(1200)
    gui.no_banner(page); gui.still(page)
    gui.frame(page, F+"cad.parts.hinge.blade.valley_round.png",
              clip={"x": max(0,px[0]-300), "y": max(0,px[1]-225), "width": 600, "height": 450})
