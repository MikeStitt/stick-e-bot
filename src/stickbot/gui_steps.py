"""The take's record — identifiers, frames and the log, written as the work happens.

Driving Onshape is `onshape_gui`; this is what turns driving into evidence. It owns the
three things a take produces that nothing else can reconstruct afterwards: the step
identifier every frame and log entry hangs off, the sentence saying what each frame
shows, and the feature list read back around each step.

    import onshape_gui as gui, gui_steps

    take = gui_steps.Take(
        page,
        draft_dir=".docs/experiments/runs/2026-08-25-draft10p9",
        guide_dir="instructions/stickbot-draft10p9",
        part="foot",
        subtree="cad.parts.foot",
    )
    with take.step("cad.parts.foot.pedestal", creates="pedestal") as s:
        s.key("p", "hide the planes so zoom to fit frames the part, not Front and Top")
        s.key("f", "zoom to fit, so the collar fills the window")
        s.shot("pick", "the socket's bottom face, highlighted orange")
        gui.pick(page, (724, 412), "socket bottom face")
        s.measure(collar_h_mm=7.35)
    take.close()          # settles every step with its last attempt

Driving a step once to learn it and again to perform it is two attempts, both staged and
both logged. `take.verdict(step, 1, "the first pass was already the clean one")` promotes
an earlier one; saying nothing takes the last.

Guide 4's `head.rst` was written from contact sheets of ninety-three finished images,
with the meaning of each one worked out by looking at it. `shows` is a required argument
here so that cannot happen again: a frame nobody could describe at the CAD is a frame
that gets described wrongly a week later.

What a take is, and what it writes, is `.docs/build/takes.md`. The cycle it belongs to is
`.docs/build/drafts.md`. What each frame has to be is `.docs/build/shots.md`.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path

AGENT_PORT = 9223

# shots.md's vocabulary. A kind outside it is a frame nobody planned.
KINDS = {
    "pick",         # a tool or a piece of geometry being selected
    "field",        # a value typed into a dialog, before it is committed
    "accepted",     # after the green tick
    "renamed",      # after a part or feature rename
    "hero",         # the finished part, at the top of the page
    "tree",         # the whole feature tree, at the end
    "version",      # the version dialog
    "part_list",    # the studio's parts, named
    "odd",          # something surprised you and the frame is the evidence
    "arrived",      # the empty document a `from: empty` draft starts at, taken once
}

# What an audit was pointed at. `takes.md` § The audit, and each draft's plan says which
# of them it runs and against what inputs.
AUDIT_KINDS = {
    "step",     # what one step left behind, against the plan's `creates`
    "part",     # the finished tab, against the design source and the reference model
    "block",    # one `.. step:` block of the page, against what happened
    "page",     # the page followed to a part by someone without the build in front of them
}

IDENT = re.compile(r"^[a-z][a-z0-9_]*(\.[a-z][a-z0-9_]*)*$")


# An assembly's tree keeps a running count in two header rows. They are not features, and
# they change whenever a feature is added, so a step that makes one mate reads as a step
# that made a mate and a header and destroyed the header it had.
COUNTER = re.compile(r"^(Loads|Mate features|Instances) \(\d+\)$")


def _features(rows):
    """The feature rows of a tree, without the parts list under them.

    `creates` names a feature. An extrude that makes a solid also puts a row in
    `Parts (n)`, and naming that part puts another one; reading those as features
    made the block step look like it created three things and refused a step that
    had done exactly what the plan said.

    The assembly's counters are dropped rather than truncated at, because the mate a step
    creates is drawn under the `Mate features (n)` row it changes.
    """
    out = []
    for r in rows:
        if r.startswith("Parts ("):
            break
        if COUNTER.match(r):
            continue
        out.append(r)
    return out

def errors(page) -> set[str]:
    """Every feature the tree marks with an error, by name.

    Onshape puts `ns-list-item-error` on the row and nothing in the name, so a tree read
    as text says a broken feature is fine.
    """
    return {n for n, cls in page.evaluate(
        """() => Array.from(document.querySelectorAll('.os-list-item')).map(e =>
            [(e.innerText || '').trim().split('\\n')[0], e.className])""")
        if "error" in cls}


# A requirement's name, from `drafts.md` § The requirements. Same grammar as an
# identifier, rooted at `req`, and always three segments: req.<namespace>.<name>.
REQ = re.compile(r"^req\.[a-z][a-z0-9_]*\.[a-z][a-z0-9_]*$")


def _reqs(req) -> list[str]:
    """Normalize one requirement or a list of them, and refuse anything unnamed."""
    if req is None:
        return []
    names = [req] if isinstance(req, str) else list(req)
    for name in names:
        if not REQ.match(name):
            raise ValueError(
                f"{name!r} is not a requirement name — expected req.<namespace>.<name>, "
                f"as listed in .docs/build/drafts.md")
    return names


def connect(playwright, port: int = AGENT_PORT):
    """Attach to the agent's browser. 9223 only — `onshape_gui.connect` says why."""
    import onshape_gui as gui
    return gui.connect(playwright, port=port)


