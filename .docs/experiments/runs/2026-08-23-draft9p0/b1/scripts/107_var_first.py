import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    ins = page.locator("#feature-dialog input")
    ins.nth(1).click(); ins.nth(1).fill("ball"); ins.nth(1).press("Tab")
    page.wait_for_timeout(600)
    ins.nth(2).click(); ins.nth(2).fill("#torsoH / 8"); ins.nth(2).press("Tab")
    page.wait_for_timeout(2000)
    print("header:", [l[0] for l in gui.labels(page)][:2])
    page.screenshot(path=D + "bs4.png", clip={"x": 246, "y": 76, "width": 320, "height": 300})
