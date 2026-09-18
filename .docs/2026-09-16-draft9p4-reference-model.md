# Phase 4 — draft9p4 to a finished reference model, over REST

**Superseded 2026-09-18. Phase 4 was dropped and this plan does not run.** draft9p5 builds the same
six tabs from an empty document, so carrying draft9p4 to a finished model would build one robot
twice. What stays useful here is the measurement of draft9p4 over REST on 2026-09-16, the
archive-rename test, and the finding that an earlier reading of tutorial 9 as nearly done was about
`stickbot-draft9p4-check` and not the build document.
[`2026-09-14-move-to-stick-e-bot.md`](2026-09-14-move-to-stick-e-bot.md) § *Phase 4* records the
decision.

Phase 4 of [`2026-09-14-move-to-stick-e-bot.md`](2026-09-14-move-to-stick-e-bot.md), which said this
work gets its own plan because building a reference model over REST is a different job from the
move. This is that plan.

**What it hands on:** `stickbot-draft9p4` holding the whole robot at the settled joints, built from
draft9p1p6's construction, proved by measurement and by pictures, and published as a named version.
No frames. No pages. draft9p5 is the guide, and it diffs against this.

## Who wrote this, and who is executing it

**Written by** the Claude session rooted at `/Users/mikestitt/projects/first/2027/sponge`, session
id `c7e95b50-7b3c-4747-a656-ece9f33b51c4`. Its transcript is at
`~/.claude/projects/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4.jsonl`
and its scratchpad at
`/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad`.
Both survive the archive being renamed, because neither lives inside it.

**Executed by** a session rooted at `/Users/mikestitt/projects/first/2027/stick-e-bot`. That session
has no task list of its own and does not need one: the numbers were retired at Constitution 5.9.0
and every unit of work here carries a dotted identifier name instead.

**The writing session is inside the archive and will stop working when it is renamed.** That is
expected, and `task.move.archive_out` below is the step that does the renaming. Nothing in this plan
needs the writing session after that point.

## What draft9p4 actually holds today

Read over REST on 2026-09-16, not recalled. `GET /elements` returns nine tabs: `body`, `head`,
`ball and socket`, `robot sizes`, `stickbot`, `u limb`, `hinge`, `foot`, `BOM : stickbot`.

| Tab | draft9p1p6 reference | draft9p4 now | What Phase 4 owes it |
| --- | --- | --- | --- |
| `robot sizes` | 23 rows | present | confirm, do not rebuild |
| `ball and socket` | 14 features | present | confirm, do not rebuild |
| `hinge` | 46 features, wedges | 48 features, **bumps and valleys** | replace the detent |
| `u limb` | 9 features | 10, ending on a sketch | finish, then diff |
| `l limb` | 9 features | **tab does not exist** | build |
| `gripper` | draft9p1p1 record | **tab does not exist** | build |
| `foot` | draft9p1p1 record | present, with a known defect | fix `sole groove` |
| `stickbot` | draft9p1p1 record | two instances | add arms, then legs |

**The hinge is the finding that changes the shape of this plan.** draft9p4 branched draft9p3, and
its `hinge` tab is still draft9p3's joint: `blade bump outline`, `blade bump`, `dome blade bump`,
`24 blade bumps`, `ear valley outline`, `ear valley`, `round ear valley rim`, `24 ear valleys`. The
settled joint is a wedge ring — `blade wedge outline`, `blade wedge`, `blade wedges`,
`ear wedge outline`, `ear wedge`, `ear wedges` — which is what
`reference/hinge.features.json` holds. So the hinge is a replacement, not a completion, and the
earlier reading that tutorial 9 was nearly done was about the check document, not this one.

**Two connectors also carry the retired word.** `fork to robot connector` and
`blade to robot connector` become `fork to robot` and `blade to robot`, per the naming settled in
draft9p4's own plan: the feature list already says a connector is a connector.

## Where the construction comes from

- **`hinge`, `u limb`, `l limb`, `ball and socket`, `robot sizes`** — `reference/` under
  [`experiments/runs/2026-09-08-draft9p4/`](experiments/runs/2026-09-08-draft9p4/), read from
  `stickbot-draft9p1p6` at version `F done - Phase F proved`, id `80c22eb7b8b0342ac03f8a6d`.
- **`body`, `head`, `foot`, `gripper`, the assembly** — `reference/` under
  [`experiments/runs/2026-08-29-draft9p3/`](experiments/runs/2026-08-29-draft9p3/), which holds
  draft9p1p1's construction with faces, geometry and sketches per tab.
