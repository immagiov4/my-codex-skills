---
name: docs-doc
description: "Reviews and reorganizes documentation and analytical reports for purpose, evidence, author voice, and readable prose. Use for documentation sets, academic or project reports, references, readmes, architecture docs, RFCs, PR descriptions, and commit messages."
---

Revise at every level: purpose and structure first, then genre, then sentences. Edit files in place when requested; otherwise return the requested text or review. Do not write a separate report unless the user explicitly asks for one.

If the user asks only for an audit, do not rewrite the document. Name each pattern, quote the affected text, and state the smallest fix. Do not score the prose, guess whether AI wrote it, or turn the audit into a sidecar document.

Write for the intended reader's knowledge and reason for reading.

Three rules sit above everything else:

- **Cut every word that does no work.** If the sentence survives without a word, the word goes. "In order to" is "to". "It is important to note that" is nothing.
- **Use the short, everyday word.** "Use", not "utilize". "Help", not "facilitate". "Do", not "perform". A long word has to buy its length with precision.
- **When a rule makes a sentence worse, fix the sentence another way or leave it alone.** The rules serve the reader. A sentence that follows every rule and sounds like a machine wrote it has failed.

For software documentation, the codebase is the word list. Write the real symbol, file, flag, or command name, not an invented synonym. For other genres, use the discipline's established terms and explain those the intended reader needs.

## Author, reader, and genre

Establish who is speaking and what the document must accomplish. When drafting
for someone, use their first-person or impersonal authorial voice. References
to "the student," "the user," or "the author" belong only where that person is
actually the subject of analysis, not as commentary about the requester.

A report develops an argument through evidence, interpretation, and consequences.
A manual explains how to act. Apply Diátaxis to documentation where it helps;
preserve a report's required sections and supplied template rather than forcing
them into separate document modes. Place content in the designated fields.

Keep a detail when it changes understanding, a decision, reproducibility, or
evaluation. Mandatory-format compliance, ordinary file handling, and routine
successful checks rarely need narration. Describe methods when they explain a
result or limitation, rather than presenting basic operations as achievements.
Put source credit in the appropriate citation or credit location; use captions
to explain what the image contributes, rather than describe the obvious.

Distinguish substantive project decisions from artifact-production mechanics.
Describe the work supported by evidence. Personal experiences, difficulties,
durations, and sequences require confirmation or records; plausible events are
not a substitute. Required disclosures still belong in the document.

When a user identifies a recurring defect, review the whole requested document
for that class of defect, preserving sound passages and necessary qualifications.

## 1. Fix the structure before polishing the prose

Your first responsibility is not prose polish. It is information architecture.

### Give every file one job

Before editing a documentation set, inventory the files in the request and the
directly linked files needed to decide ownership. Widen that set only when a
demonstrated duplication or broken path crosses its boundary. In working notes,
write one sentence that names each file's reader, purpose, and Diátaxis mode.
Do not add these role sentences to the documentation.

First decide whether each topic belongs to the project's documentation at all.
A separate file does not make generic prerequisite material relevant. Document
the product's behavior, concepts, interfaces, and project-specific setup. When
a prerequisite tool needs explanation, give only the short note needed to use
this product, then link to that tool's documentation if more help is necessary.

Each section belongs in the file whose purpose it advances. Move or cut a
section when it answers a question assigned to another file. Keep one
authoritative home for each fact. Repeat only the short context a reader needs,
then link to the owning document.

Use these ownership tests to diagnose a mixed document. They do not require a
project to have separate files for every kind of information. A short,
navigable README can remain self-contained. Split only when incompatible reader
questions interrupt the file's main path or when another document already owns
the detail. Do not create a file merely to relocate a short note.

- A README is the front door. Keep the project identity, intended users,
  requirements, shortest successful path, and links to deeper documentation.
  Move detailed command contracts or procedures when they obscure that path and
  have a useful destination.
- An architecture document explains components, boundaries, data flow,
  constraints, and design reasons. Command syntax, field catalogs, and operating
  procedures usually belong in reference or how-to documents.
- A reference document holds facts readers look up while working. Give it only
  enough project context to identify the subject, then link to the overview or
  explanation.
