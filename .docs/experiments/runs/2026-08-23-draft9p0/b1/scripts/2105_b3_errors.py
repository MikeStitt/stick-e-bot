"""B3 — sweep every tab and count anything the tree marks as an error."""
import sys, json
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui
from playwright.sync_api import sync_playwright
s = common.load(); did, wid = s["did"], s["wid"]
TAG = sys.argv[1]
TABS = [("body", s["ps_eid"]), ("head", s["head_eid"]), ("ball and socket", s["bs_eid"]),
        ("foot", s["foot_eid"]), ("hinge", s["hinge_eid"]), ("u limb", s["ul_eid"]),
        ("l limb", s["ll_eid"]), ("gripper", s["gr_eid"]), ("stickbot", s["asm_eid"])]
JS = """() => { const out = [];
  for (const e of document.querySelectorAll('[class*=error],[class*=Error],[class*=warning]')) {
    const r = e.getBoundingClientRect();
    if (!r.width || !r.height) continue;
    out.push([e.className.toString().slice(0,60), (e.innerText||'').trim().slice(0,60)]);
  } return out; }"""
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up()
    page.set_default_navigation_timeout(180000)
    for name, eid in TABS:
        page.goto(f"https://cad.onshape.com/documents/{did}/w/{wid}/e/{eid}",
                  wait_until="domcontentloaded")
        page.wait_for_timeout(11000)
        hits = page.evaluate(JS)
        print(f"{name:16} tree {len(gui.tree(page)):3} rows, {len(hits)} marked")
        for h in hits[:6]:
            print("      ", h)
        if name == "stickbot":
            gui.fit(page); page.wait_for_timeout(2500)
            page.screenshot(path=D + f"b3_asm_{TAG}.png")
