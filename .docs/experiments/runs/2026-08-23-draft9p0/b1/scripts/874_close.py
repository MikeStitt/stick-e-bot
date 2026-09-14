import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
F = D + "frames/cad.parts.u_limb."
SHOTS = [("shoulder_end", (0, 0, 0)), ("elbow_end", (0, 0, -100.4)), ("move_fork", (0, 0, -55.4))]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for name, xyz in SHOTS:
        gui.fit(page); page.wait_for_timeout(1600)
        sc, cam = gui.zoom_to(page, 26.0, at_px=gui.project(page, *xyz))
        page.wait_for_timeout(1500)
        at = [round(v) for v in gui.project(page, *xyz, cam)]
        vp = gui.viewport(page)
        print(name, "px/mm", round(sc, 2), "at", at, "vp", vp)
        gui.ring(page, F + name + ".closeup.png", at, radius=60)
