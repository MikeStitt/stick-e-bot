import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    x, y = gui.at(page, "Tangent propagation")
    page.mouse.click(x, y); page.wait_for_timeout(2500)
    print("features error:", page.get_by_text("failed to regenerate", exact=False)
          .locator("visible=true").count())
    page.screenshot(path="hd17.png", clip={"x": 0, "y": 76, "width": 1000, "height": 400})
