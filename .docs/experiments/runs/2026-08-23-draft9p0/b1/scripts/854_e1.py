import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    sc = gui.px_per_mm(page); sc = sc[0] if isinstance(sc, tuple) else sc
    a = [round(v) for v in gui.project(page, 0, 0, -100.4)]
    print("px/mm", round(sc,3), "axis", a)
    px = (a[0] + round(2.2*sc), a[1])
    print("pick", px)
    page.mouse.move(*px); page.wait_for_timeout(1200)
    page.mouse.click(*px); page.wait_for_timeout(2500)
    for r in gui.labels(page):
        if r[2] < 500: print(r)