def _check_identifier(identifier: str) -> None:
    if not IDENT.match(identifier):
        raise ValueError(f"{identifier!r} is not an identifier — see .docs/build/steps.md")


class Take:
    """One part's take: where the log goes, where the frames go, and what joins them.

    The log lives with the draft and the frames live under the guide, so the identifier
    is the only thing tying them together. That is why an identifier the subtree does not
    contain is refused here rather than producing a frame nothing can resolve.
    """

    def __init__(self, page, draft_dir, guide_dir, part: str, subtree: str,
                 resume: bool = False):
        _check_identifier(subtree)
        self.page = page
        self.part = part
        self.subtree = subtree
        self.images = Path(guide_dir) / "source" / "images" / part
        self.images.mkdir(parents=True, exist_ok=True)
        self.log_path = Path(draft_dir) / "log" / f"{part}.jsonl"
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        # A draft's log is written once. A crashed take resumes on purpose, out loud,
        # rather than a second run silently doubling the record of the first.
        if self.log_path.exists() and not resume:
            raise FileExistsError(
                f"{self.log_path} exists. Pass resume=True to continue a crashed take, "
                f"or take this part in a new draft.")
        self.attempts_dir = Path(draft_dir) / "capture" / "attempts" / part
        self.log = self.log_path.open("a")
        self.open_step: Step | None = None
        # {identifier: highest attempt taken} and the steps a verdict has settled.
        self.taken: dict[str, int] = {}
        self.settled: set[str] = set()
        # {digest: frame stem} for every frame written, so the same picture cannot go
        # into the guide twice under two names. See `shot`.
        #
        # A take driven one step per process starts each step with an empty memory, so the
        # guard only ever saw inside one step and two steps in two runs could promote one
        # picture under two names. Draft9p4's `part_list` and `tree` did, and so did its
        # `collar.grip_variables` and `section.wide`. The frames already promoted into the
        # guide are what the earlier runs left behind, so they are read back in here.
        #
        # `promoted` is that reading on its own. A step driven again replaces every frame
        # it promoted last time, so a new frame matching one of its own old ones is one
        # picture under one name and not a duplicate; a new frame matching another step's
        # is still the defect this guard is for. See `shot`.
        self.pixels: dict[str, str] = {}
        for frame in sorted(self.images.glob("*.png")):
            self.pixels.setdefault(hashlib.md5(frame.read_bytes()).hexdigest(), frame.stem)
        self.promoted: dict[str, str] = dict(self.pixels)

    def write(self, record: dict) -> None:
        """One JSON object, one line, no clock. The events file is where time lives."""
        self.log.write(json.dumps(record, sort_keys=True) + "\n")
        self.log.flush()

    def stem(self, identifier: str) -> str:
        """The frame stem: the identifier with the page's subtree taken off the front."""
        _check_identifier(identifier)
        if identifier == self.subtree or not identifier.startswith(self.subtree + "."):
            raise ValueError(f"{identifier!r} is not under {self.subtree!r}")
        return identifier[len(self.subtree) + 1:]

    def step(self, identifier: str, creates=None, renames=None, opens=False) -> "Step":
        """Open a step. Use it as a context manager so the step record always lands.

        `creates` is the name the model gains, or a list of them in the order the tree
        puts them. One step makes one feature in a Part Studio, which is where this
        started; an assembly's insert makes an instance per part, and the first one of
        those lands two rows in a single step.

        `renames` is the pair `(old, new)` for a step whose whole job is a name. The tree
        reads the assembly's own name off its top row, so renaming the tab loses one row
        and gains another while creating nothing; without saying so the check below reads
        that gain as a feature the plan never asked for. A Part Studio's tab name is not
        in its tree, so renaming that tab moves no row at all, and the check below asks
        for the swap only when the old name was a row to begin with.

        `opens` is for a step that makes a tab and leaves you standing in it. The tree
        after such a step is a different tree, not the same one with a row added, so
        comparing the two says nothing; the evidence that the step worked is the tab
        strip, which its frames carry.
        """
        if self.open_step is not None:
            raise RuntimeError(f"step {self.open_step.identifier!r} is still open")
        return Step(self, identifier, creates, renames, opens)

    def verdict(self, identifier: str, attempt: int, why: str) -> list[Path]:
        """Say which attempt stands, and put its frames into the guide.

        A step is often driven once to find out what it takes and again to perform it
        cleanly. Both passes are real work and both are captured, but only one belongs on
        the page. Naming the attempt here is what tells whoever writes the page which
        frames are the performance and which were the rehearsal.

        `why` is the difference between the attempts, and it is usually the thing the page
        owes the reader — a practice pass that needed `p` and then `f` before an edge was
        pickable found a step the clean pass will otherwise perform silently.
        """
        stem = self.stem(identifier)
        src = self.attempts_dir / stem / str(attempt)
        if not src.is_dir():
            raise FileNotFoundError(f"no attempt {attempt} of {identifier} at {src}")
        for old in self.images.glob(f"{stem}-*.png"):
            old.unlink()
        out = []
        for i, frame in enumerate(sorted(src.glob(f"{stem}-*.png")), 1):
            dest = self.images / f"{stem}-{i:02d}.png"
            shutil.copy2(frame, dest)
            out.append(dest)
        self.write({"verdict": identifier, "attempt": attempt, "why": why,
                    "frames": len(out)})
        self.settled.add(identifier)
        print(f"  verdict {identifier}: attempt {attempt} stands, {len(out)} frames")
        return out

    def unmet(self, req, why: str) -> None:
        """A requirement this take could not meet, where no one step owns the miss.

        `req.page.video` has no step to hang off — the clip covers a block, not a move —
        and neither does a shot the plan named that the take never got. Naming it here
        keeps the miss in the log rather than in somebody's memory of the session.
        """
        names = _reqs(req)
        if not why.strip():
            raise ValueError("say why the requirement was not met")
        self.write({"unmet": names, "why": why.strip()})
        for name in names:
            print(f"  UNMET {name}: {why.strip()}")

    def audit(self, identifier: str, kind: str, attacked, found=None) -> None:
        """What was checked, what it was attacked with, and what came out.

        `attacked` is required and may not be empty. Without it an empty `found` says
        only that somebody looked, and a check nobody can see the shape of is a check
        nobody can improve — `takes.md` § *The audit*.

        A finding's `severity` is `blocking` when the geometry cannot go on being built
        over it, and `carried` when the part still models and mates and only the printed
        plastic cares. That distinction is the one Mike drew on 2026-08-12 and it is what
        decides whether the next step runs.
        """
        _check_identifier(identifier)
        if identifier != self.subtree and not identifier.startswith(self.subtree + "."):
            raise ValueError(f"{identifier!r} is not under {self.subtree!r}")
        if kind not in AUDIT_KINDS:
            raise ValueError(f"audit kind {kind!r} is not one of {sorted(AUDIT_KINDS)}")
        attacked = [a.strip() for a in ([attacked] if isinstance(attacked, str) else attacked)
                    if a and a.strip()]
        if not attacked:
            raise ValueError(
                f"{identifier}: an audit says what it attacked. An audit with no attack "
                f"list is not a pass — .docs/build/takes.md")
        found = list(found or [])
        for f in found:
            if "what" not in f or f.get("severity") not in ("blocking", "carried"):
                raise ValueError(
                    f"{identifier}: a finding is {{'what': ..., 'severity': "
                    f"'blocking'|'carried'}}, got {f!r}")
        self.write({"audit": identifier, "kind": kind, "attacked": attacked, "found": found})
        blocking = [f for f in found if f["severity"] == "blocking"]
        print(f"  audit.{kind} {identifier}: attacked {len(attacked)}, "
              f"found {len(found)} ({len(blocking)} blocking)")
        for f in found:
            print(f"    {f['severity'].upper()} {f['what']}")

    def close(self) -> None:
        """Settle anything still open with its last attempt, then close the log.

        The last attempt standing is the ordinary case — drive it once to learn it, again
        to perform it — so it costs nothing to say. Promoting an earlier attempt is the
        thing that has to be written down, and `verdict()` is where.
        """
        for identifier, last in self.taken.items():
            if identifier not in self.settled:
                self.verdict(identifier, last, "last attempt; no earlier one promoted")
        self.log.close()


