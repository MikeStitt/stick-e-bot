# Run 1 — 2026-08-11

The first attempt at building the robot's parts with agents. **Frozen.** Nothing here is live;
the models were re-versioned in Onshape before run 2 started, so these links cannot move.

Read this before run 2's results, because most of run 2's briefs exist because of what went
wrong here.

## What was built, and where it is

| Directory | Onshape document | Frozen version |
| --------- | ---------------- | -------------- |
| `ball-and-socket/` | `joint-ball-socket` `dc438a192a01922a9d1ee540` | `run1-archive-2026-08-11` — `5d05ffbe66fa756558cc06b5` |
| `hinge/` | `joint-hinge` `d2f74513ef2f1a7d753a7240` | `run1-archive-2026-08-11` — `c211c28fdabe69ca77a2da49` |
| `lesson-test/` | `lesson-test-4` `c86d7c73e0b468c35d9e86fb` | `run1-archive-2026-08-11` — `380dac31299ddb5f09e565a9` |
| — | `robot-lesson-test-3` `eac50b6ec48f8a12dec5fdac` | `run1-archive-2026-08-11` — `ee0f7823048dc86891dd7fa1` |
| `socket-in-context/` | `socket-in-context` `a60ad741d213d0ee34b573ec` | `run1-archive-2026-08-11` — `fd349d8e2ace5ef92a5a8c81` |

Version link form: `https://cad.onshape.com/documents/<did>/v/<vid>/e/<eid>`.

`socket-in-context` is not an agent build — it is a FeatureScript design study written to show
what the socket looks like added to a head block and to a limb. It also holds the validated
ball-and-socket part, brought in with a **Derived** feature.

## What each run produced, in one line

- **ball-and-socket** — the crux question answered: **Boolean → Subtract with Offset applies
  uniformly over a sphere.** Mouth measured Ø4.99600 against Ø4.996 expected. 147 screenshots.
- **hinge** — stage 1 built and measured on spec; stage 2 teeth on the clevis only. Proved the
  brief's tooth geometry was **impossible as written**, and that Ø12 left only 0.2 mm of clevis
  wall. 43 screenshots.
- **lesson-test** — followed `index.rst` end to end and completed the model, but found that
  **Escape silently discards the last typed dimension** and that four Part-two steps cannot be
  performed as written. 182 screenshots.

## Why run 2 exists

Three things, in order of how much they cost:

1. **The briefs specified geometry that could not exist.** The hinge's teeth overlapped by
   0.9 mm at nominal; the ball socket's `grip` was defined one way and built the other, with an
   acceptance check that passed either way. Both were found by building, not by reading.
2. **Nobody looked at the models.** The reports were numerically perfect and still left the
   wrong shape in the reader's head — the ball socket's relief slits were described as present
   and were, in the agent's own words, "decorative". This produced the **Model inspected** gate
   in the Constitution.
3. **Every agent re-learned the Onshape GUI from nothing**, at 350–525k tokens each. That is
   what [`../../onshape-gui-howto.md`](../../onshape-gui-howto.md) exists to stop.

## What changed between run 1 and run 2

- Limbs **Ø16 → Ø12** (and briefly the other way; see *Why the limbs are Ø12* in the plan).
- Hinge fully respecified: blade 3.0, ears 1.2, fork as **slices of the limb** rather than a
  rectangle inside it, 24 teeth at 15° cut as a wave.
- Ball socket `#grip` **2.0 → 1.35**, giving 0.2 mm of retention interference.
- Every brief now requires a **"Where the work is"** section and a published version.
