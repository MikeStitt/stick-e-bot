import sys, json
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
    r = api.api(page, "GET", f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['hinge_eid']}/features")
    f = r["body"]["features"][-1]["message"]
    print(f["name"])
    for pm in f["parameters"]:
        m = pm["message"]
        v = m.get("expression", m.get("value", m.get("queries", "")))
        print(" ", m.get("parameterId"), "=", v if not isinstance(v, list) else "<queries>")
    st = {row["key"]: row["value"]["message"] for row in r["body"]["featureStates"]}
    print(json.dumps(st.get(f["featureId"]), indent=1)[:800])
