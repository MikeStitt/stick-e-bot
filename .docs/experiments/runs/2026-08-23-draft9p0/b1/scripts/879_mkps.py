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
    page.mouse.click(57, 984); page.wait_for_timeout(2500)
    hit = page.evaluate("""() => { for (const e of document.querySelectorAll('li,a,div,span')) {
        const t = (e.innerText||'').trim();
        if (t !== 'Create Part Studio') continue;
        const r = e.getBoundingClientRect();
        if (r.width && r.height && r.height < 40) return [Math.round(r.x+r.width/2), Math.round(r.y+r.height/2)];
      } return null; }""")
    print("hit", hit)
    page.mouse.move(*hit); page.wait_for_timeout(400)
    page.mouse.click(*hit); page.wait_for_timeout(8000)
    els = api.api(page, "GET", f"/api/documents/d/{s['did']}/w/{s['wid']}/elements")["body"]
    for e in els:
        print(f"  {e['elementType']:12s} {e['id']}  {e['name']}")
