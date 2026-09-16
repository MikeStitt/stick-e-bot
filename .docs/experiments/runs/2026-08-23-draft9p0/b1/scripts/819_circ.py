import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    sc = gui.px_per_mm(page)
    print("px/mm", sc)
    page.mouse.click(307, 58); page.wait_for_timeout(1200)   # circle tool
    page.mouse.move(923, 522); page.wait_for_timeout(900)
    page.mouse.click(923, 522); page.wait_for_timeout(700)
    page.mouse.move(923 + int(12*sc), 522); page.wait_for_timeout(700)
    page.mouse.click(923 + int(12*sc), 522); page.wait_for_timeout(1200)
    page.keyboard.press("Escape"); page.wait_for_timeout(1000)
    page.screenshot(path=D+"ub03.png")
