import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_screen as screen
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    page.mouse.move(900, 500); page.wait_for_timeout(400)
    cam = screen.camera(page)
    P = lambda x, y, z: tuple(round(v) for v in gui.project(page, x, y, z, cam))
    for nm, pt in (("A", (1,-5,9.6)), ("B", (-1,-5,9.6)), ("C", (0,-5,10.6)), ("D", (0,-5,8.6)),
                   ("mid", (0,-5,9.6))):
        print(nm, P(*pt))
    page.screenshot(path=D+"tl40.png")
