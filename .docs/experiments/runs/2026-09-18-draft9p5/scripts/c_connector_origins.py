#!/usr/bin/env python3
"""What each mate connector is placed on, read out of its own dialog.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/c_connector_origins.py

[`torso.md`](../../../build-briefs/torso.md) asks for the origin entity and the
offset of every connector, not its position: *a connector at the right station by
arithmetic passes a position check and still fails this one*. A connector placed
**On entity** against a face follows that face when a feature above it moves; one
placed on **Origin** with a typed **Move** is a coordinate that was right when it
was typed.

That is a feature parameter, so it is either `/features` or the dialog. This is
the dialog, read as text rather than photographed.

**A feature dialog applies to the model as it is changed**, so every path out of
each connector presses Escape, and nothing here types or picks anything.
"""

from __future__ import annotations

import sys

from playwright.sync_api import sync_playwright

from stickbot import onshape_gui as gui
from stickbot import onshape_session as api

DID, WID = "2f08b54d795df0ee6b72e321", "1d8e4c837228c90bab9ff062"
# Each tab's connectors, in tree order. `body`'s eight are the ones torso.md asks
# about: three that features are built on, then the five the assembly mates to.
TABS = {
    "body": ("5441067befc71f1e3b91482e",
             ["mate for shoulder stud", "mate for hip stud", "mate for neck stud",
              "neck", "left shoulder", "right shoulder", "left hip", "right hip"]),
    "foot": ("229aa0900e5a7e7aa4768c6f", ["mate to robot"]),
    "gripper": ("a3a4fac68ffb7372a7803003", ["mate to robot"]),
    "head": ("303898bd4ba38fc3957b0a21", ["socket mount point", "head mate"]),
}
FIELDS = "div[class*='parameter']"


def read_one(page, name):
    """Open one connector, take its parameters as text, and escape."""
    try:
        x, y = gui.row(page, name)
        page.mouse.dblclick(x, y)
        page.wait_for_timeout(2600)
        bits = []
        for i in range(page.locator(FIELDS).count()):
            t = page.locator(FIELDS).nth(i).inner_text().strip()
            if t:
                bits.append(" ".join(t.split()))
        # A ticked box reads the same as an unticked one in text, and whether
        # Move is ticked is the whole question, so read the input's own state.
        for box in ("Realign", "Move"):
            el = page.locator(f"label:has-text('{box}') input[type=checkbox]").first
            if el.count():
                bits.append(f"[{box} {'TICKED' if el.is_checked() else 'unticked'}]")
        vals = [f.input_value() for f in page.locator("input[type=text]").all()
                if f.is_visible()]
        nums = [v for v in vals if v and any(c.isdigit() for c in v)]
        if nums:
            bits.append(f"[number fields: {nums}]")
        return bits
    finally:
        page.keyboard.press("Escape")
        page.wait_for_timeout(900)
        page.keyboard.press("Escape")
        page.wait_for_timeout(400)


def main(only: str | None = None) -> int:
    with sync_playwright() as pw:
        browser, ctx, page = gui.connect(pw)
        for tab, (eid, names) in TABS.items():
            if only and tab != only:
                continue
            print(f"\n== {tab}")
            gui.open_doc(page, api.Doc(DID, WID, eid))
            gui.no_banner(page)
            for name in names:
                print(f"  {name}")
                for bit in read_one(page, name):
                    print(f"      {bit}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else None))
