import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.keyboard.press("Escape"); page.wait_for_timeout(1200)
    v = gui.px_per_mm(page); print("px_per_mm ->", v)
    sc = v[0] if isinstance(v, tuple) else v
    c = gui.project(page, 0, 0, -7.4)
    print("centre px", c, "scale", sc)
    page.screenshot(path=D+"ub04.png")
