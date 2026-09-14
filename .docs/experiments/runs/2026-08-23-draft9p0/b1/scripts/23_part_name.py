import sys, json
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api

s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.rename_row(page, "Part 1", "torso")
    print("tree:", gui.tree(page))
    base = f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['ps_eid']}"
    r = api.api(page, "GET", base + "/boundingboxes")
    print("bbox:", json.dumps(r["body"], indent=1))
    r = api.api(page, "GET", base + "/features")
    for f in r["body"]["features"]:
        print(" feature:", f["message"]["name"])
    print(" states:", {k: v["featureStatus"] for k, v in
                       (r["body"].get("featureStates") or {}).items()})
