import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    gui.clear(page)
    page.screenshot(path=D + "bs27.png")
    for spot in [(1071, 523), (1070, 523), (1069, 523)]:
        gui.clear(page)
        try:
            gui.pick(page, spot, f"outer edge {spot}")
        except RuntimeError as e:
            print("miss", spot, e)
