import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(583, 983, button="right")
    page.wait_for_timeout(1200)
    page.screenshot(path="tabmenu.png")
    for t in ["Delete", "Rename"]:
        loc = page.get_by_text(t, exact=True)
        print(t, loc.count(), [loc.nth(i).bounding_box() for i in range(min(loc.count(), 4))])
