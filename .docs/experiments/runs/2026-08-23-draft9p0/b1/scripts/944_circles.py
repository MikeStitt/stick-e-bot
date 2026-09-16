import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
CX, CY = 922, 812
S = 15.1536
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(307, 58); page.wait_for_timeout(1500)
    for r_mm in (5.0, 1.65):
        r = int(round(r_mm * S))
        page.mouse.move(CX - 40, CY - 40); page.wait_for_timeout(400)
        page.mouse.move(CX, CY); page.wait_for_timeout(1400)
        page.mouse.click(CX, CY); page.wait_for_timeout(900)
        page.mouse.move(CX + r, CY); page.wait_for_timeout(900)
        page.mouse.click(CX + r, CY); page.wait_for_timeout(1500)
        print("drew r", r_mm, "px", r)
    page.keyboard.press("Escape"); page.wait_for_timeout(1200)
    page.screenshot(path=D+"gr05.png")
