#!/usr/bin/env python3
"""Phase B tab 1 — the `robot sizes` Variable Studio.

The 23 rows come from the parent's record, and every name in it is checked
against the Variables table in `.docs/robot-build-plan.md` before anything is
written: that table is the whole ask for what is a variable, so a row the table
does not have is a row this draft must not invent.

`POST .../variables` takes the array, not the table the GET returns, and it takes
it one prefix at a time. **A row's expression must resolve against rows already
committed; a payload cannot reference a row it carries itself.** Measured on
2026-09-18 in this studio: the four literal drivers in one write are a 204, the
same four plus `#wall`, which reads `#torsoH`, are a 400, and all 23 written as
23 growing prefixes are accepted. The write replaces the whole table each time,
so the prefixes leave exactly the 23 rows.

Ring 1 for a Variable Studio is the read-back: the rows are fetched again and
compared name by name and expression by expression.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/b1_robot_sizes.py
"""

from __future__ import annotations

import json
import re
import sys

from playwright.sync_api import sync_playwright

from stickbot import onshape_session as S
from stickbot import repo_root

ROOT = repo_root()
DID = "2f08b54d795df0ee6b72e321"
WID = "1d8e4c837228c90bab9ff062"
EID = "3d67f51a630c05c2b5d0b9ea"          # robot sizes
PARENT = ROOT / ".docs/experiments/runs/2026-09-08-draft9p4/reference/variables.json"
PLAN = ROOT / ".docs/robot-build-plan.md"
OUT = ROOT / ".docs/experiments/runs/2026-09-18-draft9p5/results"


def parent_rows():
    """The studio's rows as draft9p1p6 holds them, in order."""
    doc = json.loads(PARENT.read_text())
    return [{"name": v["name"], "type": v["type"], "expression": v["expression"],
             "description": v.get("description") or ""}
            for v in doc[0]["variables"]]


def asked_for():
    """Every `#name` the build plan's tables put a row against."""
    text = PLAN.read_text()
    names = set()
    for line in text.splitlines():
        m = re.match(r"\|\s*`#(\w+)`\s*\|", line)
        if m:
            names.add(m.group(1))
    return names


def main() -> int:
    rows = parent_rows()
    asked = asked_for()
    missing = [r["name"] for r in rows if r["name"] not in asked]
    if missing:
        raise RuntimeError(f"rows the build plan does not ask for: {missing}")
    print(f"{len(rows)} rows, every one of them a row the build plan asks for")

    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        print("signed in as", S.require_signed_in(page))
        path = f"/api/variables/d/{DID}/w/{WID}/e/{EID}/variables"

        before = S.api(page, "GET", path)
        held = (before["body"] or [{}])[0].get("variables") or []
        print(f"the tab holds {len(held)} rows before the write")

        for n in range(1, len(rows) + 1):
            res = S.api(page, "POST", path, rows[:n])
            if not res["ok"]:
                raise RuntimeError(f"row {rows[n - 1]['name']!r} was refused: "
                                   f"{json.dumps(res)[:300]}")
            S.pace(page, 150)
        print(f"wrote {len(rows)} rows, as {len(rows)} growing prefixes")

        # Ring 1: read it back and compare, row by row.
        after = S.api(page, "GET", path)
        got = (after["body"] or [{}])[0].get("variables") or []
        print(f"read back {len(got)} rows")
        wrote = {r["name"]: r["expression"] for r in rows}
        read = {v["name"]: v["expression"] for v in got}
        if read != wrote:
            for name in sorted(set(wrote) | set(read)):
                if wrote.get(name) != read.get(name):
                    print(f"  differs: #{name} sent {wrote.get(name)!r} "
                          f"read {read.get(name)!r}")
            raise RuntimeError("the rows read back are not the rows sent")
        order_sent = [r["name"] for r in rows]
        order_read = [v["name"] for v in got]
        if order_sent != order_read:
            raise RuntimeError(f"order differs: sent {order_sent}, read {order_read}")
        print("every row read back with the expression it was sent, in the same order")

        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / "robot-sizes.variables.json").write_text(json.dumps(got, indent=2) + "\n")
        print(f"wrote {OUT / 'robot-sizes.variables.json'}")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
