import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load(); did, wid, eid = s["did"], s["wid"], s["foot_eid"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(451, 93); page.wait_for_timeout(1500)
    r = api.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/features")
    st = {row["key"]: row["value"]["message"]["featureStatus"] for row in r["body"]["featureStates"]}
    for f in r["body"]["features"]:
        m = f["message"]
        d = {}
        for prm in m["parameters"]:
            pm = prm["message"]
            if pm.get("parameterId") in ("name", "value", "variableType"):
                d[pm["parameterId"]] = pm.get("value", pm.get("expression"))
        print(st.get(m["featureId"]), m["name"], d)
