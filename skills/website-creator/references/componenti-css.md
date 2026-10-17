# Choose components and CSS effects

Libraries provide details to adapt. Read the official sources in the resource references for individual component code and licenses.

## Index

- [C01 · Glass surfaces over a real background](#c01)

- [C02 · An animated background confined to one section](#c02)

- [C03 · Animated heading with intact semantics](#c03)

- [C04 · A perspective card with depth layers](#c04)

- [C05 · A luminous border with a conic gradient](#c05)

- [C06 · A spotlight that follows the pointer](#c06)

- [C07 · A seamless strip of logos or testimonials](#c07)

- [C08 · A footer with contained motion](#c08)

- [C09 · An organic shape or image mask](#c09)

- [C10 · Grain, halftone, or ASCII from your own image](#c10)

- [C11 · Team cards with readable identities](#c11)

- [C12 · Adopt one effect from a component catalog](#c12)

- [C13 · A gradient confined to the opening section](#c13)

- [C14 · A radial shadow beneath a product](#c14)

- [C15 · A divider fading to transparency](#c15)

- [C16 · An oversized brand watermark](#c16)

- [C17 · Text traveling along a curve](#c17)

## C01

### Glass surfaces over a real background

Cards have translucent depth while text remains readable.

Procedure:

1. Choose the Kokonut UI example or an original CSS surface and check the specific variant's license.

2. Apply translucency, a border, and background blur against the actual page background; use the project's spacing.

3. Test bright and dark regions and adjust surface opacity to retain text and control contrast.

Source steps: [9NubqbSNbjg · 0:34](https://www.youtube.com/watch?v=9NubqbSNbjg&t=34s).

Result check: The glass effect is visible and content remains legible over the backgrounds used.

## C02

### An animated background confined to one section

A controlled abstract background supports the section's content.

Procedure:

1. Select a free React Bits or OriginKit effect and the variant matching the project.

2. Configure color, speed, and scale; keep text and actions above the decorative layer.

3. Suspend offscreen work and provide a static version for reduced motion. Compare the complete section in the browser.

Source steps: [9NubqbSNbjg · 1:55](https://www.youtube.com/watch?v=9NubqbSNbjg&t=115s), [8GfWKFyAaW4 · 2:18](https://www.youtube.com/watch?v=8GfWKFyAaW4&t=138s).

Result check: The background stays within its section, supports readability, and leaves interactions responsive.

## C03

### Animated heading with intact semantics

Words appear, blur, or react without losing the complete heading.

Procedure:

1. Choose React Bits Blur Text, Split Text, or the effect that matches the reference.

2. Keep a semantic heading containing the complete text and animate its visual presentation.

3. Test real wrapping on desktop and mobile; show the readable heading immediately with reduced motion.

Source steps: [_SVU3oC4JX8 · 7:49](https://www.youtube.com/watch?v=_SVU3oC4JX8&t=469s), [9NubqbSNbjg · 1:55](https://www.youtube.com/watch?v=9NubqbSNbjg&t=115s).

Result check: The heading is readable, wraps correctly, and remains complete for assistive technology.

## C04

### A perspective card with depth layers

A card tilts under the pointer while internal elements occupy different depths.

Procedure:

1. Build the card with perspective and separate `translateZ` layers, using the Aceternity example or original CSS.

2. Calculate rotation relative to the pointer within the card and reset it when the pointer leaves.

3. Keep actions in HTML and use a static composition on coarse-pointer devices; compare the intended depth in the browser.

Source steps: [WmSiyyisF_4 · 0:12](https://www.youtube.com/watch?v=WmSiyyisF_4&t=12s).

Result check: Depth, pointer movement, and reset work while buttons remain usable on desktop and mobile.

## C05

### A luminous border with a conic gradient

A decorative gradient travels around the card border.

Procedure:

1. Place a repeating conic gradient on a decorative layer and cover its center with the card surface.

2. Animate a registered CSS angle or rotate the layer; define local duration, border width, and colors.

3. Test corners and clickable content; retain a static border for reduced motion.

Source steps: [mwDvTHTAmo8 · 0:10](https://www.youtube.com/watch?v=mwDvTHTAmo8&t=10s).

Result check: The border follows the shape without exposing the center or obstructing controls.

## C06

### A spotlight that follows the pointer

A card highlights the area beneath the pointer.

Procedure:

1. Inspect the selected Magic Card, ObsidianUI, or Fancy Components example and its license.

2. Update the local gradient center only when needed and scope the effect to the card.

3. Provide equivalent keyboard focus and test pointer entry, movement, and exit with real content.

Source steps: [8GfWKFyAaW4 · 1:16](https://www.youtube.com/watch?v=8GfWKFyAaW4&t=76s), [Jhx7n9uAKHg · 7:03](https://www.youtube.com/watch?v=Jhx7n9uAKHg&t=423s).

Result check: The spotlight remains local and keyboard users can identify the active control.

## C07

### A seamless strip of logos or testimonials

Repeated visual content moves continuously while the semantic content appears once.

Procedure:

1. Use authorized content and the Magic UI or DesignCourse structure as a reference.

2. Duplicate the visual strip for continuity while exposing one semantic list.

3. Provide a lasting pause control and a static arrangement for reduced motion; check the join at actual widths.

Source steps: [i48q0JQQ2EA · 0:00](https://www.youtube.com/watch?v=i48q0JQQ2EA&t=0s), [9NubqbSNbjg · 8:10](https://www.youtube.com/watch?v=9NubqbSNbjg&t=490s).

Result check: The strip loops without a jump, can be paused, and retains readable content.

## C08

### A footer with contained motion

Footer decoration or layout transitions accompany stable information and links.

Procedure:

1. Build the footer with the actual contact details and links.

2. Apply the selected Motion effect to its decorative or layout layer.

3. Keep links and information stable and provide the final static state for reduced motion.

Source steps: [9NubqbSNbjg · 6:48](https://www.youtube.com/watch?v=9NubqbSNbjg&t=408s).

Result check: The footer's motion is observed and all information and links remain usable.

## C09

### An organic shape or image mask

A custom shape defines the section's image or decorative surface.

Procedure:

1. Create the shape with Shape Magic or an original SVG.

2. Export SVG or CSS `clip-path` and size it relative to the image container.

3. Test mobile cropping and keep text separate from cut edges.

Source steps: [1Y8OlBgafdE · 17:28](https://www.youtube.com/watch?v=1Y8OlBgafdE&t=1048s), [_SVU3oC4JX8 · 8:51](https://www.youtube.com/watch?v=_SVU3oC4JX8&t=531s).

Result check: The intended shape survives resizing and does not crop essential image content or text.

## C10

### Grain, halftone, or ASCII from your own image

A texture adds a specific material or graphic quality to a section.

Procedure:

1. Apply Texture Lab to your own image, or create an original SVG/CSS texture.

2. Compare definition, contrast, and asset weight at the section's display size.

3. Use a static export when interaction adds no requested function; test the mobile result.

Source steps: [_SVU3oC4JX8 · 7:49](https://www.youtube.com/watch?v=_SVU3oC4JX8&t=469s).

Result check: The texture produces the selected appearance while preserving readability and acceptable asset size.

## C11

### Team cards with readable identities

Portraits and a selected card effect present actual team members.

Procedure:

1. Prepare real portraits, roles, and links with permission to use them.

2. Select the relevant Componentry effect and check the component's license and dependencies.

3. Keep names and roles visible on touch devices and with reduced motion; test each member link.

Source steps: [8GfWKFyAaW4 · 9:28](https://www.youtube.com/watch?v=8GfWKFyAaW4&t=568s).

Result check: Every person is identifiable and reachable in all supported interaction modes.

## C12

### Adopt one effect from a component catalog

A chosen interaction is integrated into the project's visual system.

Procedure:

1. Preview the requested Skiper, Bencho, or Fancy Components effect.

2. Read its source, dependencies, and license before integrating that component.

3. Apply the anchor screen's values and retain the source URL; test the effect with the actual content.

Source steps: [Jhx7n9uAKHg · 0:36](https://www.youtube.com/watch?v=Jhx7n9uAKHg&t=36s), [8GfWKFyAaW4 · 7:37](https://www.youtube.com/watch?v=8GfWKFyAaW4&t=457s).

Result check: The selected interaction works in context and its access and license conditions are recorded.

## C13

### A gradient confined to the opening section

The hero gradient retains its extent as the document grows.

Procedure:

1. Choose the gradient colors from the project's visual system.

2. Apply the background to the opening section and tie its dimensions to that section.

3. Add the remaining content and verify that the gradient's position and proportions remain stable.

Source steps: [PASsk7lxTrc · 38:31](https://www.youtube.com/watch?v=PASsk7lxTrc&t=2311s).

Result check: Document growth preserves the opening background; this is an original CSS translation of the Figma detail.

## C14

### A radial shadow beneath a product

The product appears supported by a soft shadow on its background.

Procedure:

1. Separate the object and shadow into two container layers.

2. Use an elliptical radial gradient with color and transparency consistent with the background.

3. Adjust size, position, and intensity while viewing the image at the website's actual widths.

Source steps: [PASsk7lxTrc · 40:50](https://www.youtube.com/watch?v=PASsk7lxTrc&t=2450s).

Result check: The shadow supports the subject and the crop stays complete; this translates the Figma detail into CSS.

## C15

### A divider fading to transparency

Light lines separate columns and fade at their ends.

Procedure:

1. Place a decorative linear gradient from transparent to divider color to transparent at the column edge.

2. Derive its color from the visual system's divider value.

3. When columns stack on mobile, adapt the divider orientation to the actual layout.

Source steps: [PASsk7lxTrc · 79:25](https://www.youtube.com/watch?v=PASsk7lxTrc&t=4765s).

Result check: Separation agrees with the grid and text retains the required contrast.

## C16

### An oversized brand watermark

A large word or symbol becomes part of the section background.

Procedure:

1. Use an authorized brand SVG or separate decorative text.

2. Set contrast and cropping relative to the section, keeping the main content in front.

3. Test headings, buttons, and text selection over it. Hide purely decorative content from assistive technology.

Source steps: [PASsk7lxTrc · 83:57](https://www.youtube.com/watch?v=PASsk7lxTrc&t=5037s).

Result check: The watermark completes the composition while content remains readable and interactive.

## C17

### Text traveling along a curve

A phrase follows an SVG curve with oriented letters.

Procedure:

1. Define the SVG path and a short original phrase.

2. Use SplitText and MotionPath according to the GSAP guide; provide readable text for reduced motion.

3. Derive spacing and size from the section and rebuild on resize, restoring the previous text first.

Source steps: [Primary source](https://dmmotionarts.com/motion-text-curved-elementor-and-gsap-tutorial/).

Result check: Letters follow the path without overlap and resizing retains one active animation.
