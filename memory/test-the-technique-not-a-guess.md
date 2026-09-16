---
name: test-the-technique-not-a-guess
description:
  "Before reporting that a technique does not work, confirm the run actually performed it as
  specified."
metadata:
  type: feedback
---

The user (Mike) gave me the Shift trick for mate connectors; I built a spike that pressed Shift
*before* hovering, found nothing changed, and wrote up "Shift is not what does the work" in the
notes, the howto and a plan file. Shift locks the reference to the face **already** hovered, so
pressing it first locks nothing. The order was the technique and I had inverted it.

**Why:** a negative result about somebody's method is a claim about their method, and it gets
copied into permanent files. Mine was a claim about a sequence nobody uses.

**How to apply:** when a run is meant to test a named technique, write down the steps the
technique specifies and check the script performs them in that order before reading the result.
When the result is negative, look for a way the run could have failed to exercise the thing at
all — a modifier that never reached the app, a step done out of order — and rule it out before
writing it down. A frame comparison usually settles it: here, the locked run still drew every
inference square on arrival and the unlocked run had lost them all. Related: [[no-invented-gates]]
and [[counts-catch-what-dimensions-miss]].