- **The numbers** — `src/stickbot/make_plans.py`, which is at the settled joint: `WEDGES = 24`,
  `WEDGE_H = 0.75`, `WEDGE_C = 0.15`, `STUB = 4.0`, `BORE_D = 4.1`, `EAR = 6.10`, `SEAT = 11.80`.
  The build briefs derive from it and are current.

**The hinge review is not a source here, and it is not a defect either.**
`.docs/reviews/hinge/make_figures.py` holds `EAR` 6.85, `SEAT` 10.3, `STUB_PROUD` 1.30,
`BORE_D` 4.4 and a ring of cones in a frozen `J`, on purpose: it is the review of the joint that
was printed and measured at 210 N·mm against the 454 N·mm it was drawn for, which is the evidence
that ended that joint. Its page opens by saying so, and so does the generator. A review reads what
it reviewed. Nothing in this plan reads it and nothing should change it.

## What REST may do

**Mike granted REST for `stickbot-draft9p4` by name on 2026-09-14.** The grant covers that document
and no other; draft9p1p6 and draft9p3 are read-only sources here.

- **Reading, without limit**, in any document in scope: `/features`, `bodydetails`, `parts`,
  `boundingboxes`, `getVariable`, and the rest.
- **Writing features in `stickbot-draft9p4`**, by editing the features the parent already holds,
  with their constraints, patterns and mirrors intact. That is what *structurally right* means, and
  it is the draft9p1p6 precedent: geometry is not emitted fresh because emitting is cheaper.
- **Publishing a named version** in that document.
- **Not the check document.** `stickbot-draft9p4-check` belongs to a guide draft that is no longer
  being made. It is left where it is.

## The work, in dependency order

Each carries its identifier name. The six tab names come from
[`2026-09-14-move-to-stick-e-bot.md`](2026-09-14-move-to-stick-e-bot.md) § *The open work, by name*,
where their full descriptions live; this file says what Phase 4 does about each.

### `task.phase4.activate`

Point [`../.claude/rules/active-plan.md`](../.claude/rules/active-plan.md) at this file, replacing
the move plan's import rather than adding a second. Then read this plan's own text back out of the
injected instructions, because a broken `@` import is silent.

### `task.move.archive_out`

**Mike renames `/Users/mikestitt/projects/first/2027/sponge` to `…/sponge-old`,** and the run proves
nothing was looking for the old path. This is deliberately early: a path that only breaks under load
is worse found at the end.

What was measured before the move, so the result can be read against it:

- **35 tracked files name `2027/sponge`.** 34 are under the four pre-package run folders
  (`2026-08-16-human-run1`, `2026-08-23-draft9p0`, `2026-08-25-draft9p1`, `2026-08-26-draft9p1p1`),
  which are archived records of what was driven and are never run. The 35th is
  [`2026-09-16-python-packaging.md`](2026-09-16-python-packaging.md), which quotes the literal path
  as the thing those scripts hardcode.
- **Nothing untracked points there either**: `.venv` has zero references, the editable install
  resolves to `…/stick-e-bot/src`, and `build.ninja`, `pyproject.toml`, `uv.lock`, `.ninja_log` and
  `.idea` are clean.
- **Both browser profiles live outside both trees**, under
  `~/.cache/onshape-automation/{chrome-profile,agent-profile}`.

So the expected result is that everything passes. What to run after the move, and watch:

- `uv sync`, then `uv run python -c "from stickbot import repo_root; print(repo_root())"`
- `ninja check`, all five gates
- `ninja plan` and `ninja hinge-figures`, and confirm the artifacts come back byte-identical
- `pkill -f agent_browser.py`, then `uv run python -m stickbot.agent_browser`
- a REST read of draft9p4's element list

**A failure here is the point of the step, not an obstacle to it.** Record what broke and where the
path came from before fixing it.

### `task.phase4.gap`

Read every tab of `stickbot-draft9p4` in full — features, faces, geometry, sketches — and write the
gap against the reference records into `reference/` under this plan's own folder. Nothing is built
until this exists for the tab being built.

Three things to establish while reading, each of which changes later steps:

- **Whether `robot sizes` holds all 23 rows at their settled expressions**, `#limbD` among them.
  `task.draft9p4.carry_diff` waits on that row and on nothing else.
- **Whether `ball and socket` matches `reference/ball-and-socket.features.json`** at 14 features.
  Tutorial 4 was taken against the settled socket, so it should.
