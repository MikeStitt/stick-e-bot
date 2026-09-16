"""Create stickbot-draft9p0, stamp my page, and set workspace units to mm."""
import sys, time
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api

NAME = "stickbot-draft9p0"

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    assert not [pg for pg, n in common.marks(ctx) if n == common.MARK], "mark already taken"
    page = ctx.new_page()
    page.goto("https://cad.onshape.com/documents", wait_until="domcontentloaded")
    page.wait_for_timeout(4500)
    page.evaluate(f"window.name = {common.MARK!r}")
    print("signed in as:", api.require_signed_in(page))

    # does it already exist?
    r = api.api(page, "GET", f"/api/documents?q={NAME}&filter=0&limit=20")
    hit = [i for i in (r["body"].get("items") or []) if i["name"] == NAME]
    if hit:
        d = hit[0]
        print("already exists:", d["id"])
    else:
        btn = page.locator("button:has-text('Create'):visible").first
        btn.click()
        page.wait_for_timeout(700)
        bb = btn.bounding_box()
        page.mouse.click(bb["x"] + 30, bb["y"] + bb["height"] + 18)
        page.wait_for_timeout(1200)
        dlg = page.locator("div[role='dialog']:visible").first
        dlg.locator("input[type='text']").first.fill(NAME)
        page.wait_for_timeout(300)
        dlg.get_by_role("button", name="Create", exact=True).click()
        page.wait_for_timeout(9000)
        print("url after create:", page.url)
        for _ in range(6):
            r = api.api(page, "GET", f"/api/documents?q={NAME}&filter=0&limit=20")
            hit = [i for i in (r["body"].get("items") or []) if i["name"] == NAME]
            if hit:
                break
            page.wait_for_timeout(4000)
        d = hit[0] if hit else None
    if not d:
        raise SystemExit("document not found after create")
    did = d["id"]; wid = d["defaultWorkspace"]["id"]
    common.save(did=did, wid=wid, name=NAME)
    print("did", did, "wid", wid)
    print("page url:", page.url[:100])
