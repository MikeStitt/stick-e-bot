# The build-and-verify cycle

**Superseded by [`../build/takes.md`](../build/takes.md).** This cycle runs waves of
subagents building parts from briefs; CAD is no longer handed to a subagent. The rules of it
that are still in force were carried into the retake procedure and are stated there. What is
here is history.

The loop that turns a written brief into a built, measured part — and into a corrected brief.
One pass through it is a **wave**. The robot is finished by running waves until every part
exists, then one more wave for the assembly.

This file is the procedure. It does not restate the checks:
[`../2026-08-12-launch-gate.md`](../2026-08-12-launch-gate.md) is what the launcher performs
before and after each wave, [`build-briefs/README.md`](build-briefs/README.md) is what the
agents are held to, and [`run3-launch.md`](run3-launch.md) is a worked example of a launch —
reading list, prompt tails, document names, watchdog cadence.

## Starting one

What the user says:

> Run the build-and-verify cycle for `<parts>`. Hold between waves.

Everything else has a default, and the default is stated here so it does not have to be
negotiated each time.

| Knob | Default if unsaid |
| ---- | ----------------- |
| which parts are in the wave | parts that do not depend on each other, as many as fit the clock |
| between waves | report and hold; the user launches the next one |
| retries | one, against a corrected brief, then report and stop |
| a brief that fails twice | stop and ask — see *When to stop* |
| the assembly | never in the same wave as a part it assembles |

"Hold between waves" is the safe reading and the one to say out loud. Without it the next wave
launches on the previous wave's results without the user seeing them.

### Running it unattended

What the user says when they are going to bed:

> Run the cycle for `<parts>` without me.

Three things change, and they should be said back before starting:

- **No holding between waves.** A wave launches as soon as its dependencies are met, which is
  not the same as waiting for the previous wave to finish. A part whose brief depends only on a
  joint that is already built and corrected can start immediately; only the assembly genuinely
  waits for everything.
- **"Stop and ask" becomes "park and continue."** Every decision that would have been a question
  goes into one file with what is known and what it turns on, and the work goes on around it.
  Nothing is decided on the user's behalf, and nothing is left un-built because a decision is
  pending — those are different things.
- **Commit, do not push.** The Branch Policy already says push only when asked, and being asleep
  is not asking.

**What still stops everything**: a finding that means the geometry does not exist. Everything
else runs. See *Waves*.

## One wave

**Gate the briefs, together, and write down what the gate turned up.** Per the launch gate. All
of the wave's briefs are gated before any of the wave's agents start, because a correction made
after launch does not reach an agent that has already read the file.

**Freeze the text.** From launch until the last agent reports, the briefs and
`build-briefs/README.md` are not edited. Findings are collected and applied afterwards. This is
the rule that run 3's first attempt broke.

**Launch the wave together**, each agent in its own new Onshape document, named for the part and
the run. Record every agent's id in the run directory as it starts — the id is the only way to
interview a finished agent, and it does not outlive the launching session.

**Watchdog.** Poll each agent's `steps.log`; a log that has not moved is not proof of death, so
ping before killing. `run3-launch.md` carries the cadence and the grace period, both set by what
went wrong before.

**A watchdog that reads file age is blind across a handover.** When a replacement agent takes
over a dead one's document, it inherits the dead agent's `steps.log`, and the file's age keeps
counting from the *predecessor's* last write. The log looks hours stale while the new agent is
working normally through its reading list — which is long, because a replacement is given the
predecessor's notes on top of the usual briefs. Run 3 raised this false alarm on every handover.

The fix belongs in the prompt, not the watchdog: **tell a replacement agent to append a handover
line to `steps.log` as its first action, before it reads anything.** One line, and file age
starts telling the truth again.

**Verify each part yourself, before reading anything the agent wrote.** Open it at its published
version, turn it, take the measurements the brief asks for. Reading the report first tells you
what to expect and you will see it. This ordering is the point of the whole step.

