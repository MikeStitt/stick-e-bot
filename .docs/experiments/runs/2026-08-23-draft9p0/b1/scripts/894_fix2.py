import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    els = page.query_selector_all("#feature-dialog input")
    e = els[3]
    e.click(); page.wait_for_timeout(600)
    page.keyboard.press("Meta+A"); page.wait_for_timeout(300)
    page.keyboard.press("Backspace"); page.wait_for_timeout(400)
    print("after clear", repr(e.input_value()))
    page.keyboard.type("#limbSeg", delay=60)
    page.wait_for_timeout(800)
    print("typed", repr(e.input_value()))
    page.mouse.click(314, 93); page.wait_for_timeout(2500)
    print("after blur", repr(els[3].input_value()))
    page.screenshot(path=D+"la11.png")
