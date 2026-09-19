#!/usr/bin/env python3
"""Phase A0 — set `stickbot-draft9p5`'s workspace length unit to millimeters.

A new Onshape document is in inches, and there is no REST endpoint for workspace
units: `/api/documents/d/{did}/w/{wid}/documentsettings` and the two other paths
tried on 2026-09-18 are all 404. So this is a GUI drive, and it is the one dialog
built from real `select` elements, which is why `select_option` works here and
nowhere else.

Geometry is unaffected either way, because every expression this draft posts
carries its own unit. What the unit decides is what a reader sees: in inches the
Variable Studio shows `48 mm` back as `1.89 in`.

The green tick commits and the red cross discards silently, so the value is read
back from a freshly opened dialog rather than from the one that was typed into.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/a0_units.py
"""

from __future__ import annotations

import sys

from playwright.sync_api import sync_playwright

from stickbot import onshape_gui as gui
from stickbot import onshape_session as S

DOC = S.Doc("2f08b54d795df0ee6b72e321", "1d8e4c837228c90bab9ff062",
            "3d67f51a630c05c2b5d0b9ea")
LENGTH_UNIT = "Millimeter"
DECIMALS = "0.12345"


def open_units(page):
    """The hamburger left of the document name, then Workspace units."""
    page.click(".nav-hamburger-menu")
    page.wait_for_timeout(1200)
    page.locator("text=Workspace units").first.click()
    page.wait_for_timeout(1800)
    if page.locator("select:visible").count() < 2:
        raise RuntimeError("Workspace units dialog did not open")


def read_length(page):
    """The Length default unit and its display decimals, as the dialog holds them."""
    return page.evaluate("""() => {
        const s = [...document.querySelectorAll('select')].filter(
            e => e.getBoundingClientRect().width > 0);
        return [s[0].options[s[0].selectedIndex].label,
                s[1].options[s[1].selectedIndex].label];
    }""")


def tick(page):
    """The green tick at the dialog's top right; the cross beside it discards."""
    box = page.evaluate("""() => {
        const w = document.querySelector('.feature-dialog-wrapper');
        const icons = [...w.querySelectorAll('svg')].map(e => e.getBoundingClientRect())
            .filter(r => r.width > 20 && r.top < w.getBoundingClientRect().top + 30)
            .sort((a, b) => a.x - b.x);
        const r = icons[0];
        return [Math.round(r.x + r.width / 2), Math.round(r.y + r.height / 2)];
    }""")
    page.mouse.click(box[0], box[1])
    page.wait_for_timeout(1500)
    return box


def main() -> int:
    with sync_playwright() as p:
        browser, _ctx, page = gui.connect(p)
        gui.open_doc(page, DOC)
        gui.no_banner(page)

        open_units(page)
        before = read_length(page)
        print("before:", before)

        page.locator("select:visible").nth(0).select_option(label=LENGTH_UNIT)
        page.wait_for_timeout(400)
        page.locator("select:visible").nth(1).select_option(label=DECIMALS)
        page.wait_for_timeout(400)
        typed = read_length(page)
        print("typed: ", typed)
        print("ticked at", tick(page))

        # Read it back out of a dialog opened again, not the one just typed into.
        gui.open_doc(page, DOC)
        gui.no_banner(page)
        open_units(page)
        after = read_length(page)
        print("after: ", after)
        if after != [LENGTH_UNIT, DECIMALS]:
            raise RuntimeError(f"workspace units read back as {after}")
        print(f"read back from a fresh dialog: {after[0]}, {after[1]}")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
