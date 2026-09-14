import sys, json, re
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_session as osx
from playwright.sync_api import sync_playwright
s = common.load(); did, wid = s["did"], s["wid"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    b = osx.api(page, "GET",
        f"/api/partstudios/d/{did}/w/{wid}/e/{s['hinge_eid']}/features")["body"]
    byid = {f["message"]["featureId"]: f["message"]["name"] for f in b["features"]}
    for f in b["features"]:
        m = f["message"]
        if m["featureType"] != "circularPattern": continue
        for par in m["parameters"]:
            if par["message"].get("parameterId") == "axis":
                blob = json.dumps(par)
                ids = set(re.findall(r'"featureId":\s*"([^"]+)"', blob))
                ids |= set(re.findall(r'"deterministicIds":\s*\["([^"]+)"', blob))
                print(m["name"], "-> axis refs:",
                      [byid.get(i, i) for i in ids] or blob[:400])