- A tutorial or how-to document carries one path to one outcome. Link to
  reference and architecture material instead of retelling them.

The role map is complete when every topic belongs to the project, every file in
scope has one purpose in the working notes, every section serves that purpose,
and duplicated material is limited to local context plus a link. Split, move,
merge, or delete content until those checks pass.

### Normalize each file

Before rewriting sentences, identify the reading model of the file:

- concept-first reference
- flow-first guide with reference anchors
- API-first manual
- mixed structure that needs consolidation

If the file is structurally mixed or inconsistent, normalize the structure first. Do not keep multiple overlapping documentation styles alive in parallel just because each section is locally readable.

- Prefer a propedeutic order: concepts, then quick usage, then API/reference, then advanced details, then broader examples.
- If the user is clearly struggling with discoverability, optimize for first-read comprehension before exhaustiveness.
- Do not preserve redundant sections just because they already exist.
- If two sections explain the same concept with different shapes, consolidate them.
- If the user criticizes structure, stop making local wording fixes and re-evaluate the file architecture.

When deciding whether to split, merge, extract, or collapse content, optimize for the path a first-time reader takes to answer their next obvious question.

Structure rules:

- Large documentation files need a table of contents.
- Advanced material goes in collapsible `<details>` blocks when that reduces visual noise.
- Empty sections, empty `<details>` blocks, and boilerplate stubs are removed.
- If distant sections duplicate a large shared structure (schema, object, runtime table), document it once in a named section and link back. If only a small fragment is shared, duplicate it instead of forcing the reader to jump around. Nearby sections may refer back: "same opts as `save_to_file`" is fine.

## 2. Pick the mode first (Diátaxis)

For documentation, choose a dominant mode. Two questions help: does the content inform action (doing) or understanding (thinking), and does it serve learning or work?

- Action + learning: **tutorial**.
- Action + work: **how-to**.
- Understanding + work: **reference**.
- Understanding + learning: **explanation**.

**Tutorial: learning by doing.** You are the teacher. The learner's success is your job, not theirs. Open by saying what the learner will build, not what they will "learn". Every step produces a visible result, early and often. Tell them what they should see: the expected output, the prompt change, the log line. Cut explanation to one clause and a link. Teaching pauses break the lesson. Stay concrete. Write as "we", in commands: "First, do x. Now, do y."

**How-to: steps to a goal.** Solve a problem a person has, not an operation the machine can perform. Assume competence. Skip teaching. Action only: no digressions, no background, no completeness for its own sake. Link those instead. Allow forks and judgment: "If you want x, do y." Name the guide by the task: "How to calibrate the radar array", not "Radar array calibration".

**Reference: facts for lookup.** Describe. Only describe. No instruction, no persuasion, no opinion. Be dry, complete, and sure: state facts, options, limits, and errors with no hedging. Mirror the structure of the thing described, so code and docs can be navigated together. Put material where readers expect it. Generate from code where possible, so it stays true.

**Explanation: understanding and why.** One bounded topic, readable away from the product. Each title should tolerate an implicit "About..." in front. Anchor on a real why question. Give context: design decisions, history, constraints, alternatives. Opinion is allowed here and nowhere else.

Separate modes when they interrupt the reader's task. A required report structure takes precedence over this documentation taxonomy.

Source: diataxis.fr, fetched 2026-07-18.

## 3. Write sentences to the reader (Google developer style)

- Address readers as "you" in instructions; use the author's chosen voice in reports. Use tense to distinguish completed work, current facts, and plans.
- Say who does what: "the compiler checks", not "is checked". Passive is fine only when the actor is unknown or beside the point.
- Write instructions as commands: "Click Submit." State facts plainly. Never "should be done".
- Put the condition before the instruction: "To delete the document, click Delete." The reader skips what does not apply.
- Put the common case first. Exceptions after.
- Sound like a knowledgeable friend. No buzzwords, no figurative language, no "please" in instructions, and never "simply", "easy", or "quickly" in a procedure. If it were simple, the reader would not be here.
- Don't pre-announce ("we will soon support...") and don't start consecutive sentences with the same phrase.
- Read the awkward sentence aloud. If it stays awkward, rewrite it.
- Link with words that say where the link goes: the page title or a short description. Never "click here". Prefer a sentence of context on the page over a link off it.
- Numbered lists for sequences, bullets for everything else. Introduce a list with a complete sentence. Keep items parallel.
- Code goes in code font. UI elements go in bold. Use serial commas. Drop "etc." and say up front that a list is partial.

