import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

OX, OY, R = 923, 523, 222

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.search_tool(page, "Center point arc")
    for spot in [(OX, OY), (OX + R, OY)]:
        page.mouse.move(*spot); page.wait_for_timeout(500)
        page.mouse.click(*spot); page.wait_for_timeout(500)
    for spot in [(OX + 160, OY - 160), (OX, OY - R), (OX - 160, OY - 160)]:
        page.mouse.move(*spot); page.wait_for_timeout(350)
    page.mouse.move(OX - R, OY); page.wait_for_timeout(500)
    page.mouse.click(OX - R, OY); page.wait_for_timeout(900)
    page.keyboard.press("Escape"); page.wait_for_timeout(700)
    page.screenshot(path="hd2.png")
