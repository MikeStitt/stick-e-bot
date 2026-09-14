"""List the paragraphs a middle-school reader will find hardest.

Whole-file scores hide the paragraphs that are wrong: a document can average
grade 4 and still contain a grade-12 paragraph. So this scores paragraph by
paragraph and lists everything above the threshold.

This reports; it does not fail. A paragraph over the line is a paragraph to
look at, not a defect — a run of short verbatim UI labels scores high and reads
fine. What to do with the list is in the reorganization plan: read the
paragraphs and propose rewrites as a reviewable diff.
"""

import re
import subprocess
import sys

import textstat

THRESHOLD = 8.0

# Prose a *student* reads. Developer notes and the contract are not written for
# this reader and are not measured against this threshold.
GLOBS = ["instructions/**/*.rst", "instructions/**/*.md", "docs/*.md"]

# A session's lesson-design.md is the instructor's half — the clock, the floor
# and ceiling, the rubric. A teacher is not the reader this threshold is set for.
EXCLUDE_NAMES = {"lesson-design.md", "README.md"}

DIRECTIVE = re.compile(r"^\s*(\.\.\s|:\w+:|=+$|-+$|~+$|\*+$|#+$|\|)")
MARKUP = re.compile(r"(``?[^`]*``?|:[a-z]+:`[^`]*`|\*\*?|__?|\[|\]\([^)]*\))")


def files() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files", "--"] + GLOBS,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    return [p for p in out.splitlines() if p.rsplit("/", 1)[-1] not in EXCLUDE_NAMES]


def paragraphs(path: str):
    """Yield (first_line_number, text) for each prose paragraph."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    buf: list[str] = []
    start = 1
    in_fence = False
    for n, line in enumerate(lines, start=1):
        if line.lstrip().startswith("```") or line.strip() in (".. code-block::",):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not line.strip():
            if buf:
                yield start, " ".join(buf)
                buf = []
            continue
        if DIRECTIVE.match(line) or line.startswith("   "):
            continue
        if not buf:
            start = n
        buf.append(line.strip())
    if buf:
        yield start, " ".join(buf)


def main() -> int:
    hits = []
    for path in files():
        for line_no, text in paragraphs(path):
            plain = MARKUP.sub(" ", text).strip()
            # One clause is not a paragraph; the formulas are unreliable on it.
            if len(plain.split()) < 20:
                continue
            grade = textstat.flesch_kincaid_grade(plain)
            if grade > THRESHOLD:
                hits.append((grade, path, line_no, plain))

    if not hits:
        print(f"No paragraph above grade {THRESHOLD:.0f}.")
        return 0

    for grade, path, line_no, plain in sorted(hits, reverse=True):
        print(f"{path}:{line_no}: grade {grade:.1f}")
        print(f"    {plain[:96]}…" if len(plain) > 96 else f"    {plain}")
    print(f"\n{len(hits)} paragraph(s) above grade {THRESHOLD:.0f}. Read them; this is not a failure.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
