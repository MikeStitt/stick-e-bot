import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.wake(page, (1350, 800))
    for pt in [(0,0,3.6), (5,0.8,3.6), (12,0.8,3.6), (5,-0.8,3.6), (12,-0.8,3.6)]:
        print(pt, tuple(round(v) for v in gui.project(page, *pt)))
    page.screenshot(path=D + "bs43.png")
