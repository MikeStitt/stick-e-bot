import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(20, 95); page.wait_for_timeout(2500)
    el = page.query_selector("input[type=text]")
    el.click(); page.keyboard.press("Meta+A"); page.keyboard.type("t8 foot")
    page.wait_for_timeout(400)
    ta = page.query_selector("textarea")
    if ta:
        ta.click(); page.keyboard.type("Foot built at 2x: stadium-free tangent outline, r8 top round, 8 sole grooves, derived socket, one part.")
    page.wait_for_timeout(500)
    gui.frame(page, D + "frames/cad.parts.foot.version.png")
    page.mouse.click(912, 322); page.wait_for_timeout(4000)
    s = common.load()
    vs = api.api(page, "GET", f"/api/documents/d/{s['did']}/versions")["body"]
    for v in vs[:4]:
        print(v["name"], v["id"])
