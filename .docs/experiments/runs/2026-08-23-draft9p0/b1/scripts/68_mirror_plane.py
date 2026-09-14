import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    x, y = gui.at(page, "Mirror plane")
    page.mouse.click(x, y); page.wait_for_timeout(1200)
    rx, ry = gui.row(page, "Right")
    print("Right row:", rx, ry)
    page.mouse.click(rx, ry); page.wait_for_timeout(2000)
    print("labels:", gui.labels(page))
    gui.frame(page, D + "mi4.png")
