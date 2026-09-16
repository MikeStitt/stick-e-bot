"""Name the open Create version dialog and cut it."""
import sys
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge")
from playwright.sync_api import sync_playwright
from tools import onshape_session as S
NAME = "Recovery point"
DESC = ("draft9p1 Phase C. The model was read back against make_plans.py and agrees; "
        "#limbCenter was driven 48 to 60 and back and #fit 0.08 to 1 to 0 and back, "
        "both round trips exact. This is what draft9p2 starts from.")
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
    page.mouse.click(754, 322)
    page.wait_for_timeout(15000)
    print("create clicked")
