import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(336, 121); page.wait_for_timeout(1200)
    hit = common.menu_item(page, "Feature mirror")
    print("feature mirror at:", hit)
    if hit:
        page.mouse.click(*hit); page.wait_for_timeout(2000)
    print("labels:", gui.labels(page))
    gui.frame(page, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/mi2.png")
