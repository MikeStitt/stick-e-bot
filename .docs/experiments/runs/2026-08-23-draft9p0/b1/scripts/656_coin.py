import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

O = (923, 389)
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    gui.clear(page)
    page.mouse.move(*O); page.wait_for_timeout(500)
    page.mouse.down(); page.wait_for_timeout(300)
    page.mouse.move(1010, 460, steps=20); page.wait_for_timeout(500)
    page.mouse.up(); page.wait_for_timeout(1200)
    gui.clear(page)
    page.screenshot(path=D+"tl83.png")