Source: developers.google.com/style, fetched 2026-07-18.

## 4. Make statements load one at a time (STE rules)

- Keep procedural actions distinguishable. In analysis, keep a claim connected to its reason, condition, or consequence when that makes it easier to follow.
- Split at a change of idea or when readers must backtrack, not at a fixed word count. Sentence complexity should follow conceptual difficulty and the reader's knowledge.
- Put the warning or condition before the step it guards.
- Keep "the" and "a": "Remove backup file" reads two ways. "Remove the backup file" reads one.
- Give each word one meaning and one job, then keep it. If "check" means inspect, don't also use it for restrain.
- Pick one word per action and stick to it: "start", not "start" here and "initiate" there.
- Write procedures as direct commands, never as narration and never in the passive.
- Avoid "-ing" words where you can. They take too many grammatical jobs and breed misreadings.

Source: asd-ste100.org (Issue 9, 2025), fetched 2026-07-18. The numbered rules and dictionary live in the spec PDF. The principles above are the transferable core.

## 5. Leave no sentence open to two readings (Global English)

- Keep words like "only" and "not" next to the word they change: "only fails on growth" and "fails only on growth" say different things.
- Break up long noun strings: "the proto import budget check script" becomes "the script that checks the proto-import budget".
- Make every "it", "they", and "this" point at one obvious thing. Repeat the noun when in doubt. Never use "this" or "which" to point at a whole clause.
- Don't drop verbs: "Phase 1 moves the converters and Phase 2 the runtime" leaves Phase 2 without one. Give it one.
- Keep the small words that show structure. "Ensure that the switch is off" keeps "that" because it makes the sentence parse one way. Never trade clarity for word count.
- Repeat the article in a series when it prevents a misread: "the client and the host", not "the client and host", when they are two things.
- Say which parts "and" or "or" joins when a sentence can group two ways. "Both...and", "either...or", and "if...then" are free disambiguators.
- Use punctuation to express the relationship between clauses. Conjunctions often convey a cause or contrast more naturally than another full stop.
- Make text in parentheses a full grammatical unit or its own sentence. Never form plurals with "(s)".
- No slashes: write "a, b, or both" instead of "a/b" or "and/or".
- Call each thing by one name, everywhere. A doc that says "the gate", "the ratchet", and "the budget check" for one thing teaches three things. Don't churn what didn't change between edits.
- Skip idioms, colloquialisms, Latin abbreviations, and metaphors. A non-native reader, a translator, and an agent all parse plain constructions best.

Source: Kohl, The Global English Style Guide (SAS Press). Guideline text fetched from the Internet Archive and the SAS sample chapter, 2026-07-18.

## 6. Vary the rhythm

A doc can obey every layer and still read machine-written: every sentence clipped short, no view anywhere, nothing specific.

- Mix sentence lengths on purpose. Short sentences land a point. Longer ones that take their time carry a fact with its condition or consequence.
- Join closely related statements when the connection matters. Avoid both stacked fragments and chains of clauses that obscure the point.
- Have a view where the mode allows it. Explanation weighs trade-offs, so say what you make of them instead of listing pros and cons. Reference stays dry.
- Be specific over sterile. Not "schema changes can cause issues" but "a column rename fails the build".

## 7. Remove AI-sounding prose

Rewrite prose that sounds like chatbot output. Remove:

