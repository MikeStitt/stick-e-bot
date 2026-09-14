import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
s = common.load(); did, wid, eid = s["did"], s["wid"], s["bs_eid"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.name_feature(page, "relief slits")
    gui.tick(page)
    page.wait_for_timeout(3000)
    print(gui.tree(page))
    r = api.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/features")
    for f in r["body"]["features"]:
        m = f["message"]
        if m.get("name") != "relief slits":
            continue
        for pr in m["parameters"]:
            pm = pr["message"]
            v = pm.get("expression", pm.get("value"))
            print("  ", pm.get("parameterId"), "=", v)
    st = api.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/features/featurespecs")
    page.screenshot(path=D + "bs52.png")
