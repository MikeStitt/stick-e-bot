# Run 8p1 — the register

What was built, what was measured, what changed under the plan, and what is still open. The plan
is [`plan.md`](plan.md).

## Where the work is

| | |
| --- | --- |
| document | `run8p1-ball-and-socket`, `3366b856aa085aa851870fec` |
| workspace (live) | `72eecd7290f711fa143d09b4` |
| element | `75f993ba1f70767a3c3e2b4b` |
| version | `run8p1-ball-and-socket-v1`, `bd10d6c49334828ff973b9a6`, created 2026-08-19 — the one the page cites |
| version link | https://cad.onshape.com/documents/3366b856aa085aa851870fec/v/bd10d6c49334828ff973b9a6/e/75f993ba1f70767a3c3e2b4b |

**The version link was opened**, not assembled and left. It resolves to `run8p1-ball-and-socket |
Part Studio 1` with all ten variables, seven features and both parts in the tree.

The only other version is `Start` (`a49af54dafd830ad9c61aa5e`), which Onshape writes when a
document is created.

`run8-ball-and-socket` and `run7p1-ball-and-socket` are untouched and stay as they were. The page
this run wrote is a **new guide**, `instructions/robot-guide4/`; `robot-guide3` is untouched.

## Resolved

- **The joint is built from ten variables and nine expressions**, and every expression was read
  back off the feature list rather than assumed: `RADIUS #ball/2`, `LENGTH #stalk/2`,
  `DISTANCE #stud_len`, `DIAMETER #ball + 2 * #fit + 2 * #wall`, extrude `depth = #grip` and
  `secondDirectionDepth = #collar - #grip`, boolean `offsetDistance = #fit`, the slot's four
  `DISTANCE`s (`#slit_in`, `#slit_out`, `#slit/2`, `#slit/2`), and the cut's `#collar - #wall`.
  No bare number survives in a dimension box.

- **S-1 lands, but not by the route the plan drew.** The pattern's centre is a real, selectable
  sketch point that arrives coincident-looking with the origin and unconstrained. Constrain it
  and the sketch goes **fully defined**: every copy turns black. The reader's own test is the
  colour, and the harness measured it as blue pixels on the canvas — **3882 before Coincident,
  0 after**.

- **Run 8's S-5 is overturned.** *"A sketch circular pattern does not define its copies"* was
  wrong. The copies were blue because the pattern's centre was loose, not because the tool cannot
  define them.

- **S-4 confirmed by measurement.** Four slots that stop short of the middle leave material run
  8's plus removed, so `Socket body` comes out **larger**: 249.6806 mm³ against run 8's
  248.9915 mm³. `Ball stud` is 128.6210 mm³, identical to runs 7p1 and 8, which is the merge
  scope holding.

- **Every acceptance check measured.** `Ball stud`: sphere r 3.0000, cylinder r 1.5000, top plane
  z 5.000. `Socket body`: cavity sphere r 3.2000, collar cylinder r 4.7000, collar base
  z −4.150, top face in four pieces of 9.2966 mm² each (37.186 mm² total), slit floors at
  z −2.650 — so the floor is **1.500** and the cut **4.000** — slit sides at ±0.400 for a
  **0.800** slit, slit inner ends at **2.500** against a mouth radius of 2.9013.

- **S-3 kept as recommended.** The slit sketch is on the collar's top face, with run 6's
  dimensions taken onto it.

- **S-5 of run 8's plan kept.** The cut is `#collar - #wall` deep with **Merge scope** =
  `Socket body`, and nothing reopened it.

- **The ceiling's variable test is met.** `#fit` was changed from 0.2 to 0.3 through the tree and
  the model measured again: the cavity sphere went 3.2000 → 3.3000 **and the collar cylinder went
  4.7000 → 4.8000**, because the collar's diameter asked for `#ball + 2 * #fit + 2 * #wall`. Every
  feature regenerated `OK`; `Socket body` went 249.6806 → 256.5842 mm³. Put back to 0.2, the model
  measures 249.6806 mm³ and radii 3.2/4.7 again — bit for bit what it was. That behaviour is now
  the page's closing callout, and it is a better lesson than guide 3's: there the collar's outside
  was typed as 9.4 and the wall got thinner; here the wall stays 1.5 because the expression says
  it should.

- **Every frame the page names exists and Sphinx builds clean.** Nothing the page names is
  missing, nothing on disk is unused, and there is no missing-image warning.

## Changed under the plan, and why

