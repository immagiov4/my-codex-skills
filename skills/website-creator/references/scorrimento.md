# Build scroll-driven pages

Photographic sequences and interactive scenes have different requirements. Choose the rendering and prepare a static section before its sequence.

## Index

- [S01 · A product that comes apart as the page scrolls](#s01)

- [S02 · Separate drink or ice-cream ingredients](#s02)

- [S03 · A photographic window expands during scrolling](#s03)

- [S04 · Horizontal panels driven by vertical scrolling](#s04)

- [S05 · Staggered entrances for text and images](#s05)

- [S06 · A scroll-based editorial dossier](#s06)

- [S07 · Add scroll inertia when the result requires it](#s07)

- [S08 · Three photographic chapters for a jet or premium object](#s08)

- [S09 · Reveal images through SVG masks or tiles](#s09)

## S01

### A product that comes apart as the page scrolls

A product transitions from an intact view to separated parts with readable captions.

Procedure:

1. Prepare intact and exploded images with matching camera, light, and position, as in the shoe or microphone examples.

2. For the photographic route, optionally generate a quoted video and convert it into ordered frames. The free original variant uses authorized SVG or image parts with CSS translate/scale; its rendering differs from photographic video.

3. Pin a canvas section and map normalized progress to `Math.round(progress * (frameCount - 1))`, bounded to the actual frame count. Draw only when the frame index changes.

4. Place HTML captions at the relevant phases and provide a static poster for reduced motion. End the pinned interval before the next section.

Original Codex prompt:

> Build a scroll-controlled product opening with three readable phases: intact, opened, and details. Keep captions and buttons in HTML.

The free route animates your own layers or model. Photographic video is optional and requires a model, parameters, and authorized spending limit.

Source steps: [4Ktew-_lkk8 · 2:06](https://www.youtube.com/watch?v=4Ktew-_lkk8&t=126s).

Result check: Initial, middle, and final states work in both scroll directions; resizing and entry into the next section preserve the composition.

## S02

### Separate drink or ice-cream ingredients

A centered product transitions into its ingredients during scrolling.

Procedure:

1. Prepare consistent images of the intact glass or ice cream and separated ingredients.

2. Apply S01 for a photographic sequence, or animate your own layers with CSS/GSAP for the free route.

3. Align captions with the ingredient phases and finish the sequence before the menu, order, or booking section.

Source steps: [VBvxHIkvjeo · 0:23](https://www.youtube.com/watch?v=VBvxHIkvjeo&t=23s), [UR09nuSxGio · 7:30](https://www.youtube.com/watch?v=UR09nuSxGio&t=450s).

Result check: The product remains centered, ingredients have readable labels, and the following action is reachable.

## S03

### A photographic window expands during scrolling

A café-style image or muted video grows within the opening section.

Procedure:

1. Choose an authorized clip or photograph whose subject remains visible in a mobile crop.

2. Use a pinned container and animate its bounds or mask as the section advances.

3. Provide a poster and relevant controls, then connect the expanded window to the following section.

Source steps: [1Y8OlBgafdE · 1:44](https://www.youtube.com/watch?v=1Y8OlBgafdE&t=104s).

Result check: The crop stays useful at desktop and mobile widths, playback is muted, and the transition to the next section works.

## S04

### Horizontal panels driven by vertical scrolling

A sequence of cards moves horizontally while the page advances vertically.

Procedure:

1. Measure the actual content width and viewport width.

2. Use GSAP pin and scrub over the distance `contentWidth - viewportWidth`.

3. For animations inside the panels, use `containerAnimation` with linear container motion.

4. Use a vertical layout or native horizontal scrolling on mobile; test the last panel and exit from the section.

Source steps: [1Y8OlBgafdE · 1:50](https://www.youtube.com/watch?v=1Y8OlBgafdE&t=110s).

Result check: All cards remain reachable, the final card aligns correctly, and the next section follows without trapping navigation.

## S05

### Staggered entrances for text and images

A heading, copy, and imagery enter in a deliberate sequence.

Procedure:

1. Define the reading order with real content and stable layout.

2. Use GSAP, Anime.js, or the selected React Bits effect for contained motion.

3. Keep content immediately visible with reduced motion; clean up animations through the component lifecycle in React.

Source steps: [i48q0JQQ2EA · 105:16](https://www.youtube.com/watch?v=i48q0JQQ2EA&t=6316s), [9NubqbSNbjg · 5:39](https://www.youtube.com/watch?v=9NubqbSNbjg&t=339s).

Result check: The sequence supports reading, preserves wrapping, and creates one active animation per element.

## S06

### A scroll-based editorial dossier

A report presents a readable sequence of evidence and images.

Procedure:

1. Prepare real data, authorized assets, sources, and an ordered set of sections.

2. Build the linear reading version before synchronizing motion with the visitor journey.

3. Use the author's public Scrollcraft workflow as a reference for local corrections to a specific phase or speed; compare the relevant states.

This entry uses public author material and the description rather than a transcript. Prefer your existing assets before optional external resources.

Source steps: [QUI6Ug4cHnE · 0:00](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=0s).

Result check: The report is readable as a linear page and each animated phase corresponds to the intended evidence.

## S07

### Add scroll inertia when the result requires it

Scrolling has the intended inertia while retaining anchors and keyboard navigation.

Procedure:

1. Test native scrolling first and identify the requested behavior that needs Lenis.

2. Integrate Lenis with the existing GSAP clock according to official instructions.

3. Test anchors, inner scroll containers, keyboard use, and the complete section with one animation clock.

Source steps: [i48q0JQQ2EA · 120:18](https://www.youtube.com/watch?v=i48q0JQQ2EA&t=7218s).

Result check: The requested inertia is observed and native navigation remains usable.

## S08

### Three photographic chapters for a jet or premium object

Exterior, details, and interior form three scroll chapters with information points.

Procedure:

1. Prepare three coherent image pairs for the chapters.

2. Build static chapters, text, and hotspots before choosing optional paid clips.

3. For the video route, convert each short clip locally and assign its sequence to the corresponding scroll interval; place captions by phase.

The free route uses three images with CSS transitions; optional photographic motion follows the quoted video workflow.

Source steps: [AuQ6Gs9MGo8 · 1:42](https://www.youtube.com/watch?v=AuQ6Gs9MGo8&t=102s), [AuQ6Gs9MGo8 · 11:11](https://www.youtube.com/watch?v=AuQ6Gs9MGo8&t=671s).

Result check: All three chapters are readable, hotspots match their subjects, and the user can continue past the sequence.

## S09

### Reveal images through SVG masks or tiles

Curtains or tiles expose an image in a scroll-controlled transition.

Procedure:

1. Size the image and masks in relative coordinates for the section.

2. Animate masks with ScrollTrigger; overlap adjoining edges enough to prevent visible gaps.

3. Rebuild the geometry on resize, test reverse scrolling, and provide the completed static composition for reduced motion.

Source steps: [Primary source](https://tympanus.net/codrops/2026/03/11/svg-mask-transitions-on-scroll-with-gsap-and-scrolltrigger/).

Result check: The reveal has no gaps, reverses correctly, and retains the crop after resizing.
