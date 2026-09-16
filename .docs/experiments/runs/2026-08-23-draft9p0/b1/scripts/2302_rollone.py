"""#58 — roll back one feature in `head`, find the control that rolls forward, restore.

Deliberately the smallest possible exposure: the last feature only, and the script
does not exit until the tree says the bar is gone.
"""
import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui
from playwright.sync_api import sync_playwright
s = common.load(); did, wid = s["did"], s["wid"]
MENU = """(t) => { for (const e of document.querySelectorAll('li,a,div,span')) {
    if (e.children.length) continue;
    if ((e.innerText||'').trim() !== t) continue;
    const r = e.getBoundingClientRect();
    if (r.width && r.height && r.height < 40 && r.x > 190)
      return [Math.round(r.x + r.width/2), Math.round(r.y + r.height/2)];
  } return null; }"""
BUTTONS = """() => [...document.querySelectorAll('button,[role=button],i,svg')]
  .map(e => { const r = e.getBoundingClientRect();
    return [Math.round(r.x), Math.round(r.y), Math.round(r.width),
            (e.getAttribute('title')||e.getAttribute('aria-label')||
             e.className.toString()).slice(0,44)]; })
  .filter(a => a[0] < 250 && a[1] > 140 && a[1] < 940 && a[2] > 8)"""
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up()
    page.keyboard.press("Escape")
    page.wait_for_timeout(800)
    page.set_default_navigation_timeout(180000)
    if "/e/" + s["head_eid"] not in page.url:
        page.goto(f"https://cad.onshape.com/documents/{did}/w/{wid}/e/{s['head_eid']}",
                  wait_until="domcontentloaded")
        page.wait_for_timeout(15000)
    print("tree before:", gui.tree(page)[-4:])
    x, y = gui.row(page, "head mate")
    page.mouse.click(x, y, button="right")
    page.wait_for_timeout(1800)
    hit = page.evaluate(MENU, "Roll to here")
    print("menu hit:", hit)
    page.mouse.click(*hit)
    page.wait_for_timeout(6000)
    print("tree after roll:", gui.tree(page)[-6:])
    page.screenshot(path=D + "rolled.png")
    for b in page.evaluate(BUTTONS):
        print("   ", b)
