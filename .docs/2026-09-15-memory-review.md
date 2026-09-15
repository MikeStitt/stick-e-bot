# The memories, reviewed against the move

Twenty-nine memories, moved into the repository on 2026-09-15 so they travel with it. This file
says what to do to each one and why. The verdicts below are still owed; the move happened first.

**Where they are.** The bodies are in [`memory/`](../memory/) at the repository root, one file per
memory. The index is [`.claude/rules/MEMORY.md`](../.claude/rules/MEMORY.md), which is injected on
every request and carries a one-line hook and a pointer per memory. The bodies are not injected: a
hook is what decides whether a body is worth reading. All 29 come to 12,232 tokens against a
contract of about 12,600, so injecting them would roughly double what every request carries.
Whether a hook is enough to make a memory get read is being tried, not assumed.

**Nobody is named in a rule any more.** A role reference and a dated attribution alike now read
*the user (Mike)*, so the contract does not hardcode who is at the other end. Eighteen lines across
eleven memories changed. `trust-mike-or-read-the-docs` became
`trust-the-user-or-read-the-docs` on 2026-09-15; its `name:`, its filename and both `[[links]]`
moved together.

**The harness store is emptied.** It held the pre-move copies and would have drifted, so on
2026-09-15 its 29 bodies were deleted and its `MEMORY.md` replaced by a pointer saying the
memories live in the repository and that a new one belongs there, not beside it. `sponge`'s store
still holds all 30 files unchanged and is the backup.

**What changed under them.** The contract moved to `.claude/rules/` and `.claude/skills/` and is at
5.2.0; `.parts/` no longer exists. `CLAUDE.md` no longer instructs a re-read. A new gate, *Capture
is out*, keeps interim capture out of the tree. draft9p4 becomes the reference model rather than a
guide draft. Six guide drafts stayed in the archive, and `instructions/robot-guide/` is the design
source rather than an old guide.

**Nothing is deleted.** Every memory still carries a fact or a rule that holds. Two need rewriting
rather than patching, and one of those turns on a question only Mike can answer.

## Deleted 2026-09-15, second pass

- **`one-guide-is-the-end-state`** — the opposite finding to the limb memory, and it landed the
  same way. That one was a stale duplicate of the design source; this one was the **only** copy of
  a real rule. Nothing in the Constitution said not to edit a superseded draft: the Archive section
  covers `.docs/experiments/`, and § *Where developmental draft products live* said drafts are kept
  side by side to show the differences and stopped there. So the rule moved into that section as
  **Write and fix only the live draft** at 5.4.0, and the memory went, its facts being what had
  gone stale.

## Rewrite

- **`one-guide-is-the-end-state`** — *superseded by the deletion above.* Every fact in it is now
  wrong. It says `robot-guide` through
  `robot-guide3` are archival and `robot-guide4` is live. `robot-guide4` stayed in the archive,
  `instructions/robot-guide/` is the design source and not a guide at all, and the live guide is
  `stickbot-draft9p4`, which is about to stop being a guide and become the reference model. The
  rule underneath survives and is worth keeping: one guide is the end state, and a superseded
  guide's defect is history rather than a bug.

- **`claude-md-is-harness-not-contract`** — its mechanism is gone. It says `CLAUDE.md` exists to
  make the agent re-read `constitution.md`, and that this is why it sits outside
  `.parts/prose-style.md`. The re-read instruction was removed on 2026-09-14 and the contract is
  injected from disk instead. What remains in `CLAUDE.md` is the agreement, 377 tokens that arrive
  on every request. **Whether the prose standard now governs it is a question for Mike**, not
  something to decide inside a memory: if it does, this memory is simply wrong and goes; if it does
  not, it needs rewriting around the new mechanism.

## Deleted 2026-09-15

- **`limbs-are-twelve-mm-cylinders`** — deleted rather than corrected, because everything in it is
  already in [`robot-build-plan.md`](robot-build-plan.md) § *Stage 5 — Limbs*, said correctly.
  That section opens: *"Every limb is now a `#limbD` cylinder — Ø12 at the 48 mm robot and Ø24 at
  this one — and joints are sized to fit inside it, never the limb grown to fit a joint, so the
  four sections below do not exist. The four routes were teaching tools, not sections, and the
  route is what gives way, not the diameter."* Each of the four rows is marked *no home*, and
  lines 346 to 352 carry the reasoning — the 12 mm x 11.6 mm paddle standing 2.5 mm proud, and the
  joint having been *scaled off the torso instead of off the nozzle*.

  The memory was a second copy that went stale while the original stayed true, which is what
  [[one-fact-one-home]] and [[derive-dont-maintain]] exist to prevent. It was wrong twice: the
  value, and its own closing claim that the decision *lives in no single file*. Nothing was lost.
  The habit it ended on is the fourth Read sub-step of [[read-think-plan-do]], and that memory's
  link to it now points at Stage 5 instead.

