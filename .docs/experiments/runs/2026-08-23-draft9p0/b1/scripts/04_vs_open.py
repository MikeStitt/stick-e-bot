"""Close the units dialog; find the + (new element) button on the tab strip."""
import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    if page.locator("div[role='dialog']:visible").count():
        page.mouse.click(543, 92)
        page.wait_for_timeout(1200)
    print("dialogs:", page.locator("div[role='dialog']:visible").count())
    print("viewport:", page.viewport_size)
    for sel in ["#doc-new-element-button", "button[aria-label*='element' i]",
                "[data-bs-original-title*='element' i]", ".new-element-button"]:
        loc = page.locator(sel)
        print(sel, loc.count(), [loc.nth(i).bounding_box() for i in range(min(loc.count(), 3))])
    page.screenshot(path="tabstrip.png", clip={"x": 0, "y": 940, "width": 700, "height": 60})
