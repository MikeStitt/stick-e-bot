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
    for r in gui.labels(page):
        print(r)
    gui.tick(page); page.wait_for_timeout(3500)
    t = gui.tree(page)
    print(t[-6:])
    gui.rename_row(page, "Transform 1", "copy for hip")
    page.wait_for_timeout(2000)
    r = api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['ps_eid']}")
    for q in r["body"]:
        print(q["partId"], q["name"])
        if "stud" in q["name"].lower():
            for f in common.faces(page, api, s["did"], s["wid"], s["ps_eid"], q["partId"]):
                b = f["box"]
                print("  ", f["surface"]["type"],
                      [round(v*1000, 3) for v in b["minCorner"]],
                      [round(v*1000, 3) for v in b["maxCorner"]])
