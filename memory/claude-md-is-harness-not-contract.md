---
name: claude-md-is-harness-not-contract
description:
  "CLAUDE.md is harness plumbing to survive /clear and /compact, not part of the documentation
  system."
metadata:
  type: feedback
---

CLAUDE.md exists only because the agent reads it on every `/clear` or `/compact` — its job is to
make the agent re-read `constitution.md` and re-agree. It is not a document in the project's
documentation system, so it is outside the scope of `.parts/prose-style.md`: its MUST is not an
RFC 2119 obligation, and its numbered list is not a style violation.

**Why:** raising either as a finding is pedantry and wastes the user's attention on plumbing.

**How to apply:** review CLAUDE.md for whether it still makes the agent function. Do not audit it
against [[one-fact-one-home]] or the prose standard.
