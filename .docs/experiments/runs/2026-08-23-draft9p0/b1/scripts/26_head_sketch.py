import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_screen as screen

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.viewport(page)
    gui.clear(page)
    x, y = gui.row(page, "Front")
    page.mouse.click(x, y); page.wait_for_timeout(800)
    page.mouse.click(155, 58); page.wait_for_timeout(3000)
    print("dialog:", page.locator("#feature-dialog").count())
    page.mouse.move(*screen.CENTER)
    page.keyboard.press("n"); page.wait_for_timeout(2000)
    print(screen.hook(page))
    s, cam = gui.zoom_to(page, 6.0)
    print("px/mm", round(s, 4), "origin", gui.project(page, 0, 0, 0, cam))
    page.screenshot(path="hd1.png")
