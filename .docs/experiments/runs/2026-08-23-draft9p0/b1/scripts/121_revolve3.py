import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api, onshape_screen as screen

s = common.load()
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.name_feature(page, "revolve stud")
    gui.tick(page); page.wait_for_timeout(2500)
    print("tree:", gui.tree(page))
    print("bbox:", common.bbox(page, api, s["did"], s["wid"], s["bs_eid"]))
    r = api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['bs_eid']}")
    print("parts:", [(x["partId"], x["name"]) for x in r["body"]])
    page.mouse.move(*screen.CENTER)
    page.keyboard.press("Shift+7"); page.wait_for_timeout(1500)
    gui.fit(page); gui.still(page)
    page.mouse.move(140, 620)
    gui.frame(page, D + "bs12.png")
