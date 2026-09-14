import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    page.mouse.move(900, 700); page.wait_for_timeout(300)
    page.keyboard.press("Shift+1"); page.wait_for_timeout(2200)
    gui.fit(page); page.wait_for_timeout(1500)
    sc, cam = gui.px_per_mm(page)
    c = gui.project(page, 0.0, 0.0, -102.0, cam)
    print("px/mm", sc, "ball centre", c)
    sc, cam = gui.zoom_to(page, 14.0, at_px=(int(c[0]), int(c[1]))); page.wait_for_timeout(1500)
    at = gui.project(page, 3.0, 0.0, -104.5, cam)
    print("px/mm", sc, "pick", at)
    gui.search_tool(page, "Mate connector"); page.wait_for_timeout(2500)
    page.mouse.move(int(at[0]), int(at[1])); page.wait_for_timeout(1000)
    page.mouse.click(int(at[0]), int(at[1])); page.wait_for_timeout(2500)
    for r in gui.labels(page):
        if r[2] < 460: print(r)
    page.screenshot(path=D+"la26.png")
