import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api

s = common.load()
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.name_feature(page, "collar blank")
    gui.tick(page); page.wait_for_timeout(2500)
    print("tree:", gui.tree(page))
    r = api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['bs_eid']}")
    for x in r["body"]:
        pid = x["partId"]
        b = api.api(page, "GET",
            f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['bs_eid']}/partid/{pid}/bodydetails")["body"]
        body = common._one(b["bodies"])
        lo = [round(c*1000, 3) for c in body["box"]["minCorner"]] if "box" in body else None
        print(pid, x["name"], "faces", len(body["faces"]), "box", lo)
