import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

VALUES = ["96 mm", "72 mm", "48 mm", "48 mm"]

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for row, val in enumerate(VALUES):
        cell = page.locator("div.os-td").nth(4 * row + 2)
        ok = False
        for attempt in range(4):
            cell.dblclick()
            page.wait_for_timeout(500)
            if cell.locator("input:focus").count() == 1:
                ok = True
                print(f"row {row}: INPUT after {attempt + 1} dblclick(s)")
                break
        if not ok:
            raise SystemExit(f"row {row}: never reached INPUT")
        page.keyboard.press("Meta+A")
        page.keyboard.type(val)
        page.wait_for_timeout(300)
        page.keyboard.press("Enter")
        page.wait_for_timeout(1200)
    page.keyboard.press("Escape")
    page.wait_for_timeout(800)
    for i in range(16):
        c = page.locator("div.os-td").nth(i)
        inp = c.locator("input")
        print(i, repr(inp.first.input_value() if inp.count() else c.inner_text()[:20]))
    page.screenshot(path="vs3.png", clip={"x": 520, "y": 110, "width": 620, "height": 250})
