import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.zoom_to(page, 9.0); page.wait_for_timeout(1500)
    scale, cam = gui.px_per_mm(page)
    a = gui.project(page, 30, 0, 44, cam=cam)
    b = gui.project(page, 30, 0, 36, cam=cam)
    print(scale, a, b)
    gui.search_tool(page, "Line")
    page.wait_for_timeout(1200)
    page.mouse.click(round(a[0]), round(a[1])); page.wait_for_timeout(700)
    page.mouse.click(round(b[0]), round(b[1])); page.wait_for_timeout(700)
    page.keyboard.press("Escape"); page.wait_for_timeout(1200)
    page.screenshot(path=D + "tj03.png")