## Edit — a stated value is wrong

- **`limbs-are-twelve-mm-cylinders`** — *superseded by the deletion above.* The relation is right
  and the number is not. `#limbD` is
  `#torsoH / 4`, which the memory states correctly, but `#torsoH` is `96 mm`, so the limb is
  `24 mm` across and not `12 mm`. The design went to 2x and the memory did not. Its name, its
  index line, and the clevis inequality it quotes are all at the old scale. This is the one with
  teeth: dimensions are the whole subject here, and a memory asserting a diameter that is out by a
  factor of two will be believed.

  Recorded alongside: `robot-build-plan.md` opens by calling this *a 150 mm articulated figure*
  while its own line 713 says the 150 mm was a target the stations were fitted to. At `#torsoH`
  `96 mm` the robot is not 150 mm tall. That is a defect in the design source, not in the memory,
  and it is reported rather than fixed here.

## Edit — a path moved

- **`instructions-state-facts-not-importance`** — *"Applies to `constitution.md` and everything in
  `parts/`"*. Now `.claude/rules/constitution.md`, `.claude/rules/parts/` and the four skills.
- **`no-invented-gates`** — *"Nothing in `constitution.md`, `.parts/` or `.docs/build/` defines
  it"*. Same repoint.
- **`numbers-carry-units`** — names `.parts/prose-style.md` as what enforces the document half.
- **`feature-edits-apply-live`** — links `[[bodydetails-beats-featurescript]]`, and the file is
  `onshape-bodydetails-beats-featurescript`. A broken link inside a memory is silent the same way a
  broken `@` import is.

## Edit — a rule changed around it

- **`capture-while-you-experiment`** — still right that frames are taken on the first pass through
  a click sequence. But it argues from *"they are discarded with the scratchpad"* as a loss, and
  under the *Capture is out* gate the scratchpad is now where capture is supposed to live. The
  memory needs the new boundary: shoot on the first pass, keep it in the scratchpad, and a frame
  enters git only by being placed on a page. Without that it reads as arguing against the gate.

- **`every-feature-gets-its-name`** — *"Type the name into the feature dialog's title before
  filling the dialog in — this works for every feature type"*. It does not work for a variable.
  The `onshape` skill records that the Variable dialog has no rename pencil, its tree row offers no
  *Rename*, `F2` does nothing, and a page must not tell a reader to name one. The memory
  over-generalizes without the exception.

- **`agent-browser-borrows-its-session`** — *done 2026-09-15.* Cut back to the failure mode, which
  is the only part no file carries: `.docs/browser-access.md` describes the borrow, the session
  cookie and what a restart costs, and never mentions 401 once. What is left is the rule — a 401
  from 9223 means restart the agent browser, not ask for a sign-in — the one exception that does
  need a person, and the way out of it. Its `type:` becomes `feedback`, which is what it always
  was.

## Edit — a link that points at nothing

- **`drawing-conventions`** — links `[[robot-plan-sheets-are-generated]]`, which has never been
  written. The fact it gestures at is load-bearing and now more so: `make_plans.py` under
  `instructions/robot-guide/` renders every plan drawing from the numbers, and it is one of the few
  things that carried out of `instructions/`. Either write that memory or drop the link.

## Keep unchanged

Eighteen. Each states a rule or an observed fact that the move did not touch:
`cad-models-need-design-intent`, `conversation-mode-is-not-a-task`,
`counts-catch-what-dimensions-miss`, `derive-dont-maintain`, `design-intent-is-not-sacred`,
`draw-it-and-print-it`, `fix-the-model-retake-the-frames`, `never-busy-wait-in-bash`,
`no-em-dash-near-a-number`, `one-fact-one-home`, `onshape-api-via-browser-session`,
`onshape-bodydetails-beats-featurescript`, `plain-words-for-middle-schoolers`,
`read-think-plan-do`, `say-when-you-carry-on`, `test-the-technique-not-a-guess`,
`trust-mike-or-read-the-docs`, `write-for-students-who-will-succeed`.

`one-fact-one-home` is the one to look at twice and leave alone. Its worked example is the
Constitution restating a ritual that `CLAUDE.md` used to enforce, and that ritual no longer exists.
The example is history and it still illustrates the rule, so rewriting it would be polishing.

## Order to do them in

The value error first, because it is the one that can produce wrong geometry. Then the paths,
which are mechanical. Then the three rules, which need a sentence each. Then
`one-guide-is-the-end-state`. `claude-md-is-harness-not-contract` waits on Mike.

`MEMORY.md` carries a one-line hook per memory and two of those lines change with the bodies: the
`limbs-are-twelve-mm-cylinders` hook states `Ø12`, and the `one-guide-is-the-end-state` hook names
`robot-guide 1-3`.