- **S-1's box-select does not work, and the drag replaced it.** The plan said the two points sit
  on top of each other so *"a click and a shift-click cannot separate them"* and a selection box
  must pick up both. Tried: the box selects **one** point — the status bar reads a single `Point`
  — and Coincident after it leaves the blue exactly where it was. What does work is the drag the
  plan had put first for teaching: dragging from the origin carries the pattern's centre away,
  because the origin is fixed and the centre is not. That separates them, after which a click and
  a shift-click reach one each. **The undo the plan asked for between the drag and the constraint
  is gone** — Coincident snaps the pattern back itself, and undoing first would put the two points
  back on the same pixel and make them unpickable again.

- **Ten variables, not eight.** S-2's recommendation was taken: `#slit_in` = 2.5 and
  `#slit_out` = 6 have rows, so the slit sketch has no bare number in it either.

- **The rows were added to [`../../../robot-build-plan.md`](../../../robot-build-plan.md) before
  the build**, as the plan required, and its Variables section was restructured to say why there
  are two groups: four that drive the robot's size, and ten the joint is built from. The sentence
  that said the not-scaled numbers *"would not belong in the variables table"* was the one this
  run disagreed with, and it is settled there, not here.

- **Stages 10 and 11 are one script.** Reopening the slit sketch pans the view, which put a
  quarter of the pattern behind the dialog. The sketch now stays open from the first rectangle to
  the Coincident, and the figures are all from the same camera.

- **The slot's dimensions are picked off the ink, not off the coordinates.** A dimensioned edge
  goes black and stops matching the sketch-blue test, so what is still blue is exactly what has
  not been pinned. That is what tells each pick which edge it is on. The first attempt matched
  edges by their expected millimetre position instead, and an aliasing bug in the run-grouping put
  `#slit_in` on the outer edge and `#slit_out` on the inner one. **The geometry was identical** —
  the slot still ran from 2.5 to 6 — and only the intent was wrong: the variable named *how close
  to the centre* was holding the far end. That is exactly the lie this run exists to avoid, and
  nothing on the screen would have caught it, so the sketch was deleted and rebuilt.

- **Four picks moved off the centre line.** The origin's own horizontal and a dimension's
  extension line both run along y = 0, and a canvas click that lands on either clears the whole
  selection. The four sides of the slot are now picked at ±0.25 mm.

- **The count tag is found by sweeping, not by hovering under the seed.** It sits about 277 px
  right of the origin and 45 px below at this zoom, nowhere near the seed slot.

- **`bs-42` … `bs-45` were re-shot and their slugs renamed.** The four frames from the box-select
  attempt were deleted rather than kept, because they show a step the page does not describe.
  `bs-22` and `bs-29` lost the numbers from their names — `-the-depth-set-to-the-grip` and
  `-offset-all-set-to-the-fit` — since the dialogs now read expressions.

- **The frames are numbered straight through to `bs-54`.** The plan expected letter suffixes
  continuing from `bs-37d`; the slit section needed enough new frames that renumbering was the
  smaller edit.

## New this run

- **The build is on video.** `rec.py` records CDP screencast **event frames** — a frame when the
  page changes, not a frame rate — and encodes each stage at the speed it happened, so a step with
  no dialog and no green tick can be watched rather than inferred. Twelve clips, 4 MB total, live
  in `instructions/robot-guide4/source/video/` and are published to the site root by
  `html_extra_path`. `.gitattributes` sends `*.mp4` to LFS.

  Two things had to be fixed to make them usable. There is no system `ffmpeg`, so the renderer
  asks `imageio-ffmpeg` for one. And run 8's frame folders hold several interleaved runs, each
  numbering from 00001, which sorts into a timeline that steps backwards; `_timeline()` now raises
  on that rather than encoding a scrambled video, and each `Rec` writes its own directory.

- **H13.** A drag is only proof of a degree of freedom if the geometry moved. The canvas is read
  before and after and the run fails if the pixels are the same. It fired usefully: the drag
  changed 54167 pixels, which is what proved the centre was a separate entity after the box-select
  had failed.

## Not attempted

- **Whether a 1.5 mm floor lets the mouth open far enough to swallow the ball.** Only a print
  settles it.
- **The ceiling's other half.** The pattern section has not been walked from an empty document by
  someone who did not build it. Run 8 left this open and so does this run.
- **The brief's Ø12 limb stub check.** The page builds the collar on its own, with no limb stub,
  so there is nothing here to measure it against.
