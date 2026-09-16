import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(447, 221); page.wait_for_timeout(1800)
    sc = gui.px_per_mm(page); sc = sc[0] if isinstance(sc, tuple) else sc
    print("px/mm", round(sc,3), "axis", [round(v) for v in gui.project(page, 0, 0, -100.4)])
    page.screenshot(path=D+"ub27.png")
