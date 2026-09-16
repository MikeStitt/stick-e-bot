import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    hits = page.evaluate("""() => { const out=[];
      for (const e of document.querySelectorAll('span,div,a')) {
        if (e.children.length) continue;
        const r=e.getBoundingClientRect();
        if (r.y>965 && (e.innerText||'').trim()==='Part Studio 1')
          out.push([Math.round(r.x+r.width/2), Math.round(r.y+r.height/2)]);
      } return out; }""")
    print("tab at", hits)
    x, y = hits[0]
    page.mouse.click(x, y, button="right"); page.wait_for_timeout(2000)
    hit = page.evaluate("""() => { for (const e of document.querySelectorAll('li,a,div,span')) {
        if ((e.innerText||'').trim() !== 'Rename') continue;
        const r=e.getBoundingClientRect();
        if (r.width && r.height && r.height<40) return [Math.round(r.x+r.width/2), Math.round(r.y+r.height/2)];
      } return null; }""")
    print("rename at", hit)
    page.mouse.click(*hit); page.wait_for_timeout(1800)
    page.keyboard.press("Meta+A")
    page.keyboard.type("l limb")
    page.keyboard.press("Enter")
    page.wait_for_timeout(4000)
    els = api.api(page, "GET", f"/api/documents/d/{s['did']}/w/{s['wid']}/elements")["body"]
    for e in els:
        print(f"  {e['elementType']:12s} {e['id']}  {e['name']}")
