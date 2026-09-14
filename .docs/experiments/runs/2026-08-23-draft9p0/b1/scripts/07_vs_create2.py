import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.keyboard.press("Escape"); page.wait_for_timeout(400)
    page.mouse.click(53, 983)
    page.wait_for_timeout(1500)
    loc = page.get_by_text("Create Variable Studio", exact=True)
    print("count", loc.count(), "visible", loc.first.is_visible(), loc.first.bounding_box())
    b = loc.first.bounding_box()
    page.mouse.click(b["x"] + b["width"] / 2, b["y"] + b["height"] / 2)
    page.wait_for_timeout(4000)
    print("url:", page.url)
    btn = page.locator("button.insert-into-all-button")
    print("insert-into-all count:", btn.count(),
          btn.first.bounding_box() if btn.count() else "",
          btn.first.locator("svg.checked").count() if btn.count() else "")
    page.screenshot(path="vs2.png")
