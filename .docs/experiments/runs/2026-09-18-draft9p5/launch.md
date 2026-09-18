# How to start draft9p5

The opening message for the session that builds it. It says nothing the plan says; the plan is
injected from disk once the pointer names it.

---

You are building `stickbot-draft9p5`: one Onshape document holding the whole robot, every feature
added over REST, with a feature tree that obeys every ruling settled since the parts were last
built. It writes no pages and takes no step frames.

**Do these in order.**

- Read `.claude/rules/constitution.md`, summarize the parts that bear on this work, and agree to
  follow them.
- Write `@../../.docs/experiments/runs/2026-09-18-draft9p5/plan.md` into
  `.claude/rules/active-plan.md`, replacing what is there. It currently names
  `2026-09-14-move-to-stick-e-bot.md`; that plan's Phase 5 is this one, and it stops being the
  active plan when this one starts.
- Read the plan back out of the injected instructions and confirm it arrived. A broken `@` import
  is silent.
- Invoke the `modeling-practice` skill before the first feature, and the `onshape` skill before the
  first sketch.
- Run Phase A0, then Phase A, then Phase B tab by tab.

**What you own.** The ten tabs, the four rings, `results/`, `scripts/`, and `register.md`.

**What you do not own.** The guide under `instructions/`, the briefs under
`.docs/experiments/build-briefs/`, and `src/stickbot/make_plans.py`. Ring 2 reads all three and
compares against them. Where the model and a brief disagree, the plan says to name which is wrong;
name it in `register.md` and carry on. Do not edit a brief, a sheet or a generator to make a
comparison pass.

**What is deliberately left open, and is not yours to close.** Each is in
[`../../../tasks.md`](../../../tasks.md), by number and by name.

- `task.reproduce.draft9p4` — the *Steps reproduce* gate on tutorials 4, 5, 6, 8 and 9, in a guide
  this draft does not write.
- `task.hinge.ear_rename` — `make_plans.py` still exports `EAR`, `EAR_FREE`, `EAR_MOVE` and
  `EAR_STRESS`. The briefs say *fork prong* in prose and `EAR` in the row beneath it. Both mean the
  fork's arm. Build to the plan's names and leave the identifiers alone.
- `task.briefs.section_retakes` — `cad-body-section.png` and `cad-l-limb-section.png` carry a
  selection highlight from the session that shot them. The geometry in them is sound; read them.

**The eye is yours.** The plan's § *The head, where the eye reproduces 1.5 % oversize* holds a
1.5 % departure found by reproducing `head.rst`, with two candidate causes and no read to separate
them. Phase A takes that read; Ring 2 proves the eye this draft builds.

**Where to stop and ask.**

- A ring fails twice on the same feature with two different fixes tried.
- The plan and a brief disagree about what a feature is, rather than about a number.
- Any `POST` to a document other than `stickbot-draft9p5` looks necessary. The REST grant names
  that document and no other; building anywhere else needs a fresh grant from Mike.

Checkpoint at the end of every tab: what was built, what each ring caught, what is left.
