# Implement a visual reference faithfully

Read this when the user supplies a selected mockup, asks to refine a site through Image Gen, or expects the implementation to reproduce a reference. The selected image governs the visual details; the project's verified content governs factual claims and working behavior.

## Establish the target

1. Inventory the actual pages and meaningful states. Capture each page, its full continuation, and relevant narrow layouts. For long pages, a labeled contact sheet can show the first viewport prominently and subsequent sections in reading order. Preserve the captures used as generation inputs.
2. If the user requests image-led refinement, pass those captures to native Image Gen. Ask it to preserve the conceptual identity and improve the actual interface, including its continuation and mobile composition. Save the prompt and output. With an already selected mockup, use that exact image as the target.
3. Identify the website frame boundaries within the image. Separate depicted desktop and mobile viewports from presentation margins and board labels. Record their widths and scale section measurements relative to those widths; exported image pixels are not automatically browser CSS pixels.

Completion: each real page or relevant state has a target, its depicted viewport is identifiable, and the input/output images are available for comparison.

## Inspect every section

Examine sections separately at a readable scale. Record a compact implementation table alongside the project's existing delivery notes:

| Section | Observed reference details | Implementation | Remaining difference and reason |
|---|---|---|---|

Account for each section's height and width, outer margins, spacing between elements, column ratios, image dimensions and crop, text alignment, type size/weight/line height, heading line breaks, and content density. Observe the extent, weight, color, and placement of borders and separators. Measure the placement and scale of decorative elements and the amount of surrounding empty space.

When refining an existing site, compare the original and proposed sections directly. Identify what the proposal removed, added, shortened, widened, regrouped, or moved. Explain the visible effect on hierarchy, density, or composition using observed evidence. Treat improvements in small details as implementation requirements, alongside structural changes.

Completion: every section has concrete observed properties and an implementation decision. Broad descriptions such as "more polished" are supported by the specific changes that produce them.

## Translate the details into code

Implement the measured composition in the existing HTML/components and CSS. Reuse the visual system where its properties match the target; adjust its actual sizes, spacing, crops, and rules where they differ. Match the complete section, including its quiet areas and supporting elements.

Use verified copy, prices, contact details, logos, and authentic photographs. A generated reference can suggest composition while containing invented facts or documentary-looking imagery. Resolve those elements against the real project. Generate individual raster assets when the target needs them, inspect them in their consuming section, and keep their provenance in the delivery notes. Preserve usable controls, keyboard access, readable text, and relevant states.

Completion: each observed visual decision has been implemented or has a concrete reason for deviation, such as factual content, an unavailable authentic asset, or an interaction/accessibility requirement.

## Compare the rendered result

Capture the actual implementation at the intended desktop and mobile widths and the matching interaction state. Compare each section with its target, normalizing the frame scale. Inspect geometry, typography, whitespace, crops, line density, and decoration at a readable size. Use full-page captures to review rhythm, and section captures to review detail.

Fix unjustified differences, capture again, and update the section table. Check the full visitor action after layout changes.

The implementing agent owns the complete visual loop: capture the running site, inspect its captures beside the target, measure differences, correct the code, and capture again. When the work is delegated, that responsibility stays with the implementing agent; its delivery includes the final captures and observed comparison.

After the visual changes, run the installed Impeccable detector through `scripts/check-design.mjs`, supplying every final markup and linked stylesheet path explicitly, following [the detector review](design-direction.md#review-the-built-page). Verify findings against the rendered page and record their disposition. Repeat the scan after corrections.

Inspect small text separately: section kickers, captions, badges, helper lines, and repeated supporting labels. For each, identify the information or action it helps; remove redundant scaffolding and enlarge useful text that is difficult to read. A generated target can contain these patterns too. Reconcile its details with the user's clarity requirements and explain deliberate retained choices.

Completion: every section has a rendered comparison; corrected differences have a fresh capture; remaining differences have specific reasons; small text has a useful role; the final detector findings have a disposition; and the real controls work at the tested widths. Report resemblance and residual differences honestly. A source scan or general aesthetic approval does not establish fidelity to the selected reference.
