"""Side-by-side diff of two prose documents, ignoring where the lines were wrapped.

The same paragraph wrapped at 80 columns and at 100 differs on every line, so an
ordinary diff of two hand-wrapped documents buries the real edits under
reflowing. This joins each paragraph, list item, table row and heading back into
one logical block, matches the blocks, and only then re-wraps for display — so a
difference shown on screen is a difference in the words.

Blocks that changed are paired and the changed *words* are highlighted inside
them, rather than the whole block being reported as a delete plus an insert.

Usage:
    python3 tools/prose_diff.py OLD NEW [--width N]
    python3 tools/prose_diff.py OLD NEW | less -R      # -R keeps the color
    python3 tools/prose_diff.py OLD NEW --html out.html
"""

import argparse
import difflib
import html
import re
import shutil
import sys

RESET = "\033[0m"
STYLE = {
    "del": "\033[31m",  # whole block only on the left
    "add": "\033[32m",  # whole block only on the right
    "wdel": "\033[41;97m",  # word dropped
    "wadd": "\033[42;30m",  # word added
    "hdr": "\033[1;36m",  # heading, unchanged
    "rule": "\033[2m",
}

LIST_RE = re.compile(r"^\s*([-*+]|\d+[.)])\s+")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
# Two blocks are the same block edited, rather than one dropped and another
# added, above this similarity. Below it they read as unrelated text.
PAIR_THRESHOLD = 0.45


