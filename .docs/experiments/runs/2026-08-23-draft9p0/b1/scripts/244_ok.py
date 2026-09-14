import sys, json
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.tick(page); page.wait_for_timeout(3000)
    x, y = gui.row(page, "Sketch 1")
    page.mouse.click(x, y, button="right"); page.wait_for_timeout(1400)
    page.mouse.click(*common.menu_item(page, "Rename")); page.wait_for_timeout(1000)
    page.keyboard.press("Meta+a"); page.keyboard.type("pivot lines")
    page.keyboard.press("Enter"); page.wait_for_timeout(2500)
    r = api.api(page, "GET", f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['ps_eid']}/features")
    for f in r["body"]["features"]:
        m = f["message"]
        if m["name"] != "pivot lines":
            continue
        for pm in m["parameters"]:
            if pm["message"]["parameterId"] == "sketchEntities":
                for e in pm["message"]["value"]:
                    em = e["message"]
                    print("ENT", em["entityId"], em.get("isConstruction"),
                          [ (q["message"]["parameterId"], q["message"].get("expression") or q["message"].get("value")) for q in em["parameters"] ])
            if pm["message"]["parameterId"] == "constraints":
                for c in pm["message"]["value"]:
                    cm = c["message"]
                    print("CON", cm["constraintType"], cm.get("parameters") and
                          [ (q["message"]["parameterId"], q["message"].get("expression", q["message"].get("queryString",""))) for q in cm["parameters"] ])
