import sys, collections
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api, onshape_screen as screen

s = common.load()


def faces(page):
    r = api.api(page, "GET",
                f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['head_eid']}/partid/JHD/bodydetails")
    if not r["ok"]:
        return r["status"]
    b = r["body"]["bodies"][0]
    return len(b["faces"]), dict(collections.Counter(f["surface"]["type"] for f in b["faces"]))


with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    # delete the failed chamfer
    x, y = gui.row(page, "lower head chamfer")
    page.mouse.click(x, y, button="right"); page.wait_for_timeout(1200)
    hit = page.evaluate(
        """() => { for (const e of document.querySelectorAll('li,a,span,div')) {
             if (e.children.length) continue;
             if ((e.innerText || '').trim() !== 'Delete') continue;
             const r = e.getBoundingClientRect();
             if (r.width && r.height) return [Math.round(r.x+r.width/2), Math.round(r.y+r.height/2)];
           } return null; }""")
    print("Delete at", hit)
    page.mouse.click(*hit); page.wait_for_timeout(2500)
    print("tree:", gui.tree(page))
    # straight-from-below
    page.mouse.move(*screen.CENTER)
    for _ in range(2):
        page.keyboard.press("ArrowDown"); page.wait_for_timeout(400)
    page.wait_for_timeout(1200)
    gui.clear(page)
    gui.search_tool(page, "Chamfer")
    gui.pick(page, (923, 520), "the underside")
    print("field:", [l[0] for l in gui.labels(page) if " of " in l[0]])
    tx, ty = gui.at(page, "Tangent propagation")
    page.mouse.click(tx, ty); page.wait_for_timeout(1500)
    el = gui.number_fields(page)[0]
    gui.set_field(page, el, "6 mm")
    page.wait_for_timeout(3000)
    page.screenshot(path="hd24.png", clip={"x": 0, "y": 76, "width": 1000, "height": 400})
