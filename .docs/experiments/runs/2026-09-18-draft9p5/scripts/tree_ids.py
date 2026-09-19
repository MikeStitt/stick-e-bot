#!/usr/bin/env python3
"""Every feature's id and name, read off the GUI's tree.

    uv run python .../scripts/tree_ids.py "body"

`/features` is the route that carries feature ids and it is the one Onshape rate
limits hardest. The tree's rows carry the same ids in a `feature-id` attribute,
and the GUI is not rate limited at all, so a tab that cannot be read can still
be cleared or resumed. Read only.

**The list holds only the rows it is showing**, about thirty of them, so it is
wheeled from the top to the bottom and the readings are stitched on the id,
which is unique. Read once without scrolling it gave 29 of `body`'s 33, and a
row that is not drawn reads exactly like a row that is not there — the same
trap `onshape_gui.tree_all` was written for.
"""

from __future__ import annotations

import json
import sys

from playwright.sync_api import sync_playwright

from stickbot import onshape_gui as gui
from stickbot import onshape_session as S
from stickbot import repo_root

DID = "2f08b54d795df0ee6b72e321"
WID = "1d8e4c837228c90bab9ff062"
OUT = repo_root() / ".docs/experiments/runs/2026-09-18-draft9p5/results"
ELEMENTS = {e["name"]: e["id"] for e in json.loads(
    (OUT / "elements.json").read_text())["elements"]}

ROWS = """() => [...document.querySelectorAll('[feature-id]')].map(e => ({
    id: e.getAttribute('feature-id'),
    type: e.getAttribute('feature-type'),
    name: (e.querySelector('.os-list-item-label')?.textContent || '').trim()
}))"""


def main(tab: str) -> int:
    doc = S.Doc(DID, WID, ELEMENTS[tab])
    with sync_playwright() as p:
        browser, _ctx, page = gui.connect(p)
        gui.open_doc(page, doc)
        gui.no_banner(page)
        page.mouse.move(140, 420)
        page.mouse.wheel(0, -6000)
        page.wait_for_timeout(700)
        seen, rows = set(), []
        for _ in range(40):
            for r in page.evaluate(ROWS):
                if r["id"] not in seen:
                    seen.add(r["id"])
                    rows.append(r)
            page.mouse.wheel(0, 300)
            page.wait_for_timeout(260)
        browser.close()
    for r in rows:
        print(f"  {r['type'] or '':<16} {r['name'][:34]:<34} {r['id']}")
    stem = tab.replace(" ", "-")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{stem}.tree-ids.json").write_text(json.dumps(rows, indent=2) + "\n")
    print(f"\n{len(rows)} rows -> {OUT / f'{stem}.tree-ids.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
