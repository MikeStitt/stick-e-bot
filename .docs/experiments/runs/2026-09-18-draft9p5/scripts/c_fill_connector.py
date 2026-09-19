#!/usr/bin/env python3
"""Fill `mate to robot`'s three selections, which its record does not carry.

    uv run python .../scripts/c_fill_connector.py "foot" "Foot"

draft9p1p1's `foot` and `gripper` both return this feature with `originQuery`,
`ownerPart` and `attachTo` empty, and Onshape says so in as many words when the
feature is opened: *Cannot resolve entities. 3 missing selections*. Writing body
ids into those fields over REST is accepted and changes nothing, because a body's
id is not what they take. So they are picked, the way a person picks them.

The origin is the **Origin's vertex**, taken from the tree, which puts the
connector at the part's origin — the ball's centre, which is what the ankle and
the wrist mate on. Owner and attachment are the part itself, from the Parts list.
"""

from __future__ import annotations

import json
import sys

from playwright.sync_api import sync_playwright

from stickbot import onshape_gui as gui
from stickbot import onshape_session as S
from stickbot import repo_root

OUT = repo_root() / ".docs/experiments/runs/2026-09-18-draft9p5/results"
ELEMENTS = {e["name"]: e["id"] for e in json.loads(
    (OUT / "elements.json").read_text())["elements"]}

# Where the three selection fields sit in the open dialog.
ORIGIN_FIELD, OWNER_FIELD, ATTACH_FIELD = (356, 170), (356, 305), (356, 384)

COUNT = ("function(context is Context, queries is map)\n{\n"
         "    return toString(size(evaluateQuery(context,"
         " qBodyType(qEverything(EntityType.BODY), BodyType.MATE_CONNECTOR))));\n}")

DIALOG = """() => {
    for (const el of document.querySelectorAll('div')) {
        const t = (el.innerText || '');
        if (t.startsWith('mate to robot') && t.includes('Origin entity')
            && el.getBoundingClientRect().width < 400)
            return t.split('\\n').filter(Boolean).slice(0, 16);
    }
    return null;
}"""


def pick(page, field, row_name):
    page.mouse.click(*field)
    page.wait_for_timeout(900)
    x, y = gui.row(page, row_name)
    page.mouse.click(x, y)
    page.wait_for_timeout(1800)


def main(tab: str, part: str) -> int:
    doc = S.Doc("2f08b54d795df0ee6b72e321", "1d8e4c837228c90bab9ff062", ELEMENTS[tab])
    with sync_playwright() as p:
        browser, _ctx, page = gui.connect(p)
        gui.open_doc(page, doc)
        gui.no_banner(page)
        before = int(S.eval_fs(page, doc, COUNT))
        x, y = gui.row(page, "mate to robot")
        page.mouse.dblclick(x, y)
        page.wait_for_timeout(2500)
        if page.evaluate(DIALOG) is None:
            raise RuntimeError("the mate connector dialog did not open")
        try:
            pick(page, ORIGIN_FIELD, "Origin")
            pick(page, OWNER_FIELD, part)
            pick(page, ATTACH_FIELD, part)
            filled = page.evaluate(DIALOG)
            if "Missing Item" in filled or "Missing Entity" in filled:
                raise RuntimeError(f"a field is still empty: {filled}")
            print("filled:", filled)
            gui.tick(page)
            page.wait_for_timeout(3000)
        except Exception:
            page.mouse.click(451, 93)       # the red cross, so nothing half made stays
            page.wait_for_timeout(1200)
            raise
        after = int(S.eval_fs(page, doc, COUNT))
        print(f"connector bodies {before} -> {after}")
        if after != before + 1:
            raise RuntimeError("the feature still makes no connector")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
