#!/usr/bin/env python3
"""Turn the session transcript into the conversation report: rst, HTML and PDF.

The transcript is Claude Code's own record of the session, one JSON object per
line, with a timestamp on every message and token usage on every reply. It lives
outside the repository, so its path is an argument. The report covers the session
from its first message to Claude's answer to *Please take a note of this time and
message.*, and nothing after.

Every time, tool call and token count in the report is read from the transcript;
none is typed. The document's ids come from `ids.json`.

The PDF is Chromium printing the built HTML, because no LaTeX is installed here.

    uv run python .docs/experiments/2026-09-30-elephant-cup/report/make_report.py \
        ~/.claude/projects/<project>/<session>.jsonl
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from playwright.sync_api import sync_playwright

from stickbot import repo_root

HERE = Path(__file__).parent
SOURCE = HERE / "source"
HTML = HERE / "html"
PDF = HERE / "elephant-cup-conversation.pdf"
IDS = json.loads((HERE.parent / "ids.json").read_text())
VERSION = ("cup, 12 fl oz with 1 fl oz headroom", "1f0631a4e8285baf2d33f860")
WORKSPACE = ("Main", IDS["wid"])
COMMIT_AT = datetime.fromisoformat(subprocess.run(
    ["git", "show", "-s", "--format=%cI", "1fba2b3"], capture_output=True, text=True,
    check=True, cwd=repo_root()).stdout.strip())
LAST_MESSAGE = "Please take a note of this time and message."
ZONE = ZoneInfo("America/New_York")
REPO = str(repo_root()) + "/"
HOME = str(Path.home())


# ---------------------------------------------------------------- the record


@dataclass
class Action:
    at: datetime
    tool: str
    what: str
    detail: str = ""
    result: str = ""
    error: bool = False


@dataclass
class Message:
    at: datetime
    text: str


@dataclass
class Turn:
    at: datetime
    said: str
    shell: str = ""
    events: list = field(default_factory=list)
    ms: int = 0
    usage: dict = field(default_factory=dict)


def when(stamp: str) -> datetime:
    return datetime.fromisoformat(stamp.replace("Z", "+00:00")).astimezone(ZONE)


def short(path: str) -> str:
    path = path.replace(REPO, "")
    path = re.sub(r"/private/tmp/claude-\d+/[^/]+/[^/]+/", "session-tmp/", path)
    return path.replace(HOME, "~")


def first_line(text: str, limit: int, last: bool = False) -> str:
    lines = text.splitlines()
    for line in reversed(lines) if last else lines:
        if line.strip():
            line = short(line.strip())
            return line if len(line) <= limit else line[: limit - 1] + "…"
    return ""


def result_text(content) -> str:
    if isinstance(content, str):
        return content
    parts = []
    for c in content or []:
        if c.get("type") == "text":
            parts.append(c["text"])
        elif c.get("type") == "image":
            parts.append("(an image)")
    return "\n".join(parts)


def describe(name: str, args: dict) -> tuple[str, str]:
    """What a tool call did, in a line, and the command or path it acted on."""
    if name == "Bash":
        what = args.get("description", "")
        if args.get("run_in_background"):
            what += " (in the background)"
        return what, first_line(args.get("command", ""), 150)
    if name in ("Read", "Write", "Edit"):
        verb = {"Read": "Read", "Write": "Wrote", "Edit": "Edited"}[name]
        return f"{verb} a file", short(args.get("file_path", ""))
    if name == "Skill":
        return f"Loaded the {args.get('skill')} skill", ""
    return name, first_line(json.dumps(args), 150)


def is_real_user(row) -> bool:
    m = row.get("message") or {}
    return (row.get("type") == "user" and isinstance(m.get("content"), str)
            and not row.get("isMeta") and not row.get("isSidechain"))


def read_turns(path: Path) -> list[Turn]:
    rows = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    turns: list[Turn] = []
    pending: dict[str, Action] = {}
    usage: dict[str, dict] = {}
    for row in rows:
        if row.get("isSidechain"):
            continue
        kind = row.get("type")
        msg = row.get("message") or {}
        if is_real_user(row):
            text = msg["content"]
            if text.startswith("<bash-stdout>"):
                out = re.sub(r"</?bash-std(out|err)>", "", text)
                turns[-1].shell = out.replace("&lt;", "<").replace("&gt;", ">").strip()
                continue
            if turns and turns[-1].said == LAST_MESSAGE:
                break
            turns.append(Turn(when(row["timestamp"]), text))
            continue
        if not turns:
            continue
        turn = turns[-1]
        if kind == "system" and row.get("subtype") == "turn_duration":
            turn.ms += row.get("durationMs", 0)
        elif kind == "assistant":
            if msg.get("usage"):
                usage[msg["id"]] = msg["usage"]
                turn.usage[msg["id"]] = msg["usage"]
            for block in msg.get("content") or []:
                if block.get("type") == "text" and block["text"].strip():
                    turn.events.append(Message(when(row["timestamp"]), block["text"].strip()))
                elif block.get("type") == "tool_use":
                    what, detail = describe(block["name"], block.get("input") or {})
                    act = Action(when(row["timestamp"]), block["name"], what, detail)
                    pending[block["id"]] = act
                    turn.events.append(act)
        elif kind == "user":
            for block in msg.get("content") or []:
                if isinstance(block, dict) and block.get("type") == "tool_result":
                    act = pending.get(block.get("tool_use_id"))
                    if act:
                        act.error = bool(block.get("is_error"))
                        if act.error or act.tool == "Bash":
                            act.result = first_line(result_text(block.get("content")), 110,
                                                    last=not act.error)
    return turns


def totals(usages) -> dict:
    keys = ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens",
            "output_tokens")
    out = {k: sum(u.get(k, 0) for u in usages) for k in keys}
    out["thinking_tokens"] = sum((u.get("output_tokens_details") or {}).get("thinking_tokens", 0)
                                 for u in usages)
    out["replies"] = len(usages)
    return out


# ---------------------------------------------------------------- rst writing


def esc(text: str) -> str:
    """Plain text, safe in rst: every markup character backslash-escaped."""
    text = re.sub(r"([\\*`|_\[\]<>:])", r"\\\1", text)
    # A line of one repeated punctuation mark would read as a transition.
    return "\\" + text if re.fullmatch(r"(\W)\1+", text) else text


def inline(md: str) -> str:
    """The Markdown inline markup Claude's messages use, as rst."""
    parts = re.split(r"(`[^`]+`)", md)
    out = []
    for i, part in enumerate(parts):
        if i % 2:
            # An inline literal needs a space or punctuation on both sides.
            before = "\\ " if out and re.search(r"\w$", out[-1]) else ""
            after = "\\ " if i + 1 < len(parts) and re.match(r"\w", parts[i + 1]) else ""
            out.append(f"{before}``{part[1:-1]}``{after}")
            continue
        part = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"`\1 <\2>`__", part)
        part = part.replace("|", r"\|")
        part = re.sub(r"(\w)_(\s|$)", r"\1\\_\2", part)
        out.append(part)
    return "".join(out)


