---
name: say-when-you-carry-on
description:
  "after finishing a thing the user asked for, say what you are moving on to before you start it."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c7e95b50-7b3c-4747-a656-ece9f33b51c4
  modified: 2026-08-24T12:37:08.252Z
---

**This applies during an unattended run, not during a conversation** — see
[[conversation-mode-is-not-a-task]]. When the user asks for a specific thing and I finish it, I
should say so and name what I am moving on to next — in a message, before I start the next thing.
Not a question, just a heads-up.

**Why:** during a long unattended run I keep going by design, so the user cannot tell the
difference between "finished the ask and picked up the plan again" and "wandered off". A one-line
handover makes the seam visible, and it is the point where they would interrupt if they wanted
something else.

**How to apply:** finish the ask, commit it, then say in a sentence what was done and what is
starting next. Then start it. This is a report, not a permission request — see
[[read-think-plan-do]] and [[instructions-state-facts-not-importance]].
