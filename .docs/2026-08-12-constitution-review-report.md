# Constitution review — 2026-08-12

The adversarial review of commits `e8508af`, `fffec7c` and `cb5ab99`, and the argument that
followed it. Written 2026-08-13 from the session transcript, because it was owed on the day and
the robot runs took the session instead.

**Nothing in here has been applied.** The last commit touching `constitution.md` or `.parts/` is
`cb5ab99`, four hours before the review started. Every finding below is outstanding.

## What ran

Two agents, on branch `constitution-edits`, both since gone.

| Round | What it did |
| ----- | ----------- |
| 1 | Reviewed the three commits adversarially. Filed 19 findings. |
| 2 | Adjudicated the three findings the first round and I disagreed about. |

The review was step 4 of a five-step instruction; this report is step 5. Steps 1–3 produced the
three commits under review.

## The finding that subsumes the rest

**The pass grew the section it was written to shrink.** Working Rules, measured from *"The
behavioral contract"* to the next `##`:

| Revision | Words |
| -------- | ----- |
| `old-constitution.md` — the source being restored from | 426 |
| `user-constitution.md` = `61f73d7` — the starting point | 703 |
| `e8508af` — restore the source's wording | 786 |
| `fffec7c` — adopt the prose standard | 753 |
| `cb5ab99` — say what a step is | **782** |

The 3.1.0 changelog entry justifies the whole exercise with *"the Working Rules had grown 67% —
426 words to 712 — for the same obligations."* **The 712 is not reproducible**; the file it names
holds 703. And the pass against that diagnosis ended at 782 — larger than the figure it condemns,
and +11% on the state it inherited.

The changelog records a diagnosis and never checks the result against it.

*Correcting my own account:* in the argument I reported 706 → 785 and told the user the same
figures this morning. The reviewer's 703 → 782 is right and mine was not; the table above is
measured with the reviewer's own method. The direction was never in dispute.

## The 19 findings

Severity order is the reviewer's. I conceded fifteen without argument.

| # | Finding | Status |
| - | ------- | ------ |
| 1 | **Working Rule 12's MUST silently narrowed.** It used to bind all eleven Quality Gates; it now binds `ninja check`, which covers three. *Steps reproduce*, *Names are real*, *Fits the clock*, *Links resolve*, *Model inspected*, *Floor & ceiling*, *Recovery point* and *Prose style* carry no obligation word at all, and "and reported honestly" was deleted. Imported from a repo where `ninja check` ran ruff, mypy and pytest. | conceded |
| 2 | **The changelog's own metric shows the pass made the drift worse.** See above. | conceded |
| 3 | **`prose-style.md` rule 7's example is an edit left in the file.** The rule names "what is left" for "what remains" as the canonical forbidden reword. `e8508af` made exactly that swap; `fffec7c` codified it four minutes later and did not revert it. | conceded |
| 4 | **The seven title rewrites are self-authorization**, not an application of Bloch. | contested |
| 5 | **Working Rule 3's "report it, don't fix it" was restored after the user cut it**, under a commit message claiming source provenance. It is not in `old-constitution.md`. It also duplicates Branch Policy — and the same series cut the Governance bullet for duplicating Branch Policy. | conceded |
| 6 | **Working Rule 8 still lacks "every unverified claim."** `e8508af` dropped three obligations; `cb5ab99` restored two and presented itself as a complete reckoning. It also attributes the loss to 3.2.0 when it happened in 3.1.0. | conceded |
| 7 | **Working Rule 5 changed addressee, undisclosed.** An execution rule became a lesson-design rule about learning objectives. The changelog claims only titles, capitalization and three cuts. | conceded |
| 8 | **Working Rule 4 swapped one obligation for two invented ones, undisclosed.** "the shared utilities it would use" — the clause preventing a reimplemented helper — is gone; "contradict a convention, or use a term the reader has not met" appeared. | conceded |
| 9 | **RFC 2119 is applied so sparsely the file reads as declaring most of its own rules non-binding.** Eleven of fifteen Working Rules contain no capitalized keyword, including *Fail loud*. Rule 15 has none while rule 14 next door has three. | conceded |
| 10 | **The RFC 2119 scope claim is incoherent and its two copies disagree.** "requirements documents" appears once in the repo — in the sentence defining the scope. Nothing is one. `CLAUDE.md:11` contains a capitalized MUST, outside the declared scope. | conceded |
| 11 | **`prose-style.md` violates four of its own seven rules.** Including the two-file duplication its rule 3 forbids, and two announcing sentences its rule 4 forbids. It also credits *The C Programming Language* and *The Elements of Programming Style* to Kernighan alone. | conceded |
| 12 | **The probe-script escape hatch asserts a tool behavior that does not exist.** The checks skip three named subdirectories, not `.docs/experiments/`; and `check_spelling.py` does glob `*.py`, so a probe there **is** checked. | conceded |
| 13 | **Two of the three "duplications cut" are mischaracterized.** | narrowed |
| 14 | **The Prose style Quality Gate has no check**, in the commit whose stated motive was that the rules were unenforced prose. Its cell states a property; every other row states an action. | conceded |
| 15 | **`ninja check` is red, and Rule 12 was tightened in the same pass.** | contested |
| 16 | **Version numbers are wrong under the file's own rule.** 3.1.0 removed principles and should be MAJOR; 3.2.1 removes two obligations and should not be a PATCH. | conceded |
| 17 | **The always-read core grew.** `Writing anything at all → prose-style.md` makes one part unconditional, which contradicts the section's own heading and adds 459 words to the always-read set. | conceded |
| 18 | **The standard was declared binding for all prose and applied to one file.** `constitution-maintenance.md`, `lesson-design.md`, `modeling-practice.md`, the READMEs, `docs/` and `instructions/` are all non-compliant. | conceded |
| 19 | **Smaller reverts**: Rule 1's title lost *testing* and *building*; Rule 2 lost the code/prose/CAD widening; Rule 11's "reassess" became "restart fresh" — discarding a session is not reassessing; *Check links* → *Open links* traded a fourteen-year-old for "an account without ownership rights"; and a deleted verb left a sentence fragment at `:60`. | conceded |

