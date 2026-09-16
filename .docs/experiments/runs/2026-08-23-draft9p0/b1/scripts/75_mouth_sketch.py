import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_screen as screen, onshape_session as api

s = common.load()
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    print("volume before mouth mm3:",
          common.volume(page, api, s["did"], s["wid"], s["head_eid"], "JHD"))
    gui.clear(page)
    x, y = gui.row(page, "Front")
    page.mouse.click(x, y); page.wait_for_timeout(800)
    page.mouse.click(155, 58); page.wait_for_timeout(3000)
    print("dialog:", page.locator("#feature-dialog").count())
    page.mouse.move(*screen.CENTER)
    page.keyboard.press("n"); page.wait_for_timeout(2000)
    sc, cam = gui.zoom_to(page, 6.0)
    for n, pt in [("origin", (0, 0, 0)), ("L", (-15, 0, -18)), ("R", (15, 0, -18)),
                  ("mouth top", (0, 0, -13)), ("mouth bot", (0, 0, -23))]:
        print(n, tuple(round(v) for v in gui.project(page, *pt, cam=cam)))
    print("px/mm", round(sc, 3))
    gui.frame(page, D + "mo1.png")
