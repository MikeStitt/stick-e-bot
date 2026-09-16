import sys, re
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_screen as screen
from playwright.sync_api import sync_playwright
s = common.load(); did, wid = s["did"], s["wid"]
IMG = "/Users/mikestitt/projects/first/2027/sponge/instructions/stickbot-draft9p0/source/images/"

POINT = """() => { for (const e of document.querySelectorAll('div,span')) {
    const t = (e.innerText||'').trim();
    if (t.startsWith('Point:') && t.length < 90) return t;
  } return null; }"""

JOBS = [
    ("u limb", s["ul_eid"], "mate for fork",       "u-limb/move_fork.closeup.png",  20.0, 70),
    ("l limb", s["ll_eid"], "stud connect to robot","l-limb/move_stud.source.closeup.png", 30.0, 60),
]

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up(); page.keyboard.press("Escape"); page.wait_for_timeout(600)
    page.set_default_navigation_timeout(180000); page.set_default_timeout(120000)
    for tab, eid, rowname, out, target, radius in JOBS:
        print(f"\n=== {tab} / {rowname}")
        page.goto(f"https://cad.onshape.com/documents/{did}/w/{wid}/e/{eid}",
                  wait_until="domcontentloaded")
        page.wait_for_timeout(22000)
        screen.hook(page); gui.wake(page)
        gui.clear(page)
        page.keyboard.press("Shift+7"); page.wait_for_timeout(1500)
        page.keyboard.press("f");       page.wait_for_timeout(2500)
        page.mouse.click(*gui.row(page, rowname)); page.wait_for_timeout(2500)
        txt = page.evaluate(POINT)
        print("   status bar:", txt)
        nums = [float(v) for v in re.findall(r"-?\d+\.?\d*", txt or "")]
        if len(nums) < 3:
            print("   !! no point, skipping"); continue
        x, y, z = nums[:3]
        print(f"   point = ({x}, {y}, {z})")
        gui.zoom_to(page, target, at_px=gui.project(page, x, y, z,
                                                    cam=screen.camera(page)))
        page.wait_for_timeout(1500)
        at = gui.project(page, x, y, z, cam=screen.camera(page))
        print("   ring at", at)
        gui.ring(page, IMG + out, at, radius=radius)
        print("   wrote", out)
