import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.zoom_to(page, 14.0, at_px=(1020, 515)); page.wait_for_timeout(1500)
    scale, cam = gui.px_per_mm(page)
    q = gui.project(page, 44.3390, -4.8145, 27.2218, cam=cam)
    print(scale, q)
    gui.search_tool(page, "Mate connector")
    page.wait_for_timeout(1400)
    for i in range(2):
        page.mouse.move(round(q[0]), round(q[1])); page.wait_for_timeout(700)
        page.mouse.click(round(q[0]), round(q[1])); page.wait_for_timeout(1500)
    for row in gui.labels(page): print(row)
    page.screenshot(path=D + "tj46.png")
