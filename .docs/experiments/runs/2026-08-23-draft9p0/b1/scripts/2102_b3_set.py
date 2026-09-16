"""B3 — drive #torsoH. Pass the new value as argv[1], e.g. "120 mm"."""
import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui
from playwright.sync_api import sync_playwright
VAL = sys.argv[1]
TAG = sys.argv[2]
JS = """() => [...document.querySelectorAll('input')].map(e => {
  const r = e.getBoundingClientRect(); return [Math.round(r.x), Math.round(r.y), e.value]; })
  .filter(a => a[0] > 500)"""
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up()
    page.mouse.click(890, 204)
    page.wait_for_timeout(600)
    page.keyboard.press("Meta+A")
    page.keyboard.type(VAL)
    page.wait_for_timeout(400)
    page.keyboard.press("Enter")
    page.wait_for_timeout(6000)
    print("table now:")
    for row in page.evaluate(JS):
        print(" ", row)
    page.screenshot(path=D + f"b3_table_{TAG}.png")
