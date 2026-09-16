import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.tick(page); page.wait_for_timeout(3000)
    x, y = gui.row(page, "Plane 1")
    page.mouse.click(x, y, button="right"); page.wait_for_timeout(1400)
    page.mouse.click(*common.menu_item(page, "Rename")); page.wait_for_timeout(1000)
    page.keyboard.press("Meta+a"); page.keyboard.type("plane for shoulder")
    page.keyboard.press("Enter"); page.wait_for_timeout(2500)
    gui.wake(page)
    page.keyboard.press("Shift+5"); page.wait_for_timeout(2000)
    gui.fit(page); page.wait_for_timeout(1500)
    scale, cam = gui.px_per_mm(page)
    print("scale", scale)
    print("+Y at", gui.project(page, 0, 24, 0, cam=cam), " -Y at", gui.project(page, 0, -24, 0, cam=cam))
    print("+X at", gui.project(page, 36, 0, 0, cam=cam))
    page.screenshot(path=D + "tj14.png")
