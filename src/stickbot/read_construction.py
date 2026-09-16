"""Every feature's dependencies, read out of the GUI, for a whole Part Studio.

`/api/partstudios/.../features` is the route that carries construction, and it is the one
Onshape rate limits hardest. `Show dependencies…` on a feature's right-click menu carries
the same skeleton -- what this feature was built on, and what was built on it -- and the
GUI is not rate limited at all.

    uv run --project . python tools/read_construction.py <did> <wid> <eid> <out.json>

Read only. The menu item displays a panel; nothing is edited, and every path escapes.

A panel sometimes comes back empty on a feature that has one. Each feature gets three
tries, and any that still refuses is listed under `unread` in the record, because a
feature present in `order` and absent from `features` reads downstream as a feature the
tab does not have.
"""
import json
import sys

from playwright.sync_api import sync_playwright

from stickbot import onshape_gui as gui
from stickbot import onshape_session as api

PANEL = """() => {
    const head = Array.from(document.querySelectorAll('div,span'))
        .filter(e => (e.innerText || '').trim().startsWith('Dependencies of'))
        .map(e => e.getBoundingClientRect())
        .filter(r => r.width > 150 && r.height > 40)
        .sort((a, b) => a.height - b.height)[0];
    if (!head) return null;
    return Array.from(document.querySelectorAll('li,a,span,div'))
        .filter(e => !e.children.length && (e.innerText || '').trim())
        .map(e => {const r = e.getBoundingClientRect();
                   return [Math.round(r.y), (e.innerText || '').trim(), r.x, r.width]})
        .filter(a => a[2] >= head.x - 4 && a[2] + a[3] <= head.x + head.width + 8
                     && a[0] > head.y + 20 && a[0] < head.y + head.height + 8)
        .sort((a, b) => a[0] - b[0])
        .map(a => a[1]); }"""


def menu_item(page, text):
    return page.evaluate(
        """(want) => {
            for (const e of document.querySelectorAll('li,a,span,div')) {
                if (e.children.length) continue;
                if ((e.innerText || '').trim() !== want) continue;
                const r = e.getBoundingClientRect();
                if (r.width && r.height)
                    return [Math.round(r.x + r.width / 2), Math.round(r.y + r.height / 2)];
            }
            return null; }""", text)


def bring_row(page, name, tries: int = 14):
    """Scroll the feature list until `name` is drawn.

    Onshape keeps about thirty rows in the page at a time. `gui.tree_all` leaves the list
    at the bottom, and `gui.row` then waits thirty seconds for a row that is not in the
    DOM at all rather than one that is merely off screen.
    """
    page.mouse.move(140, 400)
    page.mouse.wheel(0, -4000)
    page.wait_for_timeout(600)
    for _ in range(tries):
        if name in gui.tree(page):
            return
        page.mouse.wheel(0, 260)
        page.wait_for_timeout(400)
    raise RuntimeError(f"{name!r} never came into the feature list")


DEFAULTS = ("Default geometry", "Origin", "Top", "Front", "Right")
TRIES = 3


def dependencies(page, name):
    """`(upstream, downstream)` for one feature, or `None` if it offers no menu item."""
    bring_row(page, name)
    x, y = gui.row(page, name)
    page.mouse.click(x, y, button="right")
    page.wait_for_timeout(1200)
    hit = menu_item(page, "Show dependencies…")
    if hit is None:
        page.keyboard.press("Escape")
        page.wait_for_timeout(500)
        return None
    page.mouse.click(*hit)
    page.wait_for_timeout(2000)
    rows = page.evaluate(PANEL) or []
    page.keyboard.press("Escape")
    page.wait_for_timeout(700)
    page.keyboard.press("Escape")
    page.wait_for_timeout(500)
    rows = [r for r in rows if r not in ("", "▲", "▼")]
    if name not in rows:
        raise RuntimeError(f"{name!r} is not in its own dependency panel: {rows}")
    i = rows.index(name)
    return rows[:i], rows[i + 1:]


def main(did, wid, eid, out):
    doc = api.Doc(did, wid, eid)
    with sync_playwright() as p:
        browser, ctx, page = gui.connect(p)
        gui.open_doc(page, doc)
        gui.viewport(page)
        page.keyboard.press("Escape")
        page.wait_for_timeout(800)
        gui.no_banner(page)
        rows = gui.tree_all(page)
        feats = []
        for r in rows:
            if r.startswith("Parts ("):
                break
            feats.append(r)
        print(f"{len(feats)} rows in the tree")
        found = {}
        for name in feats:
            if name in DEFAULTS:
                continue
            for attempt in range(TRIES):
                page.keyboard.press("Escape")
                page.wait_for_timeout(700)
                try:
                    dep = dependencies(page, name)
                except Exception as e:
                    print(f"  {name}: try {attempt} {type(e).__name__} {e}")
                    continue
                if dep is None:
                    print(f"  {name}: try {attempt} no Show dependencies")
                    continue
                found[name] = {"upstream": dep[0], "downstream": dep[1]}
                print(f"  {name}\n      on: {dep[0]}")
                break
        unread = [n for n in feats if n not in DEFAULTS and n not in found]
        with open(out, "w") as f:
            json.dump({"did": did, "wid": wid, "eid": eid, "order": feats,
                       "unread": unread, "features": found}, f, indent=1)
        print("wrote", out)
        if unread:
            print(f"{len(unread)} feature(s) never gave up a panel: {unread}")
            print("They are in the tab. Fill them in before diffing this record,"
                  " or the diff reports them as features the tab does not have.")


if __name__ == "__main__":
    main(*sys.argv[1:5])
