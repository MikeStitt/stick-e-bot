import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    page.wait_for_timeout(600)
    page.mouse.move(1000, 460); page.wait_for_timeout(700)
    page.mouse.click(1000, 460); page.wait_for_timeout(1200)
    page.mouse.click(155, 58)
    page.wait_for_timeout(3500)
    page.mouse.click(514, 58)           # Point
    page.wait_for_timeout(1500)
    page.mouse.move(980, 470); page.wait_for_timeout(700)
    page.mouse.click(980, 470); page.wait_for_timeout(1200)
    page.keyboard.press("Escape"); page.wait_for_timeout(900)
    # select the new point, add the origin, make them coincident
    page.mouse.move(980, 470); page.wait_for_timeout(500)
    page.mouse.click(980, 470); page.wait_for_timeout(900)
    page.keyboard.down("Shift")
    page.mouse.move(923, 523); page.wait_for_timeout(500)
    page.mouse.click(923, 523); page.wait_for_timeout(900)
    page.keyboard.up("Shift")
    page.wait_for_timeout(600)
    page.keyboard.press("i")
    page.wait_for_timeout(1800)
    page.screenshot(path=D + "tj71.png")
