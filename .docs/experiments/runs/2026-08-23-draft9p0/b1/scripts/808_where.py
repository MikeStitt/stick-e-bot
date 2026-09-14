import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.keyboard.press("Escape"); page.wait_for_timeout(1200)
    gui.clear(page)
    page.keyboard.press("Shift+1"); page.wait_for_timeout(2000)   # Front
    gui.fit(page); page.wait_for_timeout(1500)
    sc, cam = gui.zoom_to(page, 20.0, at_px=gui.project(page, 0, 0, 55.4))
    page.wait_for_timeout(1500)
    print("px_per_mm", round(sc, 3))
    ctr = gui.project(page, 0, 0, 55.4, cam)
    mouth = gui.project(page, 0, 0, 59.0, cam)
    print("ball centre px", ctr, " mouth px", mouth)
    x, y = ctr
    page.screenshot(path=D+"ua71.png",
                    clip={"x": x-140, "y": y-140, "width": 280, "height": 280})
