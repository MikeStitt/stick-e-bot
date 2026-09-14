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
    x, y = gui.row(page, "Front")
    page.mouse.click(x, y); page.wait_for_timeout(800)
    page.mouse.click(155, 58); page.wait_for_timeout(3000)
    page.mouse.move(*screen.CENTER)
    page.keyboard.press("n"); page.wait_for_timeout(2000)
    sc, cam = gui.zoom_to(page, 20.0)
    def px(*pt): return tuple(round(v) for v in gui.project(page, *pt, cam=cam))
    print("px/mm", round(sc, 3))
    print("origin", px(0, 0, 0), " +x test", px(10, 0, 0))
    for n, pt in [("ball bottom", (0, 0, -6)), ("arc end", (3, 0, 5.196)),
                  ("stalk top", (3, 0, 10)), ("axis top", (0, 0, 10))]:
        print(n, px(*pt))
    page.screenshot(path=D + "bs5.png")
