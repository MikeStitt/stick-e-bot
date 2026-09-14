import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    r = api.api(page, "GET", f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['ul_eid']}/features")
    for f in r["body"]["features"]:
        m = f["message"]
        if m.get("featureType") != "mateConnector": continue
        d = {}
        for pr in m["parameters"]:
            pm = pr["message"]
            if "queries" in pm:
                d[pm["parameterId"]] = [q["message"].get("geometryIds") for q in pm["queries"]]
            else:
                d[pm.get("parameterId")] = pm.get("value")
        print(f"  {m['name']:22s} {d.get('originType')}/{d.get('entityInferenceType')} q={d.get('originQuery')}")
