# Choose a visual direction

Use this before building a new website or replacing its visual identity. A local component refinement inherits the established system. The user's requested look and confirmed brand commitments govern the work.

This is a Codex adaptation of [Anthropic Frontend Design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) and [Peter Bakāus's Impeccable](https://github.com/pbakaus/impeccable). Attribution and consulted revisions are in [Design sources](design-sources.md).

## Ground the composition

1. Inspect the actual subject: content, existing logo and lettering, photographs, materials, distinctive activities, and visitor actions. Record which facts and recognizable assets must survive the redesign. Describe the visitor's situation and the page's main job.
2. Derive different composition candidates from that evidence. Compare how they open, distribute imagery, organize information, and lead to the main action. A candidate needs a concrete subject connection; adjectives such as "premium" or "modern" alone leave the design undecided.
3. Choose a candidate and record a compact direction in the project's existing brief or style document: its subject evidence, first viewport, type roles, palette, layout rhythm, and defining interaction. Sketch the first viewport when that clarifies its structure. Choose one memorable visual device and let supporting sections serve the content.

Completion: the chosen composition has a visible reason to belong to this subject, and the alternatives differ in structure and visual language rather than in accent color alone.

## Commit the visual system

- **Typography:** inspect a licensed type catalog with actual headings from the project. Select letterforms, widths, weights, and proportions that express the chosen direction. One family can be sufficient; pair families when their distinct roles earn it. Test real heading lengths at narrow widths before extending the system.
- **Color:** derive named surface, foreground, accent, and secondary roles from the subject or an identified visual reference. Choose how much surface each role occupies. Check readable text and focus against the actual backgrounds.
- **Composition:** decide whether the subject is best introduced through photography, typography, a demonstrated operation, or a scene. Establish image crops, information density, alignment, and a section rhythm fitted to the content.
- **Motion:** select a defining effect from the recipe database when it strengthens the visitor's understanding or experience. State what moves and why, including the reduced-motion presentation. Preserve a usable static default.

Use the direction to select recipes. P01 supplies reference gathering, P05 supplies a controlled combination, P08 supports typography, and P10 preserves content during redesign. Other recipes supply the required effect or interaction. A restaurant category establishes menu and visit needs; it leaves room for different visual worlds.

## Check the direction before implementation

Review the proposed first viewport and section rhythm against the brief. For each major decision, identify the subject evidence or specific reference property supporting it. Rework decisions supported only by habit.

Use these recurring combinations as diagnostic signals: warm cream plus a high-contrast italic serif and clay accent; near-black plus a single neon accent; a ruled newspaper composition; identical rounded cards; repeated tracked uppercase labels, decorative section numbers, or single-word headline accents. Any can serve an explicit brief, but a free design choice needs a subject-specific reason. Changing from one familiar combination to another still requires that reason.

Consider a name-and-photo swap with a comparable business. Identify which visible decisions would become incongruous. If the entire page remains equally plausible, strengthen its connection to the actual subject before building. Preserve specific source imagery and factual copy rather than compensating with generic decoration.

Completion: the direction explains the whole composition and identifies the evidence behind its defining choices. It can now guide the opening section and subsequent recipe integration.

## Review the built page

Inspect the rendered page before reading detector findings. Compare desktop and mobile captures with the recorded direction. Check composition, real type, crops, section rhythm, content coverage, and the complete visitor action. Resolve concrete mismatches in a batch and confirm the corrections.

Then run the installed Impeccable detector with each changed markup and stylesheet path as an explicit target:

```sh
node <website-creator>/scripts/check-design.mjs <project>/index.html <project>/styles.css
```

Use the actual stylesheet names in the project. The helper locates an installed Node-based Impeccable detector and enables its GPT-specific checks. It scans the supplied local paths; include linked styles explicitly. With a newer Impeccable installation, use its shipped `scripts/impeccable detect --json <target>` launcher, or `scripts/impeccable.cmd` on Windows, as documented by that installation. Scan project files, then verify reported states in the browser.

Treat findings as evidence: fix defects, explain justified design choices, and distinguish a hidden viewer's image assigned on opening from a broken visible image. A clean scan establishes only that its rules found no issue; visual identity, usability, and resemblance between pages still require rendered comparison. If the detector is unavailable, complete the visual review and state the scan's availability in the verification notes.

Completion: the rendered page follows its direction, required actions work, narrow layouts remain usable, and detector findings have a recorded disposition. When delivering several pages, compare their opening compositions and section rhythm together and report any remaining convergence honestly.
