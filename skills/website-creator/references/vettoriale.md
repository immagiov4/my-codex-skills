# Create vector animations

The Lottie recipes come from a direct Codex demonstration. The player, public files, and LottieFiles editor have separate conditions.

## Index

- [V01 · An original Lottie success animation](#v01)

- [V02 · Adapt an animation reference by its phases](#v02)

- [V03 · Navigation with animated SVG or Lottie details](#v03)

- [V04 · Animate an authorized SVG logo](#v04)

- [V05 · Animate an SVG detail](#v05)

- [V06 · Prepare a bitmap mark for vector animation](#v06)

## V01

### An original Lottie success animation

Codex produces editable animation JSON and a local preview.

Procedure:

1. Ask for an original circle, check mark, and fading ring as Lottie JSON with an HTML preview.

2. Play it with lottie-web and inspect every phase; the video's first version omitted the check mark.

3. Connect the animation to actual operation completion and retain a readable static state.

Original Codex prompt:

> Create an original Lottie success animation with a circle, check mark, and fading ring. Save the JSON and a local HTML preview.

lottie-web is MIT; check the license of each third-party animation file.

Source steps: [4nywV37ayjs · 0:15](https://www.youtube.com/watch?v=4nywV37ayjs&t=15s).

Result check: All requested shapes appear, the preview plays correctly, and success follows actual completion.

## V02

### Adapt an animation reference by its phases

An original vector sequence retains the reference's selected rhythm.

Procedure:

1. Describe the shapes, positions, and timing visible in the reference frames.

2. Generate original Lottie JSON and a local preview, changing shape or color while preserving the requested rhythm, such as stars becoming hearts.

3. Compare the initial, intermediate, and final phases and correct the specific difference.

Source steps: [4nywV37ayjs · 1:18](https://www.youtube.com/watch?v=4nywV37ayjs&t=78s).

Result check: The requested phases and rhythm are visible and the resulting shapes are complete.

## V03

### Navigation with animated SVG or Lottie details

The selected section has a moving icon or indicator with readable names.

Procedure:

1. Prepare authorized SVG parts, your own icons, and a reference for the navigation composition.

2. Build HTML/CSS/JavaScript selection and use Lottie for the requested icon motion.

3. Test clicks, keyboard input, and resizing against the actual active section.

Source steps: [4nywV37ayjs · 3:18](https://www.youtube.com/watch?v=4nywV37ayjs&t=198s).

Result check: The active section is identifiable, the indicator follows the real state, and names remain readable.

## V04

### Animate an authorized SVG logo

The project logo enters through animated shapes or strokes.

Procedure:

1. Use the actual SVG and identify the parts that move.

2. Request an original Lottie or SVG/CSS sequence using those layers.

3. Compare the logo, colors, and timing in the preview; use a static version for reduced motion.

Source steps: [4nywV37ayjs · 2:24](https://www.youtube.com/watch?v=4nywV37ayjs&t=144s).

Result check: The logo is complete and recognizable during and after its entrance.

## V05

### Animate an SVG detail

An icon or shape moves while its dimensions and colors remain editable.

Procedure:

1. Request an SVG with identifiable shapes and dimensions defined through `viewBox`.

2. Use CSS or Anime.js for the requested stroke, scale, position, or opacity animation.

3. Test the icon in its actual state and keep the label and action in HTML.

Source steps: [_SVU3oC4JX8 · 8:51](https://www.youtube.com/watch?v=_SVU3oC4JX8&t=531s), [9NubqbSNbjg · 5:39](https://www.youtube.com/watch?v=9NubqbSNbjg&t=339s).

Result check: The detail is crisp at the sizes used and its action remains understandable.

## V06

### Prepare a bitmap mark for vector animation

Turn an authorized bitmap logo or illustration into editable vector geometry before applying V04 or V05. This preparation fills the gap when an SVG source is unavailable; a simple geometric mark may be clearer to redraw directly.

1. Open [SVGConverter's free web app](https://svgconverter.app/free) and load the bitmap. Use original or authorized artwork appropriate for external processing.
2. Inspect the palette, background transparency, edges, smoothing, and curve fitting, then select **Vectorize**. Compare the contour, internal holes, and colors with the source; simplify noise before introducing motion.
3. Select **Download** with SVG output. Inspect the actual file for vector paths and a usable `viewBox`; compare it at the sizes needed in the website. Preserve the mark's geometry while grouping only the parts that must move independently.
4. Continue with V04 or V05 for animation and their keyboard, responsive, and reduced-motion checks. This conversion alone establishes a static asset.

Discovery: [Tony Chen / SetupsAI, Powerful websites you should know, part 1180](https://www.instagram.com/setupsai/reel/DemCV9SP7-w/), observed in authenticated Chrome on 2026-10-18. The caption and rendered video identify the conversion tool; the procedure above is this collection's adaptation, checked against [official documentation](https://svgconverter.app/docs).

Access: the [EULA](https://svgconverter.app/eula) identifies the online application as free and proprietary and the offline application as paid. The [privacy policy](https://svgconverter.app/privacy-policy) describes temporary server processing of uploaded files. Artwork rights remain a separate input requirement.

Observed result, 2026-10-18: an original 128×128 PNG containing a blue circular mark and a white rectangular cutout was converted and downloaded in Chrome. The SVG parsed as XML with `viewBox="0 0 128 128"`, six paths, and 2,024 bytes; its browser preview retained the mark and cutout. This establishes conversion/export for that sample; assess detailed artwork and the final website separately.
