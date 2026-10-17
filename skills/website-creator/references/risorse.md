# Resources and licenses

Official-source verification: 29 September 2026. Choose the individual component for the requested result and recheck the license of the version used.

## Choose a resource by its effect

This table is the collection's implementation proposal. Component and tool names were checked in official catalogs; the mapping to a result is a design judgment.

| Desired result | Resource to consult | Minimum Codex procedure | Official source |
|---|---|---|---|
| Heading that appears word by word, blurs, or reacts to the pointer | React Bits: Blur Text, Split Text, Text Pressure, Variable Proximity, Scroll Reveal | Open the component page, choose the project-compatible variant, read dependencies and code, and integrate a real heading. Retain a readable reduced-motion version. | [React Bits index](https://www.reactbits.dev/get-started/index) |
| Abstract background, distortions, grids, particles | React Bits and Background Studio | Try the effect in one section; choose interactive code or an image/video export. Use an image when interaction is unnecessary. | [React Bits tools](https://www.reactbits.dev/tools), [official repository](https://github.com/DavidHDev/react-bits) |
| Organic shapes with rounded cutouts | Shape Magic | Draw a shape, export SVG or `clip-path`, and apply the website's colors and dimensions. | [React Bits tools](https://www.reactbits.dev/tools) |
| Grain, halftone, dithering, ASCII | Texture Lab | Apply the effect to your own image, export, and compare readability, asset size, and mobile rendering. | [React Bits tools](https://www.reactbits.dev/tools) |
| Pointer-lit cards, luminous borders, light grids | Magic UI: Magic Card, Border Beam, Shine Border, Grid Pattern | Add the selected component and align its colors with the project. Start with CSS for static cards. | [Magic UI catalog](https://magicui.design/docs/components) |
| Moving logos, counters, card grids | Magic UI: Marquee, Number Ticker, Bento Grid | Reuse the component structure with real content and the website's spacing system. | [Magic UI catalog](https://magicui.design/docs/components) |
| Perspective card with depth layers | Aceternity 3D Card Effect | Integrate `CardContainer`, `CardBody`, and `CardItem`; make the interaction optional on devices without a pointer. | [3D Card Effect](https://ui.aceternity.com/components/3d-card-effect) |
| A wall of projects moving with scrolling | Aceternity Hero Parallax | Replace demonstration images and links with real projects. Test the complete section and transition to the next one. | [Hero Parallax](https://ui.aceternity.com/components/hero-parallax) |
| Pinned sections, sequences, masks, synchronized text | GSAP and ScrollTrigger | Create a scroll-controlled sequence with `scrub` and, where needed, `pin`; manage React lifecycle through `useGSAP`. | [ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/), [GSAP with React](https://gsap.com/resources/React/) |
| Entrance, exit, drag, or layout animation | Motion | Use existing project APIs; choose React or JavaScript documentation as appropriate. Apply `useReducedMotion` to respect device preferences. | [Motion](https://motion.dev/), [useReducedMotion](https://motion.dev/docs/react-use-reduced-motion) |
| Scroll inertia required by the selected result | Lenis | Integrate one scroll controller following official configuration; test anchors, keyboard input, and inner containers. | [Lenis](https://lenis.dev/), [official repository](https://github.com/propagande-studio/lenis) |
| Interactive 3D object | Three.js, or React Three Fiber in React | Create or load an object with controlled material and lighting. Keep text and controls in HTML and check React/R3F compatibility. | [Three.js](https://threejs.org/), [R3F](https://r3f.docs.pmnd.rs/) |
| Visually authored 3D scene | Spline | Use the free editor and watermarked web export for a trial. For a free unwatermarked result, recreate the scene with Three.js or use your own image. | [Spline pricing](https://spline.design/pricing), [web exports](https://docs.spline.design/exporting-your-scene/web/exporting-as-public-ur-ls) |
| Forms, dialogs, menus, application structure | shadcn/ui | Add needed components and edit their code. Layer selected decorative effects over that foundation. | [Official shadcn/ui](https://ui.shadcn.com/docs/official), [repository](https://github.com/shadcn-ui/ui) |
| Coherent typography and icons | Google Fonts, Material Symbols, Lucide | Select the families and weights actually used; prefer individual SVGs or selective icon imports. Retain licenses. | [Google Fonts](https://github.com/google/fonts), [Material Symbols](https://developers.google.com/fonts/docs/material_symbols), [Lucide](https://lucide.dev/) |

## Licenses and free portions

These descriptions were checked against official sources. Save the license for each component's actual version: catalogs can change.

| Resource | Free portion | Condition to retain | Free alternative to paid portions |
|---|---|---|---|
| React Bits | Free catalog components and creative tools; JavaScript/TypeScript variants with CSS or Tailwind | The official repository uses **MIT + Commons Clause**. Commercial use in websites and products is allowed; selling, sublicensing, or redistributing the components themselves, including collections and ports, is restricted. Retain license notices. [License](https://github.com/DavidHDev/react-bits/blob/main/LICENSE.md) | Choose the free catalog or implement an equivalent effect from your own requirements with CSS, SVG, Motion, or GSAP. [Pro has a separate license](https://pro.reactbits.dev/license). |
| Magic UI | Public repository components | MIT: retain copyright and license notices. [License](https://github.com/magicuidesign/magicui/blob/main/LICENSE.md) | Compose a page from free components; use full Pro templates when requested. [Installation and Pro distinction](https://magicui.design/docs/installation) |
| Aceternity UI | Components and sections labeled free | The official Aceternity license covers available purchases/downloads, permitting modified end products for yourself or clients while restricting source redistribution and sales of derived templates. Individual files may specify a separate license. [License](https://ui.aceternity.com/licence), [agent catalog](https://ui.aceternity.com/ai-recommendations) | Use individual free components or an original CSS/Magic UI/shadcn structure. A free Pro preview permits viewing; its code requires the corresponding license. |
| shadcn/ui | Component code and official CLI | MIT. External collections have independent licenses. [Repository](https://github.com/shadcn-ui/ui/blob/main/README.md?plain=1), [official resources](https://ui.shadcn.com/docs/official) | Use official blocks and components for structure, adding selected free effects or CSS. |
| GSAP | Library and plugins, including formerly paid plugins | Webflow license permits websites and applications. A product offering visual animation creation in competition with Webflow has a specific restriction. [Free-access announcement](https://webflow.com/updates/gsap-becomes-free), [license, section 9](https://webflow.com/legal/product-terms) | GSAP is free for ordinary website building; for a competing visual tool, assess Motion or native APIs and the applicable license. |
| Motion | Core React, JavaScript, and Vue library | MIT. Motion+ sells additional APIs, examples, and lessons. [Library](https://motion.dev/), [Motion+ distinction](https://motion.dev/pricing) | Build the animation with core APIs or CSS. |
| Lenis | Scrolling library | MIT. [Official repository](https://github.com/propagande-studio/lenis) | Native browser scrolling covers websites without custom inertia. |
| Three.js and React Three Fiber | Both libraries | MIT for both. Check 3D models, materials, and images separately. [Three.js](https://github.com/mrdoob/three.js/blob/dev/LICENSE), [R3F](https://github.com/pmndrs/react-three-fiber/blob/master/LICENSE) | Your own objects and procedural geometry; a static image when interactive rotation is unnecessary. |
| Spline | $0 Free plan, limited personal files, library access, watermarked web exports | Watermark removal for 3D exports starts with Hobby; video export starts with Pro. The pricing page places code/self-hosted exports in Enterprise. [Pricing](https://spline.design/pricing) | Three.js/R3F, your own Blender objects, SVG, or your own images. Check account access before promising a specific export. |
| Google Fonts | Fonts distributed in the repository | Read the individual family's license: many use SIL OFL 1.1, others Apache 2 or Ubuntu UFL. Distribution and self-hosting follow those licenses; modified versions may have reserved-name conditions. [Official repository](https://github.com/google/fonts#license) | System fonts when a custom family is unnecessary. |
| Material Symbols | Variable font and SVG/PNG icons | Apache 2.0. [Guide](https://developers.google.com/fonts/docs/material_symbols) | Individual SVGs or Lucide. |
| Lucide | Icons and packages | ISC; some Feather-derived icons also carry the MIT notice stated on the page. [License](https://lucide.dev/license) | Your own SVGs or Material Symbols. |
| Framer | Templates marked free, copied into your account; free plan | Check creator and content licenses. Free uses a Framer domain; a custom domain requires a paid plan. Framer documents the absence of standalone HTML export. [Templates](https://www.framer.com/help/articles/how-templates-work/), [pricing](https://www.framer.com/pricing), [export](https://www.framer.com/help/articles/can-i-export-my-website-to-html-and-self-host-it/) | Study the composition and build original local code with Codex, using images and other content you are entitled to use. |
| Webflow | Sites marked cloneable in Made in Webflow | Clone into your Webflow workspace; each entry identifies author and copyright. HTML/CSS/JS export requires a paid Workspace plan and has limitations for CMS, forms, and other features. [Cloning](https://help.webflow.com/hc/en-us/articles/33961311242515-Clone-a-site-in-Webflow), [export](https://help.webflow.com/hc/en-us/articles/33961386739347-How-do-I-export-my-Webflow-site-code) | Study layout and interactions in the preview, then create an original local page with Codex. |

### Visual references and reusable content

Pinterest helps find compositions, colors, and photography. Found images retain their authors' rights: trace the source and study the reference, or obtain permission to incorporate it. [Pinterest's copyright guidance](https://help.pinterest.com/en/article/copyright) explains this distinction.

[Awwwards collections](https://www.awwwards.com/collections/) organize examples by element and interaction. Choose a concrete opening, menu, transition, typography treatment, or footer; record URL, author, property to reproduce, and original adaptation, then inspect the linked website. An aesthetic award supports selection; the resulting project's functionality requires its own test.

[Pexels](https://www.pexels.com/license/) provides free photos and videos with modification and website use under its license. [Unsplash](https://unsplash.com/license) provides free images with commercial use and restrictions on image resale and competing services. Both can replace generative media when an appropriate scene already exists. Retain asset URL, author, and consulted license; distinguish free content from paid offerings such as Unsplash+.

## Integration checks

These checks follow the libraries' documented behavior and the problems each recipe must avoid.

- **React and GSAP:** use component-scoped `useGSAP`. The guide documents animation and ScrollTrigger cleanup on unmount. Use `contextSafe` for event-created animations and remove your event listeners. [React guide](https://gsap.com/resources/React/).
- **R3F:** match its major version to React; documentation specifies R3F 8 with React 18 and R3F 9 with React 19. The caller disposes a supplied renderer instance; R3F manages the renderer it creates. [Introduction](https://r3f.docs.pmnd.rs/), [Canvas](https://r3f.docs.pmnd.rs/api/canvas).
- **Reduced motion:** `useReducedMotion` reads the device preference so the page can select a static or quieter variant. [Motion](https://motion.dev/docs/react-use-reduced-motion).
- **Icons:** Material Symbols documents name and axis selection to load the required subset; Lucide supports selective imports. [Material Symbols guide](https://developers.google.com/fonts/docs/material_symbols), [Lucide](https://lucide.dev/).
- **Scrolling:** pinned sequences must leave content reachable on mobile and by keyboard. Test anchors, the final card, and entry into the next section. This is the collection's acceptance condition.
- **Performance:** observe the effect in the browser before adoption. Check whether backgrounds, pointer effects, or 3D impede interaction or scrolling. Suspend offscreen decorative work and use one controller for each animation. Measure this design choice in the implemented page.

## CSS details to verify

- C05 uses a registered angular property with `@property`, animated within a conic gradient. Read [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property) and test the project's required browsers.
- CSS scroll animations can use `animation-timeline`. MDN lists limited availability: establish the required browsers and verify the result. Declare it after the `animation` shorthand, which resets its value. [Documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline).
- Keep application inputs and actions in project components; assign the selected visual effect to the decorative layer.
