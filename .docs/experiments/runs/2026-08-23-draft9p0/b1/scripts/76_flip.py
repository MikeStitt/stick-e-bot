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
    sc, cam = gui.zoom_to(page, 6.0)
    for n, pt in [("origin", (0, 0, 0)), ("L x=-15", (-15, 0, -18)), ("R x=+15", (15, 0, -18)),
                  ("eye x=+16", (16, 0, 16))]:
        print(n, tuple(round(v) for v in gui.project(page, *pt, cam=cam)))
    gui.frame(page, D + "mo2.png")
