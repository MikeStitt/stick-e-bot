import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
JS = """() => { const out=[];
  for (const e of document.querySelectorAll('span,div,a')) {
    if (e.children.length) continue;
    const t=(e.innerText||'').trim();
    if (!t.startsWith('#')) continue;
    const r=e.getBoundingClientRect();
    if (r.width && r.height && r.x < 250) out.push(t);
  } return out; }"""
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    common.scroll_tree(page, -25)
    print(page.evaluate(JS))
