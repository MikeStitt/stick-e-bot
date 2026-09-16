import sys, json
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
RDID, RWID, RUL = "111f975041ddb104a6028d45", "38e73619152eec8be2c51f8b", "8c795601f43ec512c99354f3"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    r = api.api(page, "GET", f"/api/partstudios/d/{RDID}/w/{RWID}/e/{RUL}/features")
    for f in r["body"]["features"]:
        m = f["message"]
        if m.get("featureType") != "mateConnector": continue
        print("==", m["name"])
        for pr in m["parameters"]:
            pm = pr["message"]
            if "queries" in pm:
                print("   ", pm["parameterId"], [q["message"].get("geometryIds") for q in pm["queries"]])
            elif pm.get("value") not in (None, False, ""):
                print("   ", pm.get("parameterId"), "=", pm.get("value"))
