import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(1011, 449); page.wait_for_timeout(1500)
    for row in gui.labels(page): print(row)
    print("---")
    x, y = gui.row(page, "Front")
    page.mouse.click(x, y); page.wait_for_timeout(1800)
    for row in gui.labels(page): print(row)
    page.screenshot(path=D + "tj10.png")
