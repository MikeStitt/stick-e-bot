import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
S = 22.323376678466797
CX, CY = 923, 523
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(700, 800); page.wait_for_timeout(600)      # clear selection on empty sketch area
    page.mouse.click(307, 58); page.wait_for_timeout(1500)      # circle tool
    page.mouse.move(CX - 60, CY - 60); page.wait_for_timeout(500)
    page.mouse.move(CX, CY); page.wait_for_timeout(1500)
    page.mouse.click(CX, CY); page.wait_for_timeout(900)
    r = int(12 * S)
    page.mouse.move(CX + r, CY); page.wait_for_timeout(900)
    page.mouse.click(CX + r, CY); page.wait_for_timeout(1500)
    page.keyboard.press("Escape"); page.wait_for_timeout(1200)
    page.screenshot(path=D+"ub05.png")
