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
    gui.clear(page); page.wait_for_timeout(600)
    x, y = gui.row(page, "copy for shoulder")
    page.mouse.dblclick(x, y); page.wait_for_timeout(2500)
    labs = gui.labels(page)
    for r in labs:
        print(r)
    cp = [l for l in labs if l[0] == "Copy part"][0]
    fy = cp[2] - 30
    print("flip at", 258, fy)
    page.mouse.move(258, fy); page.wait_for_timeout(800)
    page.mouse.click(258, fy); page.wait_for_timeout(2000)
    gui.tick(page); page.wait_for_timeout(3500)
    r = api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['ps_eid']}")
    for q in r["body"]:
        if q["name"] != "Ball stud":
            continue
        for f in common.faces(page, api, s["did"], s["wid"], s["ps_eid"], q["partId"]):
            if f["surface"]["type"] == "sphere":
                o = f["surface"]["origin"]
                print(q["partId"], [round(v*1000, 4) for v in o])
