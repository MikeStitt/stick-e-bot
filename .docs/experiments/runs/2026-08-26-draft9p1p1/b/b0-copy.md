# B0 — the copy, and what the copy is

Phase B edits a model rather than rebuilding one, so it starts from a copy of the draft9p1 model
taken at a named version. This row records the copy, the ids everything after it addresses, and one
thing the copy did not carry.

## What was copied, and from where

`stickbot-draft9p1` `a1a859f4bfdfe42d372aff90` at version `Recovery point`
`8504f457723606c65c2ab48f`. That version is draft9p1's latest and the one its register names, so the
copy is the model as draft9p1 left it.

The command is **Copy version…**, on the document menu while the version's own URL is open. Its
dialog is titled *Copy the active version to a new document*. The route and the dialog are the ones
[`../../2026-08-25-draft9p1/b0-copy.md`](../../2026-08-25-draft9p1/b0-copy.md) describes, and both
behaved as it describes them.

## Where it went

| | |
| --- | --- |
| owner | Spires Robotics |
| folder | none — the company root |

Selecting `Spires Robotics` in the destination picker changed the button to **Open**; descending
into it and selecting nothing changed the button back to **Copy here**, which then means the folder
the breadcrumb is showing. The breadcrumb read `Spires Robotics` and the list under it held the
three folders `2026 OnShape Class`, `Coach Mike Experiments` and `FRC 2026`, none of them selected.

## The ids Phase B addresses

`stickbot-draft9p1p1` `4b2e0d48efd37d3327a90afb`, workspace `Main` `a1af16872d25103815f1c32a`,
whose parent is the copy's only version, `Start` `8a5484206371ce199e41968f`. Created
2026-08-27T16:43:45Z.

| tab | type | element id |
| --- | --- | --- |
| `robot sizes` | VARIABLESTUDIO | `f30d47abeacf3059ec4a3342` |
| `body` | PARTSTUDIO | `4e48e81a06c8d40b2a38b871` |
| `head` | PARTSTUDIO | `1562dee65e364ec088dda0ec` |
| `ball and socket` | PARTSTUDIO | `6dcfcf8856d4feea7faa440a` |
| `foot` | PARTSTUDIO | `c01ac56602d81451da6a5db5` |
| `hinge` | PARTSTUDIO | `184adaa7b3e7abc7bc4357c7` |
| `u limb` | PARTSTUDIO | `656816292447e8797ff0402d` |
| `l limb` | PARTSTUDIO | `88de5da8c7611f141a1a92a9` |
| `gripper` | PARTSTUDIO | `32166c7b3d22572c0e7dd0c3` |
| `stickbot` | ASSEMBLY | `cd2278317279029435f010de` |
| `BOM : stickbot` | BILLOFMATERIALS | `46ce791f8ddcf188cdc25a86` |

Element ids do not survive a copy. Every id above is new, and the draft9p1 ids that run's register
holds address the read-only document from here on.

## The copy carried the history

Read back before any edit, against the same read taken from the source version:

| tab | features | of them, variables |
| --- | --- | --- |
| `body` | 33 | 8 |
| `head` | 26 | 12 |
| `ball and socket` | 14 | 5 |
| `foot` | 24 | 13 |
| `hinge` | 49 | 21 |
| `u limb` | 10 | 1 |
| `l limb` | 10 | 1 |
| `gripper` | 18 | 8 |

Every row matches the source. So does the tab list, so does the assembly at 14 instances and 13
mates, and so does the Variable Studio, whose eleven rows read across identically:

```
torsoH 96 mm   torsoW 72 mm   torsoD 48 mm   limbCenter 48 mm
ball #torsoH / 8      limbD #torsoH / 4      wall #torsoH / 32
stand #ball * 5 / 6   collar 11 mm           fit 0.08 mm
grip sqrt((#ball / 2 + #fit) ^ 2 - (0.48 * #ball) ^ 2)
```

`#collar` is still the typed 11 mm. B1 is what makes it `#ball / 2 + #wall`.

## The copy did not carry the assembly's parts

**Every one of the assembly's fourteen instances still names `stickbot-draft9p1`.** They point at
document `a1a859f4bfdfe42d372aff90` at version `ankle centered` `e6fd823965e71c15d9e267cb`, which is
the ancestor rather than this copy.

In draft9p1 those were self-references: the assembly took its parts from a version of its own
document, which is what that run's B9 built and what its register records. Copying the document did
not re-point them, so the same links are now cross-document links into a document this draft holds
read-only. The copy's assembly shows draft9p1's parts and will not follow anything B1 through B4
edits.

### A workspace reference survives a copy and a version reference cannot

The eight derive features did survive. `head`'s `get socket` reads
`namespace: e6dcfcf8856d4feea7faa440a::m209c6e55ce681e6af4920dfe`, and `6dcfcf8856d4feea7faa440a` is
this copy's own `ball and socket`. The same holds in `body`, `foot`, `u limb`, `l limb` and
`gripper`: no `documentId`, no `versionId`, an element id and a microversion.

That is the whole mechanism. A reference to the same document's workspace names an element, so a
copy can re-point it. A reference to a version names a document and a version, version ids are
global objects, and the copy's only version is its own `Start`. There is no version in the copy for
`ankle centered` to become, so there is nothing to re-point onto.

**Which copy command was used makes no difference.** A throwaway **Copy workspace** of draft9p1's
`Main`, taken to test exactly this and sent to the trash afterward, came out the same way: fourteen
instances still on `stickbot-draft9p1` at `ankle centered`, one version of its own named `Start`.
Onshape's help says of both commands that *"The original and the copy are not linked in any way"*,
and that sentence is about the two documents rather than about the references their content carries.

### What each repair tool can reach

| tool | what it offered, opened on the copy |
| --- | --- |
| **Update linked document…** | the Reference manager, one row, `stickbot-draft9p1: ankle centered ⇒ Recovery point`. Both are the wrong document, and the dialog handles newer versions on one branch and nothing else |
| **Replace instances…** | a component browser that opens on the current document and lists its own Part Studios. It takes several instances in one operation and carries a *Replace all instances* box |

So the assembly can only be moved onto this document's parts by **Replace instances…**, and it takes
six operations rather than fourteen, because `torso`, `head`, `u limb`, `l limb`, `Gripper` and
`Foot` cover all fourteen instances between them. Onshape documents Replace instance as reapplying
the previously associated mates of the replaced component; whether all thirteen survive here is
measured in B5 and not assumed.

### The rule that produced this

[`../../../build-briefs/assembly.md`](../../../build-briefs/assembly.md) required insertion from a
version rather than from a workspace, on the grounds that a workspace moves under the assembly while
you work. That rule is what pinned the instances, and pinned instances are the one kind of reference
a copy cannot carry, so every draft starting from a copy paid this cost at B0.

The rule is withdrawn. [`../../../../.parts/onshape.md`](../../../../.parts/onshape.md) *Insert from
the workspace, and keep every reference inside one document* replaces it: the robot is one document,
an assembly instances the Part Studios beside it, and the assembly following an edit as it is made
is the thing the brief's *The idea being tested* asks a student to see.
[`b5-assembly.md`](b5-assembly.md) is the repair.