- puffery and significance padding: "robust", "powerful", "comprehensive", "seamlessly", "crucially", "important role", "broader context", "lasting legacy", "contributes to", "reflects broader", "shaping", "symbolizing", "fostering"
- assistant-style filler: "I hope this helps", "would you like", "here is", "below is an overview", "in this section we will"
- throat-clearing and faux-insight setups: "here's the thing", "let me be clear", "what most people get wrong", "the part everyone misses"
- stock knowledge-cutoff and source-gap disclaimers that add no relevant date, uncertainty, or evidential limit
- rhetorical contrast formulas: "not just X, but Y", "not X, but Y", "this is not ..., it is ..."
- rhetorical questions with immediate answers and dramatic colon reveals: "The best part: it learns" or "Why does this matter? Because..."
- interpretive asides that tell readers what to notice: "the key point is", "as you can see", "this distinction matters", or redundant "in other words"
- negative lists and stacked fragments: "Not X. Not Y. Z." or "X. And Y. And Z."
- elegant variation used only to avoid repeating the right technical word
- dramatic or formulaic em-dash usage
- bold used for rhetorical emphasis instead of structure
- emoji, decorative markers, or theatrical styling
- tiny tables that would be clearer as prose or lists
- formulaic section endings such as "Conclusion", "Challenges", or "Future outlook" when they only restate or speculate
- fake-profound closing lines, aphorisms, and mic-drop metaphors; end on the last concrete fact or next action instead
- placeholder prose, fill-in-the-blank text, template-like wording, or TODO-shaped sentences

Prefer the plainest accurate wording. If "is" or "has" is the clearest verb, use it. Don't inflate simple statements into "serves as", "stands as", "offers", or "features" unless the meaning genuinely changes.

Preserve useful voice: established vocabulary, cadence, bluntness, humor, uncertainty, and deliberate rough edges. Fix the weak passage, not every sentence around it. If a sentence could move unchanged to another project, it is probably filler; replace it with a project-specific fact, mechanism, consequence, or judgment, or delete it.

## 8. Keep the prose timeless

Keep stable reference prose free of incidental chronology. Reports and histories need dates when they establish the period, evidence, or sequence being discussed.

- Replace vague timing such as "recently" with a relevant date, or remove it when timing does no work. State a shared consultation date once when the required citation style permits.
- Keep future plans only if they are explicitly authored or explicitly requested by the user.

## 9. State conclusions and material limits

Lead an analytical paragraph with the supported result and its meaning, followed
by the precise condition that limits that interpretation. State each material
condition once; retain distinct limits when they change the conclusion.

Replace chains such as "does not equal", "does not demonstrate", and "does not
imply" that repeat the same misunderstanding with one affirmative conclusion
and its material condition. Preserve negative findings and substantive limits
on scope, uncertainty, comparability, causality, and verification. Necessary
negation remains valid: this is a rule about reasoning, not a word ban.

For documentation, describe behavior and foundational contracts the reader needs.
Keep clarifications that affect use or interpretation; omit defensive answers
to hypothetical misunderstandings the reader is unlikely to have.

## Evidence and claimed applications

Connect a cited method, course, or theory to an identifiable concept, the choice
it informs, and the resulting analysis or artifact. Read the relevant material
before claiming that connection, and cite a specific section or page when useful.
Elementary operations and generic labels do not establish disciplinary learning.

Choose sources for the claims they support. An availability notice may establish
a publication date, but does not support substantive analysis of the report.
Assignment instructions usually define the task rather than supply its
bibliography. Keep them as citations only when the discussion actually examines
them or citation is required. Preserve required attribution and provenance.

Distinguish observed practices from assumptions about audiences or genres.
Verify comparisons with examples, or state the project's own design choice
without inventing a contrast to justify it.

## 10. Make implicit contracts explicit

If a reader would otherwise need to inspect source code or infer behavior from examples to use the API correctly, the documentation is incomplete. Make foundational runtime contracts explicit in the reference text itself, not only in examples:

- what object a callback receives as `self`
- which fields are always present on returned objects
- what defaults apply when an option is omitted
- the difference between an omitted field and a field explicitly set to a special value
- lifecycle guarantees and deletion/reset semantics

## 11. Make API entries operationally complete

For functions and methods:

- document them as list entries, not as headings
- show the full signature in **`bold monospace`**
- state parameter types
- mark required parameters explicitly
- show defaults where they exist
- describe return values
- spell out callback signatures fully with parameter names

The result is usable as a reference manual without forcing the reader to inspect the source first.

## 12. Verify behaviors that are easy to misdocument

Before documenting defaults, special values, runtime fields, callback contracts, reset semantics, or lifecycle edge cases, verify them in the codebase instead of inferring them from naming or from existing docs. Be especially careful with:

