import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    scale, cam = gui.px_per_mm(page)
    ox, oy = gui.project(page, 0, 0, 0, cam=cam)
    print("scale", scale, "origin", ox, oy)
    page.keyboard.press("c"); page.wait_for_timeout(800)
    page.mouse.move(ox, oy); page.wait_for_timeout(600)
    page.mouse.click(ox, oy); page.wait_for_timeout(500)
    page.mouse.move(ox + 120, oy); page.wait_for_timeout(500)
    page.mouse.click(ox + 120, oy); page.wait_for_timeout(1000)
    page.keyboard.press("Escape"); page.wait_for_timeout(800)
    page.screenshot(path=D+"tk44.png")
