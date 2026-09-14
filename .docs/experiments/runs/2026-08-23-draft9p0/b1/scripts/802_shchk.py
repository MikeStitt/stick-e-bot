import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_screen as screen
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    print(gui.tree(page))
    gui.clear(page)
    page.mouse.move(*screen.CENTER)
    page.keyboard.press("Shift+1"); page.wait_for_timeout(2000)
    gui.fit(page); page.wait_for_timeout(1800)
    sc, cam = gui.zoom_to(page, 6.9)
    x, y = [round(v) for v in gui.project(page, 0, 0, 55.4, cam=cam)]
    print("px/mm", round(sc,3), "ball centre px", x, y)
    page.screenshot(path=D+"ua61.png", clip={"x": x-110, "y": y-60, "width": 220, "height": 180})
