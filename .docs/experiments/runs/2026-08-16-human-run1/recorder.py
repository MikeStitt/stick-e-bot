#!/usr/bin/env python3
"""Watch a person follow the guide, and keep what they did.

Attaches to the browser `human_browser.py` opened (port 9224) and records three
streams into one directory:

    events.jsonl   every pointer, key, dialog and feature-tree change, stamped
    frames/        the frame just before each accept, and the one just after
    session.json   when it started, what it was pointed at, what it saw

The frames come from a rolling screencast buffer rather than a screenshot taken when
something happens, because the interesting frame is the one from *before* the click —
by the time an accept is observable, the dialog is already gone. A four-second buffer
at the measured 52 fps holds it comfortably; see `phase0-findings.md`.

    python recorder.py                      # record until Ctrl-C
    python recorder.py --out somewhere/      # choose the directory

Nothing here drives the browser. It reads.
"""

from __future__ import annotations

import base64
import json
import re
import signal
import sys
import time
from collections import deque
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).parent))
import human_browser as hb  # noqa: E402

HERE = Path(__file__).parent
CAPTURE_JS = HERE / "capture.js"
ONSHAPE = "https://cad.onshape.com"

BUFFER_S = 4.0        # how far back the frame buffer reaches
BEFORE_S = 0.35       # how far before an event the "before" frame is taken from
AFTER_S = 1.20        # how long after it to wait for the "after" frame
DRAIN_MS = 200        # how often the page's ring buffer is emptied
STALL_S = 3.0         # no frames for this long means the screencast needs restarting
SUMMARY_S = 5.0       # how often session.json is refreshed, so a hard kill loses little

# The moments worth keeping a picture of. Everything else is in events.jsonl.
WORTH_A_FRAME = {
    "feature-added", "feature-removed", "dialog-error", "tree-errors",
    "note", "step", "dialog-open", "dialog-close",
}


def worth_a_frame(ev: dict) -> str | None:
    """The label for a frame pair, or None to keep no picture of this event."""
    kind = ev.get("kind")
    if kind in WORTH_A_FRAME:
        names = ev.get("names") or ([ev["was"]] if ev.get("was") else [])
        tail = names[0] if names else (ev.get("title") or ev.get("text") or "")
        return f"{kind}-{tail}" if tail else kind
    if kind == "click":
        role = (ev.get("el") or {}).get("role")
        if role in ("dialog-ok", "dialog-cancel"):
            return role
    return None


def slug(what: str) -> str:
    keep = [c.lower() if c.isalnum() else "-" for c in what]
    return "".join(keep).strip("-").replace("--", "-")[:46] or "frame"


class Tab:
    """One Onshape page: its frame buffer, its screencast, its pending after-shots."""

    def __init__(self, page, index: int, out: Path, log):
        self.page = page
        self.index = index
        self.out = out
        self.log = log
        self.frames: deque[tuple[float, bytes]] = deque()
        self.pending: list[tuple[float, str]] = []
        self.last_frame = 0.0
        self.cdp = None
        self.n = 0

    # ---- the screencast ----------------------------------------------------

    def _on_frame(self, ev) -> None:
        now = time.time()
        self.frames.append((now, base64.b64decode(ev["data"])))
        self.last_frame = now
        cutoff = now - BUFFER_S
        while self.frames and self.frames[0][0] < cutoff:
            self.frames.popleft()
        try:
            self.cdp.send("Page.screencastFrameAck", {"sessionId": ev["sessionId"]})
        except Exception:
            pass  # the tab may be navigating; the next frame re-establishes it

    def start_screencast(self, ctx) -> None:
        try:
            if self.cdp is None:
                self.cdp = ctx.new_cdp_session(self.page)
                self.cdp.on("Page.screencastFrame", self._on_frame)
            self.cdp.send("Page.startScreencast", {
                "format": "jpeg", "quality": 70,
                "maxWidth": 1600, "maxHeight": 1000, "everyNthFrame": 1,
            })
            self.last_frame = time.time()
        except Exception as exc:
            self.log("screencast", {"tab": self.index, "error": str(exc)[:120]})

    def nearest(self, when: float) -> bytes | None:
        """The buffered frame closest to a moment, or None if it has aged out."""
        if not self.frames:
            return None
        return min(self.frames, key=lambda f: abs(f[0] - when))[1]

    # ---- writing pictures --------------------------------------------------

    def write(self, png: bytes, label: str) -> str:
        self.n += 1
        name = f"{self.index}-{self.n:04d}-{slug(label)}.jpg"
        (self.out / name).write_bytes(png)
        return name

    def keep_pair(self, at: float, label: str) -> str | None:
        before = self.nearest(at - BEFORE_S)
        name = self.write(before, f"before-{label}") if before else None
        self.pending.append((at + AFTER_S, label))
        return name

    def settle_pending(self) -> None:
        now = time.time()
        still = []
        for due, label in self.pending:
            if now < due:
                still.append((due, label))
                continue
            frame = self.nearest(due)
            if frame:
                self.write(frame, f"after-{label}")
        self.pending = still


