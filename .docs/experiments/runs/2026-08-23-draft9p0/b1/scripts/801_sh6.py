import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_screen as screen
import onshape_session as api
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(447, 172); page.wait_for_timeout(1200)   # drop Vertex of Origin
    o = (923, 523)
    spot = (o[0] + 66, o[1])          # 3 mm off axis at 22 px/mm
    page.mouse.move(*spot); page.wait_for_timeout(900)
    page.mouse.click(*spot); page.wait_for_timeout(1800)
    labs = [r for r in gui.labels(page) if r[1] < 500]
    for r in labs: print(r)
    gui.name_feature(page, "shoulder end"); page.wait_for_timeout(700)
    gui.tick(page); page.wait_for_timeout(3500)
    r = api.api(page, "GET", f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['ul_eid']}/features")
    for f in r["body"]["features"]:
        m = f["message"]
        if m.get("name") != "shoulder end": continue
        for pr in m["parameters"]:
            pm = pr["message"]
            if pm.get("parameterId") in ("originType","entityInferenceType","requireOwnerPart"):
                print("   ", pm["parameterId"], pm.get("value"))
