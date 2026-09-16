"""A screencast of the agent's own browser, written frame by frame.

The steps this exists for have no dialog and no green tick, so a still taken after
the fact does not show what the pointer was doing when the manipulator appeared. CDP's
screencast does: every frame lands on disk with the time it arrived, and `mark()`
writes a line into the same clock so a moment can be found again.

CDP emits a frame only when the page changes, so these are **event frames, not a frame
rate**: one run 8p1 stage holds 220 of them across 13.9 s, three inside the first 97 ms
and one gap of 6.6 s. `render()` keeps that timing rather than resampling, so the video
runs at the speed the build actually ran.

Frames stay wherever the caller puts them — they are raw material and there are
thousands. The mp4 is what a guide ships, and at this frame rate a stage comes out
around a tenth of a megabyte.
"""

from __future__ import annotations

import base64
import json
import subprocess
import time
from pathlib import Path

# The tail of the last frame, which has no successor to measure against.
LAST_FRAME_SECONDS = 0.5


class Screencast:
    """Start recording on construction; `stop(dest)` writes the mp4."""

    def __init__(self, ctx, page, out, quality: int = 80):
        # Run 8 pointed five separate runs of one stage script at the same directory
        # and every one of them started numbering at 00001, so the folder held five
        # interleaved timelines and sorting it produced a 9.7 s step backwards. A
        # rerun gets its own directory.
        out = Path(out)
        n = 1
        while out.exists() and any(out.iterdir()):
            n += 1
            out = out.parent / f"{Path(out).name.split('~')[0]}~{n}"
        self.out = out
        (self.out / "frames").mkdir(parents=True, exist_ok=True)
        self.page = page
        self.n = 0
        self.t0 = time.time()
        self.marks: list[dict] = []
        self.cdp = ctx.new_cdp_session(page)
        self.cdp.on("Page.screencastFrame", self._frame)
        self.cdp.send("Page.startScreencast", {
            "format": "jpeg", "quality": quality,
            "maxWidth": 1600, "maxHeight": 1000, "everyNthFrame": 1,
        })

    def _frame(self, ev):
        self.n += 1
        t = time.time() - self.t0
        (self.out / "frames" / f"{self.n:05d}-{t:08.3f}.jpg").write_bytes(
            base64.b64decode(ev["data"]))
        try:
            self.cdp.send("Page.screencastFrameAck", {"sessionId": ev["sessionId"]})
        except Exception:
            pass

    def mark(self, what: str):
        """Write a moment into the recording's clock, and say it on the transcript."""
        t = time.time() - self.t0
        self.marks.append({"t": round(t, 3), "frame": self.n, "what": what})
        print(f"   [{t:7.2f}s  frame {self.n:5d}]  {what}")

    def stop(self, dest=None):
        try:
            self.cdp.send("Page.stopScreencast")
        except Exception:
            pass
        (self.out / "marks.json").write_text(json.dumps(self.marks, indent=1))
        print(f"   {self.n} frames -> {self.out}")
        if dest is not None:
            return render(self.out, dest)
        return None


def _ffmpeg() -> str:
    """The ffmpeg binary. `imageio-ffmpeg` ships one, so nothing has to be installed
    system-wide just to encode a build's screencast."""
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        return "ffmpeg"


def _timeline(frames_dir):
    """Every frame with the time it should hold the screen for.

    Frames are ordered by sequence number, not by name: the time in the name is for
    reading, and sorting on it puts 10.0 s before 9.0 s.

    Consecutive frames with identical bytes fold into the first of them. CDP sent
    three inside 97 ms at the start of every run 8 session, and encoding all three
    writes the same picture three times.
    """
    fs = sorted(Path(frames_dir).iterdir(), key=lambda p: int(p.name.split("-")[0]))
    if not fs:
        return []
    stamps = [float(p.stem.split("-")[1]) for p in fs]
    out, last = [], None
    for p, t in zip(fs, stamps):
        b = p.read_bytes()
        if b == last:
            continue
        last = b
        out.append([p, t, 0.0])
    back = [(a[0].name, b[0].name) for a, b in zip(out, out[1:]) if b[1] < a[1]]
    if back:
        raise RuntimeError(
            f"time runs backwards in {frames_dir} at {back[0]} and {len(back) - 1} "
            "other places: the folder holds more than one run. Each recording writes "
            "its own directory now, but folders written before that fix cannot be "
            "untangled — re-record rather than encode this one.")
    for i, r in enumerate(out):
        nxt = out[i + 1][1] if i + 1 < len(out) else r[1] + LAST_FRAME_SECONDS
        r[2] = round(max(nxt - r[1], 0.001), 3)
    return out


def render(session_dir, dest, crf: int = 28):
    """Encode one session's event frames to mp4, at the speed it happened.

    ffmpeg's concat demuxer takes a duration per frame, which is what keeps the
    original timing without inventing frames to fill the gaps.
    """
    session_dir, dest = Path(session_dir), Path(dest)
    rows = _timeline(session_dir / "frames")
    if not rows:
        print(f"   no frames in {session_dir}")
        return None
    listing = session_dir / "concat.txt"
    lines = []
    for p, _t, dur in rows:
        lines.append(f"file '{p.resolve()}'")
        lines.append(f"duration {dur}")
    lines.append(f"file '{rows[-1][0].resolve()}'")   # concat needs the tail repeated
    listing.write_text("\n".join(lines) + "\n")

    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = [_ffmpeg(), "-y", "-f", "concat", "-safe", "0", "-i", str(listing),
           "-fps_mode", "vfr", "-pix_fmt", "yuv420p", "-c:v", "libx264",
           "-crf", str(crf), "-movflags", "+faststart", str(dest)]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError:
        print("   ffmpeg is not installed; frames kept, no video written")
        return None
    if r.returncode:
        print(f"   ffmpeg failed:\n{r.stderr[-800:]}")
        return None
    span = rows[-1][1] - rows[0][1] + LAST_FRAME_SECONDS
    print(f"   {len(rows)} frames, {span:.1f}s -> {dest} "
          f"({dest.stat().st_size / 1e6:.1f} MB)")
    return dest