class Recorder:
    def __init__(self, out: Path):
        self.out = out
        self.frames_dir = out / "frames"
        self.frames_dir.mkdir(parents=True, exist_ok=True)
        self.events = (out / "events.jsonl").open("a", buffering=1)
        self.script = CAPTURE_JS.read_text()
        # One source for the version: the number in the file it belongs to.
        self.version = int(re.search(r"version:\s*(\d+)", self.script).group(1))
        self.tabs: dict[int, Tab] = {}
        self.counts: dict[str, int] = {}
        self.started = time.time()
        self.last_summary = 0.0

    def log(self, kind: str, data: dict) -> None:
        rec = {"t": round(time.time(), 3), "kind": kind, **data}
        self.events.write(json.dumps(rec, ensure_ascii=False) + "\n")
        self.counts[kind] = self.counts.get(kind, 0) + 1

    # ---- tabs --------------------------------------------------------------

    def adopt(self, page, ctx) -> Tab | None:
        if not page.url.startswith(ONSHAPE):
            return None
        for tab in self.tabs.values():
            if tab.page is page:
                return tab
        tab = Tab(page, len(self.tabs) + 1, self.frames_dir, self.log)
        self.tabs[id(page)] = tab
        try:
            stale = page.evaluate(
                "(want) => window.__hrec && window.__hrec.version !== want",
                self.version)
            if stale:
                # An older capture is already listening and cannot be unhooked.
                page.reload(wait_until="domcontentloaded")
                page.wait_for_timeout(6000)
                self.log("reloaded", {"tab": tab.index, "why": "older capture in the page"})
                print("reloaded the tab to pick up a newer capture.js", flush=True)
            else:
                page.evaluate(self.script)      # the page already open
        except Exception as exc:
            self.log("inject", {"tab": tab.index, "error": str(exc)[:120]})
        page.on("framenavigated", lambda fr: self.on_nav(tab, fr))
        tab.start_screencast(ctx)
        self.log("tab-added", {"tab": tab.index, "url": page.url[:120]})
        print(f"recording tab {tab.index}: {page.url[:80]}", flush=True)
        return tab

    def on_nav(self, tab: Tab, frame) -> None:
        if frame != tab.page.main_frame:
            return
        tab.frames.clear()
        self.log("navigated", {"tab": tab.index, "url": frame.url[:120]})

    # ---- the loop ----------------------------------------------------------

    def drain(self, tab: Tab, ctx) -> None:
        try:
            events = tab.page.evaluate("() => window.__hrec ? window.__hrec.drain() : null")
        except Exception:
            return  # mid-navigation; the next tick picks it up
        if events is None:
            try:
                tab.page.evaluate(self.script)   # navigation dropped the capture
                self.log("reinjected", {"tab": tab.index})
            except Exception:
                pass
            return
        for ev in events:
            ev["tab"] = tab.index
            label = worth_a_frame(ev)
            if label:
                name = tab.keep_pair(ev["t"] / 1000.0, label)
                if name:
                    ev["before"] = name
            rec = {"t": round(ev.pop("t") / 1000.0, 3), **ev}
            self.events.write(json.dumps(rec, ensure_ascii=False) + "\n")
            self.counts[ev["kind"]] = self.counts.get(ev["kind"], 0) + 1
            if ev["kind"] in ("note", "step", "dialog-error"):
                print(f"  {ev['kind']}: {ev.get('text') or ev.get('error') or ev.get('step')}",
                      flush=True)

    def tick(self, ctx) -> None:
        for page in list(ctx.pages):
            if not page.is_closed():
                self.adopt(page, ctx)
        for tab in list(self.tabs.values()):
            if tab.page.is_closed():
                continue
            self.drain(tab, ctx)
            tab.settle_pending()
            if time.time() - tab.last_frame > STALL_S:
                tab.start_screencast(ctx)
        if time.time() - self.last_summary > SUMMARY_S:
            self.write_summary()

    def write_summary(self) -> dict:
        """Kept current on a timer, not only at the end.

        A recorder is stopped by whatever is to hand, and not every way of stopping it
        runs the exit path. events.jsonl survives regardless because it is line
        buffered; this makes the summary survive too.
        """
        summary = {
            "started": self.started,
            "seconds": round(time.time() - self.started, 1),
            "counts": self.counts,
            "frames": len(list(self.frames_dir.glob("*.jpg"))),
        }
        (self.out / "session.json").write_text(json.dumps(summary, indent=2) + "\n")
        self.last_summary = time.time()
        return summary

    def finish(self) -> None:
        summary = self.write_summary()
        self.events.close()
        print("\n--- what was recorded ---")
        for kind, n in sorted(summary["counts"].items(), key=lambda kv: -kv[1]):
            print(f"  {n:6d}  {kind}")
        print(f"  {summary['frames']:6d}  frames")
        print(f"\n{self.out}")


def main() -> int:
    out = Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else \
        HERE / "capture" / time.strftime("%Y-%m-%d-%H%M%S")

    # A kill signal must land in the same place Ctrl-C does, or the summary is never
    # written and the frames' pending after-shots are dropped on the floor.
    signal.signal(signal.SIGTERM, lambda *_: (_ for _ in ()).throw(KeyboardInterrupt))

    rec = Recorder(out)
    with sync_playwright() as p:
        browser, ctx, page = hb.connect(p)
        ctx.add_init_script(rec.script)          # every page opened from here on
        rec.adopt(page, ctx)
        print(f"writing to {out}")
        print("F8 marks the next step, F9 writes a note. Ctrl-C stops.", flush=True)
        try:
            while True:
                rec.tick(ctx)
                time.sleep(DRAIN_MS / 1000.0)
        except KeyboardInterrupt:
            print("\nstopping")
        finally:
            for tab in rec.tabs.values():
                try:
                    tab.settle_pending()
                    if tab.cdp:
                        tab.cdp.send("Page.stopScreencast")
                except Exception:
                    pass
            rec.finish()
            browser.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