**Then say what the part does next, and what would stop it.** The measurements a brief asks for
are that brief's own idea of what can go wrong, so a part can satisfy every one of them and still
be unusable. For a robot part the next thing is a mate: name it, then name what would prevent it —
nothing retaining the ball, no swing, a face that binds first. This is the last question answered
before a part is accepted, and every brief's acceptance checks carry it. Run 3's head passed every
measurement in its brief with a socket no ball can enter, no relief slits, and a 1 mm collar
against a specified 5.5.

**Interview each agent.** A retrospective, not a cross-examination — the launch gate says what to
ask and why. The agent is the only witness to where the brief failed it.

**Fold the findings into the briefs.** Into the brief, not only into the run's notes. A finding
that lives in a build-notes file is a finding the next agent will not read. If a number moved,
change the generator that draws it, not the prose about it.

**Then decide: accept, retry, or stop.**

## Retries

A retry is a fresh agent, against the corrected brief, in a **new empty document**. Never reopen
the failed one. A half-built document hides the thing the retry exists to test — whether the
corrected brief gets someone from nothing to the part.

What changes between attempts is the **brief**. If nothing about the brief changed, the retry is
the same experiment and will teach the same thing.

Name the retry's document for the attempt, so the failed one stays inspectable rather than being
overwritten.

## Waves

**Parts first, in any order that respects their dependencies.** A joint is a part. Two parts that
share no numbers can be built in the same wave by different agents.

**Every part of this robot carries a joint**, so every part wave inherits whatever the joint
waves found. What it inherits is only the numbers, though — see below.

**Only a finding that stops the geometry existing blocks the next wave.** A number that moved, a
feature that cannot be built, a face that comes out square when the brief says round: let one of
those through and it is embedded in every part built afterwards. A finding that means the joint
will not *work* — the detent will not click, the socket will not retain, a wall is too thin to
survive a print — does not block anything. The part still models, still mates, still assembles;
only the printed plastic cares. Carry it forward and mark it not print-ready.

Mike's framing, 2026-08-12: *"push forward with imperfect joints, because you can make all of
the body parts, you can even mate them, the broken joints just won't work in the physical 3d
printed world."* Waiting for a joint to be perfect stalls eight parts on a defect a printer
finds and a CAD model does not.

**The assembly is its own wave**, and it cannot start until every part it uses has been built and
published as a named version. Built, not sound — a robot assembled from parts that will not print
still proves the mates and the degrees of freedom. It differs from a part wave in what gets
verified: mates and degrees of freedom rather than extents and wall thicknesses, and whether the
robot moves the way the plan says rather than whether a face measures what it should.

**A wave is most of a session.** The Constitution's clock applies to the launcher too — the gate,
the watchdog, the verification and the interviews are all hands-on time, and they run longer than
the building does.

## When to stop and ask

- **A brief fails twice for different reasons.** Once is a brief defect. Twice, in two places,
  usually means the design is wrong rather than the words describing it, and that is the user's
  call and not a thing to iterate on.
- **A finding contradicts a settled decision.** Settled means decided in conversation and
  recorded. An agent hitting one is a reason to check the record, not to reopen it — run 3's
  first attempt was thrown out for launching against a conflict that had been settled the day
  before.
- **The measurement disagrees with the report and the agent cannot say why.** Something happened
  that neither of you understands yet.

**Unattended, every one of these is parked rather than asked**, in a single file the user reads
in the morning: what was found, what it turns on, what the options cost, and — where there is
one — the cheap answer. A parked decision that stops a part being built is a decision made by
default, so build to the number as written, measure, and report the gap.

**One thing is never parked: an agent breaking a standing rule.** Run 3's hinge agent reached
into port 9222 to recover the shared Onshape session after it signed out for every agent at
once. It reported it at the top of its notes rather than burying it, which is what the contract
asks for, and it goes at the top of the parked file too — not among the design questions.

## What ends the cycle

Every part built, measured and published at a named version; the assembly built from those
versions and moving; and every brief carrying what its run found. What is left after that is the
lesson, which is tested by a different loop — a student following the written steps from an empty
document, not an agent following a brief.
