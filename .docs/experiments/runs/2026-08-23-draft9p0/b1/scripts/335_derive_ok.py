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
    gui.tick(page)
    page.wait_for_timeout(4000)
    gui.rename_row(page, "Derived 1", "copy ball stud")
    page.wait_for_timeout(2000)
    print(gui.tree(page)[-6:])
    r = api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['ps_eid']}")
    for pt in r["body"]:
        print(pt["partId"], pt["name"])
    for pt in r["body"]:
        if pt["name"] == "Ball stud":
            fs = common.faces(page, api, s["did"], s["wid"], s["ps_eid"], pt["partId"])
            for f in fs:
                b = f["box"]
                print(f["surface"]["type"], round(f["area"]*1e6, 3),
                      [round(v*1000, 3) for v in b["minCorner"]],
                      [round(v*1000, 3) for v in b["maxCorner"]])
