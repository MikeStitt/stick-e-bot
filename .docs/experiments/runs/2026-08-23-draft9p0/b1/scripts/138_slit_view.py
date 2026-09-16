import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_screen as screen

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.move(*screen.CENTER)
    page.keyboard.press("n"); page.wait_for_timeout(2500)
    sc, cam = gui.zoom_to(page, 12.0)
    def px(*pt): return tuple(round(v) for v in gui.project(page, *pt, cam=cam))
    print("px/mm", round(sc, 3))
    for n, pt in [("origin", (0, 0, 3.6)), ("+x 12", (12, 0, 3.6)), ("+y 12", (0, 12, 3.6)),
                  ("A", (5, -0.8, 3.6)), ("B", (12, 0.8, 3.6))]:
        print(n, px(*pt))
    page.screenshot(path=D + "bs25.png")
