import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(453, 230); page.wait_for_timeout(2000)
    page.mouse.click(453, 369); page.wait_for_timeout(2500)
    page.mouse.move(900, 700)
    page.keyboard.press("Shift+1"); page.wait_for_timeout(1200)
    gui.fit(page); page.wait_for_timeout(1200)
    page.mouse.move(1450, 900); page.wait_for_timeout(800)
    page.screenshot(path=D+"tl60.png")