class Step:
    """One attempt at one step, from the feature list before it to the one after it.

    Each pass through a step is its own attempt, numbered from what is already staged.
    Frames go to the attempt's own directory under `capture/attempts/`, not into the
    guide — a second attempt that wrote over the first would destroy the frames a verdict
    might still want to promote, and a take that dies halfway would leave the step with no
    frames at all. `Take.verdict` is what moves one attempt's frames into the guide, and
    that copy is the only thing that clears what was there.
    """

    def __init__(self, take: Take, identifier: str, creates, renames=None, opens=False):
        self.take = take
        self.identifier = identifier
        self.creates = creates
        self.renames = tuple(renames) if renames else None
        self.opens = bool(opens)
        self.stem_ = take.stem(identifier)
        self.n = 0
        self.measured: dict = {}
        self.keys: list[dict] = []
        self.deviation: str | None = None
        self.unmet: list[str] = []
        self.before: list[str] = []
        staged = take.attempts_dir / self.stem_
        self.attempt = 1 + max((int(d.name) for d in staged.glob("*") if d.name.isdigit()),
                               default=0)
        self.dir = staged / str(self.attempt)

    def __enter__(self) -> "Step":
        import onshape_gui as gui
        self.take.open_step = self
        self.dir.mkdir(parents=True, exist_ok=True)
        self.before = gui.tree_all(self.take.page)
        print(f"step {self.identifier}  attempt {self.attempt}  "
              f"({len(self.before)} rows in the tree)")
        return self

    # ---- what the step shot -----------------------------------------------

    def shot(self, kind: str, shows: str, clip=None, at=None) -> Path:
        """Take the next frame of this step, and say what is on the screen.

        `shows` describes the screen; it is not the caption. The page's voice depends on
        the paragraphs around the figure, so a caption written at the CAD gets pasted in
        unedited and lands in the wrong register. What the writing phase cannot recover
        on its own is what the picture contains.

        `at` draws the ring for the close-up half of a point pick, from the same pixel the
        click will use — `shots.md`, *Selecting a point always takes two frames*.
        """
        import onshape_gui as gui
        if kind not in KINDS:
            raise ValueError(f"kind {kind!r} is not one of {sorted(KINDS)}")
        if not shows or not shows.strip():
            raise ValueError(f"{self.identifier}: a frame needs a `shows`")
        if shows.strip() == self.identifier or shows.strip() == self.stem_:
            raise ValueError(f"{self.identifier}: `shows` repeats the identifier, "
                             f"which says nothing the frame name does not")
        self.n += 1
        path = self.dir / f"{self.stem_}-{self.n:02d}.png"
        if at is not None:
            gui.ring(self.take.page, path, at, clip=clip)
        else:
            # A ring frame is about where the pointer is and keeps it; every other
            # frame parks it, so no badge or highlight rides along into the picture.
            gui.frame(self.take.page, path, clip=clip, park=True)
        # Two frames of the same bytes are two names for one picture, and the second
        # `shows` then describes a screen nobody photographed. The hinge's feature list
        # was shot at its head and again at what was meant to be its foot; the scroll
        # never moved, and both frames were the head. The bytes said so and nothing else
        # did, so they are read here rather than by whoever writes the page.
        digest = hashlib.md5(path.read_bytes()).hexdigest()
        twin = self.take.pixels.get(digest)
        # A retake that lands on the same screen as the frame it replaces is the same
        # picture under the same name, which is a retake rather than a duplicate.
        if twin == path.stem:
            twin = None
        # The same, one attempt later: `verdict` unlinks every frame this step promoted
        # before it copies this attempt's in, so a match against one of those is a name
        # that is about to go. An attempt that adds a frame early shifts every number
        # after it, which is how draft9p4's `connectors.neck` met its own accepted frame
        # under the number before it.
        if (twin is not None and self.take.promoted.get(digest) == twin
                and twin.rsplit("-", 1)[0] == self.stem_):
            twin = None
        if twin is not None:
            path.unlink()
            raise RuntimeError(
                f"{path.stem} is the same picture as {twin}, to the byte. The screen did "
                f"not change, so one of the two frames shows something other than what "
                f"its `shows` claims.")
        self.take.pixels[digest] = path.stem
        self.take.write({"frame": path.stem, "step": self.identifier,
                         "attempt": self.attempt, "kind": kind, "shows": shows.strip()})
        return path

    # ---- what the step found ----------------------------------------------

    def key(self, keys: str, why: str) -> None:
        """Press a key, and record it, because the page has to tell the reader to press it.

        `robot-guide2` says *"the view swings round to look straight at it"* where the
        build pressed **n**. The keystroke was invisible to whoever wrote the page because
        it was reflexive, and the same gap swallowed **p** (hide the planes), **f** (zoom
        to fit, which needs the planes hidden first) and **shift+7** (isometric). All four
        are written down in `.docs/onshape-gui-howto.md`, which no student reads.

        `why` is what the page will say. Typing a value is not this — that goes through the
        field, and the field's frame is its record.
        """
        import onshape_gui as gui
        if not why or not why.strip():
            raise ValueError(f"{self.identifier}: a keystroke needs a `why`")
        self.take.page.keyboard.press(keys)
        self.take.page.wait_for_timeout(600)
        self.keys.append({"key": keys, "why": why.strip()})
        print(f"  key {keys:12s} {why.strip()}")

    def measure(self, **numbers) -> None:
        """Numbers read off the model. Measured, not recalled — the Constitution's gate."""
        self.measured.update(numbers)

    def deviate(self, what_happened: str, req=None) -> None:
        """The step did not work as written. Say what was expected and what happened.

        Recording a deviation also stops the feature check below from raising, because
        the surprise is already known and written down. The plan is corrected in the next
        draft's Plan phase, not here — `drafts.md`.

        `req` names any requirement this step could not meet. The plan says which
        requirements are in play and the page's `.. step:` tag carries the ones that
        shaped it; neither of those can know that an attempt fell short. That is what
        this records, and it is the only place a miss is written down — a requirement
        quietly not met reads, in every other artifact, exactly like one that was.
        """
        self.deviation = what_happened
        self.unmet.extend(_reqs(req))
        print(f"  DEVIATION {self.identifier}: {what_happened}")
        for name in _reqs(req):
            print(f"  UNMET {name}")

    # ---- the step record --------------------------------------------------

    def __exit__(self, exc_type, exc, tb) -> bool:
        import onshape_gui as gui
        self.take.open_step = None
        after = gui.tree_all(self.take.page)
        added = [r for r in _features(after) if r not in _features(self.before)]
        gone = [r for r in _features(self.before) if r not in _features(after)]
        record = {"step": self.identifier,
                  "attempt": self.attempt,
                  "creates": self.creates or "none",
                  "features_added": added,
                  "features_gone": gone,
                  "renames": list(self.renames) if self.renames else None,
                  "opens_a_tab": self.opens or None,
                  "keys": self.keys,
                  "measured": self.measured,
                  "deviation": self.deviation,
                  "unmet": self.unmet}
        self.take.taken[self.identifier] = self.attempt
        if exc_type is not None:
            record["deviation"] = f"{self.deviation or ''} take failed: {exc}".strip()
        # The record is written before anything raises, so a take that dies still leaves
        # the evidence of how far it got.
        self.take.write(record)
        if exc_type is not None:
            return False
        expected = ([self.creates] if isinstance(self.creates, str)
                    else list(self.creates)) if self.creates else []
        expected_gone = []
        if self.renames and self.renames[0] in _features(self.before):
            expected.append(self.renames[1])
            expected_gone.append(self.renames[0])
        if self.opens:
            return False
        if (added, gone) != (expected, expected_gone) and self.deviation is None:
            raise RuntimeError(
                f"{self.identifier}: plan says creates={self.creates or 'none'}, "
                f"model gained {added} and lost {gone}. "
                f"Call deviate() if this is the finding.")
        # A feature can arrive under the name the plan asked for and still be broken. A
        # plane built on a point rather than a line went in as `plane for shoulder`,
        # passed the check above four times, and every sketch asked to stand on it
        # answered *Missing*. The tree says so in the row's own class.
        bad = errors(self.take.page) if expected and self.take.page else set()
        broken = [n for n in expected if n in bad]
        if broken and self.deviation is None:
            raise RuntimeError(
                f"{self.identifier}: {broken} went in with an error on it. "
                f"Call deviate() if this is the finding.")
        return False


