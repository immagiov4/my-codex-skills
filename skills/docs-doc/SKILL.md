---
name: docs-doc
description: "Revise documentation, analytical reports, and existing policies or legal notices for purpose, structure, evidence, author voice, and readable prose. Use for document sets, reports, manuals, references, readmes, RFCs, PR descriptions, and commit messages."
---

Revise the requested files in place or return the requested text, starting with
its purpose and structure before polishing sentences. The user's instructions, format and substantive requirements
determine the document's shape; for an audit-only request, identify the affected
passages and the smallest fixes, producing a separate report when requested.

## Choose the relevant guidance

Identify the document's author, reader, purpose, and genre. Read the matching
reference before making structural or genre-specific decisions:

- For documentation sets, readmes, architecture docs, manuals, tutorials,
  how-to guides, or software reference documents, read
  [documentation](references/documentation.md).
- When documenting software interfaces or behavior, including defaults,
  callbacks, persistence, and lifecycle contracts, also read
  [software reference](references/software-reference.md).
- For analytical, academic, or project reports, read
  [reports](references/reports.md).
- For legal notices, contracts, or internal policies, read
  [legal and policy documents](references/legal-documents.md).

Load only the references that fit the requested document. For a mixed assignment,
choose guidance separately for each deliverable or section. A privacy notice that
mentions software still follows the legal branch. Apply **unslop** to the prose;
that skill owns the pattern catalog, while this skill owns purpose, structure,
evidence, and paragraph flow.

## Editing workflow

1. Establish the scope and authorial voice from the requested files and the linked
   material needed to understand them, choosing first-person or impersonal prose
   according to who speaks in each deliverable.
2. Check claims against the supplied evidence, verified sources or relevant code,
   preserving attribution and required fields while distinguishing observations,
   interpretations, plans and unresolved facts.
3. Organize sections around the reader's task so each has a purpose and a natural
   place in the reading path. Consolidate repetition and move detail to its owning
   section; split files where distinct reader needs justify it.
4. Revise using the principles below and the relevant reference, preserving sound
   passages and checking the whole document, including notes, for any recurring
   defect the user has identified.
5. Read consecutive paragraphs together to check the progression, authorial voice
   and retained meaning, then verify affected anchors and cross-links.

## Reader knowledge and paragraph flow

Keep related ideas connected throughout the document, developing each mechanism
and its consequence as a coherent paragraph at the reader's established level.
Use sentence boundaries where the thought changes or the reader would otherwise
need to backtrack, checking that each sentence advances the explanation in both
the main text and working notes.

For experienced readers, focus on the evidence and decisions they need, placing
a qualification beside its claim when the condition changes the meaning or a
concrete decision. State that condition once so the paragraph develops the
reasoning without repeated cautions or explanations of obvious distinctions.

## Prose principles

- Use familiar, precise words and the discipline's established terms. Explain the
  terms this reader needs, using one name consistently for each concept.
- Make actors and references clear. Prefer active voice when it clarifies who acts;
  preserve passive constructions that fit the chosen voice or emphasis.
- In procedures, state actions directly and put the condition before the action
  it governs. In analysis, develop the reasoning that supports the claim.
- Place modifiers such as "only" next to what they change. Resolve ambiguous
  pronouns, noun strings, and conjunctions while retaining useful grammatical words.
- Choose punctuation for its grammatical role and the document's language.
  Preserve dates, uncertainty, exceptions, and negation when they change the meaning.
- Use headings and lists to reveal structure. Sequence actions with numbered
  lists, keep list items parallel, and use tables for useful comparisons or mappings.
  Keep heading levels, navigation, and section order consistent after an edit.

These principles adapt the [Google developer style guide](https://developers.google.com/style),
[STE](https://www.asd-ste100.org/), and John R. Kohl's *Global English Style Guide*.
Use them within the document's genre, preserving requested templates and language
conventions. If a stylistic rule makes a passage less accurate or less readable,
revise it another way or preserve it.

## Completion

The revision is complete when each section serves the reader's task, required
content is present, claims match their evidence and the reading path works. Keep
unresolved substantive facts visible and give a short note describing the changes,
including the `path -> role` map when the file structure has changed.
