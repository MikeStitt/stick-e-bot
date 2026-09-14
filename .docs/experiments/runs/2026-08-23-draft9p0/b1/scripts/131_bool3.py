import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    x, y = gui.at(page, "Tools")
    page.mouse.click(x, y); page.wait_for_timeout(1000)
    bx, by = gui.row(page, "Ball stud")
    page.mouse.click(bx, by); page.wait_for_timeout(1500)
    x, y = gui.at(page, "Targets")
    page.mouse.click(x, y); page.wait_for_timeout(1000)
    sx, sy = gui.row(page, "Socket body")
    page.mouse.click(sx, sy); page.wait_for_timeout(1500)
    print("labels:", [l[0] for l in gui.labels(page)])
    page.screenshot(path=D + "bs19.png", clip={"x": 246, "y": 76, "width": 320, "height": 400})
