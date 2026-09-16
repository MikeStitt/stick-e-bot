import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    gui.pick(page, (700, 650), "the left side")
    page.mouse.click(1033, 58)
    page.wait_for_timeout(1200)
    page.screenshot(path="hd6.png", clip={"x": 940, "y": 70, "width": 220, "height": 520})
