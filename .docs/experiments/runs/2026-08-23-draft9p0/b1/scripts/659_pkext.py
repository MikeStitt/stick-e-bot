import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    s = common.load()
    page.mouse.click(336, 231); page.wait_for_timeout(1200)
    page.mouse.click(*common.menu_item(page, "Through all")); page.wait_for_timeout(1800)
    page.mouse.click(257, 314); page.wait_for_timeout(1500)   # Symmetric
    print([r for r in gui.labels(page)][-5:])
    page.mouse.click(447, 419); page.wait_for_timeout(1500)   # drop Part 1
    page.mouse.click(356, 401); page.wait_for_timeout(900)    # focus scope
    page.mouse.click(158, 721); page.wait_for_timeout(1800)   # Part 2
    print([r for r in gui.labels(page)][-5:])
