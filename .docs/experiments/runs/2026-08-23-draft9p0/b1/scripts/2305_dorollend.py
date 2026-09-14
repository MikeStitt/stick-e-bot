"""#58 — click Roll to end and prove the bar is gone."""
import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui
from playwright.sync_api import sync_playwright
BAR = """() => document.querySelectorAll('.ns-list-item-rollbackbar').length"""
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up()
    print("bars before:", page.evaluate(BAR))
    page.mouse.click(195, 675)
    page.wait_for_timeout(7000)
    print("bars after:", page.evaluate(BAR))
    print("tree:", gui.tree(page)[-5:])
    page.screenshot(path=D + "unrolled.png")