## The three I argued, and how round two ruled

### Finding 4 — the title rewrites. Both of us were partly wrong.

The charge was that `prose-style.md`'s rule 1 was written to license the edit, since its worked
example — *"Touch only what the task requires" is a rule; "Surgical changes" is a label* — was
the exact title the user had restored by hand four minutes earlier.

**That premise is false, and both the reviewer and I repeated it.** `e8508af` leaves Working Rule
3 as `**Surgical changes.**`. The user restored nothing there.

I argued the standard was commissioned, not invented: the instruction named *Effective Java* as
required prose style for the repository, and Bloch's convention is the imperative rule title.
Round two agreed, and killed "revert all seven" — reverting would undo an explicit instruction to
cure a finding that is mostly false.

It then settled the remainder on the standard's own terms, without appeal to authorship:
`prose-style.md`'s own rule 7 is titled *"Rewording is not an edit"* — declarative. Either a
declarative title carrying its whole obligation satisfies rule 1, in which case rules 13 and 15
satisfied it before they were touched, or it does not, in which case rule 1 obliges rewriting its
own rule 7 and four Quality Gate leads. The file cannot have it both ways.

**Disposition.** Revert rules **1, 13, 15**. Keep **2, 3, 5, 6** — genuine label-to-obligation
conversions, all four on titles inherited from the source.

Round two also corrected my residual list: *Read before you write* and *Checkpoint long
operations* pass rule 1's own test, while **11** and **14** fail it — and 14 fails hardest,
being a metaphor that never says "floor and ceiling." I had named the first two and omitted 14.

And it found two changes neither round one nor I had caught: rule 5 gained the new obligation
*"Say what the reader or student can do at the end"* with no changelog line, and rule 6 narrowed
"god scripts **and any other content that touches everything**" back toward code-only.

### Finding 15 — `ninja check` red. Upheld for me, and I had understated it.

The 35 wrap failures are a deliberate, temporary, user-directed reflow: both constitutions were
put on one line per block so soft wrap made them diffable side by side. Round two proved it from
the record — the gate went red at **`61f73d7`**, which is not one of the reviewed commits, and
that commit's own message says *"This fails the 100-column wrap gate on both files, deliberately
and for now."*

Adding `constitution.md` to `SKIP_FILES` would be the actual defect: it converts an announced
temporary state into a silent permanent one and removes the only thing that will force the
re-wrap. `old-constitution.md` is skipped because it is a foreign baseline that must never be
re-wrapped.

**What survives:** Working Rule 12 was tightened in the same pass, and three commits were then
declared complete under it with the gate red and no commit message saying so.

