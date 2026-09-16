import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
F = D + "frames/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for nm, z, scale in (("elbow_end", 0.0, 24.0), ("wrist_end", -102.0, 24.0)):
        page.mouse.move(900, 500); page.wait_for_timeout(300)
        page.keyboard.press("Shift+1"); page.wait_for_timeout(2000)
        gui.fit(page); page.wait_for_timeout(1600)
        sc, cam = gui.px_per_mm(page)
        c = gui.project(page, 0.0, 0.0, z, cam)
        sc, cam = gui.zoom_to(page, scale, at_px=(int(c[0]), int(c[1]))); page.wait_for_timeout(1400)
        at = gui.project(page, 0.0, 0.0, z, cam)
        page.mouse.move(1400, 800); page.wait_for_timeout(400)
        print(nm, round(sc, 2), at)
        gui.ring(page, F + f"cad.parts.l_limb.{nm}.closeup.png",
                 (int(at[0]), int(at[1])), radius=60)
