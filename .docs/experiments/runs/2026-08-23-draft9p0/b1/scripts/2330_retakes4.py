"""#59 — pick the row where it actually is on screen, then shoot."""
import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_session as osx, onshape_screen as screen
from playwright.sync_api import sync_playwright
OUT = "/Users/mikestitt/projects/first/2027/sponge/instructions/stickbot-draft9p0/source/images/"
s = common.load(); did, wid = s["did"], s["wid"]

MENU = """(t) => { let best = null, area = 1e9;
  for (const e of document.querySelectorAll('li,a,div,span,button')) {
    if ((e.innerText||'').trim() !== t) continue;
    const r = e.getBoundingClientRect();
    if (!r.width || !r.height || r.height > 46) continue;
    if (r.width * r.height < area) { area = r.width * r.height;
      best = [Math.round(r.x + r.width/2), Math.round(r.y + r.height/2)]; }
  } return best; }"""
ROW = """(t) => { for (const e of document.querySelectorAll('div,span')) {
    if ((e.innerText||'').trim() !== t) continue;
    const r = e.getBoundingClientRect();
    if (r.width && r.height && r.height < 40 && r.x < 250)
      return [Math.round(r.x + r.width/2), Math.round(r.y + r.height/2)];
  } return null; }"""
BARY = """() => { const e = document.querySelector('.ns-list-item-rollbackbar');
  if (!e) return null; const r = e.getBoundingClientRect();
  return [Math.round(r.x + r.width/2), Math.round(r.y + r.height/2)]; }"""

def faces(page, eid):
    b = osx.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/bodydetails")["body"]
    return sum(len(body["faces"]) for body in b["bodies"])

def wheel(page, n):
    page.mouse.move(140, 400)
    for _ in range(abs(n)):
        page.mouse.wheel(0, 300 if n > 0 else -300); page.wait_for_timeout(300)
    page.wait_for_timeout(1000)

def find(page, name):
    """The row's pixel, scrolled into the tree's middle band first."""
    for _ in range(20):
        hit = page.evaluate(ROW, name)
        if hit and 170 < hit[1] < 620:
            return hit
        wheel(page, 1 if (hit is None or hit[1] >= 620) else -1)
    raise AssertionError(f"cannot bring {name!r} into view")

def shot(page, pt, med, close, target, radius):
    page.mouse.move(*gui.EMPTY); page.wait_for_timeout(1500)
    if med:
        gui.frame(page, OUT + med); print("  wrote", med)
    at = gui.project(page, *pt, cam=screen.camera(page))
    gui.zoom_to(page, target, at_px=at); page.wait_for_timeout(1500)
    at2 = gui.project(page, *pt, cam=screen.camera(page))
    print("  ring at", [round(v) for v in at2])
    page.mouse.move(*gui.EMPTY); page.wait_for_timeout(1200)
    gui.ring(page, OUT + close, at2, radius=radius); print("  wrote", close)

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up(); page.keyboard.press("Escape"); page.wait_for_timeout(800)
    page.set_default_navigation_timeout(180000); page.set_default_timeout(60000)

    print("=== ball and socket")
    page.goto(f"https://cad.onshape.com/documents/{did}/w/{wid}/e/{s['bs_eid']}",
              wait_until="domcontentloaded"); page.wait_for_timeout(20000)
    screen.hook(page); gui.wake(page); gui.viewport(page); gui.clear(page)
    wheel(page, -12)
    page.mouse.move(900, 500)
    page.keyboard.press("Shift+7"); page.wait_for_timeout(1600)
    gui.fit(page); page.wait_for_timeout(2500)
    xy = find(page, "stud connect to robot"); print("  row at", xy)
    page.mouse.click(*xy); page.wait_for_timeout(2500)
    shot(page, (0.0, 0.0, 10.0), None, "l-limb/move_stud.source.closeup.png", 26.0, 70)

    print("\n=== hinge")
    page.goto(f"https://cad.onshape.com/documents/{did}/w/{wid}/e/{s['hinge_eid']}",
              wait_until="domcontentloaded"); page.wait_for_timeout(20000)
    screen.hook(page); gui.wake(page); gui.viewport(page); gui.clear(page)
    end = faces(page, s["hinge_eid"]); print(f"  {end} faces at the end")
    try:
        xy = find(page, "axis for circular patterns"); print("  row at", xy)
        page.mouse.click(xy[0], xy[1], button="right"); page.wait_for_timeout(2000)
        hit = page.evaluate(MENU, "Roll to here")
        assert hit, "no 'Roll to here'"
        page.mouse.click(*hit); page.wait_for_timeout(9000)
        print(f"  rolled back: {faces(page, s['hinge_eid'])} faces")
        gui.wake(page); gui.clear(page)
        page.mouse.move(900, 500)
        page.keyboard.press("Shift+7"); page.wait_for_timeout(1600)
        gui.fit(page); page.wait_for_timeout(2500)
        page.mouse.click(*find(page, "axis for circular patterns")); page.wait_for_timeout(2500)
        shot(page, (0.0, -12.50871, 0.0), "hinge/blade.pattern_axis.medium.png",
             "hinge/blade.pattern_axis.closeup.png", 34.0, 100)
    except Exception as e:
        print("  !!", type(e).__name__, str(e)[:200])
    finally:
        page.keyboard.press("Escape"); page.wait_for_timeout(600)
        bar = page.evaluate(BARY)
        if bar:
            page.mouse.click(bar[0], bar[1], button="right"); page.wait_for_timeout(2000)
            hit = page.evaluate(MENU, "Roll to end")
            if hit: page.mouse.click(*hit); page.wait_for_timeout(9000)
            else: page.keyboard.press("Escape")
        back = faces(page, s["hinge_eid"])
        print(f"  {back} faces", "RESTORED" if back == end else "*** NOT RESTORED ***")