### Finding 13 — the Governance bullet. Agreed as narrowed.

The cut is defensible — it was rationale, and cutting rationale was the instruction — but the
changelog's justification ("restated Branch Policy") is false. **The remedy is the changelog
line, not the bullet.**

## The revert is unexecutable as written

Round one's bottom line was to revert `constitution.md` to `user-constitution.md` and re-apply
only obligation-carrying changes. `user-constitution.md` is byte-identical to
`61f73d7:constitution.md` and carries three defects the user did not intend: **two rules both
numbered 7** (with rule 6 between them), a stray blank-line block splitting the ordered list, and
three misspellings — `buiding`, `conent`, `meaining`.

The spell gate would not recover the misspellings. `check_spelling.py` runs codespell with
`--builtin en-GB_to_en-US`, which restricts the extra dictionaries to the British-to-American
list; round two ran those three words through it and got a clean exit. **A revert loses them
silently and permanently.**

The correct baseline is `e8508af:constitution.md` — the user's edits plus the mechanical
corrections the user commissioned, before any prose-standard rewrite. But round two advised
against a revert at all: the disputed surface is seven titles, one Governance bullet, one
changelog paragraph and one body sentence. Four targeted edits reach the same end state, and a
revert-and-reapply would itself be a mass reword of undisputed text — which is what
`prose-style.md` rule 7 exists to forbid.

## Where we agreed to disagree

Nowhere, in the end. Round two ruled on all three contested points and I accept all three
rulings, including the one against me.

**The ruling against me is the part of this report worth keeping.** Round two found motivated
reasoning in my rebuttal, and it is right:

> You folded an undisclosed narrowing of the user's own sentence — dropping *testing* and
> *building* from a rule your very next commit treats as covering builds and tests — into a
> bucket labeled "three titles that were already complete sentences," a stylistic category where
> the stakes are zero. That framing takes the one change in these three commits that actually
> altered an obligation without saying so, and files it under housekeeping. It also happens to be
> the framing under which your proposed remedy looks generous rather than mandatory.

It also noted that I conceded more than the evidence supported on cheap points — four of the
seven conversions act on source-inherited titles, not the user's — while compressing the
expensive one into a stylistic aside. Its diagnosis: *"Conceding more than the evidence supports
on the cheap points, while compressing the expensive one into a stylistic aside, is the shape the
argument takes when the conclusion is chosen first."*

## What is outstanding

Nothing below has been done.

- **Restore Working Rule 12's scoping** so the MUST binds all the gates again (finding 1).
- **Restore "every unverified claim"** to Working Rule 8, and correct 3.2.1's attribution from
  3.2.0 to 3.1.0 (finding 6).
- **Revert "what is left" to "what remains"** and grep the diff for the same class (finding 3).
- **Revert the titles of rules 1, 13 and 15**; keep 2, 3, 5, 6.
- **Rewrite the 3.1.0–3.2.1 changelog entries against the actual diff** — the word count, the
  "six titles that were labels" that enumerates seven and is false for three, the two
  mischaracterized duplications, and the `check_*.py` skip claim. The same "six titles" defect is
  in `fffec7c`'s commit message.
- **Decide rules 5 and 6's undisclosed body changes**, either way, with a changelog line.
- **Fix `prose-style.md`**: replace rule 1's worked example with one from outside the diff; add
  the missing sentence *a title that already carries its whole obligation is not rewritten*; fix
  the four self-violations and the two book attributions.
- **Make the RFC 2119 scope coherent** — drop "requirements documents", state it once, and settle
  `CLAUDE.md`'s capitalized MUST.
- **Give the Prose style gate a check, or state it as a performable action** (finding 14).
- **Correct the version numbers** under the file's own semantic rule (finding 16).
- **Re-wrap `constitution.md` to 100 columns**, which is the only thing standing between
  `ninja check` and green. While it is red, the spelling and reading-level checks never run.
- **Fix the probe-script claim or the tools**, so the escape hatch describes what the checks do.

## Not done, and not the same thing

The **reviewer pass on tone and judgments about people** — Phase 3 of the reorganization, Fable
writing `<YYYY-MM-DD>-professional-review-report.md` — has still not been run. It is a different
review from this one, scoped to unprofessional statements and judgments based on age or status.
What counts as a finding is in [`README.md`](README.md), under *The reviewer pass has not been
run*.
