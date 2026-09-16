import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.move(986, 734)
    page.wait_for_timeout(900)
    page.screenshot(path=D+"tj97.png")
    page.keyboard.down("Shift")
    page.mouse.click(986, 734)
    page.keyboard.up("Shift")
    page.wait_for_timeout(1500)
    for r in gui.labels(page):
        print(r)
    page.screenshot(path=D+"tj98.png")
