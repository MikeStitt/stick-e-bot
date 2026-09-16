import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(356, 208); page.wait_for_timeout(900)     # From field
    page.mouse.move(923, 466); page.wait_for_timeout(800)
    page.mouse.click(923, 466); page.wait_for_timeout(1600)
    print("after From pick:")
    for r in gui.labels(page):
        print(" ", r)
