import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
F = D + "frames/cad.parts.u_limb."
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.fit(page); page.wait_for_timeout(1600)
    common.open_feature(page, gui, "limb")
    page.mouse.move(400, 261); page.wait_for_timeout(1500)
    gui.frame(page, F + "limbseg.png", clip={"x": 240, "y": 80, "width": 300, "height": 360})
    for r in gui.labels(page):
        if r[2] < 300: print(r)
