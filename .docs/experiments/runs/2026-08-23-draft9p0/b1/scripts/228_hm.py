import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.tick(page); page.wait_for_timeout(3000)
    x, y = gui.row(page, "Mate connector 1")
    page.mouse.click(x, y, button="right"); page.wait_for_timeout(1400)
    page.mouse.click(*common.menu_item(page, "Rename")); page.wait_for_timeout(1200)
    page.keyboard.press("Meta+a"); page.keyboard.type("head mate")
    page.keyboard.press("Enter"); page.wait_for_timeout(2500)
    r = api.api(page, "GET", f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['head_eid']}/features")
    for f in r["body"]["features"]:
        print(f["message"]["featureType"], "|", f["message"]["name"])
    print([st["message"]["featureStatus"] for st in r["body"]["featureStates"].values()])
