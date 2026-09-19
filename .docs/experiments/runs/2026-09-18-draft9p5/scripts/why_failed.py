#!/usr/bin/env python3
"""What Onshape says about a feature that did not regenerate.

    uv run python .../scripts/why_failed.py "body" "trim shoulder cut" ...

`featureStates` carries only OK or ERROR and needs `/features`; the sentence that
says what went wrong is in the tree row's tooltip, and the GUI is not rate
limited. Read only: it hovers rows and reads text.
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

TEXT = """() => [...document.querySelectorAll('div,span')]
    .filter(e => !e.children.length && (e.innerText||'').trim().length > 12)
    .map(e => (e.innerText||'').trim())
    .filter(t => /did not regenerate|error|cannot|could not|unable|missing|empty|failed/i.test(t))
    .slice(0, 4)"""


def main(tab: str, names: list[str]) -> int:
    doc = S.Doc(DID, WID, ELEMENTS[tab])
    with sync_playwright() as p:
        browser, _ctx, page = gui.connect(p)
        gui.open_doc(page, doc)
        gui.no_banner(page)
        for name in names:
            try:
                x, y = gui.row(page, name)
            except Exception as exc:
                print(f"{name}: no such row ({exc})")
                continue
            page.mouse.move(x, y)
            page.wait_for_timeout(2200)
            said = page.evaluate(TEXT)
            print(f"{name}:")
            for s in said:
                print(f"    {s}")
            if not said:
                print("    (nothing said)")
            page.mouse.move(900, 600)
            page.wait_for_timeout(400)
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2:]))
