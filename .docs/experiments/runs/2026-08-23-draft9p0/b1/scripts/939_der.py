import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    gui.search_tool(page, "Derive"); page.wait_for_timeout(2500)
    page.mouse.click(368, 148); page.wait_for_timeout(3500)
    hit = common.menu2(page, "ball and socket")
    print("row", hit)
    page.mouse.click(*hit); page.wait_for_timeout(4500)
    page.screenshot(path=D+"gr01.png")
    rows = page.evaluate("""() => { const o=[];
      for (const e of document.querySelectorAll('div,span')) { if (e.children.length) continue;
        const r=e.getBoundingClientRect(); if (r.x>500 && r.width>0)
          o.push([(e.innerText||'').trim(), Math.round(r.x+r.width/2), Math.round(r.y+r.height/2)]); }
      return o.filter(a=>a[0]); }""")
    for r in rows: print(r)
