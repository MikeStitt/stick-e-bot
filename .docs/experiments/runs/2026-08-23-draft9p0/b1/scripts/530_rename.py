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
    if (r.width && r.height && r.y > 960) out.push([Math.round(r.x+r.width/2), Math.round(r.y+r.height/2)]);
  } return out; }"""
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    hit = page.evaluate(JS, "Part Studio 1")
    print("tab", hit)
    page.mouse.click(*hit[0], button="right"); page.wait_for_timeout(1500)
    page.screenshot(path=D+"tl03.png")
    r = common.menu_item(page, "Rename")
    print("rename at", r)
    if r:
        page.mouse.click(*r); page.wait_for_timeout(1500)
        page.keyboard.press("Meta+A"); page.keyboard.type("hinge")
        page.keyboard.press("Enter"); page.wait_for_timeout(2500)
    s = common.load()
    els = api.api(page, "GET", f"/api/documents/d/{s['did']}/w/{s['wid']}/elements")["body"]
    print([e["name"] for e in els])
