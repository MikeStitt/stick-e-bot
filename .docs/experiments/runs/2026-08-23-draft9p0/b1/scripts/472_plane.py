import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"

def plane_now(page):
    for lab, x, y in gui.labels(page):
        if lab.endswith("plane") and y < 200 and x > 250:
            return lab, x, y
    return None

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    print("before:", plane_now(page))
    # cancel the sketch that landed on the wrong plane
    page.keyboard.press("Escape"); page.wait_for_timeout(400)
    page.mouse.click(451, 93); page.wait_for_timeout(2000)
    print("cancelled; features:", len([r for r in gui.tree(page)]))
    gui.clear(page)
    x, y = gui.row(page, "Top")
    print("Top row at", x, y)
    page.mouse.click(x, y); page.wait_for_timeout(900)
    page.screenshot(path=D+"tk61.png")
    page.mouse.click(155, 58); page.wait_for_timeout(4000)
    print("after:", plane_now(page))
    page.screenshot(path=D+"tk62.png")
