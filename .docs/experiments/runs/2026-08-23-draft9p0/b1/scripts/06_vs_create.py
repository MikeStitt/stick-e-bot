import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    loc = page.get_by_text("Create Variable Studio", exact=True)
    if loc.count():
        loc.first.click()
        page.wait_for_timeout(3000)
    print("url:", page.url)
    btn = page.locator("button.insert-into-all-button")
    print("insert-into-all count:", btn.count())
    if btn.count():
        print("  box:", btn.first.bounding_box())
        print("  checked svg:", btn.first.locator("svg.checked").count())
    page.screenshot(path="vs.png")
