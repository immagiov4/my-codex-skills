---
name: writing-for-humans
description: "Write or revise text for people, including conversation, documents, reports and messages, preserving the author's voice, the reader's competence and supported meaning. Use for human-facing prose; agent instructions follow writing-for-agents."
---

# Writing for humans

Start with what this reader needs to understand, decide or do, using the author's voice and the requested language, medium and structure. Infer their knowledge from the task and supplied examples, then develop the evidence, mechanism and consequence at that level. Preserve good passages and the scope of a narrow edit.

Write each plain-text or Markdown prose paragraph on one physical line and let the reader's interface wrap it visually. This includes Git commit messages, PR/MR descriptions, documentation and chat messages; fixed-width conventions such as 72-column commit bodies do not override this rule. Use blank lines between distinct paragraphs and preserve structural line breaks in code, lists, tables and other syntax. Before saving, committing or publishing, inspect the actual text for inserted line breaks inside prose paragraphs.

## Write the thought

Keep related ideas connected so each sentence develops the explanation rather than making the reader assemble isolated assertions. Put sentence boundaries where the thought changes or the syntax needs relief, retaining the useful connections between facts, reasons and consequences. Short steps work in a procedure; an argument needs its reasoning. Apply the same judgment to notes, captions and conclusions.

Choose familiar, precise words and established terms, keeping one name for each concept and making actors and references clear. Preserve product, skill and interface names in their established form; a preference for a language governs the surrounding prose unless the user requests renaming or localization. Give a qualification its specific substance beside the claim when it changes meaning or a decision. Respect the reader's existing knowledge, using the space for evidence and choices rather than reminders of obvious distinctions or imagined extreme interpretations.

Preserve attribution, quantities, dates, negation, substantive exceptions and the difference between observed behavior and plans. Match factual claims to the supplied evidence or sources actually checked, retaining unresolved facts where needed. Choose headings, lists and tables for the reading task and requested format, with emphasis carrying information rather than filling the page.

## Choose the relevant guidance

Read only the references the task calls for, alongside [prose patterns](references/prose-patterns.md) when drafting or polishing more than a brief reply:

- [Conversation and messages](references/conversation.md) for explanations, correspondence, progress updates and short replies.
- [Documentation](references/documentation.md) for document sets, manuals, readmes and guides; add [software reference](references/software-reference.md) when describing interfaces or observable behavior.
- [Reports](references/reports.md) for analytical, academic and project writing.
- [Legal and policy documents](references/legal-documents.md) for editorial work on obligations, notices and policies.
- [Public and persuasive writing](references/public-writing.md) for educational posts, product copy and campaigns. A marketing workflow can supply offer and audience research while this skill owns the prose and its review.

For mixed work, choose guidance by deliverable. Instructions an agent executes belong to `writing-for-agents`; apply this skill to the accompanying human-facing explanation. Tool-specific document skills own rendering and editing mechanics.

## Check and review

Before sending any prose, read it in context for the intended meaning, useful connections and the reader's level. When the user identifies a recurring defect, check every affected part, including notes, rather than repairing only the quote.

Then test each sentence against the reader: do they already know it, or would removing it change what they understand or decide? If neither, delete it. How the work was done in the session, such as commands run, restarts, attempts and the writer's own process, usually fails this test.

Private responses and documents intended only for the requester use the guidance and local reread above, including substantive drafts and document-wide revisions.

For material intended for publication or for people beyond the requester, a substantive draft or rewrite, or a user-requested correction across a document, requires an independent reviewer following [independent review](references/independent-review.md). A substantive change creates or reshapes a complete explanation, message or section; a typo or a routine short conversational reply needs the local check. Within that audience scope, a request to fix the writing throughout triggers review even when individual edits are small. Apply independent review and its recheck procedure to the requested deliverable; reviewer findings and brief coordination messages use the local check, with findings assessed through the resolution procedure.

Deliver once the required content and evidence are intact, consequential findings are resolved and the affected prose has been checked again. Save or edit in the requested destination, describing the useful changes briefly when needed.
