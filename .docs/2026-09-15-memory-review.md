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
eleven memories changed. `trust-mike-or-read-the-docs` keeps its filename and its `name:`, because
those are its identity and two `[[links]]` resolve through them; only its prose and its index title
changed.

**Two copies still exist and will drift.** The harness's own store is still at
`~/.claude/projects/-Users-mikestitt-projects-first-2027-stick-e-bot/memory/`, holding the versions
as they were before this move, and the memory tool writes there rather than to `memory/`. Emptying
it is a deletion of the user's data and is not done here. `sponge`'s store is frozen with that
repository.

**What changed under them.** The contract moved to `.claude/rules/` and `.claude/skills/` and is at
5.2.0; `.parts/` no longer exists. `CLAUDE.md` no longer instructs a re-read. A new gate, *Capture
is out*, keeps interim capture out of the tree. draft9p4 becomes the reference model rather than a
guide draft. Six guide drafts stayed in the archive, and `instructions/robot-guide/` is the design
source rather than an old guide.

**Nothing is deleted.** Every memory still carries a fact or a rule that holds. Two need rewriting
rather than patching, and one of those turns on a question only Mike can answer.

## Rewrite

- **`one-guide-is-the-end-state`** — every fact in it is now wrong. It says `robot-guide` through
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

## Edit — a stated value is wrong

- **`limbs-are-twelve-mm-cylinders`** — the relation is right and the number is not. `#limbD` is
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

- **`agent-browser-borrows-its-session`** — accurate, and its rare case is live right now: the
  borrow reports no session because 9222 itself is signed out. It tells you how to recognize that
  case and does not name the way out of it, which is
  `uv run --project . python -u tools/browser.py --signin`.

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
