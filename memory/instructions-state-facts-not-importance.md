---
name: instructions-state-facts-not-importance
description:
  "Instructions and the Constitution state rules and facts only — no rationale, no superlatives, no
  invented statistics."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f7a2d0bd-c646-4b69-9103-9c444fdbf1e2
  modified: 2026-08-12T23:18:13.828Z
---

Three rules, in order of how strongly the user holds them.

**1. Never assert a fact you have not established.** Frequency and ranking claims are the
usual offenders — "the single most common way an eight-hour course becomes a ten-hour course",
"the single most useful decision in the project". No evidence exists for either. Inventing a
statistic to make a rule sound weightier is the same failure as reporting an unperformed
verification. Since 2026-08-11 the Constitution says so outright: Working Rule 8 carries a
sub-bullet — *do not grandstand, and do not use hyperbole; do not assert as fact anything you
have not established, or would not be able to prove; claim success, justify a rule, or persuade
a reader or subagent only from established, provable information.*

**2. The Constitution states rules, not why.** Cut the argument for a rule; keep the rule.
Researching or defending a rule's rationale is a separate task, done when asked. Applies to
`constitution.md` and everything in `parts/`.

**3. No selling in instructions.** Do not rank a document's importance, quote what it cost to
produce, or tell the reader it is the highest-value thing they will do. Say what it contains.
"1.2 million tokens of hard-won knowledge" described a 12 KB file and misled the agent who read
it. **Do not give its size either** — a line count is the same move in a quieter voice, and it
tells the reader nothing they can act on. See [[derive-dont-maintain]].

**4. Do not fill the context with information that changes nothing.** Not a summary of what
just happened, not an inventory nobody asked for, not internal bookkeeping the reader cannot
see. Ask what decision the sentence changes; if none, cut it. See [[derive-dont-maintain]] for
the maintenance cost of the same habit written into a file.

**Why (the user's own reasoning): grandstanding causes things to be ignored.** An overstated
claim invites the reader to discount everything near it, so emphasis spent on importance buys
less attention than plain facts would have.

**How to apply:** agent prompts, build briefs, README headers, commit messages, and replies to
the user. Emphasis is still fine on a *specific* hazard with a *specific* observed consequence —
"check the bounding box after any offset extrude; a rod went through the fork and the preview
looked right" is a report of something that happened. "This is critical" is not. See
[[plain-words-for-middle-schoolers]] for the parallel rule on vocabulary.
