# Moving to stick-e-bot

This repository is 1.5 GB of git history holding 12,977 PNGs, and it is named after a robot we
stopped building. `https://github.com/MikeStitt/stick-e-bot.git` is the replacement. This file says
what moves, what does not, what stops the same accident happening again, and in what order.

## What was measured, 2026-09-14

| | |
| --- | ---: |
| Tracked PNG under `.docs/experiments/runs/` — interim capture, never published | 1,235 MB |
| Tracked PNG under `instructions/` — nine guide drafts, one of them live | 416 MB |
| Everything else tracked — prose, plans, logs, reference JSON, tools | 28 MB |
| `.git`, of which 1.4 GB is the Git LFS object cache and 129 MB is the pack | 1.5 GB |

- **PNG is 1,651 MB of the 1,679 MB tracked, across 12,977 files.** Everything else is rounding.
- **The largest file ever committed is 2.12 MB**, `c1-raw.json`. GitHub warns at 50 MB and blocks
  at 100 MB.
- **71 files of built Sphinx HTML are tracked**, which is the same accident in a different costume.
- **`instructions/stickbot-draft9p4/` is 80.12 MB of frames and 0.53 MB of everything else** — 20
  source files and 22 toolbar close-ups.

**The old repository already uses Git LFS, and this file said otherwise until 2026-09-14.** Its
`.gitattributes` routes `*.png` and `*.mp4` through LFS and 12,989 tracked files are LFS-managed,
which is why the pack is only 129 MB while `.git` is 1.5 GB. LFS was doing its job; the repository
is large because 12,977 screenshots were committed, not because they were stored badly.

**The new repository needs nothing today, and inherits no rule.** It carries 22 toolbar close-ups
totaling 0.13 MB, and its largest file of any kind is 2.12 MB against GitHub's 50 MB warning and
100 MB block. The old `.gitattributes` is deliberately not carried, because a routing rule that
arrives by inheritance is a decision nobody made.

**The decision is owed when draft9p5 starts publishing frames**, at roughly 130 KB each and perhaps
800 a draft. Two things have to be established first, neither of them from memory: what GitHub
Pages does with an LFS-tracked image, and what the account's LFS storage and bandwidth allowance
is. A guide served from Pages whose figures are pointer files is worse than a large pack.

## Settled decisions

- **Fresh `git init`. No history, no `git-filter-repo`.** Rewriting 1.5 GB costs a day, breaks
  every path in every archived record, and buys a log this directory already holds. This repository
  stays on disk as the archive, which is what the Constitution's Archive section already calls it.
- **`stick-e-bot` is public.** GitHub Pages is free on public repositories and needs a paid plan on
  private ones. Publishing `.docs/project.md` hands over identifiers, not access: on 2026-09-14 a
  second Onshape account was given the exact document and workspace id of `stickbot-draft9p4` and
  was refused with *document does not exist or you don't have permission to access it*. Knowing an
  id is not enough to open a document, and that is now performed rather than assumed.
- **draft9p4 becomes the reference model, not a guide.** It is finished over REST so it is
  structurally right, and it publishes no pages. draft9p5 is the guide, built from an empty
  workspace in the GUI, and it captures its own frames.
- **Interim capture leaves the repository.** A take writes its frames to the session scratchpad. A
  frame reaches git only by being placed on a page, or by being the evidence a written finding
  rests on. This is the whole of what went wrong: 1,235 MB arrived because capture and publication
  shared a tree.

## Phase 1 — the gate, before the first commit — **done 2026-09-14**

- **`.gitignore` denies images by default.** Ignore `*.png` and `*.jpg`/`*.jpeg` anywhere, then
  un-ignore exactly `instructions/*/source/images/`. Ignore `instructions/*/build/` and
  `**/capture/`.
- **`check-images` joins `ninja check`.** It fails if a tracked image sits outside
  `instructions/*/source/images/`, and fails if built HTML is tracked. One pass over
  `git ls-files`, the shape of `check_wrap.py`.
- **A size ceiling with a number in it.** The check also fails on any tracked file over 5 MB.
  Nothing legitimate here approaches it and the one that tries will be an accident.

**Why this is Phase 1 and not Phase 5.** The rule was already written down. `retakes-changes.md`,
dated 2026-08-23, named the missing `.gitignore`, the exact paths it had to cover, and the 1.2 GB
it would hide from `git status` — three weeks before the bill came due. Nobody acted on it. Writing
the rule down is the thing that failed, so the gate is a check that runs rather than a sentence
somebody is meant to remember.

## Phase 2 — carry the text — **done 2026-09-14**

`git init` in `/Users/mikestitt/projects/first/2027/stick-e-bot`, the remote, the first commit.

