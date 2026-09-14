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
    page.mouse.move(900, 500)
    gui.fit(page); page.wait_for_timeout(1200)
    s, cam = gui.zoom_to(page, 16.0)
    P = lambda x, y, z: tuple(round(v) for v in gui.project(page, x, y, z, cam))
    tgt = P(8.485, 0, 8.485)
    print("scale", round(s,3), "round-end face", tgt, "origin", P(0,0,0))
    gui.ring(page, D+"tl42.png", tgt, radius=26)
