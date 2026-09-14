import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    els = page.query_selector_all("#feature-dialog input")
    for expr in ["#ball", "#wall", "#ball / 2", "#ball/2+#wall", "#ball / 2 + #wall"]:
        els[2].fill(expr)
        page.wait_for_timeout(400)
        page.keyboard.press("Tab")
        page.wait_for_timeout(900)
        title = page.query_selector("#feature-dialog").inner_text().split("\n")[0]
        print(repr(expr), "->", title)
