---
name: constitution-maintenance
description:
  "The amendment workflow for the contract, and the dated changelog. Read before changing
  .claude/rules/constitution.md, any file under .claude/rules/parts/, or any of these skills."
---

# Constitution — Maintenance part

Read this part **only** when you are amending the constitution itself
(`.claude/rules/constitution.md` or any file under `.claude/rules/parts/`). It
records the maintenance plan — how amendments are made and versioned — and holds
the full **Changelog** moved out of the always-read core so that core stays lean.
Read together with the [constitution](../../rules/constitution.md)'s Governance
section.

**Amendments**: any change to this constitution MUST be documented with a version
bump and rationale.

**Versioning**: semantic. MAJOR — principle removals or incompatible
redefinitions. MINOR — new principles or material expansions. PATCH — wording
clarifications and typo fixes.

## Maintenance plan

Amending the constitution is itself governed work; treat the rules below as the
checklist for any change to `constitution.md` or a part.

1. **Edit the right home.** Behavioral rules and the always-read core live in
   `constitution.md`; per-work-type detail lives in `.parts/`. Change a rule in
   exactly one place — never duplicate it into the agent-doc pointer
   (`CLAUDE.md`).
2. **Bump the version.** Apply the semantic rule from Governance: MAJOR for
   principle removals or incompatible redefinitions, MINOR for new principles or
   material expansions, PATCH for wording clarifications and typo fixes. Update
   the `**Version**` and `**Last amended**` line in `constitution.md`.
3. **Record it in the changelog.** Add a dated entry to the
   [Changelog](#changelog) below — newest first — stating what changed and
   _why_. The rationale is the valuable part; a bare "updated X" is not enough.
4. **Update companions in the same commit.** If the change has an on-disk
   companion (e.g. the `check` target, its dictionary, or a hook that enforces
   the rule), change it in the same commit so the documented rule and its
   enforcement never drift apart.
5. **Exercise config companions, don't just edit them** (Working Rule 8, and
   _Verification is evidence, not assertion_). A rule whose enforcement lives in
   config is only amended once the config has been _run_ and shown to behave as
   intended — editing the file is not verification. Run the `check` target and
   watch it catch what the new rule is meant to catch.

## Changelog

- **5.1.0 (2026-09-14)** — MINOR: the contract moves into `.claude/`, and a new Working Rule
  requires the active-plan pointer. `constitution.md` becomes `.claude/rules/constitution.md` and
  `prose-style.md` becomes `.claude/rules/parts/prose-style.md`; the other four parts become skills
  under `.claude/skills/`. A new part,
  [`../../rules/parts/plan-activation.md`](../../rules/parts/plan-activation.md), says how a plan
  becomes active and how it stops being active. The Parts table gains a column for how each part
  arrives, and the obligation to invoke a skill before the work it governs begins.

  _Why:_ the contract reached context by a ritual re-read named in `CLAUDE.md`, and the ritual did
  not fire. Across draft9p4 it came due about 35 times, `constitution.md` was read twice, and the
  active plan was never read at all. A file re-read after a compaction comes back as a bare path
  once it passes roughly 5,000 tokens, so the 10,342-token run plan was the document most certain
  to be missing. Everything under `.claude/rules/` is injected from disk on every request, which is
  not subject to that limit and does not depend on anybody remembering.
  [`../../../.docs/2026-09-14-contract-into-claude-rules.md`](../../../.docs/2026-09-14-contract-into-claude-rules.md)
  holds what was measured and what was proven.

  No rule is removed or redefined, which is why this is a MINOR. The one new obligation is the
  pointer; the agreement to follow the constitution is unchanged and stays unconditional on a plan.

  _Companion changes, same commit._ `CLAUDE.md` keeps the agreement and drops the instruction to
  re-read a file that is now injected. `.gitignore` ignores `.claude/*` and re-includes `rules/`
  and `skills/`. Live references across `.docs/`, `README.md`, the draft9p4 plan and two tools were
  repointed; references in archived run records were left pointing at where the files lived when
  they were written, and the constitution's Archive section now says that is what they mean.

  _Config companion, exercised._ `check_wrap.py` and `check_spelling.py` build their file lists
  from `git ls-files`, so they followed the contract into `.claude/` without being changed. Both
  were run over the moved tree; the wrap check caught eight lines the new paths pushed past 100
  columns, which were re-wrapped. `check_reading_level.py` never covered the contract and is
  untouched. Nothing enforces the new Working Rule, so there is no companion to exercise for it.

