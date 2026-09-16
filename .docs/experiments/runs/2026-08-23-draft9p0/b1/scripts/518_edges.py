import sys, json
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    s = common.load()
    r = api.api(page, "GET",
        f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['foot_eid']}/partid/JHD/bodydetails")
    body = common._one(r["body"]["bodies"])
    e0 = body["edges"][0]
    print(json.dumps(e0, indent=1)[:600])
    seen = {}
    for e in body["edges"]:
        c = e.get("curve", {})
        if c.get("type") in ("circle", "arc"):
            rad = round(c.get("radius", 0) * 1000, 4)
            org = tuple(round(v * 1000, 3) for v in (c.get("origin") or [0, 0, 0]))
            seen.setdefault((rad, org), 0)
            seen[(rad, org)] += 1
    for k in sorted(seen):
        print(k, seen[k])
