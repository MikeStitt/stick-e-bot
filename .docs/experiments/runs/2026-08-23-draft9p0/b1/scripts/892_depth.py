import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(400, 261); page.wait_for_timeout(500)
    page.keyboard.press("Meta+A")
    page.keyboard.type("#limbSeg")
    page.wait_for_timeout(600)
    page.mouse.click(328, 93); page.wait_for_timeout(2500)
    print([r for r in gui.labels(page) if r[2] < 500])
    page.keyboard.press("Shift+1"); page.wait_for_timeout(1500)
    gui.fit(page); page.wait_for_timeout(1500)
    page.screenshot(path=D+"la10.png")