- **5.0.0 (2026-08-18)** — MAJOR: *use a variable wherever a number repeats* is removed. A
  measurement becomes a variable **only when the build plan asks for it** — the Variables table in
  [`.docs/robot-build-plan.md`](../../../.docs/robot-build-plan.md) is the whole ask, and a number
  is a variable when it has a row there and not otherwise. A session plan, a build brief or a run
  plan may argue for a row; it does not create one. Every other measurement is typed, and a
  constraint or a reference carries the intent. Changed in [`onshape.md`](../onshape/SKILL.md) and
  [`modeling-practice.md`](../modeling-practice/SKILL.md).

  This is a principle removal and an incompatible redefinition, twice over: a model that types a
  repeated number, which the old rule rejected, now passes; and a model that declares a variable no
  row asks for, which the old rule required, now fails.

  _Why:_ the old rule decided a design question by standing rule rather than where the design is
  recorded, so it produced variables nobody asked for and nobody was responsible for keeping true.
  4.0.0 had already bolted on a bound, *not every variable is a scaling knob*, which was the
  everywhere rule over-reaching and being patched instead of narrowed. Naming the build plan as the
  single asker also gives the vocabulary one owner: a variable is a promise that a number means the
  same thing in every part that uses it, and that promise cannot be made by a document that sees
  one part.

  What does not change: constraints, fully defined sketches, anchoring each sketch to the geometry
  that gives it meaning, and the ban on a typed number standing in for a reference. The acceptance
  test in [`modeling-practice.md`](../modeling-practice/SKILL.md) still requires that changing one
  driving dimension reproportions the model rather than breaking it; it no longer assumes that
  dimension is a variable.

  _Companion change, same commit._ [`.docs/robot-build-plan.md`](../../../.docs/robot-build-plan.md)
  is the ask, so it was cut from 24 rows to the four numbers a student changes to make the robot
  their own: `#torsoH`, `#torsoW`, `#torsoD` and `#limbSeg`, the three torso numbers now independent
  of each other rather than expressions on the height. The other nineteen measurements moved to a
  **Proportions — recorded, not driven** table that keeps the ratio each came from, so promoting one
  later is a decision rather than a re-derivation. The 27 references to the retired names in the
  plan's prose became plain dimensions.

  _What this costs._ `run7p1-ball-and-socket` holds eight variables and not one of them now has a
  row. `#wall`, `#collar`, `#slit` and `#stud_len` never had one; `#ball` and `#stalk` were the
  plan's `#ballD` and `#stalkD` under other names; `#fit` and `#grip` are typed measurements from
  this commit on. Run 7's `M1` asked for all eight, and from this version an ask in a run plan is
  not an ask. So `instructions/robot-guide3/source/ball-and-socket.rst`, which teaches those eight
  as its opening move and shows them in 47 captured frames, no longer matches the contract.
  Rewriting it is open and is not decided here.

  No config companion enforces the rule, so maintenance step 5 has nothing to exercise; the check
  target was run and its state reported.

- **4.0.1 (2026-08-17)** — PATCH: `.parts/onshape.md` drops the sentence *a tool used once is a
  tool forgotten by the next week*. _Why:_ it was a maxim standing in for a reason, and it is not
  true of this course. Eight hours cannot introduce every feature a robot needs and then use each
  one twice; a tool that appears once and does its job is a tool the class got the use of. Quoting
  the maxim was about to decide whether **Shell** stays in the course, which is a judgment about
  the robot, not a rule that can be applied from a sentence.

  The obligation it was attached to — *reuse each one at least twice in the same session* — is
  unchanged, which is why this is a PATCH and not a principle removal.

- **4.0.0 (2026-08-17)** — MAJOR: `.parts/onshape.md` no longer says **sketch on planes over
  faces**. That principle is removed, not reworded, and the rule that replaces it can be violated
  by a model the old one approved, so it is an incompatible redefinition. The new rule is
  **anchor each sketch to the geometry that gives it meaning** — a plane when the shape is placed
  from the origin, a face or edge when it is placed from a part.

  _Why:_ the old rule was written on 2026-08-10 in `8630961`, the bulk rewrite that created the
  file, before anything in this repository had been modeled; the earliest run is dated the next day.
  It had no build behind it, and it hid a defect rather than preventing one. A sketch put on the Top
  plane because the collar happened to be extruded from the Top plane still depends on that collar —
  the dependency is simply no longer recorded anywhere, so moving the collar leaves a model that
  regenerates clean and is wrong. Avoiding faces is also what is expensive over the REST API rather
  than what is wrong in the UI, which is the failure
  [`modeling-practice.md`](../modeling-practice/SKILL.md) already names: _never let the tool dictate
  the pedagogy._ The two files had been pulling against each other, one condemning magic numbers
  while the other produced them.

  Carried in the same amendment: **not every variable is a scaling knob.** A joint's dimensions
  come from how the plastic bends, not from how big the robot is, so the change-one-number
  demonstration belongs on a major shape and never on a joint. Without it, _use a variable wherever
  a number repeats_ invites a student to scale a ball and break its fit.

  No config companion enforces either rule, so maintenance step 5 has nothing to exercise; the
  check target was run and its state reported.

