import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.move(1045, 146); page.wait_for_timeout(800)
    page.mouse.dblclick(1045, 146); page.wait_for_timeout(1800)
    el = [e for e in page.query_selector_all("input") if e.is_visible() and "deg" in (e.get_attribute("value") or "")]
    print("fields", len(el))
    if el:
        el[0].fill("90 deg - #tilt")
        page.wait_for_timeout(500)
        page.keyboard.press("Enter"); page.wait_for_timeout(2200)
    page.screenshot(path=D + "tj37.png", clip={"x": 900, "y": 70, "width": 500, "height": 420})
