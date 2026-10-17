# Improve concrete user journeys

These recipes extend the two supplied Wyatt Feaster videos with 2026 app critiques, demonstrated redesigns, and NN/g explanations. Choose the task to improve, inspect the linked passage, and adapt the procedure to the project's actual data and interactions. The procedures and Codex prompts are collection adaptations.

## Choose by the user's task

| Task or obstacle | Recipes to combine |
|---|---|
| A routine form requires too many initial decisions | U01; [A08 for retained answers after an error](applicazioni.md#a08) |
| Users encounter registration before understanding the result | U02–U03; [A10 for completion](applicazioni.md#a10) |
| A trial, upgrade, or expiry notice is difficult to understand | U04–U06 |
| Mobile shoppers lose track of quantity, price, or the purchase action | U07; [P09 for product imagery](procedure.md#p09) |
| A quote or reservation leaves costs and conditions unclear | U08–U09 |
| Search loses the item, query, or comparison position on navigation | U10–U11; [A07 for no results](applicazioni.md#a07) |
| A button changes appearance without explaining its outcome | U12; [A08 for recovery](applicazioni.md#a08) |
| Collection actions, search scope, or playback become inconsistent | U13–U14 |
| A dashboard looks complete until a menu or real record is opened | U15–U16; [A06 for existing controls](applicazioni.md#a06), [A07 for empty states](applicazioni.md#a07), [A08 for errors](applicazioni.md#a08) |
| Users cannot find the status of a submitted request again | U17; [A10 for confirmation](applicazioni.md#a10) |
| A complex task loses answers or overwhelms the user | U18; [A09 for actual completed steps](applicazioni.md#a09) |
| Metrics repeat across views or a feature illustration is generic | U19–U20; [P11 for a working product demo](procedure.md#p11) |
| The starting configuration or return journey ignores a user's goal | U21–U22 |

For visual composition, combine the chosen task recipe with the relevant [website combination](modelli.md), typography, or CSS effect. An individual workflow can fit a shop, dashboard, service portal, or media library without adopting the recording's whole product.

## Translate the psychological explanation into a concrete change

| Explanation in the videos | Implementable use | Evidence to collect in the project |
|---|---|---|
| Decision effort and defaults | U01 selects safe editable operational choices; declarations remain explicit. | Correct values, edits, and recoverable submission. |
| Goal gradient and already-earned progress | [A09](applicazioni.md#a09) counts actual completed steps in a defined process, including an already completed step if it belongs to that process. | The displayed total agrees with completion records, including Back and retries. |
| Seeing value before signup | U02 shows actual useful output and explains what an account enables. | Users can assess the preview and retain it through the supported account transition. |
| Investment in a configured object | U03 preserves a meaningful draft the user chose to create. | Object identity and edits survive failed registration and return navigation. |
| Loss aversion and urgency | U04 explains a real deadline and its actual consequences with supported alternatives. | Dates, consequences, and actions agree with authoritative policy. |
| Price context and anchoring | U05 compares matching billing periods and authentic reference prices. | The user can identify the amount payable and the basis of savings. |
| Predictability and feedback | U06, U12, and U17 clarify real events, outcomes, and next steps. | Expected action, observed outcome, and recovery agree. |
| Continuity while comparing and browsing | U10 and U14 preserve task context and shared state. | Returning or browsing keeps the expected query, item, queue, or position. |

These explanations are hypotheses for a particular task. A creator's popularity, before/after composition, or proposed psychology does not establish a measured conversion improvement. For a product evaluation, define the same task before and after the change and assess completion, misunderstood choices, retries, time, and user feedback as appropriate. Describe observed results separately from the expected benefit.

## Read the evidence precisely

All nine added videos were published in 2026. Their complete available YouTube transcripts were reviewed; six selected frames were observed in Chrome with playback paused and muted. Dates and view counts are YouTube metadata snapshots from 30 September 2026. The [video catalog](video.md) identifies each source and its related recipes; the [atlas](atlante.md) preserves selected compositions.

The subsequent additions include the supplied Kole Jain app redesign and Wyatt Feaster's retention video found in homepage recommendations, with their complete transcripts reviewed. U19–U22 collect context-specific metrics, real UI illustrations, explicit personalization, and a useful return journey. The retention video describes a 1,000-app analysis without supplying its dataset or measurements in the reviewed material; its psychological and retention explanations remain author claims. These adaptations use actual user progress and controllable reminders, preserving supported account and export choices.

The uxpeak psychology video's narration recommends threatening file-loss wording at [9:01](https://www.youtube.com/watch?v=2TlIg3VokY8&t=541s) and fake progress at [11:17](https://www.youtube.com/watch?v=2TlIg3VokY8&t=677s), while its description explicitly rejects fake urgency and progress. U04 uses actual policy and neutral choices; A09 counts actual work. Its price example compares a monthly subscription with a one-time laptop purchase at [10:05](https://www.youtube.com/watch?v=2TlIg3VokY8&t=605s); U05 makes periods and the comparison basis explicit.

The three-redesign video describes A/B tests without providing experimental data in the reviewed material. Its trial reminder, fixed quote, reference discount, and cancellation examples are adapted only when the product actually supports those facts. The Juxtopposed recordings provide critiques and proposed redesigns of the interfaces shown at that time; their ratings and preferences are the author's assessments. The recipes supply checks for the implemented product.

## Use the free route

Start with public video passages, the project's authorized flows, original assets, and existing components. Inspect a complete task in the browser, then ask Codex to implement the selected pattern locally. Optional illustration work can use native Codex image generation within the account's limits; reuse the [media workflow](immagini-video.md) when appropriate.

Mobbin is an optional reference library promoted by several videos. Its permanent Free tier was checked on 30 September 2026: the latest four apps and four sites, up to three collections; search, flows, and animations are excluded. A demonstrated full-library search therefore needs a different free reference route. Recheck limits before relying on the service. [Official pricing](https://mobbin.com/pricing)

For narrow confirmation of a pattern, use primary guidance: [optional registration](https://www.nngroup.com/articles/optional-registration/), [progressive disclosure](https://www.nngroup.com/articles/progressive-disclosure/), [filters](https://www.nngroup.com/articles/applying-filters/), [scroll position](https://www.nngroup.com/articles/saving-scroll-position/), [validation](https://design-system.service.gov.uk/patterns/validation/), and [cognitive design patterns](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o1p03-consistent-design/). Older documentation corroborates the 2026 videos and retains its own publication context.

For persistent bars, panels, and compact controls, assess the applicable accessibility criteria in the project. WCAG 2.2's AA [target-size minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum) is 24×24 CSS pixels or an allowed exception; the separate AAA [target-size criterion](https://www.w3.org/WAI/WCAG21/Understanding/target-size) uses 44×44. Also test [focus visibility around persistent content](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum) and [status announcements](https://www.w3.org/WAI/WCAG21/Understanding/status-messages). A screenshot comparison verifies composition; keyboard, state-transition, and user-task checks establish the corresponding behavior.

## Index

- [U01 · Editable defaults that shorten a routine task](#u01)

- [U02 · A useful result preview before account creation](#u02)

- [U03 · Preserve a configured draft through signup](#u03)

- [U04 · Explain a real deadline and its consequences](#u04)

- [U05 · Compare prices with matching periods and totals](#u05)

- [U06 · A trial timeline with the actual first charge](#u06)

- [U07 · A mobile product page with quantity and total in view](#u07)

- [U08 · Quotes that distinguish a fixed price from an estimate](#u08)

- [U09 · A booking summary with dates, nights, total, and cancellation](#u09)

- [U10 · Dish search that carries context into the menu](#u10)

- [U11 · Configured basket items and explicit substitution choices](#u11)

- [U12 · Control states that confirm the actual action](#u12)

- [U13 · Consistent library actions and search scopes](#u13)

- [U14 · A persistent player while browsing](#u14)

- [U15 · Dashboard structure chosen from the data and task](#u15)

- [U16 · Progressive disclosure with complete secondary interactions](#u16)

- [U17 · A status tracker that remains findable after submission](#u17)

- [U18 · A complex task with clear steps and sensory controls](#u18)

- [U19 · Metrics that belong to the current task](#u19)

- [U20 · Feature illustrations made from the actual product UI](#u20)

- [U21 · Personalization from an explicit task goal](#u21)

- [U22 · Return to useful progress with user-controlled reminders](#u22)

## U01

### Editable defaults that shorten a routine task

A booking or configuration form starts with useful, clearly visible choices that the user can change.

Procedure:

1. List the decisions required to complete this particular task. Separate operational choices from factual declarations, consent, and paid commitments.

2. Reuse an existing valid user preference or a safe operational default, such as a supported sort order. Show its selected value and a direct way to edit it.

3. Require an explicit answer where a preselected declaration or commitment could be submitted accidentally. Do not infer personal facts from a visual example.

4. Update dependent results from the actual selected values. Preserve edits after a recoverable submission error.

Original Codex prompt:

> Inspect this form and identify safe operational defaults supported by its domain. Implement visible editable selections, preserve user edits, and keep declarations and consent explicit.

Source steps: [2TlIg3VokY8 · 0:22](https://www.youtube.com/watch?v=2TlIg3VokY8&t=22s), [2TlIg3VokY8 · 1:00](https://www.youtube.com/watch?v=2TlIg3VokY8&t=60s), [Primary source](https://design-system.service.gov.uk/components/radios/), [Primary source](https://www.nngroup.com/articles/top-10-application-design-mistakes/).

Result check: Complete the task using defaults, then change every default and retry after an error. The recorded values match the visible choices; declarations remain explicit.

## U02

### A useful result preview before account creation

Users can assess an actual result before deciding whether to create an account to save or extend it.

Procedure:

1. Choose a useful portion of the existing service that can run without an account under its access rules. Identify what registration actually adds.

2. Run the real operation and show its available output: for example, found issues, a sample export, or a working preview. Describe any limits beside the result.

3. Offer account creation where it enables saving or continuing. Keep a supported guest route visible when the task allows one.

4. Carry the result into the next step and preserve it if account creation fails. Use A08 for recovery and A10 for actual completion.

Original Codex prompt:

> Adapt this workflow to show a useful authorized preview before registration. Explain what an account enables, preserve the result across that transition, and verify successful and interrupted paths.

Source steps: [2TlIg3VokY8 · 3:54](https://www.youtube.com/watch?v=2TlIg3VokY8&t=234s), [2TlIg3VokY8 · 4:32](https://www.youtube.com/watch?v=2TlIg3VokY8&t=272s), [Primary source](https://www.nngroup.com/articles/optional-registration/).

Result check: Try an empty result, a useful result, a failed operation, and interrupted registration. Each preview reflects real output, and continuing retains it.

## U03

### Preserve a configured draft through signup

A user names, styles, or configures an object and can continue with that same draft after creating an account.

Procedure:

1. Expose the smallest meaningful configuration the product already supports, such as a title, selected template, or theme.

2. Render those choices in a real draft. Keep the editable values and draft identity separate from whether the user is authenticated.

3. Follow the project's draft-storage and privacy rules when carrying it across registration. Use an explicit saved-state indicator only after storage succeeds.

4. Restore the draft after a failed signup or return navigation. Explain any real expiration or storage limit and provide the supported recovery route.

Original Codex prompt:

> Keep this configured draft intact across the existing signup flow. Reuse the project's storage boundary, retain its identity and edits, and demonstrate recovery after failed registration.

Source steps: [2TlIg3VokY8 · 5:38](https://www.youtube.com/watch?v=2TlIg3VokY8&t=338s), [2TlIg3VokY8 · 6:24](https://www.youtube.com/watch?v=2TlIg3VokY8&t=384s), [Primary source](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p02-back-undo/).

Result check: Configure a draft, navigate to signup, fail validation, return, and complete registration. Choices and object identity survive the supported transitions.

## U04

### Explain a real deadline and its consequences

A storage, trial, or reservation notice gives the actual deadline, affected content, and available alternatives.

Procedure:

1. Read the authoritative expiration policy and current record. Derive dates and consequences from that state.

2. Name the affected item and explain what happens at the deadline in plain language. Use a countdown only if it represents an actual changing deadline.

3. Present supported alternatives such as export, retain a basic plan, extend, or dismiss. Use neutral labels and disclose each choice's cost or consequence.

4. Connect the action to its real outcome and refresh the notice when the policy or record changes. Preserve work where the product permits it.

Original Codex prompt:

> Build this notice from the actual expiration policy. Name what is affected, show the real date and supported alternatives, and use neutral action labels with accurate consequences.

Source steps: [2TlIg3VokY8 · 9:01](https://www.youtube.com/watch?v=2TlIg3VokY8&t=541s), [Primary source](https://www.nngroup.com/articles/deceptive-patterns/).

Result check: Exercise an active deadline, an extended deadline, expiration, and dismissal. Displayed dates and available actions agree with the recorded policy.

## U05

### Compare prices with matching periods and totals

A pricing comparison makes recurring cost, billing interval, renewal, and any reference price understandable.

Procedure:

1. Use actual plan prices and the project's authoritative billing definitions. Identify whether each figure is per month, per year, or a one-time purchase.

2. Display the payable billing amount beside any monthly equivalent. Calculate comparisons over the same period and show that period.

3. Use a previous price or discount only when the product's pricing data establishes it. State the basis of a percentage saving or cheaper claim.

4. Place known fees, renewal conditions, and the relevant next action near the decision. Label remaining variable amounts as estimates.

Original Codex prompt:

> Make this price comparison use matching periods and actual totals. Show the amount billed, renewal terms, and the basis of any savings claim next to the purchase action.

Source steps: [2TlIg3VokY8 · 9:36](https://www.youtube.com/watch?v=2TlIg3VokY8&t=576s), [2TlIg3VokY8 · 10:05](https://www.youtube.com/watch?v=2TlIg3VokY8&t=605s), [Primary source](https://baymard.com/research-articles/product-page-price-discounts), [Primary source](https://www.nngroup.com/articles/sneaking/).

Result check: Switch billing intervals and compare the displayed equivalent with the actual charge. Savings use a stated matching basis, and variable costs stay identifiable.

## U06

### A trial timeline with the actual first charge

A trial offer shows when access begins, when billing starts, and how cancellation works.

Procedure:

1. Read the real trial duration, initial and renewal charges, cancellation policy, and reminder capability.

2. Lay out the meaningful events in order: access now, a reminder if supported, and the first charge on its actual date.

3. Show what the trial unlocks with authorized product examples. Identify payment requirements and recurring terms beside the action that starts the trial.

4. Link to the working cancellation route. Promise a reminder or a short cancellation procedure only when that behavior has been verified.

Original Codex prompt:

> Replace this trial offer with a clear timeline based on the real billing contract. Show product access, supported reminders, first charge, renewal, and the verified cancellation route.

Source steps: [zr37ibqXl1U · 2:03](https://www.youtube.com/watch?v=zr37ibqXl1U&t=123s), [zr37ibqXl1U · 2:33](https://www.youtube.com/watch?v=zr37ibqXl1U&t=153s), [zr37ibqXl1U · 3:40](https://www.youtube.com/watch?v=zr37ibqXl1U&t=220s), [Primary source](https://www.nngroup.com/articles/sneaking/).

Result check: Start with representative dates and billing intervals. The timeline agrees with the billing record, the action explains the commitment, and cancellation is reachable.

## U07

### A mobile product page with quantity and total in view

Product identity, unit price, selected quantity, and the purchase action remain coherent while browsing a long page.

Procedure:

1. Compose the page with the actual product, unit of sale, availability, verified review data, and authorized images. Use P08 and P09 for consistent typography and imagery.

2. Give controls on photographs a contrasting backing that works over bright, dark, and busy crops. Retain accessible labels when removing redundant visible labels.

3. Keep quantity separate from the product name. Calculate the selected total from authoritative price and quantity data; label units and constraints.

4. Where the long-page task needs it, keep product context and quantity/purchase controls available during scrolling. Reserve space so the persistent bar does not cover content or focus.

5. Offer quantity shortcuts only for supported amounts. Keep the normal selector available and preserve the selected amount when the bar changes position.

Original Codex prompt:

> Adapt this product page to mobile with coherent unit pricing, quantity, and total. Keep purchase controls usable during scrolling, preserve selection, and verify image contrast and keyboard visibility.

Source steps: [GGg61sdEjeI · 0:37](https://www.youtube.com/watch?v=GGg61sdEjeI&t=37s), [GGg61sdEjeI · 10:16](https://www.youtube.com/watch?v=GGg61sdEjeI&t=616s), [GGg61sdEjeI · 10:57](https://www.youtube.com/watch?v=GGg61sdEjeI&t=657s), [GGg61sdEjeI · 12:16](https://www.youtube.com/watch?v=GGg61sdEjeI&t=736s), [Primary source](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum).

Result check: Check long names, image extremes, stock limits, quantity changes, scrolling, and the mobile keyboard. The displayed total matches the selected amount and every focused control stays visible.

## U08

### Quotes that distinguish a fixed price from an estimate

A comparison of rides or services makes price certainty, arrival, and the decision clear.

Procedure:

1. Inspect the quote response and identify which values are binding prices, estimated ranges, current availability, and arrival estimates.

2. Show a single price when the service actually guarantees it. Preserve a labeled range when the amount can still vary.

3. Group each price with its relevant service, availability, and arrival information. State the comparison basis for cheaper or faster labels.

4. Revalidate the selected quote at the product's required boundary and explain a changed or expired quote before commitment.

Original Codex prompt:

> Present these service quotes with clear certainty labels. Preserve real estimates, compare like-for-like options, and make quote expiration or a changed amount visible before confirmation.

Source steps: [zr37ibqXl1U · 6:55](https://www.youtube.com/watch?v=zr37ibqXl1U&t=415s), [zr37ibqXl1U · 8:28](https://www.youtube.com/watch?v=zr37ibqXl1U&t=508s), [Primary source](https://www.nngroup.com/articles/explicit-differences/).

Result check: Compare fixed and variable quotes, unavailable services, expiration, and a changed price. The user can identify what is guaranteed before confirming.

## U09

### A booking summary with dates, nights, total, and cancellation

A booking page combines credible property information with the complete selected reservation.

Procedure:

1. Use authorized venue photographs and actual host, amenity, and review information. Keep descriptive copy tied to supported facts.

2. Derive weekday labels, date range, and night count from the selected dates and the project's date/time rules.

3. Calculate the payable total with known fees. Show the nightly rate as supporting detail, and use discounts only when established by pricing data.

4. Place the selected stay and real cancellation deadline beside the booking action. Allow changing dates while retaining other valid choices.

5. Show confirmation and reference details after the booking is recorded; use A10 for the completion state.

Original Codex prompt:

> Build the reservation summary from the selected dates and authoritative prices. Show nights, fees, total, and cancellation near the action; preserve valid choices when dates change.

Source steps: [zr37ibqXl1U · 10:55](https://www.youtube.com/watch?v=zr37ibqXl1U&t=655s), [zr37ibqXl1U · 12:45](https://www.youtube.com/watch?v=zr37ibqXl1U&t=765s), [zr37ibqXl1U · 13:06](https://www.youtube.com/watch?v=zr37ibqXl1U&t=786s), [zr37ibqXl1U · 13:29](https://www.youtube.com/watch?v=zr37ibqXl1U&t=809s), [Primary source](https://design-system.service.gov.uk/patterns/check-answers/).

Result check: Change dates across month boundaries, vary guest count, and test fee and cancellation variants. The summary, recorded stay, payable amount, and completion agree.

## U10

### Dish search that carries context into the menu

Searching for an item leads to its matching details and preserves the comparison context on return.

Procedure:

1. Choose one concrete task, such as finding a vegetarian dish and comparing two restaurants. Inspect that entire task in the reference, including the return path.

2. Carry the query and matching item identity into the restaurant or product view. Highlight or jump to the matching item when that supports the task.

3. Distinguish result types and scopes. Show matching dishes across suppliers only when the catalog and search service support that query.

4. Retain filters, comparison choices, and list position when returning to a stable same-session result list. Explain changed results when the data has refreshed.

5. Connect genuine reviews and review photos to the product they describe. Use A07 for no matches and A08 for failed search.

Original Codex prompt:

> Improve the complete item-search journey: carry the matching item into its menu, keep query and filters on return, and preserve the comparison position when results remain stable.

Source steps: [USwP7w9BKC0 · 3:43](https://www.youtube.com/watch?v=USwP7w9BKC0&t=223s), [USwP7w9BKC0 · 11:49](https://www.youtube.com/watch?v=USwP7w9BKC0&t=709s), [USwP7w9BKC0 · 12:50](https://www.youtube.com/watch?v=USwP7w9BKC0&t=770s), [USwP7w9BKC0 · 20:00](https://www.youtube.com/watch?v=USwP7w9BKC0&t=1200s), [Primary source](https://www.nngroup.com/articles/saving-scroll-position/), [Primary source](https://www.nngroup.com/articles/applying-filters/).

Result check: Search, open a match, customize it, go Back, and compare a second supplier. The query and list context survive; stale or empty results have a useful next step.

## U11

### Configured basket items and explicit substitution choices

A basket preserves each item's options, shows known costs, and handles unavailable stock with the user's chosen preference.

Procedure:

1. Use radios for a required single choice and checkboxes for multiple extras. Leave ordinary optional extras unchecked; use an exclusive None answer when the flow needs an explicit response.

2. Represent two copies with different options as distinct configured lines. Allow duplicating a line and changing the new copy's options without altering the original.

3. Show the running total with known fees before checkout. Identify estimates and which later selection determines the remaining cost.

4. Ask what to do about unavailable items where the service supports substitutions. Preserve that preference and explain an actual stock conflict before the order commits.

Original Codex prompt:

> Make basket lines preserve their individual options. Use appropriate single/multiple-choice controls, show known fees in the running total, and retain the supported substitution preference.

Source steps: [USwP7w9BKC0 · 4:50](https://www.youtube.com/watch?v=USwP7w9BKC0&t=290s), [USwP7w9BKC0 · 9:20](https://www.youtube.com/watch?v=USwP7w9BKC0&t=560s), [USwP7w9BKC0 · 13:10](https://www.youtube.com/watch?v=USwP7w9BKC0&t=790s), [USwP7w9BKC0 · 14:34](https://www.youtube.com/watch?v=USwP7w9BKC0&t=874s), [Primary source](https://design-system.service.gov.uk/components/checkboxes/), [Primary source](https://design-system.service.gov.uk/components/radios/).

Result check: Add two differently configured copies, edit one, remove it, and trigger unavailable stock. Options, totals, and substitution behavior agree with the actual basket state.

## U12

### Control states that confirm the actual action

Buttons and fields distinguish availability, interaction, pending work, success, and failure.

Procedure:

1. Enumerate the states the real control supports: default, focus, hover, pressed, disabled, and operation states where applicable.

2. Use the existing component family to make each state recognizable. Keep a keyboard focus indicator and an accessible name independent of decoration.

3. Treat pressed as interaction feedback. Confirm copied, saved, or submitted only after the corresponding operation succeeds.

4. Provide a concise nearby status message and recovery action when needed. Announce meaningful asynchronous changes without moving focus; use A08 for recoverable errors.

Original Codex prompt:

> Complete the states of these existing controls. Distinguish pressed feedback from confirmed success, connect operation states to real outcomes, and verify keyboard and asynchronous feedback.

Source steps: [EcbgbKtOELY · 7:29](https://www.youtube.com/watch?v=EcbgbKtOELY&t=449s), [EcbgbKtOELY · 8:07](https://www.youtube.com/watch?v=EcbgbKtOELY&t=487s), [EcbgbKtOELY · 8:23](https://www.youtube.com/watch?v=EcbgbKtOELY&t=503s), [Primary source](https://www.w3.org/WAI/WCAG21/Understanding/status-messages).

Result check: Use mouse, keyboard, and touch, then force pending, success, and failure. Visual feedback and announced status correspond to what happened.

## U13

### Consistent library actions and search scopes

A media or document library uses stable actions and makes the searched collection clear.

Procedure:

1. Define the actual meanings of Save, Favorite, Add to Collection, and Download. Reuse those actions and accessible labels across item, creator, collection, and library views.

2. Show downloaded or favorite status from real storage and record state. Explain unavailable actions instead of displaying success for unsupported operations.

3. Focus the search field when opening Search. Label whether it searches the entire catalog, current creator, or current collection.

4. Group result types and offer supported filters and sorts, such as Favorites, Downloaded, or Date Added. Preserve the active scope and query during detail/return navigation.

Original Codex prompt:

> Make library actions consistent across views and label each search scope. Preserve query and filters through navigation, and show download/favorite state from actual records.

Source steps: [yT_aFozeDc8 · 2:08](https://www.youtube.com/watch?v=yT_aFozeDc8&t=128s), [yT_aFozeDc8 · 5:52](https://www.youtube.com/watch?v=yT_aFozeDc8&t=352s), [yT_aFozeDc8 · 7:03](https://www.youtube.com/watch?v=yT_aFozeDc8&t=423s), [yT_aFozeDc8 · 8:48](https://www.youtube.com/watch?v=yT_aFozeDc8&t=528s), [Primary source](https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification).

Result check: Apply the same action in several views, then search globally and within a collection. Labels, results, state, and download availability remain consistent.

## U14

### A persistent player while browsing

Playback remains understandable and controllable as the user changes the page or queue view.

Procedure:

1. Place playback state at the project's appropriate shared boundary so ordinary browsing does not recreate the playing item.

2. Keep actual item identity, playback position, and the necessary controls visible in a compact player. Use readable control contrast and reserved space.

3. Make queue, details, and panel resizing explicit actions. Preserve track, position, and queue when opening another library view.

4. Resume across devices only when actual shared playback state and permissions support it. Adapt native-device controls to the web product's supported controls.

Original Codex prompt:

> Keep this player available while browsing using the existing shared state. Retain track, position, and queue, clarify panel controls, and test navigation and keyboard visibility.

Source steps: [yT_aFozeDc8 · 17:12](https://www.youtube.com/watch?v=yT_aFozeDc8&t=1032s), [yT_aFozeDc8 · 17:56](https://www.youtube.com/watch?v=yT_aFozeDc8&t=1076s), [yT_aFozeDc8 · 18:58](https://www.youtube.com/watch?v=yT_aFozeDc8&t=1138s), [Primary source](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum).

Result check: Start playback, browse, open/close the queue, resize, seek, and navigate back. The player retains the correct item and position, and keyboard focus remains visible.

## U15

### Dashboard structure chosen from the data and task

A dashboard uses a table, timeline, or chart according to the comparison the user needs to make.

Procedure:

1. Inspect representative domain records and name the task: compare rows, follow events, or see change over time.

2. Use a table for comparable records, a timeline for ordered events, or a chart for the relevant relationship. Keep chronological order and the project's units explicit.

3. Align comparable numeric columns consistently and make full truncated values accessible. Use status labels from actual domain states.

4. Add color or icons as supporting signals with readable labels. Keep inactive records understandable and indicate actions at the correct row or selection scope.

5. Use A06 for existing controls, A07 for empty states, and A08 for errors. Verify the same task with realistic large and incomplete records.

Original Codex prompt:

> Inspect the actual dashboard data and choose the representation for its main task. Preserve units, ordering, complete values, and meaningful status labels before adding decoration.

Source steps: [Ksx9C2-3yMo · 0:22](https://www.youtube.com/watch?v=Ksx9C2-3yMo&t=22s), [Ksx9C2-3yMo · 0:34](https://www.youtube.com/watch?v=Ksx9C2-3yMo&t=34s), [Ksx9C2-3yMo · 1:14](https://www.youtube.com/watch?v=Ksx9C2-3yMo&t=74s), [Ksx9C2-3yMo · 1:47](https://www.youtube.com/watch?v=Ksx9C2-3yMo&t=107s).

Result check: Compare representative records, inspect long values, follow event order, and use a status without relying on color. The representation supports the named task.

## U16

### Progressive disclosure with complete secondary interactions

Common actions stay easy to find while secondary actions have a usable menu, panel, or next step.

Procedure:

1. Identify the frequent action and the secondary controls for this task. Keep the frequent action visible, and choose an existing labeled disclosure pattern for the rest.

2. Implement the complete popover or panel: selected-object context, contents, empty/error behavior, and a clear close/return route.

3. Provide keyboard and touch access to actions demonstrated on hover or swipe. Set focus on opening and return it appropriately on closing.

4. For onboarding, reveal a useful next step after actual completion, or use A09 for a real checklist. Retain a supported way to skip or revisit guidance.

5. Test the disclosed state and the underlying page together, including nested decisions and content scrolling.

Original Codex prompt:

> Keep this task's frequent action visible and complete the secondary menu states. Preserve selected-object context, support keyboard and touch, and verify opening, action, closing, and focus return.

Source steps: [Ksx9C2-3yMo · 2:24](https://www.youtube.com/watch?v=Ksx9C2-3yMo&t=144s), [Ksx9C2-3yMo · 2:53](https://www.youtube.com/watch?v=Ksx9C2-3yMo&t=173s), [Ksx9C2-3yMo · 3:48](https://www.youtube.com/watch?v=Ksx9C2-3yMo&t=228s), [Ksx9C2-3yMo · 4:59](https://www.youtube.com/watch?v=Ksx9C2-3yMo&t=299s), [Primary source](https://www.nngroup.com/articles/progressive-disclosure/).

Result check: Open and close each secondary interaction using keyboard and touch, complete its action, and return. Context and focus remain correct; no essential action depends only on hover.

## U17

### A status tracker that remains findable after submission

An order or long-running service has a persistent route to its current state and next steps.

Procedure:

1. Offer the tracker after the request is recorded and include its supported reference on the confirmation page.

2. Make it reachable again from the product's existing order or request history. Explain any required lookup information and where the user can find it.

3. Map actual process states to plain language and chronological events. Distinguish invalid references, information not available yet, and a failed process.

4. Show the supported next step and relevant timing. Let users change contact or notification preferences only within the service's actual capabilities and cutoff rules.

5. Keep progress and updates tied to real events. Use A09 for a measured checklist and U12 for accessible status announcements.

Original Codex prompt:

> Add a persistent tracker for the recorded request using actual process states. Make it findable from confirmation and history, explain lookup failures precisely, and verify leaving and returning.

Source steps: [jiSNAXoaOh8 · 0:42](https://www.youtube.com/watch?v=jiSNAXoaOh8&t=42s), [jiSNAXoaOh8 · 1:21](https://www.youtube.com/watch?v=jiSNAXoaOh8&t=81s), [jiSNAXoaOh8 · 2:31](https://www.youtube.com/watch?v=jiSNAXoaOh8&t=151s), [jiSNAXoaOh8 · 3:10](https://www.youtube.com/watch?v=jiSNAXoaOh8&t=190s), [Primary source](https://www.nngroup.com/articles/status-tracker-progress-update/), [Primary source](https://design-system.service.gov.uk/patterns/confirmation-pages/).

Result check: Submit, leave, return through history, and refresh after a state change. Test a wrong reference and a not-yet-ready record; each has a distinct explanation and recovery route.

## U18

### A complex task with clear steps and sensory controls

Users can complete a complex flow with predictable language, retained work, and control over distracting presentation.

Procedure:

1. Observe the actual task and ask users about obstacles and useful adjustments. Base choices on task evidence and stated preferences.

2. Separate dependent decisions into clear steps when that helps the task, using U16 and A09 for disclosure and actual progress. Keep Back and editing predictable.

3. Use direct labels, concise instructions, and an identifiable primary action. Preserve entered answers when returning or correcting an error.

4. Honor reduced motion and provide control over optional animation, sound, and nonurgent reminders where present. Save preferences through the existing mechanism.

5. Test the flow with interruptions, keyboard navigation, and relevant user feedback. Treat cognitive design guidance as supplementary guidance; assess required accessibility criteria separately.

Original Codex prompt:

> Inspect this complex flow for unclear steps, lost answers, and distracting presentation. Preserve work, clarify actions, honor motion preferences, and validate the changes with task-based checks.

Source steps: [ss7OpC9V7h4 · 3:34](https://www.youtube.com/watch?v=ss7OpC9V7h4&t=214s), [ss7OpC9V7h4 · 4:01](https://www.youtube.com/watch?v=ss7OpC9V7h4&t=241s), [ss7OpC9V7h4 · 4:25](https://www.youtube.com/watch?v=ss7OpC9V7h4&t=265s), [ss7OpC9V7h4 · 5:12](https://www.youtube.com/watch?v=ss7OpC9V7h4&t=312s), [Primary source](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o1p03-consistent-design/), [Primary source](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p02-back-undo/).

Result check: Pause midway, return, correct an answer, and finish with reduced motion and keyboard use. Work is retained, the next step is understandable, and presentation controls take effect.

## U19

### Metrics that belong to the current task

Overview, usage, billing, and analysis views expose the information needed for their own decisions.

Procedure:

1. Inventory the actual metrics and decisions on each view. Identify repeated counters that have no role in the current task.

2. Keep the overview summary in its appropriate view. Organize usage, billing, or analysis through the project's existing navigation and supported functions.

3. Show actual consumption with its unit, allowance, period, and meaningful comparison. Use the chart representation appropriate to the data, following U15.

4. Explain real plan differences and supported discounts using U05. Retain complete secondary controls through U16, and avoid changing plan contracts just to match a mockup.

Original Codex prompt:

> Review the role of every displayed metric in this application. Keep useful information in its task context, show actual allowances and periods, and reuse supported navigation and plan definitions.

Source steps: [PDcQJOPby1k · 1:11](https://www.youtube.com/watch?v=PDcQJOPby1k&t=71s), [PDcQJOPby1k · 3:24](https://www.youtube.com/watch?v=PDcQJOPby1k&t=204s), [PDcQJOPby1k · 4:09](https://www.youtube.com/watch?v=PDcQJOPby1k&t=249s), [PDcQJOPby1k · 4:49](https://www.youtube.com/watch?v=PDcQJOPby1k&t=289s).

Result check: Navigate among representative views and explain the main decision on each. Metrics agree with their authoritative records and billing periods, and secondary actions remain reachable.

## U20

### Feature illustrations made from the actual product UI

A landing page explains a feature using a truthful, readable example of the interface that performs it.

Procedure:

1. Choose a feature and the real component state that demonstrates it. Use owned example content suitable for public display.

2. Compose a focused view of those components or an authorized screenshot. Keep the visible values and controls coherent with the feature claim.

3. Use CSS for any presentation tilt, framing, or surrounding caption. Retain readable live page text, and separate a static illustration from a working demo.

4. Connect the accompanying action to the actual feature or relevant explanation. Use P11 when a small interactive demo would explain the behavior better.

Original Codex prompt:

> Create a feature illustration using this product's real components and public-safe example content. Keep the behavior truthful, the caption readable, and the feature action connected to its actual destination.

Source steps: [PDcQJOPby1k · 5:36](https://www.youtube.com/watch?v=PDcQJOPby1k&t=336s), [PDcQJOPby1k · 5:52](https://www.youtube.com/watch?v=PDcQJOPby1k&t=352s), [PDcQJOPby1k · 6:01](https://www.youtube.com/watch?v=PDcQJOPby1k&t=361s).

Result check: Compare the illustration with the corresponding product state, then inspect the landing page on mobile. The feature claim, visible state, and action agree.

## U21

### Personalization from an explicit task goal

A product asks for a small relevant preference and makes its effect on the next step understandable.

Procedure:

1. Identify the supported decision that a preference changes, such as a lesson goal, content category, or available session length.

2. Ask the relevant question with clear choices and a supported skip or later-edit route. Keep factual declarations distinct from optional preferences.

3. Apply the answer to an actual supported recommendation or starting configuration. Explain the relationship so the user can understand and change it.

4. Bring the user to a useful real result promptly, using U02 or P11. Retain preferences through the existing account and storage rules.

Original Codex prompt:

> Use one relevant user preference to improve this task's starting configuration. Explain how it changes the result, allow supported skipping/editing, and bring the user to actual value.

Source steps: [ihWJtNaLYLo · 0:36](https://www.youtube.com/watch?v=ihWJtNaLYLo&t=36s), [ihWJtNaLYLo · 1:23](https://www.youtube.com/watch?v=ihWJtNaLYLo&t=83s), [Primary source](https://www.nngroup.com/articles/mobile-apps-initial-use/).

Result check: Choose different goals, skip an optional question, and change the answer later. The supported recommendation changes appropriately and the task stays completable.

## U22

### Return to useful progress with user-controlled reminders

A repeat-use product makes the next useful task and recorded progress easy to find after an absence.

Procedure:

1. Identify the user's recurring goal and actual completed activity. Choose the next supported task from that record.

2. Show meaningful history or fresh information when it exists, and identify an achievable next step. Derive any streak, challenge, or achievement from real activity and the product's date rules.

3. Offer supported reminder timing and controls that the user can change, pause, or disable. Keep nonurgent prompts compatible with the task and presentation preferences in U18.

4. Make returning after a missed session understandable and preserve prior work. Keep supported export, cancellation, and account-management routes discoverable.

Original Codex prompt:

> Improve the return journey around the user's actual goal and recorded progress. Show a useful next step, preserve work after an absence, and keep supported reminder and account choices easy to control.

Source steps: [ihWJtNaLYLo · 2:14](https://www.youtube.com/watch?v=ihWJtNaLYLo&t=134s), [ihWJtNaLYLo · 2:55](https://www.youtube.com/watch?v=ihWJtNaLYLo&t=175s), [ihWJtNaLYLo · 3:24](https://www.youtube.com/watch?v=ihWJtNaLYLo&t=204s), [Primary source](https://www.nngroup.com/articles/deceptive-patterns/).

Result check: Return after completing, pausing, and missing a session; change a reminder preference. History, next steps, progress counts, and notification state agree with actual records.
