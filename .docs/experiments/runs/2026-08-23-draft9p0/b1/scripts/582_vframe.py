import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
F = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/frames/"
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    x, y = common.jrow(page, "Front")
    page.mouse.click(x, y)               # toggle the tree selection off
    page.wait_for_timeout(600)
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    page.mouse.move(900, 500)
    page.keyboard.press("Shift+7"); page.wait_for_timeout(1500)
    gui.fit(page); page.wait_for_timeout(1200)
    cam = None
    s, cam = gui.zoom_to(page, 14.0)
    px = tuple(round(v) for v in gui.project(page, 0, -5, 9.6, cam))
    print("scale", round(s,3), "valley at", px)
    s2, cam2 = gui.zoom_to(page, 55.0, at_px=px)
    px2 = tuple(round(v) for v in gui.project(page, 0, -5, 9.6, cam2))
    print("scale2", round(s2,3), "valley now", px2)
    gui.no_banner(page); gui.still(page)
    page.screenshot(path=D+"tl38.png")
