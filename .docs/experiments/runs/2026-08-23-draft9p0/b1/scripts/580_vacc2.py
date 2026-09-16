import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.tick(page); page.wait_for_timeout(4000)
    feats = common.features(page, api, s["did"], s["wid"], s["hinge_eid"])
    print(feats[-1])
    r = api.api(page, "GET", f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['hinge_eid']}/features")
    m = r["body"]["features"][-1]["message"]
    for q in m["parameters"]:
        qm = q["message"]
        if qm["parameterId"] in ("depth", "startOffsetDistance", "hasOffset", "startOffsetOppositeDirection", "oppositeDirection"):
            print("   ", qm["parameterId"], "=", repr(qm.get("expression", qm.get("value"))))
    pid = "JHD"
    print("vol", common.volume(page, api, s["did"], s["wid"], s["hinge_eid"], pid))
    for f in common.faces(page, api, s["did"], s["wid"], s["hinge_eid"], pid):
        su = f["surface"]
        if su["type"] == "cylinder" and round(su["radius"]*1000,3) == 1.0:
            print("valley wall", [round(x*1000,3) for x in su["origin"]], [round(x,3) for x in su["axis"]])
        if su["type"] == "plane" and abs(round(su["origin"][1]*1000,3)) not in (5.0, 6.6, 0.0):
            print("plane y", [round(x*1000,3) for x in su["origin"]], round(f["area"]*1e6,3))
