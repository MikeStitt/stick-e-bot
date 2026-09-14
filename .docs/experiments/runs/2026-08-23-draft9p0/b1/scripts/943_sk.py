import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    r = gui.row(page, "Right")
    print("right row", r)
    page.mouse.click(r[0], r[1]); page.wait_for_timeout(1200)
    page.mouse.click(155, 58); page.wait_for_timeout(5000)       # Sketch
    page.keyboard.press("Shift+4"); page.wait_for_timeout(2500)  # Right view
    sc, cam = gui.zoom_to(page, 15.0)
    page.wait_for_timeout(1200)
    print("px/mm", round(sc, 4))
    for nm, pt in [("origin", (0,0,0)), ("clipC", (0,0,-19)), ("clipR", (0,5,-19)),
                   ("bot", (0,0,-24)), ("recTL", (0,-5,0)), ("recBR", (0,5,-19))]:
        print(nm, gui.project(page, *pt, cam))
    page.screenshot(path=D+"gr04.png")
