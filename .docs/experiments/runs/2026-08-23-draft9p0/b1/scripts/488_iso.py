import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    page.keyboard.press("Shift+7"); page.wait_for_timeout(1500)
    gui.fit(page); page.wait_for_timeout(1500)
    s, cam = gui.px_per_mm(page)
    P = lambda x, y, z: tuple(round(v) for v in gui.project(page, x, y, z, cam))
    spots = {"toe_top": P(0, -64, -12), "toe_bot": P(0, -64, -24),
             "heel_top": P(0, 32, -12), "sideL_top": P(-19.795, -9.14, -12),
             "sideR_top": P(19.795, -9.14, -12)}
    print(round(s, 3), spots)
    gui.ring(page, D + "tk75.png", spots["toe_top"], radius=18)
