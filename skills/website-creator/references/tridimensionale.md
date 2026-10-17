# Build 3D scenes

A tilted photograph, a photographic sequence, and a WebGL model provide different interactions. Each recipe identifies the variant that supports the requested behavior.

## Index

- [T01 · A spherical photo portfolio that becomes a grid](#t01)

- [T02 · Optional hand gestures for the portfolio](#t02)

- [T03 · A mountain journey with route and data](#t03)

- [T04 · A tilting product and an entered showroom](#t04)

- [T05 · A globe beside actual service coverage](#t05)

- [T06 · One persistent 3D scene across page transitions](#t06)

- [T07 · A character carousel with layered depth](#t07)

## T01

### A spherical photo portfolio that becomes a grid

Photos occupy a navigable sphere and transition into a stable project grid.

Procedure:

1. Prepare authorized portraits with consistent crops and a limited set of reused images.

2. Place cards on a Three.js sphere with stable project identities.

3. Define matching sphere and grid positions and interpolate between them.

4. Add pointer or drag navigation; keep menus and project links in HTML and provide a direct grid for reduced motion.

Source steps: [VHrpHmZ3AhE · 10:58](https://www.youtube.com/watch?v=VHrpHmZ3AhE&t=658s).

Result check: Rotation, project opening, grid transition, and return preserve the correspondence between photos and projects.

## T02

### Optional hand gestures for the portfolio

Requested camera gestures control the sphere alongside pointer and touch input.

Procedure:

1. Complete and test T01 with pointer and touch controls first.

2. Add MediaPipe Hands mappings only when hand interaction is requested; expose an explicit camera-enable control.

3. Handle permission grant and rejection, retain ordinary controls, and release the camera and tracking resources when stopped.

Source steps: [VHrpHmZ3AhE · 16:08](https://www.youtube.com/watch?v=VHrpHmZ3AhE&t=968s).

Result check: Granting, refusing, and stopping camera access all leave the portfolio usable.

## T03

### A mountain journey with route and data

A landscape in chapters follows a route with readable data panels.

Procedure:

1. Establish the static landscape's horizon, scale, depth, and chapter content.

2. Choose the actual rendering: your own terrain and camera path for real 3D, or a photographic sequence. Label the selected variant.

3. Synchronize camera position, the route line, and narrative panels with the same phases. Use real data when the route represents a real place.

4. Add lighting changes and clouds after the journey is readable.

Source steps: [1A20nUPbkOc · 10:12](https://www.youtube.com/watch?v=1A20nUPbkOc&t=612s).

Result check: The camera follows the whole route in both directions, panels remain readable, and the page provides a static version.

## T04

### A tilting product and an entered showroom

A product opening leads into alternate product views with a clear return action.

Procedure:

1. Build the product opening from an authorized image using P02; layers provide a 2.5D tilt and a static mobile version.

2. Implement an explicit entry transition and showroom views.

3. Add product selection and reset or return controls.

4. Use a real 3D model when the user needs genuine object rotation; test that separately from tilting an image plane.

Source steps: [3t3TogERIdw · 8:01](https://www.youtube.com/watch?v=3t3TogERIdw&t=481s), [3t3TogERIdw · 10:12](https://www.youtube.com/watch?v=3t3TogERIdw&t=612s).

Result check: The entry action is keyboard-reachable; views, product switching, and return work on mobile, with the intended kind of rotation.

## T05

### A globe beside actual service coverage

A decorative globe accompanies readable coverage or language information.

Procedure:

1. Choose the free Magic UI Globe component and inspect its code and license.

2. Place it beside an HTML list of the service's actual regions or languages.

3. Scope styles and test performance; use an SVG or static illustration when continuous motion is unnecessary.

Source steps: [9NubqbSNbjg · 8:10](https://www.youtube.com/watch?v=9NubqbSNbjg&t=490s).

Result check: Coverage remains readable independently of the globe and the page interactions stay responsive.

## T06

### One persistent 3D scene across page transitions

Navigation changes the camera and HTML content within a shared scene.

Procedure:

1. Create one persistent Three.js canvas with your own geometry and materials.

2. Define the camera for each page and use existing navigation, adding Barba only where needed. Synchronize camera and content transitions with GSAP.

3. Clean up transition resources and test back and forward navigation. Local HTML and your own materials replace the tutorial's Webflow/Photoshop steps.

Original local adaptation: HTML and your own materials replace the author's Webflow and Photoshop steps.

Source steps: [Primary source](https://tympanus.net/codrops/2026/03/18/building-seamless-3d-transitions-with-webflow-gsap-and-three-js/).

Result check: The object stays coherent during navigation, links remain accessible, and repeated transitions retain one active scene.

## T07

### A character carousel with layered depth

The selected character stands centrally with neighboring figures and oversized type.

Procedure:

1. Create a coherent series of original images with the same camera and style, using transparent backgrounds. Edit references to retain character identity.

2. Place the selected subject in front of a large word and neighboring subjects at the sides using 2D layers.

3. Make arrows, keyboard, and touch update the same selection index; preload neighbors and apply a spring transition.

Source steps: [Primary source](https://limora.ai/learn/pixar-character-page/).

Result check: All controls update selection while preserving proportions and identity; motion uses 2D layers unless a real model is requested.
