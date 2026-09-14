import sys, json
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load(); did, wid = s["did"], s["wid"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    r = api.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{s['bs_eid']}/features")
    for f in r["body"]["features"][:12]:
        m = f["message"]
        if m["featureType"] != "variable": continue
        out = {}
        for prm in m["parameters"]:
            pm = prm["message"]
            out[pm.get("parameterId")] = pm.get("value", pm.get("expression"))
        print(json.dumps(out))
