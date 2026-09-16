import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.wake(page)
    page.keyboard.press("Shift+1"); page.wait_for_timeout(2500)
    gui.fit(page); page.wait_for_timeout(1800)
    gui.zoom_to(page, 12.0); page.wait_for_timeout(1500)
    scale, cam = gui.px_per_mm(page)
    for z in (-36.0, -43.4, -47.0):
        print(z, gui.project(page, 0, 0, z, cam=cam))
    print("scale", scale)
    px = gui.project(page, 0, 0, -43.4, cam=cam)
    page.screenshot(path=D + "hs31.png",
                    clip={"x": px[0]-180, "y": px[1]-160, "width": 360, "height": 320})
