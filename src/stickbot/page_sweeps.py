"""Four sweeps over one written page, for `audit.block` and `audit.page`.

A page of a hundred and fifty figures is not readable. Two close readings of `torso-joints.rst`
missed a duplicate figure, twenty-two pictures with no instruction above them and eleven of the
take's own keystrokes; these four sweeps found all of it in a second.

Two of them compare the page against the run's log, two compare the page against itself, and none
of them needs a model or a browser.

    uv run --project . python tools/page_sweeps.py <draft> <guide> <page> [sweep ...]

`<draft>` is the run directory under `.docs/experiments/runs/`, `<guide>` the directory under
`instructions/`, and `<page>` the stem shared by `instructions/<guide>/source/<page>.rst` and
`<draft>/log/<page>.jsonl`. A page stem is not unique across guides — every guide has a `torso` —
so the guide is named rather than searched for. With no sweep named, all of them run.

None of them is a pass or a fail. `altdiff` in particular prints every pair it can see a
difference in, because the log is not an answer key: two of the `shows` records on torso-joints
were wrong where the page was right, and a sweep that trusted the log would have "corrected" the
page into agreeing with them.
"""
import collections
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# A single letter matches anywhere in a page of prose, so a key is looked for in the form the page
# has to write it in: bold, and in the case Onshape's own tooltip uses.
KEY_FORMS = {"escape": ["Escape"],
             # The arrow keys have no tooltip to copy, and a page for readers at grade 8 writes
             # them the way a keyboard is read out loud.
             "arrowup": ["**up arrow**", "**arrowup**"],
             "arrowdown": ["**down arrow**", "**arrowdown**"],
             "arrowleft": ["**left arrow**", "**arrowleft**"],
             "arrowright": ["**right arrow**", "**arrowright**"]}


def key_forms(key: str) -> list:
    return KEY_FORMS.get(key.lower(), [f"**{key.lower()}**"])


def read(draft: pathlib.Path, guide: str, page: str):
    """The page's text, its guide's source directory, and the log records that stand."""
    src = ROOT / "instructions" / guide / "source"
    text = (src / f"{page}.rst").read_text()
    best, frames, keys = {}, {}, {}
    log = draft / "log" / f"{page}.jsonl"
    for line in log.read_text().splitlines():
        if line.strip():
            r = json.loads(line)
            if "verdict" in r:
                best[r["verdict"]] = r["attempt"]
    for line in log.read_text().splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        if best.get(r.get("step")) != r.get("attempt"):
            continue
        if "frame" in r:
            frames[r["frame"]] = (r["kind"], r["shows"])
        if r.get("keys"):
            keys[r["step"]] = r["keys"]
    return src, text, best, frames, keys


def figures(text: str) -> list:
    return re.findall(r"^\s*\.\. (?:image|figure):: (\S+)", text, re.M)


def alts(text: str) -> dict:
    """{frame stem: its alt, run together on one line}."""
    out, lines = {}, text.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"\s*\.\. (?:image|figure):: images/[^/]+/(\S+)\.png\s*$", line)
        if not m:
            continue
        alt, j = None, i + 1
        while j < len(lines) and lines[j].strip():
            f = re.match(r"\s+:alt: (.*)$", lines[j])
            if f:
                alt = [f.group(1)]
                j += 1
                while (j < len(lines) and lines[j].strip()
                       and not re.match(r"\s+:[a-z]+:", lines[j])):
                    alt.append(lines[j].strip())
                    j += 1
                break
            j += 1
        out[m.group(1)] = " ".join(" ".join(alt).split()) if alt else "<no alt>"
    return out


def blocks(text: str) -> dict:
    """The page cut into blocks at its `.. step:` tags, so a key is looked for where it belongs."""
    marks = [(m.start(), m.group(1)) for m in re.finditer(r"^\.\. step: (\S+)$", text, re.M)]
    return {name: text[pos:(marks[i + 1][0] if i + 1 < len(marks) else len(text))]
            for i, (pos, name) in enumerate(marks)}


# --- the sweeps ---------------------------------------------------------------


