import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
JS = """(t) => { const out=[];
  for (const e of document.querySelectorAll('span,div,a')) {
    if (e.children.length) continue;
    if ((e.innerText||'').trim() !== t) continue;
    const r = e.getBoundingClientRect();
    if (r.width && r.height && r.x < 250) out.push([Math.round(r.x+r.width/2), Math.round(r.y+r.height/2)]);
  } return out; }"""
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(343, 231); page.wait_for_timeout(900)
    page.mouse.move(150, 400)
    for _ in range(30):
        page.mouse.wheel(0, -120); page.wait_for_timeout(40)
    page.wait_for_timeout(900)
    hit = page.evaluate(JS, "Right")
    print("Right", hit)
    page.mouse.click(*hit[0]); page.wait_for_timeout(2000)
    page.mouse.click(313, 149); page.wait_for_timeout(1500)   # make sure Add
    gui.tick(page); page.wait_for_timeout(3500)
    s = common.load()
    parts = api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['foot_eid']}")["body"]
    for pt in parts:
        print(pt["name"], common.volume(page, api, s["did"], s["wid"], s["foot_eid"], pt["partId"]))
    print([r for r in gui.tree(page)][-4:])