- **3.2.1 (2026-08-12)** — PATCH: Working Rule 8 says what a step is — a
  software or hardware build, a calculation, an analysis, a compilation, a test,
  a validation, a verification — so "surface every skipped step" cannot be read
  as covering only the written instructions. The same edit restores two
  obligations 3.2.0 dropped, *every assumption you could not check* and *if a
  step failed, say so and describe it*, and removes two it had imported from the
  source that describe a file installer rather than this repo: *refused
  overwrite* and *missing dependency*.

- **3.2.0 (2026-08-12)** — MINOR: a written prose standard, and this file
  rewritten to obey it. `.parts/prose-style.md` names four sources — Kernighan
  for the register, Bloch's *Effective Java* for the shape of a rule, Strunk for
  omitting needless words, RFC 2119 for obligation vocabulary — and the seven
  rules that follow from them. It is now the first row of the Parts table,
  required for any writing, and a Quality Gate. _Why:_ the rules against
  overwriting were all unenforced prose, and the file kept growing by rewording.
  A standard that names what a rule looks like is checkable by a reader in a way
  that "be concise" is not.

  Applied to this file: six rule titles that were labels became the obligation
  itself, so a reader who stops at the bold lead still knows what to do —
  *Simplicity first* became **Build the simplest thing that solves the problem**,
  *Surgical changes* became **Touch only what the task requires**, and likewise
  for rules 1, 5, 6, 13 and 15. RFC 2119 words were capitalized where an
  obligation is actually being set. Three duplications were cut: the *Timing must
  be measured* note restated Working Rule 9, the `shadedviews` paragraph restated
  the bullet above it, and the Governance compliance bullet restated Branch
  Policy.

- **3.1.0 (2026-08-12)** — MINOR: the rules the source constitution carried were
  brought back to their original wording, widened from code to content (code,
  prose, or CAD) where the domain was the only thing that differed. _Why:_ a
  side-by-side of the two files showed the Working Rules had grown 67% — 426
  words to 712 — for the same obligations. The growth was rewording, not new
  rules, and rewording without a rule change is drift. Two principles were
  restored that adapting had dropped:
  - **Small, bounded, side-effect-free** (source rule 7), which had no
    counterpart here, generalized to sentences and paragraphs in prose and
    sketches in CAD.
  - **Documentation is part of the change** (source _Documentation Hygiene_),
    now Working Rule 13. A documentation gap is a defect, not a follow-up.

  Also carried forward: the source's **never force-push or rewrite published
  history** clause into Branch Policy, and its **scratch / probe script escape
  hatch** into the Quality Gates notes, where it documents what
  `tools/check_*.py` already skips. The rules renumbered 1–15; two rules had
  both been numbered 7.

- **3.0.0 (2026-08-12)** — MAJOR: the course subject changed from SpongeBob to a
  150 mm articulated robot figure, and the **character and artwork** principle
  was **removed** rather than reworded. A principle removal is a major bump.
  _Why:_ that principle existed to keep a rights holder's character inside the
  classroom — no copyrighted reference art, nothing published or sold. An
  original robot has no rights holder, so the rule had nothing left to enforce
  and keeping a reworded version would have implied a constraint that no longer
  applies. Carried in the same reorganization:
  - **Governance** and this maintenance part, both adapted from the
    `book-em-danno` constitution. Before this there was no written rule for
    changing the rules, so amendments left no version bump and no rationale.
  - `parts/` became **`.parts/`** and gained `modeling-practice.md`, which opens
    by declaring itself the standard every model must meet — contract text that
    had been filed as a working note. Session material moved out to
    `instructions/`; the Parts section now describes both, plus the audience
    rule that decides which folder anything else goes in.
  - Working Rule 8 gained a **no grandstanding, no hyperbole** clause: claim
    success, justify a rule, or persuade a reader or subagent only from
    established, provable information.
  - Two new Quality Gates, **Spelling** and **Reading level**, with the
    on-disk companion they need: `build.ninja`'s `check` target over
    `tools/check_wrap.py`, `check_spelling.py`, `check_reading_level.py` and
    `tools/dictionary.txt`. Per maintenance step 5 it was **run**, not merely
    written — the first run found 118 British spellings and 2 over-long lines.
    The compound the plan sheets use for the vertical axis is not in the builtin
    dictionary and was caught only after `tools/dictionary.txt` was added, which
    is why the project dictionary exists at all.
- **2.0.0 (2026-08-09)** — the version this changelog opens at. Recorded from
  the footer rather than reconstructed: adapted from the **mostrobotpy
  constitution v1.0.0** and repurposed for this Onshape CAD course. It keeps
  that structure — a lean always-read core plus per-work-type parts, and the
  numbered Working Rules — and carries the rules this course needs: the
  eight-hour budget, floor and ceiling, a published recovery version per
  session, and Quality Gates that make a written step prove itself before it is
  called done. Entries before this one were not kept, so this is where the
  history starts.

## See also

- [`.claude/rules/constitution.md`](../../rules/constitution.md) — Working Rules, Quality Gates, and
  the Governance section this part expands.
