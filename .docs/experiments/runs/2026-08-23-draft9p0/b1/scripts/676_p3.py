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
    parts = api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['hinge_eid']}")["body"]
    pid = [q["partId"] for q in parts if q["name"] == "Part 3"][0]
    r = api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['hinge_eid']}/partid/{pid}/massproperties")
    b = common._one(r["body"]["bodies"])
    print("centroid mm", [round(v*1000,4) for v in b["centroid"][:3]])
    for f in common.faces(page, api, s["did"], s["wid"], s["hinge_eid"], pid):
        print(f["surface"]["type"], round(f["area"]*1e6,4), f["surface"].get("origin"), f["surface"].get("normal"))
