import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    gui.pick(page, (1050, 514), "top edge")
    for spot, what in [((1050, 531), "bottom"), ((1063, 518), "right"), ((982, 518), "left")]:
        gui.pick(page, spot, what, add=True)
    gui.search_tool(page, "Circular pattern", settle=2500)
    page.mouse.dblclick(1003, 535)
    page.wait_for_timeout(1200)
    page.keyboard.press("Meta+a")
    page.keyboard.type("4")
    page.keyboard.press("Enter")
    page.wait_for_timeout(1500)
    print("cursor", gui.cursor(page))
    # what confirm-ish controls exist anywhere on screen?
    got = page.evaluate("""() => {
      const out = [];
      for (const e of document.querySelectorAll('button,[role=button],.os-button,svg use')) {
        const r = e.getBoundingClientRect();
        if (!r.width || !r.height) continue;
        const t = (e.getAttribute('title') || e.getAttribute('aria-label') || e.innerText || '').trim();
        if (!t) continue;
        if (/ok|accept|check|confirm|done|apply/i.test(t))
          out.push([t, Math.round(r.x + r.width/2), Math.round(r.y + r.height/2)]);
      }
      return out; }""")
    print(got)
    page.screenshot(path=D + "bs36.png")
