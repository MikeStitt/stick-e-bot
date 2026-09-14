import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    scale, cam = gui.px_per_mm(page)
    for z in (10, 3.6, 0, -7.4, -20):
        print(f"z={z:>6}", tuple(round(v) for v in gui.project(page, 0, 0, z, cam=cam)))
