import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_screen as screen

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    page.mouse.move(*screen.CENTER)
    page.keyboard.press("Shift+2"); page.wait_for_timeout(2000)     # Top view
    sc, cam = gui.zoom_to(page, 15.0)
    def px(*pt): return tuple(round(v) for v in gui.project(page, *pt, cam=cam))
    print("px/mm", round(sc, 3), "origin", px(0, 0, 0), "r7.4", px(7.4, 0, 3.6))
    spot = px(7.4, 0, 3.6)
    gui.pick(page, spot, "collar top face")
    print("labels:", [l[0] for l in gui.labels(page)])
    page.screenshot(path=D + "bs22.png")
