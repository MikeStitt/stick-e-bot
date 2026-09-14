import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    x, y = gui.row(page, "Front")
    page.mouse.click(x, y); page.wait_for_timeout(800)
    page.mouse.click(155, 58); page.wait_for_timeout(3000)
    for row in gui.labels(page): print(row)
    page.keyboard.press("Shift+1"); page.wait_for_timeout(2000)
    gui.zoom_to(page, 6.0); page.wait_for_timeout(1500)
    scale, cam = gui.px_per_mm(page)
    for pt in [(0,0,0), (36,0,48), (36,0,40), (-36,0,-48)]:
        print(pt, gui.project(page, *pt, cam=cam))
    print("scale", scale)
    page.screenshot(path=D + "tj02.png")
