#!/usr/bin/env python3
"""Delete the `gripper` tab's own `#ball` and `#wall`, so both read the studio's rows.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/c_drop_shadow_vars.py

The tab declares `#wall = #torsoH / 32`, 3.000 mm, where `robot sizes` holds
`#torsoH * 3 / 160`, 1.800 mm. The local shadows the row, so `#collarR` resolves
to 9.000 mm there and the clip body, written as `2 x #collarR`, comes out
18.000 mm against the Ø15.600 collar the derived socket brings in. It also
declares `#ball`, with the studio's own expression, which agrees today and
shadows the row all the same.

`#ball` goes first. It resolves to the same number either way, so the row
vanishing with no change to the shape is what proves the delete worked before the
one that does change the shape runs.

[`.docs/onshape-gui-howto.md`](../../../../onshape-gui-howto.md) line 238:
**right-click a variable row → Delete** removes it. The `/features` DELETE shares
its quota with the writes and is refused; the menu is not rate limited.
"""

from __future__ import annotations

import sys

from playwright.sync_api import sync_playwright

from stickbot import onshape_gui as gui
from stickbot import onshape_session as api

DOC = api.Doc("2f08b54d795df0ee6b72e321", "1d8e4c837228c90bab9ff062",
              "a3a4fac68ffb7372a7803003")
DROP = ["#ball", "#wall"]


def row_text(page, prefix):
    """The tree row that starts with this variable's name, as Onshape prints it."""
    for r in gui.tree_all(page):
        if r.startswith(prefix + " ="):
            return r
    return None


def drop(page, prefix):
    text = row_text(page, prefix)
    if text is None:
        print(f"  {prefix}: no such row; nothing to delete")
        return False
    print(f"  {prefix}: row reads {text!r}")
    x, y = gui.row(page, text)
    page.mouse.click(x, y)                 # the context menu wants a plain click first
    page.wait_for_timeout(700)
    for attempt in range(3):               # the first right-click after a connect can be swallowed
        page.mouse.click(x, y, button="right")
        page.wait_for_timeout(900)
        item = page.get_by_text("Delete", exact=True).locator("visible=true")
        if item.count():
            item.first.click()
            page.wait_for_timeout(2500)
            break
        print(f"      no Delete in the menu on attempt {attempt + 1}; clicking again")
    else:
        raise RuntimeError(f"the context menu for {text!r} never offered Delete")
    gone = row_text(page, prefix) is None
    print(f"      {'deleted' if gone else 'STILL THERE'}")
    return gone


def main() -> int:
    with sync_playwright() as pw:
        browser, ctx, page = gui.connect(pw)
        gui.open_doc(page, DOC)
        gui.no_banner(page)
        before = [r for r in gui.tree_all(page) if r.startswith("#")]
        print("variable rows before:", before)
        for prefix in DROP:
            drop(page, prefix)
        after = [r for r in gui.tree_all(page) if r.startswith("#")]
        print("variable rows after: ", after)
    return 0


if __name__ == "__main__":
    sys.exit(main())
