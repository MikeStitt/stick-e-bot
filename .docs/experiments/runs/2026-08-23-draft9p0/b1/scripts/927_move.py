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
    page.keyboard.press("Shift+1"); page.wait_for_timeout(2000)
    gui.fit(page); page.wait_for_timeout(1600)
    sc, cam = gui.px_per_mm(page)
    c = gui.project(page, 0.0, 0.0, -97.0, cam)
    sc, cam = gui.zoom_to(page, 14.0, at_px=(int(c[0]), int(c[1]))); page.wait_for_timeout(1400)
    page.mouse.move(1450, 300); page.wait_for_timeout(400)
    gui.frame(page, F + "cad.parts.l_limb.move_stud.medium.png")
    a = gui.project(page, 0.0, 0.0, -92.0, cam)
    b = gui.project(page, 0.0, 0.0, -102.0, cam)
    print("target", a, "source", b)
    gui.ring(page, F + "cad.parts.l_limb.move_stud.target.closeup.png",
             (int(a[0]), int(a[1])), radius=45)
    gui.ring(page, F + "cad.parts.l_limb.move_stud.source.closeup.png",
             (int(b[0]), int(b[1])), radius=45)
