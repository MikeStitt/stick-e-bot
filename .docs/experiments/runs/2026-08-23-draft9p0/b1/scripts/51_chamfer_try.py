import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api

s = common.load()


def states(page):
    r = api.api(page, "GET",
                f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['head_eid']}/features")
    names = [f["message"]["name"] for f in r["body"]["features"]]
    st = r["body"].get("featureStates")
    out = {}
    if isinstance(st, list):
        for f, v in zip(r["body"]["features"], st):
            out[f["message"]["name"]] = v.get("message", {}).get("featureStatus")
    else:
        byid = {f["message"]["featureId"]: f["message"]["name"] for f in r["body"]["features"]}
        for k, v in (st or {}).items():
            out[byid.get(k, k)] = v.get("message", {}).get("featureStatus", v)
    return names, out


with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    if page.locator("#feature-dialog").count():
        page.mouse.click(451, 93); page.wait_for_timeout(1800)
    gui.clear(page)
    gui.search_tool(page, "Chamfer")
    gui.pick(page, (923, 560), "the underside")
    print("field:", [l[0] for l in gui.labels(page) if " of " in l[0]])
    x, y = gui.at(page, "Tangent propagation")
    page.mouse.click(x, y); page.wait_for_timeout(1200)
    el = gui.number_fields(page)[0]
    gui.set_field(page, el, "6 mm")
    page.wait_for_timeout(2500)
    gui.name_feature(page, "lower head chamfer")
    gui.tick(page)
    page.wait_for_timeout(2000)
    print(states(page))
