"""Confirm the Workspace units dialog with its green tick, then re-open and read back."""
import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)

    dlg = page.locator("div[role='dialog']:visible").first
    if dlg.count() and dlg.is_visible():
        print("dialog box:", dlg.bounding_box())
        page.mouse.click(543, 92)          # the green tick, located from units.png
        page.wait_for_timeout(1500)
    print("dialog still visible:", page.locator("div[role='dialog']:visible").count())

    # re-open and read back
    page.mouse.click(155, 17)              # the hamburger
    page.wait_for_timeout(900)
    page.mouse.click(252, 236)             # "Workspace units..."
    page.wait_for_timeout(1800)
    dlg = page.locator("div[role='dialog']:visible").first
    sels = dlg.locator("select")
    for i in range(sels.count()):
        el = sels.nth(i)
        print(f"  [{i}] value={el.input_value()!r} text={el.locator('option:checked').first.text_content()!r}")
    print("box:", dlg.bounding_box())
    page.screenshot(path="units2.png", clip={"x": 240, "y": 75, "width": 360, "height": 120})
