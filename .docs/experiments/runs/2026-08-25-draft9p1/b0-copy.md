# B0 — the copy, and what the copy is

Phase B edits a model rather than rebuilding one, so it starts from a copy of the draft9p0 model
taken at a named version. This row records the copy and the ids everything after it addresses.

## What was copied, and from where

`stickbot-draft9p0` `0f4b79a78707651ae20df5b2` at version `t14 legs` `737db64e2567c96e2d3de63f`.
That version is draft9p0's latest and is the parent of its Main workspace, so the copy is the model
as draft9p0 left it, not a point part-way through.

Onshape's documented command for this is **Copy workspace**, reached by right-clicking a document
on the Documents page. It copies a workspace, and the plan needs the version. Opening the version's
own URL and using the document menu offers **Copy version…** instead, whose dialog is titled *Copy
the active version to a new document*. That is the command used.

## Where it went

| | |
| --- | --- |
| owner | Spires Robotics |
| folder | none — the company root |

The dialog's destination picker is a folder navigator, not a list. Selecting a container changes
its button to **Open**; the button reads **Copy here** only when nothing is selected, and then it
means the folder the breadcrumb is showing. So the copy is taken after descending into Spires
Robotics and selecting nothing.

The company root is where draft9p0 itself lives, read back over REST before the copy:
`globaltreenodes/document/…/parentInfo` returns a `resourcecompanyowner` node for draft9p0 and a
`resourceuserowner` node for `stickbot` and `stickbot-for-bot-review`. The two read-only documents
are under *Owned by me*; the draft is not.

## The ids Phase B addresses

`stickbot-draft9p1` `a1a859f4bfdfe42d372aff90`, workspace `Main` `d3a590c94880f445e3c56902`,
whose parent is the copy's only version, `Start` `8e4b28cc2cf504aef52a7a9a`.

| tab | type | element id |
| --- | --- | --- |
| `robot sizes` | VARIABLESTUDIO | `8e21e5ac45ee843a1c536e1b` |
| `body` | PARTSTUDIO | `6f635a750e13ccbf30d05ba2` |
| `head` | PARTSTUDIO | `915098789c7845370c86c914` |
| `ball and socket` | PARTSTUDIO | `365f6106c79b2ef1684bf939` |
| `foot` | PARTSTUDIO | `95448bc5d270c9d8370bf3cf` |
| `hinge` | PARTSTUDIO | `f2f0dbd682ff7413d3ce2443` |
| `u limb` | PARTSTUDIO | `3f27ca39a14117e276b7c449` |
| `l limb` | PARTSTUDIO | `fa98530f59d5f18889fe7c00` |
| `gripper` | PARTSTUDIO | `7ef73a118e1331213bc1554f` |
| `stickbot` | ASSEMBLY | `4515305b332af7d4379b81b3` |
| `BOM : stickbot` | BILLOFMATERIALS | `5c2dbc15ab682bee35723620` |

Element ids do not survive a copy. Every id above is new, and the draft9p0 ids the previous run's
register holds address the read-only document from here on.

## The copy carried the history

Read back before any edit, and matching the counts A7 read off draft9p0:

| tab | features | of them, variables |
| --- | --- | --- |
| `body` | 35 | 10 |
| `head` | 14 | 0 |
| `ball and socket` | 19 | 10 |
| `foot` | 28 | 17 |
| `hinge` | 49 | 21 |
| `u limb` | 10 | 1 |
| `l limb` | 10 | 1 |
| `gripper` | 15 | 8 |

The Variable Studio holds the four it held: `#torsoH` 96 mm, `#torsoW` 72 mm, `#torsoD` 48 mm and
`#limbSeg` 48 mm. `#limbSeg` is still its old name — B1 renames it and adds the rows A13 promoted.
