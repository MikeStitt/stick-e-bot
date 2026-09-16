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
    scale, cam = gui.px_per_mm(page)
    spot = tuple(round(v) for v in gui.project(page, 5.3, 5.3, -7.4, cam=cam))
    print("spot", spot)
    gui.search_tool(page, "Mate connector", settle=2500)
    gui.pick(page, spot, "collar bottom face")
    page.wait_for_timeout(1500)
    for row in gui.labels(page):
        print(row)
    page.screenshot(path=D + "bs58.png")
