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
    page.mouse.click(447, 172)          # drop the face from Origin entity
    page.wait_for_timeout(1500)
    page.mouse.move(900, 600); page.wait_for_timeout(400)
    cam = screen.camera(page)
    tgt = tuple(round(v) for v in gui.project(page, 0, -6.6, 0, cam))
    print("stub front face centre", tgt)
    gui.pick(page, tgt, "stub front face")
    page.wait_for_timeout(1500)
    page.screenshot(path=D+"tl44.png")
