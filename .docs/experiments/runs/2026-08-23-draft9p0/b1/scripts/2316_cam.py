import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_screen as screen
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up(); page.keyboard.press("Escape"); page.wait_for_timeout(600)
    print("hook:", screen.hook(page))
    gui.wake(page)
    page.wait_for_timeout(2500)
    cam = screen.camera(page)
    print("camera:", "none" if cam is None else "got one")
    if cam:
        print("origin at", gui.project(page, 0, 0, 0, cam=cam))
        print("x=-49.55 z=19.24 at", gui.project(page, -49.55086, -7.8236, 19.23548, cam=cam))
        print("x=-24 z=-58 at", gui.project(page, -24, 0, -58, cam=cam))
        print("px per mm:", gui.px_per_mm(page))
