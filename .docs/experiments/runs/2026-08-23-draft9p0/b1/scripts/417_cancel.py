import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(451, 93)          # cancel the Ball dialog
    page.wait_for_timeout(2000)
    page.mouse.move(100, 235); page.wait_for_timeout(800)
    page.mouse.click(219, 235); page.wait_for_timeout(2000)   # unhide head
    for r in gui.tree(page):
        print(r)
    page.mouse.click(380, 984)          # body tab
    page.wait_for_timeout(7000)
    page.screenshot(path=D+"tk32.png")
    print("on body")
