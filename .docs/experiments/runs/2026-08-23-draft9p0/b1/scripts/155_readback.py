import sys, json
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api

s = common.load()
did, wid, eid = s["did"], s["wid"], s["bs_eid"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    r = api.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/features")
    feats = r["body"]["features"]
    for f in feats:
        m = f["message"]
        print(f"{m.get('name'):22s} {m.get('featureType')}")
    sk = [f["message"] for f in feats if f["message"].get("name") == "slit profile"][0]
    for c in sk.get("constraints", []):
        cm = c["message"]
        if cm.get("constraintType") != "CIRCULAR_PATTERN":
            continue
        print("CIRCULAR_PATTERN parameters:")
        for pr in cm["parameters"]:
            pm = pr["message"]
            print("   ", pm.get("parameterId"), "=", pm.get("value", pm.get("expression", pm.get("queryString", ""))))
