import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(343, 255)   # focus Mirror plane
    page.wait_for_timeout(800)
    page.mouse.move(140, 400)
    for _ in range(8):
        page.mouse.wheel(0, -300)
        page.wait_for_timeout(150)
    page.wait_for_timeout(1000)
    print(gui.row(page, "Right"))
    page.screenshot(path=D+"tj99.png")