def sweep_blockcheck(src, text, best, frames, keys, page, draft):
    """Real files, once each, under tags the log knows."""
    imgs = figures(text)
    missing = [i for i in imgs if not (src / i).exists()]
    print(f"figures: {len(imgs)}, missing: {missing}")

    by_hash = collections.defaultdict(list)
    for i in imgs:
        if (src / i).exists():
            by_hash[hashlib.sha256((src / i).read_bytes()).hexdigest()].append(i)
    print(f"published twice: {[v for v in by_hash.values() if len(v) > 1]}")

    tags = re.findall(r"^\.\. step: (\S+)$", text, re.M)
    known = set(best) | {f.rsplit("-", 1)[0] for f in frames}
    print(f"step tags: {len(tags)}, unknown: {[t for t in tags if t not in known]}")

    reqs = sorted({r.strip() for line in re.findall(r"^\.\. req: (.+)$", text, re.M)
                   for r in line.split(",")})
    drafts = (ROOT / ".docs/build/drafts.md").read_text()
    print(f"req tags: {reqs}, unknown: {[r for r in reqs if r not in drafts]}")

    promoted = {p.name for p in (src / f"images/{page}").glob("*.png")}
    used = {pathlib.Path(i).name for i in imgs if f"{page}/" in i}
    print(f"on disk {len(promoted)}, used {len(used)}, unused: {sorted(promoted - used)}")


def sweep_instruction_first(src, text, best, frames, keys, page, draft):
    """`req.page.instruction_first`: a picture follows the sentence that asks for it."""
    lines, bare = text.splitlines(), 0
    for i, line in enumerate(lines):
        if not re.match(r"^\s*\.\. image:: ", line):
            continue
        j = i - 1
        while j >= 0 and not lines[j].strip():
            j -= 1
        # A toolbar close-up and the shot that places it on screen are one pair, and the sentence
        # above the pair covers both — `shots.md`, the two-frame rule.
        if j >= 0 and ":class: button" in lines[j]:
            while j >= 0 and lines[j].strip():
                j -= 1
            while j >= 0 and not lines[j].strip():
                j -= 1
        above = lines[j] if j >= 0 else ""
        if (not above.strip() or above.startswith("..") or re.match(r"^\s+:", above)
                or re.match(r"^[-=~^\"']+$", above.strip())):
            bare += 1
            print(f"  {i + 1}: {line.strip()[:70]}  <- above is {above.strip()[:50]!r}")
    print(f"{bare} picture(s) with no sentence above them")


def sweep_keycheck(src, text, best, frames, keys, page, draft):
    """`req.page.view_keys`: every press the take recorded is written down."""
    body_of, missing = blocks(text), 0
    for step, presses in keys.items():
        for k in presses:
            if not any(f in body_of.get(step, "") for f in key_forms(k["key"])):
                missing += 1
                print(f"  {step}: {k['key']!r} not in the block  ({k['why'][:60]})")
    print(f"{sum(len(v) for v in keys.values())} presses across {len(keys)} steps, "
          f"{missing} missing")


def sweep_altdiff(src, text, best, frames, keys, page, draft):
    """Each alt beside the `shows` the take wrote with the frame on screen."""
    differ = 0
    for name, alt in sorted(alts(text).items()):
        kind, shows = frames.get(name, ("?", "<not in the log>"))
        a, s = alt.lower().rstrip("."), shows.lower().rstrip(".")
        if a == s or a in s or s in a:
            continue
        differ += 1
        print(f"{name}  [{kind}]\n   shows: {shows}\n   alt:   {alt}")
    print(f"{differ} of {len(alts(text))} alts differ from the log; look at each")


def sweep_census(src, text, best, frames, keys, page, draft):
    """The student attack, made mechanical: every name with the line it first appears on."""
    first = {}
    for i, line in enumerate(text.splitlines(), 1):
        for m in re.finditer(r"``([^`]+)``|\*\*([^*]+)\*\*", line):
            first.setdefault((m.group(1) or m.group(2)).strip(), i)
    for name, i in first.items():
        print(f"  {i:5d}  {name}")
    print(f"{len(first)} names")


SWEEPS = {"blockcheck": sweep_blockcheck, "instruction_first": sweep_instruction_first,
          "keycheck": sweep_keycheck, "altdiff": sweep_altdiff, "census": sweep_census}

if __name__ == "__main__":
    draft = ROOT / ".docs/experiments/runs" / sys.argv[1]
    guide, page = sys.argv[2], sys.argv[3]
    wanted = sys.argv[4:] or list(SWEEPS)
    src, text, best, frames, keys = read(draft, guide, page)
    for name in wanted:
        print(f"--- {name} ---")
        SWEEPS[name](src, text, best, frames, keys, page, draft)
