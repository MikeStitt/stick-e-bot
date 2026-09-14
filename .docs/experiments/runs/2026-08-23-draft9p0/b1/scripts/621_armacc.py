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
    gui.tick(page); page.wait_for_timeout(5000)
    common.scroll_tree(page, -25)
    gui.rename_row(page, "Extrude 1", "blade arm")
    page.wait_for_timeout(2000)
    print(common.features(page, api, s["did"], s["wid"], s["hinge_eid"])[-1])
    print(common.bbox(page, api, s["did"], s["wid"], s["hinge_eid"]))
    print("vol", common.volume(page, api, s["did"], s["wid"], s["hinge_eid"], "JHD"))
    r = api.api(page, "GET", f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['hinge_eid']}/features")
    m = r["body"]["features"][-1]["message"]
    for q in m["parameters"]:
        qm = q["message"]
        if qm["parameterId"] in ("depth", "startOffsetDistance", "oppositeDirection", "startOffsetOppositeDirection"):
            print("   ", qm["parameterId"], "=", repr(qm.get("expression", qm.get("value"))))
