import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load(); did, wid, eid = s["did"], s["wid"], s["ps_eid"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for n, f, st in common.features(page, api, did, wid, eid):
        print(f"{st:12s} {n}")
    r = api.api(page, "GET", f"/api/parts/d/{did}/w/{wid}/e/{eid}")
    for part in r["body"]:
        print(part["partId"], part["name"])
