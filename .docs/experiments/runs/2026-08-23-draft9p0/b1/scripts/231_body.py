import sys, json
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    r = api.api(page, "GET", f"/api/variables/d/{s['did']}/w/{s['wid']}/e/{s['vs_eid']}/variables")
    for tbl in r["body"]:
        for v in tbl["variables"]:
            print("%-14s %-10s %s" % (v["name"], v["type"], v["expression"]))
    print("--- body features ---")
    r = api.api(page, "GET", f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['ps_eid']}/features")
    for f in r["body"]["features"]:
        print(f["message"]["featureType"], "|", f["message"]["name"])
    print("--- body bbox ---", common.bbox(page, api, s['did'], s['wid'], s['ps_eid']))
