import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    page.mouse.click(700, 900); page.wait_for_timeout(600)   # deselect on empty
    page.keyboard.press("Alt+c"); page.wait_for_timeout(700)
    page.keyboard.type("rectangle", delay=60); page.wait_for_timeout(1600)
    page.screenshot(path=D + "tj27.png", clip={"x": 1000, "y": 40, "width": 600, "height": 320})
