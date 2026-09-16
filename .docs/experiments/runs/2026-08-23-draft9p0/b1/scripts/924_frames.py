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
    page.mouse.move(900, 500); page.wait_for_timeout(300)
    page.keyboard.press("Shift+1"); page.wait_for_timeout(2200)
    gui.fit(page); page.wait_for_timeout(1800)
    page.mouse.move(1350, 700); page.wait_for_timeout(400)
    gui.frame(page, F + "cad.parts.l_limb.ends.medium.png")
    sc, cam = gui.px_per_mm(page)
    print("px/mm", sc)
    for nm, z in (("elbow_end", 0.0), ("wrist_end", -102.0)):
        at = gui.project(page, 0.0, 0.0, z, cam)
        print(nm, at)
        gui.ring(page, F + f"cad.parts.l_limb.{nm}.medium.png",
                 (int(at[0]), int(at[1])), radius=40)
