---
name: unslop
description: Cut AI tells from any writing. Must always apply.
---

# Unslop

Revise formulaic prose while preserving meaning, the author's voice, and the
reader's needs. Treat patterns as editing signals, not evidence of authorship.

When **docs-doc** applies, follow its guidance on purpose, structure, evidence,
genre, and paragraph flow. Use this catalog within those decisions. Explicit
instructions, required wording, and substantive accuracy govern the revision.

## Process

1. Scan for the patterns below.
2. Rewrite. Preserve meaning, match intended tone.
3. Preserve the author's voice and the reader's level (see next section).
4. Check the whole text for the recurring patterns found, not only the quoted examples. Judge clarity and substance rather than guessing authorship.

## Voice and rhythm

Preserve the voice appropriate to the author, audience, and genre.

- **Use judgment where the genre calls for it.** Ground interpretation in evidence and preserve the author's position; do not invent opinions to make prose lively.
- **Follow the thought.** Let sentence length reflect the relationship between ideas. Preserve useful connective words and keep related reasoning together; split when the idea changes or readers must backtrack.
- **Preserve complexity that matters.** Keep uncertainty, conditions, and exceptions that change the meaning, using precise words instead of added sentiment.
- **Keep the chosen authorial voice.** Use first person when it fits the author and genre; formal or organizational prose can remain impersonal.
- **Preserve natural voice.** Keep useful variation and deliberate rough edges; invent neither mistakes nor personal experience to simulate authenticity.
- **Be specific.** Name the observation, mechanism, or consequence supported by the material. Preserve interpretation when the genre calls for it.

## Patterns to detect and fix

### Content

1. **Puffery.** "pivotal moment", "testament to", "evolving landscape", "setting the stage for", "indelible mark", "deeply rooted". Cut puffery, state what happened.
2. **Name-dropping.** Listing authorities or outlets without explaining their contribution. Identify the claim each relevant source supports and retain required attribution.
3. **Superficial -ing phrases.** "highlighting...", "ensuring...", "reflecting...", "showcasing...", "fostering..." can add an unsupported interpretation. State the supported relationship or remove the filler; preserve grammatical constructions that carry meaning.
4. **Unsupported promotion.** Replace claims such as "groundbreaking" or "renowned" with supported descriptions. Preserve persuasive language when the requested genre calls for it and the claim is accurate.
5. **Vague attributions.** "Experts believe", "Industry reports suggest", "Some critics argue". Name the source or delete.
6. **Formulaic challenges.** "Despite challenges... continues to thrive." Replace with specific facts.

### Language

7. **Inflated vocabulary.** Words such as "delve", "pivotal", "tapestry", or "underscore" can pad a plain claim. Use the clearest accurate word, retaining established terms and connectives that do useful work.
8. **Inflated copulas.** Use "is" or "has" when they express the whole meaning. Retain "serves as" or "features" when the role or function actually matters.
9. **"Not just X, but Y."** State the point directly instead.
10. **Rule of three.** Forcing ideas into groups of three. Use the natural number.
11. **Synonym cycling.** Protagonist, main character, central figure, hero all in one paragraph. Pick one, repeat it.
12. **False ranges.** "from X to Y" where X and Y aren't on a meaningful scale. List topics directly.

### Style

13. **Staged punctuation.** Replace decorative interruptions with a direct grammatical connection. Choose punctuation for meaning and genre, rather than turning every clause into a separate sentence.
14. **Dramatic colons.** Rewrite staged reveals and redundant lead-ins into direct prose. Keep a colon when it introduces an explanation, specification, list, or example with a clear grammatical role.
15. **Boldface overuse.** Don't bold every proper noun or acronym.
16. **Inline-header lists.** The tell is a bold label and colon that restates the line: "**Performance:** Performance improved...". Convert those to prose. A bold lead-in that ends in a period, names the item, and is followed by genuinely new detail ("**Schema in TypeScript.** Tables live in one file.") is fine, not a tell.
17. **Title case headings.** Use sentence case.
18. **Decorative emojis.** Remove from headings and bullets.
19. **Inconsistent typography.** Follow the document's language and house style. Preserve exact quotations, code, and syntax; changing quotation marks mechanically can damage them.

### Communication artifacts

20. **Chatbot phrases.** "I hope this helps!", "Let me know if...", "Of course!", "Certainly!", "Found the smoking gun!" Remove.
21. **Stock source-gap disclaimers.** Replace generic disclaimers with the relevant date, missing evidence, or precise limit when it affects the claim; otherwise remove them.
22. **Sycophantic tone.** "Great question! You're absolutely right!" Respond directly.

### Filler

23. **Filler phrases.** "In order to" becomes "To". "Due to the fact that" becomes "Because". "It is important to note that" gets deleted.
24. **Excessive hedging.** "could potentially possibly be argued that it might" becomes "may". Preserve uncertainty and conditions supported by the evidence or required by the subject.
25. **Generic conclusions.** "The future looks bright." State specific plans or facts.

### Jargon

26. **Abstract metaphor nouns.** Substrate, wedge, vector, locus, vantage, nexus, primitive (as noun), harness (as metaphor), surface (as in "API surface"), bedrock, scaffolding (as metaphor), modality, paradigm, gold-plating, ratchet (as metaphor), evacuate (for moving code), endgame, north star, flywheel. These read as technical but usually have a plainer concrete word. "Substrate" becomes "base". "Wedge in" becomes "add". "Vector" becomes "way" or "method". "Gold-plating" becomes "more than the job needs". "Ratchet" becomes the mechanism's real name or "a limit that only tightens". "Evacuate" becomes "move out". "Endgame" becomes "the last phase". Pick the concrete word.

### Plain speech

27. **Vague benefits.** In factual prose, explain the supported behavior or consequence: "`.toSQL()` returns the exact string sent to the database" or "a column rename fails the build". Keep interpretation, reader context, and required standard wording when they serve the document; make project-specific claims specific.
28. **Mechanical fragmentation.** Repeated standalone sentences can obscure a shared reason, condition, or consequence. Connect the thought naturally, preserving the reader's level; simplify overloaded syntax where it forces backtracking. Do not alternate sentence lengths by formula.
29. **Voice and agency.** Prefer active voice when it clarifies who acts: "the compiler validates queries" names the actor. Preserve passive constructions that fit the genre, authorial voice, or intended emphasis.
30. **Unsupported intensifiers.** Replace "significantly improves" with a supported effect or measured difference. Keep adverbs that specify a real degree, time, frequency, or condition.
31. **Prefer the plain word.** "utilize" becomes "use", "leverage" becomes "use", "facilitate" becomes "help", "numerous" becomes "many", "in the event that" becomes "if". The fancier synonym is rarely clearer.
32. **Obviousness and defensive padding.** Cut adjectives, process narration, and exclusions that the context already establishes. Keep the specific fact that changes interpretation, including uncertainty or a real limitation. When `$docs-doc` also applies, it owns document-level voice, evidence, and genre decisions.
