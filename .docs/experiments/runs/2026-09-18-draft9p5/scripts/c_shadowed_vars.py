#!/usr/bin/env python3
"""Every Part Studio variable that redeclares a name the Variable Studio holds.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/c_shadowed_vars.py

The `onshape` skill's rule: **do not redeclare a Variable Studio name inside a
Part Studio.** The local shadows the studio's row, so the tab goes on using its
own value, the row moves without it, and nothing turns red.

`/api/variables/.../variables` answers while `/features` is refused, and it gives
each tab's own rows with their expressions. Comparing the studio's names against
each tab's names is the whole check; where a name appears in both, the expression
on each side says whether the two agree today, which is a different question from
whether the tab is following the row.
"""

from __future__ import annotations

import sys

from playwright.sync_api import sync_playwright

from stickbot import make_plans as P
from stickbot import onshape_session as api

DID, WID = "2f08b54d795df0ee6b72e321", "1d8e4c837228c90bab9ff062"
STUDIO = ("robot sizes", "3d67f51a630c05c2b5d0b9ea")
TABS = [("ball and socket", "1a8322899842a1934e85851d"),
        ("hinge", "db0ef2ae9777492e7b242acf"),
        ("body", "5441067befc71f1e3b91482e"),
        ("head", "303898bd4ba38fc3957b0a21"),
        ("foot", "229aa0900e5a7e7aa4768c6f"),
        ("u limb", "fc89b8128993be73a0c9f092"),
        ("l limb", "be3bd8b485e32946c24ed799"),
        ("gripper", "a3a4fac68ffb7372a7803003")]


def rows(page, eid):
    """This element's own variable rows, as name to expression."""
    r = api._raw_api(page, "GET", f"/api/variables/d/{DID}/w/{WID}/e/{eid}/variables")
    if r["status"] != 200:
        return {}, r["status"]
    got = {}
    for table in r["body"]:
        for v in table.get("variables", []):
            got[v.get("name")] = v.get("expression")
    return got, 200


def main() -> int:
    with sync_playwright() as pw:
        browser, ctx, page = api.connect(pw)
        studio, status = rows(page, STUDIO[1])
        print(f"{STUDIO[0]}: {len(studio)} rows  (status {status})")
        shadowed = []
        for tab, eid in TABS:
            local, status = rows(page, eid)
            clash = sorted(set(local) & set(studio))
            print(f"\n{tab}: {len(local)} local rows, {len(clash)} redeclare a studio row")
            for name in clash:
                same = local[name] == studio[name]
                print(f"    #{name:<10} tab: {local[name]!r}")
                print(f"     {'':<11} studio: {studio[name]!r}"
                      f"   {'same expression' if same else 'DIFFERENT'}")
                shadowed.append((tab, name, local[name], studio[name], same))
        print("\nwhat each disagreeing pair resolves to, with #torsoH"
              f" = {P.TORSO_H} mm:")
        for tab, name, loc, stud, same in shadowed:
            if not same:
                print(f"    {tab} #{name}: tab {loc}, studio {stud}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
