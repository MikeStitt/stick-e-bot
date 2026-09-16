import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
F = D + "frames/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
W, H = 560, 420
def clipbox(x, y):
    cx = max(246, min(1600 - W, int(x) - W // 2))
    cy = max(80,  min(965 - H,  int(y) - H // 2))
    return {"x": cx, "y": cy, "width": W, "height": H}
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for nm, z in (("elbow_end", 0.0), ("wrist_end", -102.0)):
        page.mouse.move(900, 500); page.wait_for_timeout(300)
        page.keyboard.press("Shift+1"); page.wait_for_timeout(2000)
        gui.fit(page); page.wait_for_timeout(1600)
        sc, cam = gui.px_per_mm(page)
        c = gui.project(page, 0.0, 0.0, z, cam)
        sc, cam = gui.zoom_to(page, 24.0, at_px=(int(c[0]), int(c[1]))); page.wait_for_timeout(1400)
        at = gui.project(page, 0.0, 0.0, z, cam)
        page.mouse.move(1450, 820); page.wait_for_timeout(400)
        print(nm, round(sc, 2), at, clipbox(*at))
        gui.ring(page, F + f"cad.parts.l_limb.{nm}.closeup.png",
                 (int(at[0]), int(at[1])), radius=60, clip=clipbox(*at))