def md_table(lines: list[str], indent: str) -> list[str]:
    rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in lines]
    rows = [r for r in rows if not all(re.fullmatch(r":?-+:?", c) for c in r)]
    out = [f"{indent}.. list-table::", f"{indent}   :header-rows: 1",
           f"{indent}   :class: summary", ""]
    for r in rows:
        for j, c in enumerate(r):
            out.append(f"{indent}   {'* -' if j == 0 else '  -'} {inline(c) or ' '}")
    return out + [""]


def md_to_rst(md: str, indent: str) -> list[str]:
    """Headings, paragraphs, nested bullets, pipe tables and fenced code."""
    out: list[str] = []
    lines = md.splitlines()
    i = 0
    last_level = -1
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            j = i + 1
            block = []
            while j < len(lines) and not lines[j].strip().startswith("```"):
                block.append(lines[j])
                j += 1
            out += ["", f"{indent}.. code-block:: text", ""]
            out += [f"{indent}   {b}" for b in block] + [""]
            i = j + 1
            last_level = -1
            continue
        if line.lstrip().startswith("|"):
            j = i
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                j += 1
            out += [""] + md_table(lines[i:j], indent)
            i = j
            last_level = -1
            continue
        m = re.match(r"^(#+)\s+(.*)", line)
        if m:
            out += ["", f"{indent}.. rubric:: {inline(m.group(2))}", ""]
            i += 1
            last_level = -1
            continue
        m = re.match(r"^(\s*)- (.*)", line)
        if m:
            level = len(m.group(1)) // 2
            text = m.group(2)
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r"^\s*(- |\||#)",
                                                                       lines[i]):
                text += " " + lines[i].strip()
                i += 1
            if level != last_level:
                out.append("")
            out.append(f"{indent}{'  ' * level}- {inline(text)}")
            last_level = level
            continue
        if not line.strip():
            out.append("")
            i += 1
            continue
        para = [line.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^\s*(- |\||#|```)",
                                                                   lines[i]):
            para.append(lines[i].strip())
            i += 1
        out += ["", f"{indent}{inline(' '.join(para))}", ""]
        last_level = -1
    return out


def clock(t: datetime) -> str:
    return t.strftime("%H:%M:%S")


def minutes(ms: int) -> str:
    s = round(ms / 1000)
    h, m, s = s // 3600, s % 3600 // 60, s % 60
    return (f"{h} h {m} min {s} s" if h else f"{m} min {s} s" if m else f"{s} s")


def replies(k: int) -> str:
    return "1 reply" if k == 1 else f"{k} replies"


def n(x: int) -> str:
    return f"{x:,}"


# Quoted tool output is not prose: codespell skips a line carrying this marker, and the
# `hidden` role keeps the marker off the page.
QUOTED = " :hidden:`codespell:ignore`"


def actions_table(acts: list[Action]) -> list[str]:
    out = [".. list-table::", "   :header-rows: 1", "   :widths: 10 12 50 28",
           "   :class: actions", "", "   * - Time", "     - Tool", "     - What was done",
           "     - What came back"]
    for a in acts:
        what = esc(a.what) or " "
        detail = f"``{a.detail}``" if a.detail and "`" not in a.detail else esc(a.detail)
        result = ("**error:** " if a.error else "") + (esc(a.result) or " ")
        out += [f"   * - {clock(a.at)}", f"     - {a.tool}", f"     - {what}"]
        if detail:
            out += ["", f"       {detail}{QUOTED}"]
        out += [f"     - {result}{QUOTED if a.result else ''}"]
    return out + [""]


def turn_rst(turn: Turn) -> list[str]:
    title = f"{clock(turn.at)} EDT"
    out = [title, "-" * len(title), ""]
    u = totals(turn.usage.values())
    out += [f"*Working time {minutes(turn.ms)}; {replies(u['replies'])}; "
            f"{n(u['output_tokens'])} output tokens.*", ""]
    heading = "Mike, in the shell" if turn.shell else "Mike"
    out += [f".. admonition:: {heading}, {clock(turn.at)}", "   :class: from-mike", ""]
    if turn.shell:
        cmd = re.sub(r"</?bash-input>", "", turn.said)
        out += ["   .. code-block:: text", "", f"      $ {cmd}"]
        out += [f"      {ln}" for ln in turn.shell.splitlines()] + [""]
    else:
        out += [f"   {esc(ln) if ln.strip() else ''}" for ln in turn.said.splitlines()] + [""]
    acts: list[Action] = []
    for e in turn.events + [None]:
        if isinstance(e, Action):
            acts.append(e)
            continue
        if acts:
            out += actions_table(acts)
            acts = []
        if isinstance(e, Message):
            out += [f".. admonition:: Claude, {clock(e.at)}", "   :class: from-claude", ""]
            out += md_to_rst(e.text, "   ") + [""]
    return out


def document(turns: list[Turn]) -> str:
    start, end = turns[0].at, turns[-1].events[-1].at
    usages = [u for t in turns for u in t.usage.values()]
    u = totals(usages)
    fresh = u["input_tokens"] + u["cache_creation_input_tokens"]
    calls = sum(isinstance(e, Action) for t in turns for e in t.events)
    work = sum(t.ms for t in turns)
    did = IDS["did"]
    title = "elephant cup: the conversation"
    out = [".. role:: hidden", "", "=" * len(title), title, "=" * len(title), "",
           f"The session of {start:%Y-%m-%d} on branch ``elephant``, from Mike's first message "
           f"to Claude's answer to *{LAST_MESSAGE}* Every time, message, tool call and token "
           "count below is read from Claude Code's transcript of the session by "
           "``make_report.py``. Times are Eastern Daylight Time.", "",
           ".. figure:: cup-isometric.png", "   :class: cup", "   :align: center",
           "   :alt: The cup, isometric", "",
           f"   The cup, isometric, rendered by Onshape from the named version "
           f"“{VERSION[0]}”.", "",
           "Where the work is", "=================", "",
           ".. list-table::", "   :widths: 28 72", "   :class: summary", "",
           "   * - Onshape document", f"     - ``{IDS['document']}``, id ``{did}``",
           "   * - Workspace", f"     - ``{WORKSPACE[0]}``, id ``{WORKSPACE[1]}``",
           "   * - Part Studio", f"     - ``cup``, element ``{IDS['eid']}``, one part ``Cup``",
           "   * - Named version", f"     - “{VERSION[0]}”, id ``{VERSION[1]}``",
           "   * - Version link",
           f"     - https://cad.onshape.com/documents/{did}/v/{VERSION[1]}",
           "   * - Git", "     - branch ``elephant``, commit ``1fba2b3``, pushed to ``origin``",
           "   * - Repository record",
           "     - ``.docs/experiments/2026-09-30-elephant-cup/README.md``", "",
           "The session", "===========", "",
           ".. list-table::", "   :widths: 28 72", "   :class: summary", "",
           "   * - Model", "     - Claude Opus 5.5 (``claude-opus-5-5``), effort ``high``, "
           "both as the transcript records them",
           "   * - Started", f"     - {start:%Y-%m-%d %H:%M:%S} EDT",
           "   * - Ended", f"     - {end:%Y-%m-%d %H:%M:%S} EDT",
           "   * - Elapsed", f"     - {minutes(int((end - start).total_seconds() * 1000))}, "
           "most of it waiting on Mike between messages",
           "   * - Claude working", f"     - {minutes(work)}, the sum of the turn durations",
           "   * - Messages from Mike", f"     - {len(turns)}",
           "   * - Tool calls", f"     - {calls}",
           "   * - Replies from the model", f"     - {u['replies']}",
           "   * - Output tokens",
           f"     - {n(u['output_tokens'])}, of which {n(u['thinking_tokens'])} were thinking",
           "   * - Input tokens, new", f"     - {n(fresh)} "
           f"({n(u['input_tokens'])} uncached, {n(u['cache_creation_input_tokens'])} "
           "written to the cache)",
           "   * - Input tokens, from cache", f"     - {n(u['cache_read_input_tokens'])}",
           "   * - Input tokens, all",
           f"     - {n(fresh + u['cache_read_input_tokens'])}", "",
           "Each reply sends the whole conversation so far as input, so the input total counts "
           "the same early context once per reply; most of it is served from the cache. The "
           "counts cover the main session only. No subagent was started.", "",
           "The timeline", "============", "",
           "One section per message from Mike. Each opens with his message, then Claude's "
           "tool calls and messages in the order they happened. What came back is the last "
           "line a shell command printed, or the first line of an error, cut short where it is "
           "long. Paths under the session's temporary directory are shortened to "
           "``session-tmp/``.", ""]
    for t in turns:
        out += turn_rst(t)
    note = turns[-1]
    gap = (note.at - COMMIT_AT).total_seconds()
    out += ["A correction", "============", "",
            "Claude's last reply says the message came in at 16:18:44 EDT, 47 s after the "
            "commit. 16:18:44 EDT is when Claude read the clock. The transcript records the "
            f"message at {clock(note.at)} EDT, {gap:.0f} s after commit ``1fba2b3`` at "
            f"{clock(COMMIT_AT)} EDT.", ""]
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- building


def build_html():
    with tempfile.TemporaryDirectory() as doctrees:
        subprocess.run([sys.executable, "-m", "sphinx", "-q", "-E", "-b", "html",
                        "-d", doctrees, str(SOURCE), str(HTML)], check=True)
    (HTML / ".buildinfo").unlink(missing_ok=True)
    (HTML / ".buildinfo.bak").unlink(missing_ok=True)


def build_pdf():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto((HTML / "index.html").resolve().as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")
        page.pdf(path=str(PDF), format="Letter", print_background=True,
                 margin={"top": "0.6in", "bottom": "0.6in", "left": "0.6in",
                         "right": "0.6in"})
        browser.close()


def main() -> int:
    turns = read_turns(Path(sys.argv[1]).expanduser())
    if turns[-1].said != LAST_MESSAGE:
        raise RuntimeError(f"the transcript has no message {LAST_MESSAGE!r}")
    (SOURCE / "index.rst").write_text(document(turns))
    print("wrote", SOURCE / "index.rst")
    build_html()
    print("built", HTML / "index.html")
    build_pdf()
    print("printed", PDF, f"{PDF.stat().st_size / 1024:.0f} KiB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
