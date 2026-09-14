import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api

s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(256, 335); page.wait_for_timeout(1200)     # Copy part
    gui.tick(page); page.wait_for_timeout(3500)
    gui.rename_row(page, "Transform 1", "copy for shoulder")
    page.wait_for_timeout(2000)
    r = api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['ps_eid']}")
    for q in r["body"]:
        if q["name"] != "Ball stud":
            continue
        fs = common.faces(page, api, s["did"], s["wid"], s["ps_eid"], q["partId"])
        sph = [f for f in fs if f["surface"]["type"] == "sphere"][0]
        b = sph["box"]
        c = [round((b["minCorner"][i] + b["maxCorner"][i]) / 2 * 1000, 4) for i in range(3)]
        print(q["partId"], "ball bbox centre", c)
