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
    r = api.api(page, "GET", f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['ps_eid']}/features")
    names = [f["message"]["name"] for f in r["body"]["features"]]
    print(names)
    tgt = [f for f in r["body"]["features"] if f["message"]["name"] == "pivot lines"]
    if tgt:
        m = tgt[0]["message"]
        print([pm["message"]["parameterId"] for pm in m["parameters"]])
        js = json.dumps(m, indent=1)
        open("/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/pivot.json", "w").write(js)
        print(len(js))
