import sys, json
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load(); did, wid, eid = s["did"], s["wid"], s["ps_eid"]
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
name = sys.argv[1]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    page.mouse.move(140, 400)
    for _ in range(12):
        page.mouse.wheel(0, 300); page.wait_for_timeout(100)
    page.wait_for_timeout(1200)
    vis = gui.tree(page)
    if name not in vis:
        raise SystemExit(f"{name} not visible: {vis}")
    px, py = gui.row(page, "torso")
    print("torso row", px, py)
    x, y = gui.row(page, name)
    page.mouse.dblclick(x, y)
    page.wait_for_timeout(2500)
    rows = gui.labels(page)
    sel = [r for r in rows if r[0] == "Select owner entity"]
    if not sel:
        oy = [r[2] for r in rows if r[0] == "Owner entity"][0]
        page.mouse.click(256, oy); page.wait_for_timeout(1500)
        rows = gui.labels(page)
        sel = [r for r in rows if r[0] == "Select owner entity"]
    page.mouse.click(sel[0][1], sel[0][2]); page.wait_for_timeout(800)
    page.mouse.click(px, py); page.wait_for_timeout(1800)
    for r in gui.labels(page):
        print("  ->", r)
    gui.tick(page); page.wait_for_timeout(2500)
    r = api.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/features")
    for f in r["body"]["features"]:
        m = f["message"]
        if m["name"] != name: continue
        for prm in m["parameters"]:
            pm = prm["message"]
            if pm.get("parameterId") == "ownerPart":
                print("ownerPart", json.dumps(pm.get("queries", pm.get("value")))[:300])
