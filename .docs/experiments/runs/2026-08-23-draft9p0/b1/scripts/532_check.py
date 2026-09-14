import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    s = common.load()
    r = api.api(page, "GET", f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['hinge_eid']}/features")
    st = {row["key"]: row["value"]["message"]["featureStatus"] for row in r["body"]["featureStates"]}
    for f in r["body"]["features"]:
        m = f["message"]
        d = {}
        for prm in m["parameters"]:
            pm = prm["message"]
            d[pm["parameterId"]] = pm.get("expression", pm.get("value"))
        print(f"{st.get(m['featureId']):6} {d.get('name')} = {d.get('value')}")