**Carries:** `tools/` entire; `.claude/rules/` and `.claude/skills/`; `pyproject.toml`, `uv.lock`,
`build.ninja`, `.gitattributes`; `docs/`; `.docs/` including `build/`, `project.md`,
`robot-build-plan.md`, `session-state.md`, `onshape-gui-howto.md`, `onshape-api.md`,
`browser-access.md`, `verification-lessons.md`, `reviews/`; every run folder's text — plans, notes,
registers, logs and `reference/*.json`; and from `instructions/stickbot-draft9p4/`, the 20 source
files and the 22 toolbar close-ups.

**Does not carry:** 12,977 PNGs; the eight superseded guide drafts entire; the built HTML;
a retired experiment's guide directory, which the Constitution already calls retired;
`old-constitution.md`, whose diff has been taken.

**Resolved on 2026-09-14.** `draft-prose-style.md` and `pre-plan.md` were deleted, along with the
untracked scratch files `process-map.md` and `retakes-changes.md`; every finding those two held has
either landed or is carried by this plan. `old-constitution.md` stays here in the archive and does
not carry, which makes `SKIP_FILES = ("old-constitution.md",)` in `src/stickbot/check_wrap.py` dead
in the new repository — it comes out with the file.

## Phase 3 — the rename and the contract — **done 2026-09-16**

- **The old repository's name appears in 12 live tracked files**, the Constitution among
  them. This is a meaning change, so the prose rule permits the edit.
- **`src/stickbot/check_spelling.py`** carries the old name in its dictionary or its docstring.

**The third item was withdrawn, not done.** It asked for the Constitution's *Where developmental
draft products live* to name the example completed CAD once Phase 4 published one. Mike ruled on
2026-09-16 that the Constitution does not track where a version of the stickbot lives, and replaced
the placeholder with *an example completed CAD in Onshape*. The other two items landed in `42466c8`
and were verified on 2026-09-16: one citation of the old name survives, in
[`2026-09-16-python-packaging.md`](2026-09-16-python-packaging.md), where it quotes the literal
path 47 archived scripts hardcode.

## The active plan, settled 2026-09-14

**draft9p4's plan is deactivated by agreement, and this file is the active plan.**
`.claude/rules/active-plan.md` imports
[`2026-09-14-move-to-stick-e-bot.md`](2026-09-14-move-to-stick-e-bot.md).

Phase 4 gets its own plan when it starts, because building a reference model over REST is a
different job from this move. Until then this file governs.

**The pointer carried verbatim and kept naming the old plan.** `active-plan.md` came across with
the rest of `.claude/rules/` and went on importing draft9p4's plan, so the first session opened in
`stick-e-bot` correctly read that plan and correctly concluded it was active. The file is one line
and it is easy to forget precisely because nothing about it looks like state. A repository that
copies its contract copies its plan pointer with it.

## Phase 3.5 — re-root, and prove the new root before trusting it — **done 2026-09-14**

**Start a Claude Code session whose working directory is `stick-e-bot`, and do everything after
this from there.** The old repository becomes read-only archive at that moment.

This is a phase rather than a footnote because a session rooted in the wrong repository reads the
wrong contract, and nothing in the injected text says which one arrived. Phase 4 is the largest
piece of work left; finding a broken root during it costs more than finding one now.

**The version string is the test.** The archive's constitution is 5.1.0 and this one is 5.2.0, so
the `**Version**` line in the injected text says which repository the session is reading, with no
ambiguity and nothing to set up.

What the first request in the new session checks:

- **The contract arrived, at 5.2.0**, along with `prose-style.md`, `plan-activation.md` and
  `CLAUDE.md`.
- **`active-plan.md` names this file, and its import resolved.** A broken `@` import is silent, so
  read the plan's own text back rather than assuming it arrived.
- **`/context` lists the files**, which is cheaper than a compaction and catches one that quietly
  did not load.
- **The four project skills are listed.** A skill directory registers at session start, so a fresh
  session should have them without `/reload-skills`.
- **`uv sync` and `ninja check` are green from this root**, and `ninja check` now has four gates.

If any of those fails, fix it before Phase 4 rather than working around it.

**What the first request checked, 2026-09-14.** Four of the five closed and nothing failed, so
Phase 4 is not blocked on this phase.

- **The contract arrived at 5.2.0**, with `prose-style.md`, `plan-activation.md` and `CLAUDE.md`,
  and the four project skills were listed without `/reload-skills`.
- **`ninja check` exited 0 on all four gates, watched**: wrap, codespell, reading level, and the
  tracked-image check. `uv sync` resolved 42 packages and audited 40, installing nothing.
- **The reading-level gate listed 37 paragraphs above grade 8**, across
  `instructions/stickbot-draft9p4/source/` and `instructions/robot-guide/source/`, the worst of them
  grade 8.9. The gate says in its own output that this is not a failure, and the Constitution's
  *Reading level* gate is what adjudicates them.
