"""Name the open Create version dialog and cut it."""
import sys, base64
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge")
from playwright.sync_api import sync_playwright
from tools import onshape_session as S

OUT = ("/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/runs/"
       "2026-08-26-draft9p1p1/c/frames/")
NAME = "Recovery point"
DESC = ("draft9p1p1 Phase C. #collar is re-based on the ball's center, the relief slit is a "
        "slot for its whole depth, and the gripper's clip top is flat and square. #fit was "
        "driven 0.08 to 1 to 0 and back and the robot stood 317.0000 at every value, with "
        "no joint station moving. #torsoH was driven 96 to 120 and back and #collar "
        "followed. This is what draft9p2 starts from.")

with sync_playwright() as p:
    browser, ctx, page = S.connect(p)
    page.mouse.click(371, 101)
    page.wait_for_timeout(700)
    page.keyboard.press("Meta+a")
    page.wait_for_timeout(300)
    page.keyboard.type(NAME)
    page.wait_for_timeout(500)
    page.mouse.click(641, 198)
    page.wait_for_timeout(700)
    page.keyboard.type(DESC)
    page.wait_for_timeout(700)
    got = page.evaluate("""() => {
        const out = [];
        for (const el of document.querySelectorAll('input,textarea')) {
            const r = el.getBoundingClientRect();
            if (r.width > 40 && r.height > 4 && r.y < 300) out.push([el.tagName, el.value]);
        }
        return out;
    }""")
    print("fields:", got)
    cdp = ctx.new_cdp_session(page)
    d = cdp.send("Page.captureScreenshot", {"format": "png"})
    open(OUT + "c3-version-typed.png", "wb").write(base64.b64decode(d["data"]))
    page.mouse.click(754, 322)
    page.wait_for_timeout(18000)
    print("create clicked")
