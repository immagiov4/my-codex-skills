---
name: docs-doc
description: "Revise documentation, analytical reports, and existing policies or legal notices for purpose, structure, evidence, author voice, and readable prose. Use for document sets, reports, manuals, references, readmes, RFCs, PR descriptions, and commit messages."
---

Revise purpose and structure before polishing sentences. Edit the requested files
in place, or return the requested text. For an audit-only request, identify the
affected passages and the smallest fixes without rewriting them. Create a separate
report only when the user asks for one.

The user's instructions, required format, and substantive requirements determine
the document's shape. Apply editorial defaults within those constraints.

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

1. Establish scope and attribution. Use the requested files and directly linked
   material needed to understand them. Choose the author's first-person or
   impersonal voice, keeping it consistent within each deliverable.
2. Check the substance. Connect claims to the supplied evidence, verified sources,
   or code when applicable. Distinguish observations, interpretations, plans, and
   unresolved facts. Preserve required fields, qualifications, and attribution.
3. Organize for the reader's task. Give each section a purpose and a natural place
   in the reading path. Consolidate repetition and relocate material when it
   belongs elsewhere; split files when distinct reader needs justify the split.
4. Revise connected prose using the principles below and the relevant reference.
   Preserve sound passages. When the user reports a recurring defect, review the
   whole requested document for that defect.
5. Read consecutive paragraphs together. Check the progression, the author's
   voice, and the retained meaning, then verify affected anchors and cross-links.

The revision is complete when every section serves the intended reader, required
content and material limits remain visible, supported claims stay accurate, and
the reading path works. Identify unresolved substantive facts rather than making
them sound certain.

## Prose principles

- Develop each paragraph around a connected thought. Keep a claim with its reason,
  condition, or consequence when that helps the reader follow it.
- Let sentence length follow meaning and the reader's knowledge. Split where the
  idea changes or the reader must backtrack; use connective words where they carry
  a real relationship. Joining sentences solely to lengthen them also weakens prose.
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

Give a short note describing the categories of changes. When file architecture
changes, include the compact `path -> role` map that guided the revision.