def blocks(path: str) -> list[str]:
    """One string per heading, paragraph, list item, table row or code line."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    out: list[str] = []
    buf: list[str] = []

    def flush() -> None:
        if buf:
            out.append(" ".join(s.strip() for s in buf))
            buf.clear()

    in_fence = False
    for line in lines:
        if FENCE_RE.match(line):
            flush()
            out.append(line.rstrip())
            in_fence = not in_fence
            continue
        if in_fence:
            out.append(line.rstrip())
            continue
        stripped = line.strip()
        if not stripped:
            flush()
        elif stripped.startswith("#") or stripped.startswith("|"):
            flush()
            out.append(stripped)
        elif LIST_RE.match(line):
            flush()
            buf.append(line.rstrip())
        else:
            buf.append(line)
    flush()
    return out


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def pair_replace(left: list[str], right: list[str]) -> list[tuple]:
    """Match edited blocks within a region difflib called wholly different."""
    matches: dict[int, int] = {}
    last = -1
    for li, lblock in enumerate(left):
        best, best_ratio = None, PAIR_THRESHOLD
        for ri in range(last + 1, len(right)):
            ratio = difflib.SequenceMatcher(None, norm(lblock), norm(right[ri])).ratio()
            if ratio > best_ratio:
                best, best_ratio = ri, ratio
        if best is not None:
            matches[li] = best
            last = best

    out, li, ri = [], 0, 0
    while li < len(left) or ri < len(right):
        if li < len(left) and li in matches:
            while ri < matches[li]:
                out.append((None, right[ri], "add"))
                ri += 1
            out.append((left[li], right[ri], "chg"))
            li, ri = li + 1, ri + 1
        elif li < len(left):
            out.append((left[li], None, "del"))
            li += 1
        else:
            out.append((None, right[ri], "add"))
            ri += 1
    return out


def align(a: list[str], b: list[str]) -> list[tuple]:
    na, nb = [norm(x) for x in a], [norm(x) for x in b]
    pairs: list[tuple] = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, na, nb, autojunk=False).get_opcodes():
        if tag == "equal":
            pairs += [(a[i1 + k], b[j1 + k], "equal") for k in range(i2 - i1)]
        elif tag == "delete":
            pairs += [(a[k], None, "del") for k in range(i1, i2)]
        elif tag == "insert":
            pairs += [(None, b[k], "add") for k in range(j1, j2)]
        else:
            pairs += pair_replace(a[i1:i2], b[j1:j2])
    return pairs


def styled_words(left: str | None, right: str | None, kind: str) -> tuple[list, list]:
    """(word, style) for each side, with the changed words marked."""
    if kind == "equal":
        style = "hdr" if left.startswith("#") else None
        words = [(w, style) for w in left.split()]
        return words, list(words)
    if kind == "del":
        return [(w, "del") for w in left.split()], []
    if kind == "add":
        return [], [(w, "add") for w in right.split()]

    lw, rw = left.split(), right.split()
    lt, rt = [], []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, lw, rw, autojunk=False).get_opcodes():
        lt += [(w, None if tag == "equal" else "wdel") for w in lw[i1:i2]]
        rt += [(w, None if tag == "equal" else "wadd") for w in rw[j1:j2]]
    return lt, rt


def wrap(words: list[tuple], width: int, indent: int) -> list[list[tuple]]:
    lines: list[list[tuple]] = []
    cur: list[tuple] = []
    used = 0
    for word, style in words:
        room = width - (indent if lines else 0)
        while len(word) > room:  # a URL longer than the column
            head, word = word[:room], word[room:]
            if cur:
                lines.append(cur)
            lines.append([(head, style)])
            cur, used, room = [], 0, width - indent
        if cur and used + 1 + len(word) > room:
            lines.append(cur)
            cur, used = [], 0
        if cur:
            cur.append((" ", None))
            used += 1
        cur.append((word, style))
        used += len(word)
    if cur:
        lines.append(cur)
    return lines


def emit(line: list[tuple], width: int, indent: int, first: bool) -> str:
    pad = "" if first else " " * indent
    text = "".join(f"{STYLE[s]}{w}{RESET}" if s else w for w, s in line)
    visible = len("".join(w for w, _ in line)) + len(pad)
    return pad + text + " " * max(0, width - visible)


CSS = """
:root {
  --bg: #fdfdfc; --fg: #23211d; --rule: #ddd9d2; --muted: #7a746a;
  --gone-bg: #fdeceb; --gone-fg: #8a2b21; --new-bg: #eaf7ec; --new-fg: #1d6b32;
  --wdel: #f7c6c2; --wadd: #b9e7c4; --chg: #fffaf0;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1c1b19; --fg: #e6e2da; --rule: #3a3833; --muted: #989184;
    --gone-bg: #3a1f1c; --gone-fg: #f0a79d; --new-bg: #16301f; --new-fg: #8fd6a3;
    --wdel: #6d2a24; --wadd: #24572f; --chg: #262420;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg); color: var(--fg);
  font: 15px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
}
header {
  position: sticky; top: 0; background: var(--bg); border-bottom: 1px solid var(--rule);
  padding: .6rem 1rem; z-index: 2;
}
header .files { display: grid; grid-template-columns: 1.6rem 1fr 1fr; gap: 0 1.2rem; font-weight: 600; }
header .legend { color: var(--muted); font-size: 13px; margin-top: .3rem; }
header .legend b { font-weight: 600; }
main { padding: .5rem 1rem 4rem; }
.row {
  display: grid; grid-template-columns: 1.6rem 1fr 1fr; gap: 0 1.2rem;
  padding: .3rem 0; border-bottom: 1px solid var(--rule); align-items: start;
}
.row.chg { background: var(--chg); }
.mark { color: var(--muted); font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
.cell { min-width: 0; overflow-wrap: break-word; }
.cell.mono { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 13px; }
.cell.hdr { font-weight: 700; font-size: 17px; padding-top: .5rem; }
.gone { background: var(--gone-bg); color: var(--gone-fg); }
.new { background: var(--new-bg); color: var(--new-fg); }
.wdel { background: var(--wdel); }
.wadd { background: var(--wadd); }
"""


def runs(words: list[tuple]) -> list[list]:
    """Collapse a word list into (style, text) runs so each becomes one span."""
    out: list[list] = []
    for word, style in words:
        if out and out[-1][0] == style:
            out[-1][1] += " " + word
        else:
            out.append([style, word])
    return out


def cell(words: list[tuple], classes: str) -> str:
    body = " ".join(
        html.escape(text) if not style else f'<span class="{style}">{html.escape(text)}</span>'
        for style, text in runs(words)
    )
    return f'<div class="cell {classes}">{body}</div>'


def render_html(pairs: list[tuple], old: str, new: str, counts: dict) -> str:
    rows = []
    for left, right, kind in pairs:
        lw, rw = styled_words(left, right, kind)
        if kind == "del":
            lw = [(w, "gone") for w, _ in lw]
        elif kind == "add":
            rw = [(w, "new") for w, _ in rw]
        src = left if left is not None else right
        classes = ""
        if src.startswith("|") or FENCE_RE.match(src) or src.startswith("    "):
            classes = "mono"
        elif src.startswith("#"):
            classes = "hdr"
            lw = [(w, None) for w, _ in lw] if kind == "equal" else lw
            rw = [(w, None) for w, _ in rw] if kind == "equal" else rw
        marker = {"equal": "", "chg": "~", "del": "&lt;", "add": "&gt;"}[kind]
        rows.append(
            f'<div class="row {kind}"><div class="mark">{marker}</div>'
            f"{cell(lw, classes)}{cell(rw, classes)}</div>"
        )

    summary = (
        f"{counts['equal']} identical &middot; {counts['chg']} edited &middot; "
        f"{counts['del']} only left &middot; {counts['add']} only right"
    )
    return (
        f"<title>{html.escape(old)} vs {html.escape(new)}</title>"
        f"<style>{CSS}</style>"
        f'<header><div class="files"><div></div><div>{html.escape(old)}</div>'
        f"<div>{html.escape(new)}</div></div>"
        f'<div class="legend"><b>&lt;</b> only left &middot; <b>&gt;</b> only right &middot; '
        f"<b>~</b> edited &middot; {summary}</div></header>"
        f"<main>{''.join(rows)}</main>"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("old")
    ap.add_argument("new")
    ap.add_argument("--width", type=int, default=0, help="total columns; default is the terminal")
    ap.add_argument("--html", metavar="PATH", help="write an HTML page instead of printing")
    args = ap.parse_args()

    total = args.width or shutil.get_terminal_size((160, 40)).columns
    col = max(30, (total - 5) // 2)

    pairs = align(blocks(args.old), blocks(args.new))
    counts = {"equal": 0, "chg": 0, "del": 0, "add": 0}
    for _, _, kind in pairs:
        counts[kind] += 1

    if args.html:
        with open(args.html, "w", encoding="utf-8") as fh:
            fh.write(render_html(pairs, args.old, args.new, counts))
        print(f"{args.html}: {len(pairs)} block(s)")
        return 0

    print(f"{STYLE['rule']}{'─' * (col * 2 + 5)}{RESET}")
    print(f"  {args.old[:col].ljust(col)} │ {args.new[:col]}")
    print(f"  {'< only here'.ljust(col)} │ > only here     ~ edited")
    print(f"{STYLE['rule']}{'─' * (col * 2 + 5)}{RESET}")

    for left, right, kind in pairs:
        lw, rw = styled_words(left, right, kind)
        src = left if left is not None else right
        indent = 2 if LIST_RE.match(src) else 0
        llines, rlines = wrap(lw, col, indent), wrap(rw, col, indent)
        marker = {"equal": " ", "chg": "~", "del": "<", "add": ">"}[kind]
        for i in range(max(len(llines), len(rlines))):
            lf = llines[i] if i < len(llines) else []
            rt = rlines[i] if i < len(rlines) else []
            head = marker if i == 0 else " "
            print(f"{head} {emit(lf, col, indent, i == 0)} │ {emit(rt, col, indent, i == 0)}")
        print(f"  {' ' * col} │")

    print(f"{STYLE['rule']}{'─' * (col * 2 + 5)}{RESET}")
    print(
        f"  {counts['equal']} block(s) identical, {counts['chg']} edited, "
        f"{counts['del']} only in {args.old}, {counts['add']} only in {args.new}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
