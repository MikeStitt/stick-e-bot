import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    els = gui.number_fields(page)
    els[0].click(); page.wait_for_timeout(400)
    page.keyboard.press("Meta+A"); page.wait_for_timeout(200)
    page.keyboard.type("#valley_deep"); page.wait_for_timeout(900)
    page.mouse.click(287, 369)          # the "Depth" label of the offset block, to blur
    page.wait_for_timeout(2000)
    for e in gui.number_fields(page):
        print(repr(e.input_value()))
    page.screenshot(path=D+"tl36.png")
