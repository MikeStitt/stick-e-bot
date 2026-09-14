import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

for name in ["torsoW", "torsoD", "limbSeg"]:
    pass

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for name in ["torsoW", "torsoD", "limbSeg"]:
        page.locator("div.temporary-next-cell").first.click()
        page.wait_for_timeout(500)
        assert page.evaluate("document.activeElement.tagName") == "INPUT", name
        page.keyboard.type(name)
        page.wait_for_timeout(300)
        page.keyboard.press("Tab")
        page.wait_for_timeout(1400)
        print("added", name)
    cells = page.locator("div.os-td")
    print("os-td count:", cells.count())
    for i in range(cells.count()):
        c = cells.nth(i)
        b = c.bounding_box()
        print(i, (round(b["x"]), round(b["y"])), repr(c.inner_text()[:20]))