# --- comparing this draft against its parent ----------------------------------


def read_log(path) -> dict:
    """A log as {identifier: the step record that stands}, plus that attempt's frames.

    A step driven twice writes two step records. The verdict says which one is the
    performance and which was the rehearsal, so everything downstream — the comparison
    against the parent draft, and whoever writes the page — reads one record per step.
    """
    attempts, frames, verdicts, unmet, audits = {}, {}, {}, [], []
    for line in Path(path).read_text().splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        if "audit" in r:
            audits.append(r)
        elif "verdict" in r:
            verdicts[r["verdict"]] = r["attempt"]
        elif "unmet" in r and "step" not in r:
            unmet.extend({"req": name, "why": r["why"], "step": None} for name in r["unmet"])
        elif "frame" in r:
            frames.setdefault((r["step"], r.get("attempt", 1)), []).append(r)
        elif "step" in r:
            attempts.setdefault(r["step"], {})[r.get("attempt", 1)] = r
    steps, kept = {}, {}
    for ident, by_attempt in attempts.items():
        stands = verdicts.get(ident, max(by_attempt))
        steps[ident] = by_attempt[stands]
        kept[ident] = frames.get((ident, stands), [])
    # A miss recorded against a step counts only if that step's attempt is the one that
    # stands — a requirement missed in a rehearsal and met in the performance is not a miss.
    for ident, rec in steps.items():
        unmet.extend({"req": name, "why": rec.get("deviation") or "", "step": ident}
                     for name in rec.get("unmet", []))
    return {"steps": steps, "frames": kept, "verdicts": verdicts, "unmet": unmet,
            "audits": audits,
            "practice": {k: sorted(v) for k, v in attempts.items() if len(v) > 1}}


