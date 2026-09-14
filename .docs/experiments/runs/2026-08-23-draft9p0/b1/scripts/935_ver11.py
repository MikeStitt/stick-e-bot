import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
def tab(page, name):
    hits = page.evaluate("""(nm) => { const out=[];
      for (const e of document.querySelectorAll('span,div,a')) {
        if (e.children.length) continue;
        const r=e.getBoundingClientRect();
        if (r.y>965 && (e.innerText||'').trim()===nm)
          out.push([Math.round(r.x+r.width/2), Math.round(r.y+r.height/2)]);
      } return out; }""", name)
    page.mouse.click(*hits[0]); page.wait_for_timeout(6000)
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    tab(page, "l limb")
    page.keyboard.press("Escape"); page.wait_for_timeout(1500)
    gui.clear(page)
    page.mouse.click(20, 95); page.wait_for_timeout(2500)
    el = page.query_selector("input[type=text]")
    el.click(); page.keyboard.press("Meta+A"); page.keyboard.type("t11 l limb")
    page.wait_for_timeout(400)
    ta = page.query_selector("textarea")
    if ta:
        ta.click()
        page.keyboard.type("Lower limb built in the same frame as the upper: blade derived at base origin so the "
                           "hinge axis is the studio origin, limb hanging down #limbSeg from the blade arm's end "
                           "face, ball stud on the far end. elbow end between the two stub axle faces, wrist end "
                           "on the ball. Segment 102, part 120 long, 40056.825 mm3.")
    page.wait_for_timeout(500)
    gui.frame(page, D + "frames/cad.parts.l_limb.version.png")
    page.mouse.click(912, 322); page.wait_for_timeout(7000)
    s = common.load()
    vs = api.api(page, "GET", f"/api/documents/d/{s['did']}/versions")["body"]
    for v in vs[:3]:
        print(v["name"], v["id"])
