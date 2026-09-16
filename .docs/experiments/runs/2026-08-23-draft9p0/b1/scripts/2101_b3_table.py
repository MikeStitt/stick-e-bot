"""B3 — how the variable table reads back through the DOM."""
import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui
from playwright.sync_api import sync_playwright
JS = """() => document.querySelectorAll('input,textarea').length ? [...document.querySelectorAll('input,textarea')]
  .map(e => { const r = e.getBoundingClientRect();
    return [Math.round(r.x), Math.round(r.y), Math.round(r.width), e.value, e.className.slice(0,40)]; })
  .filter(a => a[2] > 20) : []"""
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up()
    for row in page.evaluate(JS):
        print(row)
