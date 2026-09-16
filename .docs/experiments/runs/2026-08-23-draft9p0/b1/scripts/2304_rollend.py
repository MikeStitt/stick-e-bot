"""#58 — put the rollback bar back at the end of `head`."""
import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui
from playwright.sync_api import sync_playwright
s = common.load(); did, wid, eid = s["did"], s["wid"], s["head_eid"]
BAR = """() => [...document.querySelectorAll('*')].filter(e => {
  const c = e.className ? e.className.toString() : '';
  return /rollback|roll-bar|rollBar/i.test(c); })
  .map(e => { const r = e.getBoundingClientRect();
    return [e.tagName, e.className.toString().slice(0,50),
            Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)]; })"""
MENU = """() => [...document.querySelectorAll('li,a,div,span')]
  .filter(e => !e.children.length)
  .map(e => { const r = e.getBoundingClientRect();
    return [(e.innerText||'').trim(), Math.round(r.x + r.width/2), Math.round(r.y + r.height/2),
            Math.round(r.height)]; })
  .filter(a => a[0] && a[0].length < 40 && a[3] > 0 && a[3] < 40 && a[1] > 190 && a[1] < 500)"""
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up()
    page.keyboard.press("Escape"); page.wait_for_timeout(800)
    print("tree:", gui.tree(page)[-5:])
    for b in page.evaluate(BAR):
        print("  bar:", b)
    page.mouse.click(140, 651, button="right")
    page.wait_for_timeout(1800)
    for m in page.evaluate(MENU):
        print("  menu:", m)
