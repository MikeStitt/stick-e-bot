import sys, json
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_session as osx
from playwright.sync_api import sync_playwright
s = common.load(); did, wid = s["did"], s["wid"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    r = osx.api(page, "GET",
        f"/api/partstudios/d/{did}/w/{wid}/e/{s['hinge_eid']}/features")
    b = r["body"]
    for f in b["features"]:
        m = f["message"]
        if m["name"] in ("axis for circular patterns", "24 valleys"):
            print("###", m["name"], "|", m["featureType"])
            print(json.dumps(m.get("parameters"), indent=1)[:3000])
