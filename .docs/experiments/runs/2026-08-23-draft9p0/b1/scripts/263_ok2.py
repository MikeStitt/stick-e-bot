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
    r = api.api(page, "GET", f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['ps_eid']}/features")
    fs = {f["message"]["featureId"]: f["message"]["name"] for f in r["body"]["features"]}
    bad = [fs.get(row["key"], row["key"]) for row in r["body"]["featureStates"]
           if row["value"]["message"]["featureStatus"] != "OK"]
    print("not OK:", bad)
    gui.wake(page)
    page.keyboard.press("Shift+5"); page.wait_for_timeout(2200)
    gui.fit(page); page.wait_for_timeout(1500)
    page.screenshot(path=D + "tj22.png")