def compare(parent_log, this_log, renames: dict[str, str] | None = None) -> dict:
    """Join two logs on the step identifier and report what moved.

    Not a text diff: a draft whose plan changed has steps the parent never had, so line
    order carries nothing and the identifier carries everything. `renames` maps a parent
    identifier to this draft's, and comes from the plan's `was` field — this function
    does not read the plan.

    It reports. Whether a difference is the fix that was intended or a regression nobody
    asked for is the register's judgment.
    """
    renames = renames or {}
    a, b = read_log(parent_log)["steps"], read_log(this_log)["steps"]
    a = {renames.get(k, k): v for k, v in a.items()}
    out = {"gone": sorted(set(a) - set(b)),
           "new": sorted(set(b) - set(a)),
           "moved": {}}
    for key in sorted(set(a) & set(b)):
        deltas = {}
        for field in ("creates", "features_added", "keys"):
            if a[key].get(field) != b[key].get(field):
                deltas[field] = [a[key].get(field), b[key].get(field)]
        for name in sorted(set(a[key].get("measured", {})) | set(b[key].get("measured", {}))):
            was, now = a[key]["measured"].get(name), b[key]["measured"].get(name)
            if was != now:
                deltas[name] = [was, now]
        if deltas:
            out["moved"][key] = deltas
    return out


def _main(argv) -> int:
    if len(argv) != 3 or argv[0] != "compare":
        print("usage: gui_steps.py compare <parent-log.jsonl> <this-log.jsonl>")
        return 2
    print(json.dumps(compare(argv[1], argv[2]), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    import sys
    raise SystemExit(_main(sys.argv[1:]))
