import sys, json
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_screen as screen
from playwright.sync_api import sync_playwright
s = common.load(); did, wid = s["did"], s["wid"]
DUMP = """() => { const out = [];
  for (const e of document.querySelectorAll('div,span')) {
    const r = e.getBoundingClientRect();
    if (r.y < window.innerHeight - 120) continue;
    const t = (e.innerText||'').trim();
    if (t && t.length < 120) out.push([Math.round(r.x), Math.round(r.y), t]);
  } return out.slice(0, 40); }"""
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up(); page.keyboard.press("Escape"); page.wait_for_timeout(600)
    page.set_default_navigation_timeout(180000)
    page.goto(f"https://cad.onshape.com/documents/{did}/w/{wid}/e/{s['ul_eid']}",
              wait_until="domcontentloaded")
    page.wait_for_timeout(22000)
    screen.hook(page); gui.wake(page); gui.clear(page)
    page.keyboard.press("Shift+7"); page.wait_for_timeout(1200)
    page.keyboard.press("f"); page.wait_for_timeout(2500)
    print("BEFORE:", json.dumps(page.evaluate(DUMP)))
    page.mouse.click(*gui.row(page, "mate for fork")); page.wait_for_timeout(3000)
    print("AFTER :", json.dumps(page.evaluate(DUMP)))
