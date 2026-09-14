import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common, json
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.tick(page); page.wait_for_timeout(3000)
    gui.rename_row(page, "Mate connector 1", "mate to robot"); page.wait_for_timeout(1500)
    s = common.load()
    r = api.api(page, "GET", f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['foot_eid']}/features")
    for f in r["body"]["features"]:
        m = f["message"]
        if m["name"] == "mate to robot":
            for prm in m["parameters"]:
                pm = prm["message"]
                if pm["parameterId"] in ("ownerPart", "originQuery"):
                    print(pm["parameterId"], json.dumps(pm.get("queries", pm.get("value")))[:200])
    for name, fid, st in common.features(page, api, s["did"], s["wid"], s["foot_eid"]):
        if st != "OK":
            print("NOT OK:", st, name)
    print([r for r in gui.tree(page)][-4:])
