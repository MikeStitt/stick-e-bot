#!/usr/bin/env python3
"""Add a derived part through the GUI, because the REST route does not return.

    uv run python .../scripts/c_gui_derive.py "head" "ball and socket" "Socket body" "get socket"

`POST .../features` with an `importDerived` feature hangs: measured on
2026-09-18 with a ten-minute budget, it never answered and created nothing,
while every other feature type wrote in under a second. The GUI is not rate
limited and does it at once, which is what the onshape skill says to reach for.

Two traps, both draft9p3's, and both guarded here:

- **Choosing the tab brings every part in it.** The narrowing has to be seen in
  the page's own feature list, because `/api/parts` answers from the committed
  model and cannot see what a dialog is previewing. This reads `Parts (n)` off
  the panel before and after the part is picked and refuses to tick if the count
  did not come down.
- **The dialog writes to the model as you type.** Every failure path presses the
  red cross, or the half-made feature stays.
"""

from __future__ import annotations

import json
import re
import sys

from playwright.sync_api import sync_playwright

from stickbot import onshape_gui as gui
from stickbot import onshape_session as S
from stickbot import repo_root

OUT = repo_root() / ".docs/experiments/runs/2026-09-18-draft9p5/results"
ELEMENTS = {e["name"]: e["id"] for e in json.loads(
    (OUT / "elements.json").read_text())["elements"]}
DID = "2f08b54d795df0ee6b72e321"
WID = "1d8e4c837228c90bab9ff062"
RED_X = (451, 93)

# Exact leaf text first, then a leaf that starts with it: the Part Studio field
# reads `Select Part Studio...` on screen and its trailing dots are not always in
# the text node.
FIND = r"""([want, minX]) => {
    const hit = [];
    for (const e of document.querySelectorAll('div,li,span,button,td')) {
        if (e.children.length) continue;
        const t = (e.innerText || '').trim();
        if (!t) continue;
        const r = e.getBoundingClientRect();
        if (!(r.width > 10 && r.height > 5 && r.y < 900)) continue;
        if (r.x < minX) continue;
        const at = [Math.round(r.x + r.width / 2), Math.round(r.y + r.height / 2)];
        if (t === want) return at;
        if (t.startsWith(want) || want.startsWith(t.replace(/\.+$/, ''))) hit.push(at);
    }
    return hit.length ? hit[0] : null;
}"""


def parts_count(page):
    for row in gui.tree(page):
        m = re.match(r"^Parts \((\d+)\)$", row)
        if m:
            return int(m.group(1))
    return None


def click_text(page, want, what, min_x=0):
    """Click a leaf that reads `want`.

    `min_x` keeps a pick inside the picker: the tab's own parts list sits at the
    left of the panel and carries the same names as the dialog's list, so a
    search over the whole page picks the tree row and the narrowing never
    happens.
    """
    at = page.evaluate(FIND, [want, min_x])
    if at is None:
        raise RuntimeError(f"{what}: nothing on the page reads {want!r}")
    page.mouse.click(*at)
    return at


def main(tab, source, part, name) -> int:
    doc = S.Doc(DID, WID, ELEMENTS[tab])
    with sync_playwright() as p:
        browser, _ctx, page = gui.connect(p)
        gui.open_doc(page, doc)
        gui.no_banner(page)
        before = parts_count(page)
        print(f"`{tab}` holds Parts ({before}) before")
        try:
            gui.search_tool(page, "Derived")
            page.wait_for_timeout(1800)
            click_text(page, "Select Part Studio", "the Part Studio field")
            page.wait_for_timeout(2500)
            click_text(page, source, "the source tab", min_x=500)
            page.wait_for_timeout(3000)
            every = parts_count(page)
            print(f"choosing `{source}` previews Parts ({every})")
            click_text(page, part, "the part to keep", min_x=500)
            page.wait_for_timeout(2500)
            narrowed = parts_count(page)
            print(f"picking `{part}` narrows it to Parts ({narrowed})")
            if not (before is not None and narrowed == before + 1):
                raise RuntimeError(f"expected Parts ({before + 1}) after narrowing to one "
                                   f"part, the panel reads Parts ({narrowed})")
            gui.tick(page)
            page.wait_for_timeout(3000)
        except Exception:
            page.mouse.click(*RED_X)
            page.wait_for_timeout(1200)
            raise
        # A second derive in the same tab arrives as `Derived 2`, so the row to
        # rename is whichever `Derived N` the tick just left behind.
        fresh = [r for r in gui.tree_all(page) if re.match(r"^Derived \d+$", r)]
        if not fresh:
            raise RuntimeError("no `Derived N` row to rename after the tick")
        gui.rename_row(page, fresh[-1], name)
        page.wait_for_timeout(1500)
        tree = gui.tree_all(page)
        if name not in tree:
            raise RuntimeError(f"{name!r} is not in the tree after the rename")
        print(f"committed and named `{name}`; the tab now reads "
              f"Parts ({parts_count(page)})")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:5]))
