import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(53, 983)
    page.wait_for_timeout(1200)
    page.screenshot(path="plusmenu.png", clip={"x": 0, "y": 600, "width": 460, "height": 400})
    for t in ["Create Variable Studio", "Create Part Studio", "Create Assembly"]:
        loc = page.get_by_text(t, exact=True)
        print(t, loc.count(), [loc.nth(i).bounding_box() for i in range(min(loc.count(), 2))])
