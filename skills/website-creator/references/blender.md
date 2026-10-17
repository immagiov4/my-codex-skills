# Create Blender graphics and camera sequences

Use Blender when the requested effect needs editable geometry, a controlled camera, or a compositor graphic. These six recipes adapt public 2026 videos to local Codex work. Keep the scene editable and choose the web delivery format from the required interaction.

## Choose the output

| Requested result | Recipe | Delivery |
|---|---|---|
| Ring-like distortion around a display word or logo | B01 | A composited still or rendered animation |
| Colored variable-size dots forming a letter, image, or logo | B02 | A still or tested motion sequence |
| The exact finished appearance in a page | B03 | Image, video, or numbered frames |
| A controllable camera path before optional photographic generation | B04 | Editable scene, timed shot list, and local preview |
| Product parts separate, pause, and recombine | B05; [S01](scorrimento.md#s01), [S02](scorrimento.md#s02) | Rendered frames or actual mesh animation |
| A sphere-based graphic in a hero with live text | B06; [P02](procedure.md#p02) | Rendered art or deliberately implemented mesh interaction |

A compositor render stores the final appearance in pixels. A `.glb` stores supported geometry, materials, and animation for a browser renderer. Choose a rendered asset when that appearance is the requirement; use actual geometry when the user needs object or camera interaction. The [glTF manual](https://docs.staging.blender.org/manual/en/latest/addons/scene_gltf2.html) identifies supported export arrangements, and [GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html) documents browser loading. Keep unique headings, copy, and actions in HTML.

## Prepare the local workflow with Codex

1. Identify the installed Blender version and the required nodes or geometry features. Use an official [Blender distribution](https://www.blender.org/download/) when installation is needed for the requested asset work.
2. Prepare a project-local Python script for the scene and effect. Keep named parameters for subject, camera, resolution, seed, palette, and the few defining effect controls.
3. Create the scene through Blender's `bpy`, save its `.blend` file, and render a small preview. Confirm framing and the defining effect before producing delivery assets.
4. Render the required output, inspect dimensions/color/alpha and any loop seam, then verify the resulting section in the browser. Record scene creation, successful rendering, and successful browser behavior separately.

The following command shapes apply to a prepared script and the scene it saves. Resolve `blender` to the verified executable and adapt the project paths:

```text
blender --version
blender --background --python-exit-code 1 --python "work/build_asset.py"
blender --background "work/asset.blend" --render-output "//renders/frame_####" --render-format PNG --render-frame 1
blender --background "work/asset.blend" --render-output "//renders/frame_####" --render-format PNG --render-anim
```

Blender executes arguments in order: load the scene, configure output, then render. Python exceptions should return a nonzero exit code. [Command-line rendering](https://docs.staging.blender.org/manual/en/latest/advanced/command_line/render.html), [arguments](https://docs.staging.blender.org/manual/en/latest/advanced/command_line/arguments.html), [render API](https://docs.staging.blender.org/api/current/bpy.ops.render.html)

For Blender 5.x, scripts use a `CompositorNodeTree` assigned to `scene.compositing_node_group`, with `NodeGroupOutput` and a Color output socket. Math uses `ShaderNodeMath`; choose socket identifiers from the actual build. The 5.0 migration changed the older `scene.node_tree` and Composite-output setup. [Compositor migration](https://developer.blender.org/docs/release_notes/5.0/migration/compositor_migration/), [Python API changes](https://developer.blender.org/docs/release_notes/5.0/python_api/)

## Reference settings for the two compositor looks

These are settings shown by Ducky 3D, useful for the first comparison render. Blur and threshold appearance depend on resolution, image intensity, and the chosen output transform. Tune the named controls for the delivered asset.

| Effect | Settings shown | Defining connections |
|---|---|---|
| B01 radial display text | Emission 2; heavier Blur about 100, lighter Blur about 22; Noise detail 0/scale 4; spherical Rings Wave scale about 10; Bloom strength about 30. | Noise → Color Ramp controls mixing between blur branches. Wave scalar is the Less Than Value; mixed subject intensity is Threshold. Bloom/inversion and an accent ramp finish the mask. |
| B02 halftone glyph | 1800×1800 render; emission 5; Blur about 185; regular Voronoi scale 40/randomness 0. | Voronoi Distance is the Less Than Value; remapped blurred intensity is Threshold. Noise can vary the remapped size bounds. The resulting mask mixes the background and an intensity-driven palette. |

Higher dot thresholds expand the region around feature points; Voronoi scale changes the pattern frequency. Keep dot-size and palette mapping independent. Inspect the smallest useful dots at the actual desktop/mobile size to identify disappearing detail or moiré. The source uses Helvetica for one example; choose a font with suitable permissions from the project's own resources.

| Version or node detail | Practical implication | Official reference |
|---|---|---|
| Procedural compositor textures, Blender 4.5 onward | Verify Noise, Wave, and Voronoi in the selected build. | [4.5 compositor notes](https://developer.blender.org/docs/release_notes/4.5/compositor/) |
| Film Grain, Blender 5.2 | It is a compositor asset. Use the available asset and its interface rather than assuming a standalone `CompositorNodeFilmGrain` class. | [5.2 compositor notes](https://developer.blender.org/docs/release_notes/5.2/compositor/) |
| Scalar threshold and remapping | Less Than returns a binary comparison; input order and remapping bounds determine the mask. | [Math](https://docs.staging.blender.org/manual/en/latest/compositing/types/utilities/math/math.html), [Map Range](https://docs.staging.blender.org/manual/en/latest/compositing/types/utilities/math/map_range.html) |
| Procedural coordinates | Center and scale coordinates deliberately when changing aspect ratio or texture dimensions. | [Image Coordinates](https://docs.staging.blender.org/manual/en/latest/compositing/types/input/image_coordinates.html), [Wave](https://docs.staging.blender.org/manual/en/latest/compositing/types/texture/wave.html), [Voronoi](https://docs.staging.blender.org/manual/en/latest/compositing/types/texture/voronoi.html) |
| Bloom and alpha | Glare/Bloom changes image-space appearance; choose an explicit matte when transparency is needed. | [Glare](https://docs.staging.blender.org/manual/en/latest/compositing/types/filter/glare.html), [Set Alpha](https://docs.staging.blender.org/manual/en/latest/compositing/types/color/set_alpha.html) |
| Web color | Record the output transform and declare color versus data textures correctly in the browser. Compare the delivered asset with the render. | [Blender color spaces](https://docs.staging.blender.org/manual/en/latest/render/color_management/color_spaces.html), [Three.js color management](https://threejs.org/manual/pages/color-management.html) |

## Adapt the source tools and costs

The Ducky workflows use local text, nodes, and rendering; the promoted course is separate from the public procedure. B04–B05 adapt Higgsfield's demonstrated agent/plugin workflow to Codex-generated `bpy` scenes and editable shot lists. The tutorial presents its plugin as free. A local Blender preview and optional generated video have separate costs and capabilities. Use the [media workflow](immagini-video.md) to verify supported reference inputs, model, duration, aspect ratio, price, and spending authorization before a metered step. Measure credit savings from actual comparable attempts when evaluating that claim.

The sphere short records Blender 4.4.3 with hair particles, alongside Figma and a final presentation workflow whose description names After Effects. B06's current geometry route is an explicit collection adaptation: [Distribute Points on Faces](https://docs.staging.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) and [Instance on Points](https://docs.blender.org/manual/en/5.2/modeling/geometry_nodes/instances/instance_on_points.html) distribute an owned strand or curl on the shell. BlenderKit assets require their individual access and license check; use an owned core object for a self-contained free route. [BlenderKit creator terms](https://www.blenderkit.com/terms-and-conditions-for-creators-2026/)

For animated web assets, honor reduced motion and provide the required pause/stop controls. Use a useful text alternative when the graphic carries unique information, and an empty alternative for a decorative duplicate. [Decorative images](https://www.w3.org/WAI/tutorials/images/decorative/), [reduced motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion), [Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)

## Index

- [B01 · Radially distorted display text in the compositor](#b01)

- [B02 · Voronoi halftone letters or image graphics](#b02)

- [B03 · Deliver the Blender result as a still, loop, sequence, or mesh](#b03)

- [B04 · Lock a camera path before optional generated video](#b04)

- [B05 · Editable product disassembly and camera beats](#b05)

- [B06 · A sphere-based graphic in a live website hero](#b06)

## B01

### Radially distorted display text in the compositor

A rendered display word or logo gains ring-like distortion, an accent ramp, and optional grain.

Procedure:

1. Prepare owned text or a logo, a licensed display font, a camera, and an emissive subject on a dark world. Render the source for compositing.

2. Create two Blur branches. Mix their images with a Noise Texture passed through a Color Ramp so distortion varies across the subject.

3. Feed a spherical Rings Wave Texture into the Value of a Less Than Math operation and the mixed subject image into its Threshold. Inspect the resulting subject mask.

4. Use Glare/Bloom, inversion, and a Color Ramp to shape the chosen accents. Add the available Film Grain compositor asset when it contributes to the result.

5. Save the editable scene and render an appropriate web image or loop through B03. Adjust the named effect parameters at the intended output resolution.

Original Codex prompt:

> Build an editable Blender compositor scene for owned display text with two blur branches, noise-controlled mixing, spherical wave threshold distortion, and a chosen accent ramp. Render a web-sized preview and tune the effect at that size.

Source steps: [72xChVM08jI · 0:57](https://www.youtube.com/watch?v=72xChVM08jI&t=57s), [72xChVM08jI · 2:28](https://www.youtube.com/watch?v=72xChVM08jI&t=148s), [72xChVM08jI · 3:19](https://www.youtube.com/watch?v=72xChVM08jI&t=199s), [72xChVM08jI · 4:52](https://www.youtube.com/watch?v=72xChVM08jI&t=292s), [72xChVM08jI · 6:19](https://www.youtube.com/watch?v=72xChVM08jI&t=379s), [Primary source](https://developer.blender.org/docs/release_notes/5.2/compositor/).

Result check: Compare the unprocessed subject and final render at the intended web size. Its defining shape remains recognizable, accents fit the page, and grain survives compression without obscuring it.

## B02

### Voronoi halftone letters or image graphics

A large letter, logo, or image becomes a colored grid of variable-sized dots.

Procedure:

1. Render a thin display letter or authorized image and blur its intensity. Keep detailed reading text in HTML outside this decorative treatment.

2. Set a Voronoi Texture to a regular distribution and pass Distance into the Value of a Less Than Math operation.

3. Remap the blurred subject through Map Range and connect it to Threshold. Adjust the minimum and maximum to control the dot sizes.

4. Use an additional remapped Noise Texture in the size range for spatial variation where desired. Mix a background color and an intensity-driven Color Ramp using the dot mask.

5. Inspect optional Film Grain and animation of a supported texture coordinate. Save the editable scene and deliver a still or loop through B03.

Original Codex prompt:

> Create an editable halftone graphic from this owned subject using blurred intensity, regular Voronoi distance, a remapped threshold, and a chosen color ramp. Tune dot size at the intended web resolution and keep important page text live.

Source steps: [72xChVM08jI · 6:47](https://www.youtube.com/watch?v=72xChVM08jI&t=407s), [72xChVM08jI · 8:58](https://www.youtube.com/watch?v=72xChVM08jI&t=538s), [72xChVM08jI · 10:16](https://www.youtube.com/watch?v=72xChVM08jI&t=616s), [72xChVM08jI · 12:34](https://www.youtube.com/watch?v=72xChVM08jI&t=754s), [72xChVM08jI · 14:35](https://www.youtube.com/watch?v=72xChVM08jI&t=875s).

Result check: Render at the actual page size, then check dot visibility, subject recognition, crop, and optional loop continuity. The smallest useful dots remain visible after delivery encoding.

## B03

### Deliver the Blender result as a still, loop, sequence, or mesh

The website receives an asset format that preserves the required appearance or supports the required interaction.

Procedure:

1. Identify whether the requested result is a composited appearance, a fixed animation, a scroll sequence, or a mesh the user must manipulate.

2. For composited appearance, render an image or image sequence at the intended aspect ratio. Choose an opaque page-compatible background or a tested alpha workflow.

3. For a loop, review motion and encode the rendered sequence with an appropriate poster and playback controls. For scroll scrubbing, use the established sequence recipe S01 and its direction/resizing checks.

4. For actual object interaction, export the required geometry and supported materials as glTF/GLB, then implement the camera and controls in the existing browser renderer. Recreate required compositor-only effects separately or use baked image assets.

5. Use Codex to prepare version-correct bpy files and render commands, preserving the editable .blend source. Verify the result in the actual browser section and its reduced-motion presentation.

Original Codex prompt:

> Choose the delivery format for this Blender result from its actual interaction requirement. Preserve the composited appearance in renders, use GLB for true object manipulation, and verify the asset in the browser with editable source retained.

Source steps: [72xChVM08jI · 14:35](https://www.youtube.com/watch?v=72xChVM08jI&t=875s), [Primary source](https://docs.blender.org/manual/en/latest/advanced/command_line/render.html), [Primary source](https://docs.blender.org/manual/en/latest/addons/scene_gltf2.html), [Primary source](https://developer.blender.org/docs/release_notes/5.0/migration/compositor_migration/).

Result check: Open the delivered section on desktop and mobile and perform its intended interaction. Still/loop/sequence appearance matches the render; mesh controls manipulate actual geometry with usable page content.

## B04

### Lock a camera path before optional generated video

A local editable scene establishes framing, timing, and motion before evaluating a video-generation service.

Procedure:

1. Describe the desired shot as a timed list: subject positions, camera position or path, lens changes, look-at target, and the visible event at each important time.

2. Ask Codex to build the scene with simple geometry and keyframes through bpy. Keep camera path and target separately editable.

3. Render or inspect a low-cost local preview and correct framing, timing, and transitions in the scene. Save the accepted structure and its shot list.

4. Use the Blender render as the final asset when it meets the brief. For optional generation, select a provider/model that actually accepts the required reference-video or image inputs, with the intended duration and aspect ratio.

5. Prepare the reference, timed prompt, parameters, and spending cap through the existing media workflow. Compare the resulting shot with the local preview and revise a specific difference.

Original Codex prompt:

> Prepare this shot locally in Blender with simple geometry, a timed camera path, and a separate target. Review the preview before any metered generation and prepare an input-compatible model route with a spending cap only if needed.

Free route: local Blender geometry, scripting, and previews. The tutorial promotes a free plugin; generated video is a separate service. Provider credit-saving claims are author demonstrations, so assess savings from actual comparable attempts.

Source steps: [OiULPvTJ-0E · 1:28](https://www.youtube.com/watch?v=OiULPvTJ-0E&t=88s), [OiULPvTJ-0E · 3:19](https://www.youtube.com/watch?v=OiULPvTJ-0E&t=199s), [OiULPvTJ-0E · 10:51](https://www.youtube.com/watch?v=OiULPvTJ-0E&t=651s), [OiULPvTJ-0E · 18:20](https://www.youtube.com/watch?v=OiULPvTJ-0E&t=1100s).

Result check: Review important times in the local preview and optional final clip: subject continuity, camera target, event timing, and framing agree with the shot list. Record actual attempts and cost if measuring savings.

## B05

### Editable product disassembly and camera beats

A product sequence has editable parts, separation distances, camera moves, and moments for its captions.

Procedure:

1. Represent the product and its separable parts with owned geometry or a licensed model. Use simple placeholders while deciding the sequence.

2. Name each visible event in a timed shot list: intact view, separation, detail, recombination, and final action as the brief requires.

3. Keyframe object transforms and the camera separately. Tune acceleration, pauses, and transitions against the intended composition and caption timing.

4. Render a local preview and revise an individual part, beat, or framing without rebuilding the whole sequence. Prepare captions and purchase controls as separate HTML.

5. Deliver using B03 and the relevant scroll recipe. For optional photographic restyling, use B04 and the authorized media workflow while retaining the editable source.

Original Codex prompt:

> Create an editable local product sequence with separately named parts and timed camera beats. Preserve the scene for targeted revisions, keep captions in HTML, and verify the delivered section in both scroll directions.

Source steps: [OiULPvTJ-0E · 13:33](https://www.youtube.com/watch?v=OiULPvTJ-0E&t=813s), [OiULPvTJ-0E · 13:59](https://www.youtube.com/watch?v=OiULPvTJ-0E&t=839s), [OiULPvTJ-0E · 14:59](https://www.youtube.com/watch?v=OiULPvTJ-0E&t=899s), [OiULPvTJ-0E · 16:01](https://www.youtube.com/watch?v=OiULPvTJ-0E&t=961s).

Result check: Inspect intact, separated, and final states, then scroll forward/backward in the web section. Part identity, framing, caption readability, and the next page section remain coherent.

## B06

### A sphere-based graphic in a live website hero

An original rendered spherical object supplies the main image while headings, benefits, and the action remain editable page elements.

Procedure:

1. Build the HTML grid, live heading, short description, benefits, and main action around the requested content. Reserve a deliberate space for the graphic.

2. Create an owned UV-sphere-based subject in Blender. The reference cuts a sphere in half, shifts its origin, adds thickness, and duplicates/rotates the shell.

3. Choose the supported geometry treatment for the target Blender version. The recording uses 4.4.3 hair particles. The current Geometry Nodes adaptation distributes points on the hemisphere and instances an owned curled strand, aligned to the surface normals, with explicit density, seed, and scale.

4. Place an owned or individually licensed core object inside the shells. Compose its materials, lighting/glow, camera, and page-compatible background, then render through B03.

5. Integrate the asset with live HTML. Use native CSS/SVG or the existing browser renderer for the required web motion, keeping a static/reduced-motion presentation.

Original Codex prompt:

> Build an original sphere-based hero graphic in Blender and integrate it into this page with live HTML text. Use supported geometry and owned assets, choose the delivery format explicitly, and verify crop, readable content, and reduced motion.

The short demonstrates Figma, Blender, and After Effects, and offers files through a comment request. This adaptation uses local HTML/CSS, owned geometry, and native web motion; any external asset needs its individual access and license checked.

Source steps: [q1QQN08ZK6I · 0:04](https://www.youtube.com/watch?v=q1QQN08ZK6I&t=4s), [q1QQN08ZK6I · 0:15](https://www.youtube.com/watch?v=q1QQN08ZK6I&t=15s), [q1QQN08ZK6I · 0:27](https://www.youtube.com/watch?v=q1QQN08ZK6I&t=27s), [q1QQN08ZK6I · 0:44](https://www.youtube.com/watch?v=q1QQN08ZK6I&t=44s), [q1QQN08ZK6I · 0:54](https://www.youtube.com/watch?v=q1QQN08ZK6I&t=54s), [Primary source](https://docs.staging.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html), [Primary source](https://docs.blender.org/manual/en/5.2/modeling/geometry_nodes/instances/instance_on_points.html).

Result check: Check the original object's framing in the hero on desktop and mobile. Text and the action remain live, the graphic respects the crop, and motion follows the chosen still/loop/mesh delivery route.
