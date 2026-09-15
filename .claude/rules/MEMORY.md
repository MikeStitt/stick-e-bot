# MEMORY.md — the memories, and how to use them

Each line below names one memory and says what it holds. **Read the ones a line makes relevant to
the work in hand, before starting that work**, and operate per what they say. They are findings and
standing corrections, not obligations: where a memory and
[`constitution.md`](constitution.md) disagree, the Constitution wins and the memory is the defect.

The bodies live in [`memory/`](../../memory/) at the repository root, one file per memory, so they
travel with the repository. This index is injected on every request; the bodies are not.

A memory links to another as `[[its-name]]`, which is the other file's `name:` field and its
filename.

- [CAD models need design intent](../../memory/cad-models-need-design-intent.md) — constraints and
  variables, never magic coordinates; the model must survive a driving-dimension change.
- [Onshape API via browser session](../../memory/onshape-api-via-browser-session.md) — XSRF header,
  geometryIds, defaultScope, unstable part IDs, and why featureStatus lies.
- [The agent browser borrows its session](../../memory/agent-browser-borrows-its-session.md) — a 401
  on 9223 is a stale cookie copy; restart agent_browser.py, don't ask for a sign-in.
- [bodydetails beats featurescript](../../memory/onshape-bodydetails-beats-featurescript.md) — every
  face's surface, radius, axis and area, and it survives the 429 that kills featurescript.
- [Drawing conventions](../../memory/drawing-conventions.md) — no counts on drawings; every
  dimension carries its unit, not a word.
- [Plain words for middle-schoolers](../../memory/plain-words-for-middle-schoolers.md) — say
  "handedness", not "chirality"; keep real CAD vocabulary.
- [Instructions state facts, not
  importance](../../memory/instructions-state-facts-not-importance.md) — no selling, no
  superlatives, no token-cost boasts in prompts or briefs.
- [One fact, one home](../../memory/one-fact-one-home.md) — never restate what another file
  enforces; state it where it is enforced and link.
- [Read, Think, Plan, Do](../../memory/read-think-plan-do.md) — the default working cycle; Read
  means spec, investigation, and what happened last time.
- [Derive, don't maintain](../../memory/derive-dont-maintain.md) — never store a count or list that
  grep or Python can produce; it goes stale and lies.
- [Design intent is not sacred](../../memory/design-intent-is-not-sacred.md) — no design source
  outranks another; a constraint causing disproportionate work is itself the suspect.
- [Write for students who will succeed](../../memory/write-for-students-who-will-succeed.md) —
  advice, not warnings; say what to do and what you will see when it works.
- [Every feature gets its name](../../memory/every-feature-gets-its-name.md) — name it in the dialog
  title before you fill the dialog; a shot per click and per field.
- [Trust the user or read the docs](../../memory/trust-the-user-or-read-the-docs.md) —
  `.docs/onshape-gui-howto.md` first, then the user (Mike); testing every dialog is not a plan.
- [Capture while you experiment](../../memory/capture-while-you-experiment.md) — take named frames
  on the first pass; a debugging screenshot is not a frame.
- [CLAUDE.md is harness, not contract](../../memory/claude-md-is-harness-not-contract.md) — plumbing
  for /clear and /compact; not in scope for the prose standard.
- [Say when you carry on](../../memory/say-when-you-carry-on.md) — in an unattended run only: finish
  the ask, then name the next thing before starting it.
- [Conversation mode is not a task](../../memory/conversation-mode-is-not-a-task.md) — while the
  user is talking, answer and stop; an unanswered question is a no.
- [Never busy-wait in bash](../../memory/never-busy-wait-in-bash.md) — `read -t </dev/zero` spins a
  core; wait on the notification, not a poll loop.
- [No em dash near a number](../../memory/no-em-dash-near-a-number.md) — it reads as a minus sign;
  use a semicolon.
- [Feature edits apply live](../../memory/feature-edits-apply-live.md) — the dialog writes to the
  model as you type; only its × reverts, so escape on every failure path.
- [Fix the model, retake the frames](../../memory/fix-the-model-retake-the-frames.md) — a frame of a
  state the model no longer has is a page defect; retaking is part of the fix.
- [Counts catch what dimensions miss](../../memory/counts-catch-what-dimensions-miss.md) — every row
  can agree while the topology is wrong; count the patches too.
- [Numbers carry units](../../memory/numbers-carry-units.md) — every quantity value takes its unit
  with a space, in conversation as much as in files.
- [Draw it and print it](../../memory/draw-it-and-print-it.md) — never refuse a shape because it
  might not print as drawn; print it and let the part correct the model.
- [No invented gates](../../memory/no-invented-gates.md) — never coin a term like "signed off"; name
  the missing evidence in plain words, and update the record when a result closes it.
- [Test the technique, not a guess](../../memory/test-the-technique-not-a-guess.md) — before writing
  that a method failed, prove the run performed it in the order it specifies.
