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
    r = api.api(page, "GET", f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['ll_eid']}/features")["body"]
    st = {x["featureId"]: x["featureStatus"] for x in r["featureStates"]}
    for f in r["features"]:
        fid = f["message"]["featureId"]
        print(f"{st.get(fid,'?'):8s} {f['message']['name']}")
        for pm in f["message"].get("parameters", []):
            m = pm["message"]
            if m.get("parameterId") in ("depth",) and "expression" in m:
                print("        depth expression:", m["expression"])
