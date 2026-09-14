# Retrospective — what the agent runs have taught, across runs 1 and 2

**Synthesized, not interviewed.** An agent that has finished cannot be reached — `ListAgents`
returns empty — so runs 1 and 2 could only be read back out of what they wrote. Everything below
is quoted or drawn from the six `build-notes.md` and `report.md` files under
[`runs/`](runs/). From run 3 onward a retrospective is a required deliverable, written by the
agent about its own run, so the next version of this file will have first-hand answers in it.

That gap is itself the first finding: **whatever you want from an agent has to be asked for
before it starts.**

## What went well

- **Rendering each part on its own caught what every number missed.** Twice. The ball-and-socket
  agent rendered the socket alone and found relief slits 2.7 mm deep against 5.5 specified,
  after every acceptance number had passed. The hinge agent found the entire fork invisible in
  all four standard whole-model views, because the parts overlapped along the camera axis — the
  joint had never actually been looked at. This is now a rule in every brief.
- **One crux question, answered decisively.** Both joint briefs named a single measurement that
  would settle the design. Subtract-with-Offset applies uniformly over a sphere: mouth measured
  Ø5.802586 against Ø5.803. The question was worth more than the part.
- **`steps.log` made slow distinguishable from dead.** An "about to" line before each action and
  a "result" line after is what let a quiet agent be pinged instead of killed — which saved a
  live build in run 2.
- **The how-to stopped the re-learning tax.** Every run-1 agent rediscovered the Onshape GUI
  from nothing, at 350–525k tokens each. Run 2's agents read
  [`../onshape-gui-howto.md`](../onshape-gui-howto.md) instead.
- **Measurement routes were named, not just results.** "FS `evSurfaceDefinition`", "off
  Onshape's own bottom-right readout, photographed". A number whose provenance is stated can be
  disbelieved; one without cannot.

## What went poorly

- **Stale numbers survived a driver change.** Six brief errors in run 2 alone, and almost all
  were the same failure: a driving dimension moved and the numbers derived from it did not.
- **Acceptance checks passed on wrong parts.** The half-depth slit passed every headline
  dimension. A socket built upside down measures the same mouth as a correct one — 2 × √(3.2² −
  1.35²) either way — and is distinguished only by cavity volume, 109.48 mm³ against 27.78.
- **Direction errors were caught by volume, not by preview.** The hinge agent built, checked,
  found wrong and rebuilt four features — the stub twice, once as a 226 mm circle and once
  pointing into the ear — and reported that "all three direction errors were caught by volume,
  not by looking at the preview."
- **The modeling standard was not followed, and the agent said why.** The hinge model has no
  variables at all: 6.11 typed in four places, 12 in two. Its notes say variables have to
  precede the features that use them, and it realized too late to re-roll the tree safely.
- **Timings mean nothing and keep being collected.** One run reports 82 minutes, another
  "several hours", and both say the same thing about it: the cost was not modeling, it was that
  every dialog field had to be picked by coordinate and verified by screenshot. Agent pace is
  not student pace and never will be.
- **The same gate has been unmet three runs running.** No link has ever been checked from a
  student-level account. Every report says so honestly, and nothing changes, because no agent
  can fix it.
- **Ambiguous phrasing cost a guess.** "About 10 wide and 10 tall", of a profile drawn to one
  side of a revolve axis, could mean Ø10 or Ø20. The agent picked Ø10 and said so.

## What to change

1. **When a driver moves, recompute everything downstream in the same edit.** This is the single
   largest source of error across both runs. It is a rule about editing, not about CAD.
2. **Every acceptance check must be able to fail on the specific wrong part it guards.** If a
   check passes on both the right build and the failure it was written for, it is not a check.
   The cavity-volume and slit-z-extent checks exist because of this and both now appear in every
   brief that has a socket.
3. **Put variables in a Variable Studio**, so ordering stops mattering and a model can be given
   its variables after the fact. The hinge agent's own recommendation.
4. **Stop asking for timings that cannot mean anything.** Ask for the *shape* of where the time
   went — which steps dominated and why — and say in the prompt that a student estimate is not
   wanted. The clock gate has to be met by a person walking the steps.
5. **Give a diameter or a half-width, never a width.** A brief describing a revolve profile must
   say which side of the axis it means.
6. **Ask for the retrospective up front.** Applied from run 3.
7. **One person needs to open the links from a student account, once.** No agent can close this
   gate, and it has now been carried as an open item through three runs.

## Still open after two runs

- Nothing has been **printed**. Every fit — the snap, the detent, the 0.197 mm of retention — is
  a number that survived being modeled, not one that survived being used.
- The *Steps reproduce* gate is unmet for both joints. Neither was rebuilt from an empty
  document following only the written steps; run 3 is the first attempt at that.
- The lesson does not fit the clock: 82 minutes at agent pace against a 90-minute budget, with
  Part two 1.7× Part one.
