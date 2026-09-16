import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
F = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/frames/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.no_banner(page); gui.still(page)
    gui.ring(page, F+"cad.parts.hinge.blade.pattern_axis.medium.png", (849, 514), radius=34)
    s, cam = gui.zoom_to(page, 60.0, at_px=(849, 514))
    px = tuple(round(v) for v in gui.project(page, 0, -6.6, 0, cam))
    print("scale", round(s,3), "axis at", px)
    gui.still(page)
    gui.ring(page, F+"cad.parts.hinge.blade.pattern_axis.closeup.png", px, radius=60,
             clip={"x": max(0,px[0]-300), "y": max(0,px[1]-225), "width": 600, "height": 450})