- **What `u limb`'s tenth feature is**, and whether the tab is nine settled features plus one stray
  or a different construction that happens to be ten.

### `task.draft9p4.hinge`

Replace the detent. The bump and valley features come out, the wedge ring goes in, against
`reference/hinge.features.json` — 46 features. `blade profile` is four entities and cost draft9p1p5
eight attempts, four of whose findings left a blade that looked right, so every sketch is read back
with `read_sketches.py` and `diff_geometry.py` before the next feature is added. The two parts keep
their names. The two robot connectors lose the word *connector*.

### `task.foot.sole_groove`

Independent of the limbs and small, so it lands here rather than waiting. `sole groove` has two
Opposite direction arrows and only the Starting offset one was turned, so the cut starts 22 mm below
the sketch and runs 2 mm back up, leaving eight tunnels across the foot above an unbroken sole
instead of eight open notches. Turn the Depth arrow; `sole ribs` follows. The check that catches it:
the sole at z -24 mm is nine faces, not one, and no face stands at z -20 mm. Amend
[`build/plan/08-foot.md`](build/plan/08-foot.md)'s `## Built`.

### `task.draft9p4.u_limb`

Finish against `reference/u-limb.features.json`. It derives both joints, `add socket` and
`add fork`. Whether the rod reproduces volume the derived fork's arm already occupies has never been
checked for this tab at all, so measure it.

### `task.draft9p4.l_limb`

Build the tab. `reference/l-limb.features.json`, nine features, deriving `add blade` and
`add ball stud`. Settle the same volume question draft9p1p5's Phase E raised and never ran to
ground.

### `task.draft9p4.gripper`

Build the tab, from draft9p3's `reference/gripper.*`. `clip profile` follows the socket's outside
profile and is drawn after `copy socket`, so the whole tab moves with the settled socket and the
record it is diffed against predates that move. Where the record and the settled socket disagree,
the socket wins and the departure is written down.

### `task.draft9p4.assembly_arms`, then `task.draft9p4.assembly_legs`

The assembly gains both arms, then both legs, against draft9p3's `reference/assembly.*`. Legs last:
the version it publishes is what the *Recovery point* gate wants.

### `task.draft9p4.carry_diff`

Re-read `head` and `body` and diff against draft9p3's `log/head.faces.json` and `body.faces.json`.
The copy half is already proved — draft9p4 at its Start version matched face for face, 47 on `head`
and 20 on `body`. The settled half could not run while the studio was empty, and can once
`robot sizes` carries `#limbD`.

### `task.phase4.prove`

**Numbers and pictures, and the picture decides.** Per tab: `read_shape.py` and `diff_shape.py`
against the reference, `diff_features.py` and `diff_sketches.py` for the construction, and rendered
views chosen by writing the feature list first and picking the view each feature is visible in. A
feature with no view in the set is a feature nobody looked at. Each part is rendered beside the part
it was derived from, in the same views.

Two things this cannot do, and the register says so rather than reporting a pass: the features after
each derive in `head`, `body`, `foot` and `gripper` have no counterpart in either reference, and
`gripper` is diffed against a record that predates the settled socket.

### `task.phase4.register`

`register.md` under this plan's folder: what was built, what each check attacked, what it found and
what was done about each finding. Every tab gets its state and its version. A check that did not run
says so by name.

## What is not in this plan

- **No frames and no pages.** draft9p4 publishes nothing to `instructions/`.
- **`stickbot-draft9p4-check` is not touched.**
- **`task.foot.bottom_view`, `task.capture.zoom_fit`** — page and capture work, which is Phase 5's.
- **`task.print.whole_robot`, `task.hinge.wedge_loss`** — standing, in neither phase.

## What we do not know yet

- **How much of draft9p4's `hinge` survives the replacement.** The 19 variables and the blade and
  fork blanks may carry; the detent does not. `task.phase4.gap` answers it.
- **Whether REST can edit a `circularPattern`'s seed without rebuilding the pattern.** The wedge
  ring is two patterns of 24, and replacing a seed feature under a pattern is the step most likely
  to need a different approach than editing in place.
- **What the `gripper` record's disagreement with the settled socket amounts to.** It is known to
  exist and its size is not.
- **Whether `/features` is rate limited today.** It answered on 2026-09-16. draft9p3 was refused for
  long enough that it read construction through the GUI instead, so the plan should degrade rather
  than stall.