- **`/context` was not run.** It is a slash command the session cannot call for itself, so it is
  Mike's to perform. It is the one item of this phase still open.
- **A pointer edited inside a session does not reach the injected text until the next request.**
  `active-plan.md` was repointed at this file mid-session, and the injected copy went on carrying
  draft9p4's plan, so this plan's text was read back with `cat` rather than out of the injection.
  The import path resolves and the file is on disk, which is what the check asked for.

## Phase 4 — draft9p4 to a finished reference model, over REST

Tutorials 9 to 14 are unbuilt: the hinge is part way, and `u limb`, `l limb`, `gripper` and the two
assembly tutorials have not started. The joints come from `stickbot-draft9p1p6`, the rest from
draft9p1p1's construction, exactly as draft9p4's own declaration says.

**draft9p4's own plan does not govern this work, and a new one is owed.**
[`experiments/runs/2026-09-08-draft9p4/plan.md`](experiments/runs/2026-09-08-draft9p4/plan.md) is a
guide-draft plan: it claims *Steps reproduce*, it forbids REST from building the model, and it ends
in fourteen written pages. Phase 4 does none of that. So `active-plan.md` points at a plan written
for this work, and the draft9p4 plan is agreed deactivated rather than quietly contradicted.

**Two conditions, both from the draft9p1p6 precedent:**

- **The grant is per-document and does not carry.** draft9p1p6's plan records that the earlier
  permission covered `stickbot-draft9p1p2` and `stickbot-draft9p1p4` and did not extend. **Mike
  granted REST for `stickbot-draft9p4` by name on 2026-09-14**, so Phase 4 is authorized in that
  document and in no other.
- **REST edits features; it does not emit geometry.** The same plan: geometry is written *by
  editing the features the parent already holds, with their constraints, patterns and mirrors
  intact, not by emitting fresh geometry because emitting is cheaper*. That is the whole of what
  "structurally right" means here, and it is what `modeling-practice` asks for.

No frames are taken. The tab is proved by `read_shape.py`, `diff_shape.py` and rendered views, the
way a reference model is proved.

**What this drops:** the 208 uncommitted hinge frames and draft9p4's eight written pages. The
frames were captured for a guide draft9p4 is no longer making. The pages carry forward as text for
draft9p5 to write against.

## Phase 5 — draft9p5 from empty

A new plan, a new empty Onshape workspace, the GUI for every feature, and draft9p4 as the reference
the audits diff against. The frames it publishes are the only frames that reach git.

## The open work, by name

Sixteen tasks were open when the numbers were retired. Each is named here and placed in the phase
that will do it, or recorded as superseded. [`tasks.md`](tasks.md) holds the number each was
written under and the full text of what it asked for.

**Phase 4 holds the model work.** The pages these tasks also asked for are Phase 5's, because
Phase 4 takes no frames and writes no pages.

- **`task.draft9p4.hinge`.** The hinge tab: twenty-four wedges on a ring with a fifteen degree
  step, where draft9p3's page still describes bumps and valleys. `blade profile` is four entities
  and cost draft9p1p5 eight attempts, four of whose findings left a blade that looked right, so
  every sketch step reads back what it drew before the next one runs.
- **`task.draft9p4.u_limb`.** Never taken in any draft. Derives both joints, `add socket` and
  `add fork`. Whether the rod reproduces volume the derived fork's arm already occupies has never
  been checked for this tab at all.
- **`task.draft9p4.l_limb`.** Never taken. Derives `add blade` and `add ball stud`, and settles the
  same volume question draft9p1p5's Phase E raised and never ran to ground.
- **`task.draft9p4.gripper`.** `clip profile` follows the socket's outside profile and is drawn
  after `copy socket`, so the whole tab moves with the settled socket.
- **`task.draft9p4.assembly_arms`.** Never taken. The assembly gains both arms.
- **`task.draft9p4.assembly_legs`.** Never taken. The assembly gains both legs and the robot
  stands. The version it publishes is what the *Recovery point* gate wants.
- **`task.draft9p4.carry_diff`.** Re-read `head` and `body` from the draft9p4 workspace once
  tutorial 6 types `#limbD` back, and diff against draft9p3's `head.faces.json` and
  `body.faces.json`. The copy half is already proved: draft9p4 at its Start version matches
  draft9p3 face for face, 47 on `head` and 20 on `body`.
- **`task.foot.sole_groove`.** `sole groove` has two Opposite direction arrows and only the
  Starting offset one was turned, so the cut starts 22 mm below the sketch and runs 2 mm back up.
  The foot has eight tunnels across its width above an unbroken sole, where it should have eight
  open notches. The check that catches it: the sole at z -24 mm is nine faces, not one, and no face
  stands at z -20 mm.
