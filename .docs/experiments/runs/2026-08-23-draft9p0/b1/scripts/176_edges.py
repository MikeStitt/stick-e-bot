import sys, json, collections
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load(); did, wid, eid = s["did"], s["wid"], s["bs_eid"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    r = api.api(page, "GET", f"/api/parts/d/{did}/w/{wid}/e/{eid}/partid/JKD/bodydetails")
    body = common._one(r["body"]["bodies"])
    print("body keys", list(body.keys()))
    f0 = body["faces"][0]
    print("face keys", list(f0.keys()))
    print(json.dumps(f0, indent=1)[:900])
