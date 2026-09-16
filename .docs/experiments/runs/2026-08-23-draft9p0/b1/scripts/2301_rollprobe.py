"""#58 — what the feature row's context menu offers. Nothing is clicked in it."""
import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui
from playwright.sync_api import sync_playwright
s = common.load(); did, wid = s["did"], s["wid"]
JS = """() => { const out = [];
  for (const e of document.querySelectorAll('li,a,div,span')) {
    if (e.children.length) continue;
    const t = (e.innerText||'').trim();
    if (!t || t.length > 40) continue;
    const r = e.getBoundingClientRect();
    if (!r.width || !r.height || r.height > 40) continue;
    if (r.x < 200) continue;
    out.push([t, Math.round(r.x), Math.round(r.y)]);
  } return out; }"""
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up()
    page.set_default_navigation_timeout(180000)
    page.goto(f"https://cad.onshape.com/documents/{did}/w/{wid}/e/{s['head_eid']}",
              wait_until="domcontentloaded")
    page.wait_for_timeout(15000)
    x, y = gui.row(page, "get socket")
    print("row at", x, y)
    page.mouse.click(x, y, button="right")
    page.wait_for_timeout(2000)
    for row in page.evaluate(JS):
        print("   ", row)
    page.keyboard.press("Escape")
    page.wait_for_timeout(800)
