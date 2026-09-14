import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
JS = """() => { const out=[];
  for (const e of document.querySelectorAll('li,a,span,div,button')) {
    if (e.children.length) continue;
    const t=(e.innerText||'').trim();
    if (!t || t.length>40) continue;
    const r=e.getBoundingClientRect();
    if (r.width && r.height && r.x>150 && r.x<700 && r.y>600) out.push([t, Math.round(r.x+r.width/2), Math.round(r.y+r.height/2)]);
  } return out; }"""
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(148, 767, button="right")
    page.wait_for_timeout(2000)
    for r in page.evaluate(JS):
        print(r)
    page.screenshot(path=D+"tl16.png")
