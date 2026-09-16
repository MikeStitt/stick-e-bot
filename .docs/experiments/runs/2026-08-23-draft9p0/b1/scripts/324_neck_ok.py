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
    gui.tick(page)
    page.wait_for_timeout(3000)
    t = gui.tree(page)
    print(t[-4:])
    name = [n for n in t if n.startswith("Sketch")][-1]
    gui.rename_row(page, name, "neck connector location")
    page.wait_for_timeout(2000)
    r = api.api(page, "GET", f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['ps_eid']}/features")
    for f in r["body"]["features"]:
        m = f["message"]
        if m["name"] in ("neck connector location", "hip connector location"):
            print("==", m["name"])
            for e in m["entities"]:
                em = e["message"]
                print("  ", e["typeName"], em.get("entityId"), json.dumps(em.get("geometry", {}).get("message", {})))
