import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(356, 203); page.wait_for_timeout(1000)
    for dx, dy in [(0, -56), (0, -58), (56, 0)]:
        px = (922 + dx, 864 + dy)
        page.mouse.move(*px); page.wait_for_timeout(1200)
        page.mouse.click(*px); page.wait_for_timeout(2200)
        got = [r for r in gui.labels(page) if r[2] < 500 and r[1] == 349]
        print(px, got)
        if any("Edge" in g[0] for g in got):
            break
        # drop whatever landed in the Between field
        for r in gui.labels(page):
            if r[0] == "×" and r[2] > 190 and r[2] < 240:
                page.mouse.click(447, r[2]); page.wait_for_timeout(1500)
