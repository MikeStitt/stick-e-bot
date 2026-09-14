"""Workspace units -> Millimeter, decimals 0.12345."""
import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api

s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    print("on:", page.url[:80])

    # the hamburger, left of the document name
    page.locator("#documentMenuButton, button[aria-label='Document menu']").first.click()
    page.wait_for_timeout(900)
    page.get_by_text("Workspace units", exact=False).first.click()
    page.wait_for_timeout(1800)
    dlg = page.locator("div[role='dialog']:visible").first
    sels = dlg.locator("select")
    n = sels.count()
    print("selects in dialog:", n)
    for i in range(n):
        el = sels.nth(i)
        opts = el.locator("option").all_text_contents()
        print(f"  [{i}] value={el.input_value()!r} opts={opts[:8]}")
