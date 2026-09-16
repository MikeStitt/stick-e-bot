import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

O, Rc, TL, BR = (923,389), (1063,389), (760,323), (1086,552)

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.search_tool(page, "Circle")
    for spot in (O, Rc):
        page.mouse.move(*spot); page.wait_for_timeout(800)
        page.mouse.click(*spot); page.wait_for_timeout(900)
    page.keyboard.press("Escape"); page.wait_for_timeout(700)
    gui.search_tool(page, "Corner rectangle")
    for spot in (TL, BR):
        page.mouse.move(*spot); page.wait_for_timeout(800)
        page.mouse.click(*spot); page.wait_for_timeout(900)
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    page.keyboard.press("Escape"); page.wait_for_timeout(800)
    gui.clear(page)
    page.screenshot(path=D+"tl72.png")
