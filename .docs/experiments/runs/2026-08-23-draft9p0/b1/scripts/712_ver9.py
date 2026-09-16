import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(20, 95); page.wait_for_timeout(2500)
    el = page.query_selector("input[type=text]")
    el.click(); page.keyboard.press("Meta+A"); page.keyboard.type("t9 hinge")
    page.wait_for_timeout(400)
    ta = page.query_selector("textarea")
    if ta:
        ta.click()
        page.keyboard.type("Hinge built at 2x: blade with stub axle and 24 valleys, fork with two full-slice ears, "
                           "0/4.4 axle hole, 24 domed click bumps, r12 round ends on both halves, no slit.")
    page.wait_for_timeout(500)
    gui.frame(page, D + "frames/cad.parts.hinge.version.png")
    page.mouse.click(912, 322); page.wait_for_timeout(5000)
    s = common.load()
    vs = api.api(page, "GET", f"/api/documents/d/{s['did']}/versions")["body"]
    for v in vs[:4]:
        print(v["name"], v["id"])
