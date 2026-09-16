"""#59 — retake the three unusable frames, each from the state its step is in.

Every one of the three connectors is coincident with something else at the end
of its tab's feature list, so each frame is shot with the tree rolled back to
the feature it is about, and every roll is undone in a finally and checked
against the face count REST reports.
"""
import sys, json
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
BARY = """() => { const e = document.querySelector('.ns-list-item-rollbackbar');
  if (!e) return null; const r = e.getBoundingClientRect();
  return [Math.round(r.x + r.width/2), Math.round(r.y + r.height/2)]; }"""

def faces(page, eid):
    b = osx.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/bodydetails")["body"]
    return sum(len(body["faces"]) for body in b["bodies"])

def box(page, eid):
    return osx.api(page, "GET",
        f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/boundingboxes")["body"]

def rollto(page, name):
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    page.mouse.click(*gui.row(page, name), button="right"); page.wait_for_timeout(1800)
    hit = page.evaluate(MENU, "Roll to here")
    assert hit, f"no 'Roll to here' on {name!r}"
    page.mouse.click(*hit); page.wait_for_timeout(9000)

def rolltoend(page):
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    bar = page.evaluate(BARY)
    assert bar, "no rollback bar in the DOM"
    page.mouse.click(bar[0], bar[1], button="right"); page.wait_for_timeout(1800)
    hit = page.evaluate(MENU, "Roll to end")
    if hit is None:
        page.keyboard.press("Escape"); return "already at the end"
    page.mouse.click(*hit); page.wait_for_timeout(9000)
    return "rolled to end"

# tab, eid, roll to, row to select, point, medium, closeup, px/mm, radius
JOBS = [
  ("u limb", s["ul_eid"], "mate for fork", "mate for fork", "zmin",
   None, "u-limb/move_fork.closeup.png", 20.0, 70),
  ("l limb", s["ll_eid"], "add ball stud", "stud connect to robot", (0.0, 0.0, 10.0),
   None, "l-limb/move_stud.source.closeup.png", 30.0, 60),
  ("hinge", s["hinge_eid"], "axis for circular patterns", "axis for circular patterns",
   (0.0, -12.50871, 0.0),
   "hinge/blade.pattern_axis.medium.png", "hinge/blade.pattern_axis.closeup.png", 40.0, 110),
]

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up(); page.keyboard.press("Escape"); page.wait_for_timeout(800)
    page.set_default_navigation_timeout(180000); page.set_default_timeout(120000)
    for tab, eid, upto, pick, pt, med, close, target, radius in JOBS:
        print(f"\n=== {tab}")
        page.goto(f"https://cad.onshape.com/documents/{did}/w/{wid}/e/{eid}",
                  wait_until="domcontentloaded")
        page.wait_for_timeout(20000)
        end = faces(page, eid); print(f"  {end} faces at the end")
        try:
            rollto(page, upto)
            print(f"  rolled to {upto!r}: {faces(page, eid)} faces")
            b = box(page, eid); print("  box:", json.dumps(b))
            if pt == "zmin":
                pt = (0.0, 0.0, b["lowZ"] * 1000.0)
            print("  point:", pt)
            screen.hook(page); gui.wake(page)
            gui.viewport(page); gui.clear(page)
            page.mouse.move(900, 500)
            page.keyboard.press("Shift+7"); page.wait_for_timeout(2000)
            gui.fit(page); page.wait_for_timeout(2500)
            page.mouse.click(*gui.row(page, pick)); page.wait_for_timeout(2500)
            page.mouse.move(*gui.EMPTY); page.wait_for_timeout(1500)
            if med:
                gui.frame(page, OUT + med); print("  wrote", med)
            at = gui.project(page, *pt, cam=screen.camera(page))
            print("  medium pixel:", at)
            gui.zoom_to(page, target, at_px=at); page.wait_for_timeout(1500)
            at2 = gui.project(page, *pt, cam=screen.camera(page))
            print("  closeup pixel:", at2)
            page.mouse.move(*gui.EMPTY); page.wait_for_timeout(1200)
            gui.ring(page, OUT + close, at2, radius=radius); print("  wrote", close)
        finally:
            print("  ", rolltoend(page))
            back = faces(page, eid)
            print(f"  {back} faces", "RESTORED" if back == end else "*** NOT RESTORED ***")