- omitted versus explicit values
- sentinel values like `0`, `false`, or empty tables
- runtime-added fields on objects
- persistence versus ephemeral state
- cleanup, stop, and restart semantics

## 13. Preserve examples, but control where they live

- Keep examples in the main documentation file when they help readers learn the grammar of the API.
- Leave short one-line grammar examples inline when they directly clarify the adjacent text.
- Move medium or long inline examples into local `<details>` blocks when they interrupt the section's explanatory flow.
- Keep broader, tutorial-like, or comparative examples in dedicated examples sections when the file already has them.
- Do not delete an example unless it is wrong, misleading, or redundant with a better one.
- Shorten verbose example comments.
- Advanced examples shouldn't shy away from being complex. That is their purpose.
- Examples show practical applications, not made-up improbable use cases. Designing the example is half of the work.

## 14. Formatting patterns

- Headings carry the point, not just the topic ("Pick the mode first", not "Modes"). Sentence case. A task heading is a bare verb phrase ("Create an instance"). A concept heading is a noun phrase. One h1 per page, no skipped levels.
- Avoid tiny tables when prose or lists are clearer.
- Avoid inline-header list spam unless that shape is genuinely the clearest format.
- Use bold mainly for structural anchors such as method signatures, not emphasis.
- Indent code snippets with tabs. Write real paths and real symbols.

## Voice and repo specifics

- Apply the **unslop** skill to every doc this skill touches. That skill owns the slop-pattern catalog: AI vocabulary, filler, hedging, formatting tells.
- PR descriptions and commit messages are writing too. Every layer except Diátaxis applies to them.
- Product UI strings are not documentation. Use your product's copy guidelines for those.
- Make every count or tree claim true at the commit that lands it, and include the command that regenerates it.

## Worked example

Before:

> Configuration of the proto import ratchet budget script parameters is performed via budget.json. Note that it's important to remember that running with --write, which updates the committed budget to reflect the current count, should only be done when lowering it. If exceeded, CI fails.

After:

> `budget.mjs` reads the committed budget from `budget.json` and counts the files that import protos. If the count exceeds the budget, CI fails. Run `budget.mjs --write` only to lower the budget.

The fixes, by layer: "configuration is performed" becomes "`budget.mjs` reads", so someone does something (Google). "Ratchet" goes away. The script's real filename does the naming (jargon rule). The five-noun string breaks up into plain clauses (Global English). The hedge "note that it's important to remember" is deleted (cut every word that does no work). The failure condition moves ahead of the step it explains (STE). The buried "should only be done when lowering" becomes a command with "only" next to its verb (STE). "If exceeded" gets a subject: the count (Global English).

## Review checklist

Apply to any prose this skill covers. Item 1 applies only to document sets:

1. Does every documented topic belong to this project rather than a prerequisite tool?
2. Can you state one job for each file, and does every section serve that job?
3. Does the structure suit the genre and preserve required sections or fields?
4. Is the file structure consistent, or do multiple documentation styles coexist? Normalize first.
5. Is every instruction written as a command, with its condition in front?
6. Does the syntax clarify relationships at the reader's level, with varied sentence lengths?
7. Can any word be cut without losing meaning? Cut it.
8. Is "only" next to the word it changes? Does every "it" point at one thing? Does every clause keep its verb?
9. Does each thing have exactly one name across the docs?
10. Would a developer say these words out loud? Replace invented metaphors and fancy synonyms with the plain word or the real symbol name.
11. Are all symbols, paths, and counts real at this commit, with the commands that regenerate the counts?
12. Are defaults, sentinel values, and lifecycle contracts verified against the code, not inferred?
13. Does analysis lead with a supported result and its meaning, state each material condition once, and preserve negative findings, relevant dates, and the author's voice?

## Editing rules

- Edit the documentation file directly.
- Do not invent APIs, features, behaviors, or options that are not present in the codebase.
- Do not rewrite the entire file unless the structure is genuinely broken.
- Do not produce a sidecar summary file.
- If you make structural changes, ensure the table of contents, anchors, cross-links, and section ordering stay synchronized.

When you finish, give a short completion note that lists only the categories of
changes made. If you changed the file architecture, include the compact
`path -> role` map that guided the change.
