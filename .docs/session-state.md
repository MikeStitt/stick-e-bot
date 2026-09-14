# Session state — 2026-08-11, end of run 2

Written before a hard clear. Self-contained: assume the reader knows nothing about today.

**Nothing is running.** No agents, no cron jobs. Branch `robot-course-plan`, all work committed.

## What this project is

A four-session CAD course for middle-schoolers, taught in Onshape. The subject is a **150 mm
articulated robot** — 8 unique printed parts, 14 instances, thirteen joints of two kinds. The
repo holds the text; the models live in Onshape. `.claude/rules/constitution.md` is the
contract.

## Where every model is

Version link form: `https://cad.onshape.com/documents/<did>/v/<vid>/e/<eid>`

| Document | did | eid | Version |
| -------- | --- | --- | ------- |
| `ball-socket-run2` | `b58c15803eb989fe3f676150` | `f2b99ffa760d66d00534d1cb` | `v1-ball-and-socket` `278e2c9bf3329c2d7f1244f4` |
| `hinge-run2` | `2348323d25181f7cb2a9aa9b` | `e4c380b1b66226462df485f2` | `stage-2-detents` `474270a65596f317b77999cd` |
| `lesson-run2` | `ca8494ebddc1d41126fd580e` | `67cd64530e81afd24476f8ba` | `run2-session1-complete` `24dafb83c2f7814714e20c7e` |
| `socket-in-context` | `a60ad741d213d0ee34b573ec` | `371701b2fae84ee9c9fa7acc` | design study, FeatureScript |

Run 1's five documents are frozen at `run1-archive-2026-08-11`; ids in
[`runs/2026-08-11-run1/README.md`](experiments/runs/2026-08-11-run1/README.md).

## The design, as settled today

- **Limbs Ø12** = `#torsoH / 4`. Went to Ø16 and came back; see *Why the limbs are Ø12* in
  [`robot-build-plan.md`](robot-build-plan.md).
- **Ball joint**: ball Ø6, fit 0.2, **grip 1.35** → mouth 5.803, retention 0.197. Collar Ø9.4
  standing 5.5 proud, four 0.8 slits its full length. Sweep 74°, deliberately capped there.
- **Hinge**: blade 3.0, ears 1.2, gap 0.3, **fork span 6.0**. Every layer is a **full slice of
  the Ø12 limb**, not a rectangle inside it — that is the idea the whole design turns on. Round
  end r5.81, set-back 6.11 → **±91°**, detents on 0° and ±90°. **24 teeth at 15°**, band
  r4.40–5.20 (the rim outboard of it must stay ≥0.6). Round bumps beat wedges for printing.
- **PETG, 0.4 mm nozzle.** Nothing below ~0.4 mm gets drawn; the nozzle rounds every corner to
  ~0.2 anyway.

## What run 2 proved

- **Boolean → Subtract with Offset applies uniformly over a sphere.** Mouth measured Ø5.802586
  against 5.803. The joint design rests on this and it holds.
- **The slice fork fits.** Both hinge parts measure exactly 12.000 across X and Y.
- **The lesson builds**, and its model measures right: eyes r5, mouth 20.000 overall, neck Ø12.

## What is still wrong, in priority order

1. **No build has been rebuilt from the corrected briefs.** All three briefs and the lesson were
   corrected *after* run 2 built from them. A run 3 would be the first test of the current text.
2. **Nine errors in my own briefs were found by building** — six in run 2 alone. Most were stale
   numbers carried from a superseded revision. Recompute derived numbers when a driver changes.
3. **Acceptance checks are still too weak.** A slit came out half depth and every check passed.
   Briefs now ask for the z-extent of cut faces and the thinnest wall anywhere in the part.
4. **The lesson does not fit the clock.** 82 minutes at agent pace, Part two 1.7× Part one, and
   agent pace is not student pace. Working Rule 10 and the *Fits the clock* gate are unmet.
5. **Open design questions**: the hip stand-off (still red on sheet 2); the hand's C-clip Ø10
   against a Ø12 wrist; whether to adopt the 154 mm height stack (currently drawn 150).
6. **The reorganization plan** in [`reorganization-plan.md`](reorganization-plan.md) is written
   and unexecuted — Phase 0 was superseded by the day's work, so re-read it before running it.
7. **Print orientation** blocks the edge-treatment rules — see *Future work* in
   [`README.md`](README.md). Both tab-strain calculations assume a favorable orientation
   nobody has declared.

## How the agent runs work

Read [`onshape-gui-howto.md`](onshape-gui-howto.md) before driving the browser — it is the
accumulated GUI knowledge from six builds, and every agent gets pointed at it first.

- Playwright over CDP on **port 9223 only. Never 9222** — that is the user's own browser.
- Each agent creates its own page and **stamps it with `window.name`**; identifying a page by
  title or URL finds someone else's document. This has gone wrong three times.
- Agents cannot be resumed once they complete — `ListAgents` returns empty. **Whatever you want
  from them must be a required deliverable**, which is why every brief asks for GUI lessons in
  `build-notes.md`. The Write tool refuses files named `report.md`; use `build-notes.md`.
- **Do not `git add -A` while agents are writing** to `.docs/experiments/build-log/`. Scope commits.
- A watchdog cron every ~14 min works well, but **ping a quiet agent before killing it** — that
  saved a live build once.

## Standing conventions the user has set

- **US spelling.** `uvx codespell --builtin en-GB_to_en-US <files>`. It skips hidden directories
  silently and does not know `centerline`.
- **Prose wrapped at 100 columns**, tables exempt.
- **No counts on drawings**; every dimension carries its unit. Plain words over technical ones.
- **Instructions state rules and facts — no rationale, no superlatives, no invented statistics.**
  The Constitution says what the rule is; defending it is a separate task.
- Feature branches, never `main`. Push only when asked.
