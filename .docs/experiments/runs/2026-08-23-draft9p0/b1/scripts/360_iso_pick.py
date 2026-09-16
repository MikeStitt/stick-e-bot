import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.keyboard.press("Shift+7"); page.wait_for_timeout(2500)
    gui.fit(page); page.wait_for_timeout(2000)
    scale, cam = gui.px_per_mm(page)
    print("scale", scale)
    for pt in [(0,0,48), (0,0,10), (24,0,-48)]:
        print(pt, gui.project(page, *pt, cam=cam))
    page.screenshot(path=D + "tj88.png")
