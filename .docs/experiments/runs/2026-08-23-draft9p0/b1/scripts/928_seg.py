import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
F = D + "frames/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    common.open_feature(page, gui, "limb")
    page.wait_for_timeout(1500)
    for r in gui.labels(page):
        if r[2] < 420: print(r)
    page.mouse.move(380, 261); page.wait_for_timeout(2200)
    page.screenshot(path=D + "la27.png")
