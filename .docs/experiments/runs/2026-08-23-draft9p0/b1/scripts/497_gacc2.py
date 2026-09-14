import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.tick(page); page.wait_for_timeout(3500)
    gui.rename_row(page, "Extrude 1", "sole groove"); page.wait_for_timeout(1200)
    s = common.load()
    r = api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['foot_eid']}")
    pid = r["body"][0]["partId"]
    print("part", pid, "vol", common.volume(page, api, s["did"], s["wid"], s["foot_eid"], pid))
    fs = common.faces(page, api, s["did"], s["wid"], s["foot_eid"], pid)
    lev = {}
    for f in fs:
        su = f.get("surface", {})
        if su.get("type") == "plane":
            n = su.get("normal") or []
            if n and abs(n[2]) > 0.99:
                z = round(su["origin"][2] * 1000, 3)
                lev[z] = lev.get(z, 0) + 1
    print("planar z levels (normal +-Z):", dict(sorted(lev.items())))
    print(common.bbox(page, api, s["did"], s["wid"], s["foot_eid"]))