- **`task.draft9p4.register`.** What was built, what each audit attacked, what it found and what
  was done about each finding. Every step gets its `state` and its `version`, every claimed gate
  gets the evidence that closes it, and a gate that did not close says so.

**Phase 5 holds the capture and page work.**

- **`task.capture.zoom_fit`.** Teach and perform `f` zoom fit throughout, in the guide prose and in
  the capture run that produces the frames, since they are the same script. It depends on hiding
  the default planes: `f` frames Top, Front and Right rather than the part. In the human run the
  follower scrolled 75 wheel notches and used zoom to fit zero times.
- **`task.foot.bottom_view`.** `shift+5` gives the Top view, not the bottom, so three frames
  captioned as the sole with grooves across it are top views and the page never shows the sole.
  Find the key that does give it, and correct every place a page tells a reader to press it.

**Standing, in neither phase.**

- **`task.print.whole_robot`.** Recorded in
  [`robot-build-plan.md`](robot-build-plan.md) § *Nothing here is settled until the whole robot is
  printed*, which is where it belongs: it is the question the whole design answers to, not a step
  in a draft.
- **`task.hinge.wedge_loss`.** The blade holds 96 cone faces from `#limbD` 18 mm to 33.5 mm and
  comes back with 94 at 34 mm, 90 at 36 mm and 82 at 40 mm; the fork holds 96 to 33.5 mm, then 92
  at 36 mm and 84 at 40 mm. No feature reports an error at any size. The built size is 24 mm, so
  34 mm is 1.42 times the design, and nothing here plans to drive `#limbD` that far.

**Superseded, and the reason.** These three are recorded as closed rather than carried. Each asks
for work on a draft that is no longer the live one.

- **`task.capture.tutorials_1_to_5`.** draft9p0's first five pages have a hero and no frame of any
  single step. draft9p5 captures every page from empty, so the re-run it asks for is work draft9p5
  does anyway.
- **`task.reproduce.draft9p3`.** Paused 2026-09-04 with `stickbot-draft9p3-check` holding tutorial
  1 through `cad.variables.rename` and no version published. draft9p3 is not the live draft; the
  *Steps reproduce* gate it was serving moves to draft9p5.
- **`task.draft9p3.u_limb`.** Paused 2026-08-30 while the hinge was fixed. `task.draft9p4.u_limb`
  builds the same tab against the settled joints.

## What we do not know yet

- **Whether a shared Onshape document opens for an account without ownership rights.** The refusal
  on 2026-09-14 proves an unshared one does not. Nothing has tested a shared one, and the
  *Recovery point* gate wants a published named version a student can start from.
- **Why it refused.** Onshape returns one message for both cases — *document does not exist or you
  don't have permission to access it* — so the refusal does not say which. What it does say is that
  the account was signed in and the request was evaluated rather than bounced, so the test was
  performed. The id came off `reference/documents.json`, read from the model.
- **Which Onshape plan this account is on.** If it is an Education or team license rather than
  Free, then no draft has ever been built under the constraint students face, and
  `before-you-start.rst` describes a plan nobody here has used.

## What Phases 1 and 2 actually did, 2026-09-14

`68efa74` is the first commit of `stick-e-bot`: 1,479 files, 27 MB, `.git` 11 MB.

- **The ignore rules were proven before anything was copied.** A probe file at
  `instructions/stickbot-draft9p4/source/images/toolbar/` came back tracked; the same name under a
  `capture/` directory and at the repository root came back ignored.
- **`src/stickbot/check_images.py` is the fourth gate**, wired into `ninja check`. It refuses a
  tracked raster image or video outside `instructions/*/source/images/`, tracked Sphinx output, and
  any file over 5 MB — so it catches what `.gitignore` cannot, which is `git add -f`.
- **The carry list was derived from `git ls-files`, not written by hand**, and the first derivation
  was wrong: a rule dropping any path containing `/build/` swallowed all 20 files of
  `.docs/build/`, the build specification. Checking a list of must-have paths against the derived
  list is what caught it.
- **`instructions/robot-guide/` is not an archived draft and carries in full.** It holds
  `make_plans.py`, `make_brief_sheets.py`, `make_target.py` and the two plan SVGs — the design
  source, named by seven live documents. Only its committed `build/` was dropped.
- **`build.ninja` lost the targets for the six guides that did not carry**, and the comment saying
  `robot-guide`'s `build/` is committed, which is no longer true.
- **`ninja check` is green on all four gates, watched.** It first failed on `check_images.py`'s own
  docstring, which said *totaling*.

Still open from Phase 3: `CLAUDE.md` and `README.md` name the old repository, and its name appears
in 12 carried files.
