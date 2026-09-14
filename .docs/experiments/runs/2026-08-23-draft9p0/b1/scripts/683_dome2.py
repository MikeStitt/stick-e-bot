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
    s = common.load()
    page.mouse.click(400, 288); page.wait_for_timeout(500)
    page.keyboard.press("Meta+A"); page.keyboard.type("#bump_d / 2")
    page.wait_for_timeout(400)
    page.mouse.click(328, 93); page.wait_for_timeout(2000)
    page.screenshot(path=D+"tm00.png")
    gui.tick(page); page.wait_for_timeout(4000)
    print([(n, st) for n, f, st in common.features(page, api, s["did"], s["wid"], s["hinge_eid"])[-2:]])
    for pt in api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['hinge_eid']}")["body"]:
        print(pt["name"], common.volume(page, api, s["did"], s["wid"], s["hinge_eid"], pt["partId"]))
