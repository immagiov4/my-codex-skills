# Images and video with Codex

Availability and pricing verified on 29 September 2026. Start with project images and session tools; photographic video is an optional, quoted step.

For visual editors that create website materials from existing images or interface screens, read [asset editors and showcase recipes](social-design-resources.md#create-website-materials): Animos, Effect.app, Raylight, Gradientool and Ditther, checked on 18 October 2026. Choose them for a defined exported result, with their recorded account, plan and reuse conditions.

## Translate tutorial operations into local tools

These substitutions are implementation proposals. The tutorial provides the sequence and effect; Codex produces local files and verifies them in the project.

| Tutorial step | Codex-centered substitution | Verifiable result |
|---|---|---|
| Open Antigravity, Cursor, or another agent and paste instructions | Use Codex in the actual project with the goal, references, and selected recipe | Local code and a running page |
| Request a hero image from a generator | Use available native Codex image tools; alternatively use your own image or a verified free source | Original file and suitable desktop/mobile crop |
| Buy a page template | Extract the required structure and select free components or original HTML/CSS | A reproducible section with real content |
| Add an entire decorative library | Read and integrate the specific effect defining the result | Necessary dependencies and inspectable code |
| Use a paid Spline scene | Generate Three.js/R3F code for a defined scene or use your own geometry and materials | Local interactive scene or static image |
| Generate an AI video background | First try CSS/SVG/WebGL, Background Studio, or a suitable Pexels video | Comparable appearance and motion without a paid generative request |
| Install an agent collection just to acquire a component | Open that component's documentation, code, and instructions | The useful component code in the project |

Read an official command before applying it. Verified examples: `npx shadcn@latest add @react-bits/BlurText-TS-TW`, `pnpm dlx shadcn@latest add @magicui/globe`, `npx shadcn@latest add @aceternity/3d-card`. Use the project's package manager and variant; inspect added files and dependency resolution. Sources: [React Bits](https://github.com/DavidHDev/react-bits), [Magic UI](https://magicui.design/docs/installation), [Aceternity](https://ui.aceternity.com/components/3d-card-effect).

## Create images and motion at the lowest suitable cost

**Observed in the research environment:** `image_gen.imagegen` was callable for image generation and editing. Recipes can therefore use native generation when available. This establishes session capability; account limits and service costs still apply. An external key is needed when choosing an external service.

For each asset, use the first suitable route that satisfies the requested result:

1. Existing media supplied and authorized for the project.
2. CSS/SVG or a static image for shapes, lighting, and textures.
3. Free licensed photography/video when the required scene exists.
4. Available native Codex image generation for an original composition.
5. Programmed animation or Background Studio for abstract motion.
6. Metered generative video for a specific moving photographic scene.

This order aims to reduce cost and work. For a rotating object, Three.js can also provide the requested interaction; a photographic shot requires a choice based on subject and movement.

## OpenRouter and Higgsfield

### OpenRouter: documented video generation and public catalog

**Verified against official sources.** OpenRouter provides text/image-to-video generation through an asynchronous API. `GET /api/v1/videos/models` lists models, durations, resolutions, aspect ratios, and price entries. `POST /api/v1/videos` creates a job; `GET /api/v1/videos/{jobId}` reads its state; `GET /api/v1/videos/{jobId}/content?index=0` retrieves the output. `generate_audio` can affect cost: explicitly use `generate_audio: false` for the cheap example below. State requests and downloads require `Authorization: Bearer <key>`, including retrieval of returned output URLs. The research queried the public catalog; read actual configurations for prices because documentation examples are illustrative. [Official guide](https://openrouter.ai/docs/guides/overview/multimodal/video-generation), [public catalog](https://openrouter.ai/api/v1/videos/models).

**Verified price example, without a quality comparison:** [Veo 3.1 Lite](https://openrouter.ai/google/veo-3.1-lite) lists 720p at $0.03/s without audio and $0.05/s with audio; 1080p at $0.05/s and $0.08/s respectively. Documented durations are 4, 6, and 8 seconds. Four seconds at 720p without audio therefore cost $0.12 in model usage before applicable fees or taxes. This is a list-price calculation, not a generation-success guarantee.

The [pricing page](https://openrouter.ai/pricing), [official cost comparison](https://openrouter.ai/blog/insights/openrouter-vs-litellm/), and [terms, §4.1](https://openrouter.ai/terms/) state a 5.5% credit-purchase fee, with a $0.80 minimum, and a $5 minimum purchase. The fee applies to a top-up; generation consumes balance at model prices. Distinguish $0.12 usage from the payment required with an empty balance. Compare per-second and per-token prices only through the configuration's actual formula.

### Higgsfield: an API separate from website subscriptions

**Verified against official sources.** Higgsfield has official REST APIs and SDKs using a USD balance and a $5 minimum top-up. Application subscriptions and credits are separate products. Official documentation distinguishes the API from MCP/CLI tools using plan credits. Outputs remain available for at least seven days; purchased balance expires after one year. [API help center](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api).

For a configuration estimate, call `POST https://api.higgsfield.ai/estimate/<model-path>` with generation parameters. The response contains `usd`; use this authenticated estimate before spending. Credentials use `KEY_ID:KEY_SECRET` and remain in the server environment. [Billing and estimates](https://docs.higgsfield.ai/docs/concepts/billing-and-retention), [model example](https://open.higgsfield.ai/models/alibaba/wan-3.0-prime/text-to-video/api-reference).

Some model pages expose only a “from” price. That establishes an advertised floor; the actual configuration requires its price table or estimate endpoint. The public API catalog can differ from the application catalog. [Catalog](https://open.higgsfield.ai/explore), [help center](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api).

### Optional video workflow

Prepare a concrete choice before requesting a purchase:

1. Define subject, movement, framing, duration, resolution, aspect ratio, and audio.
2. Present the recipe's free alternative when it meets the goal.
3. Read current official catalogs; compare the same model and configuration.
4. Calculate cost per attempt, authorized attempt count, and total cap. Use Higgsfield's authenticated estimate or OpenRouter's actual model price entries and applicable charges.
5. Obtain the user's choice, credentials in the appropriate environment, and spending limit. Keep keys out of public code. Carry forward authorization already given for this scope.
6. Prepare one attempt with continuity and movement suited to the section; submit after spending authorization.
7. Inspect the returned file and its page integration; save a static frame for the alternative presentation.

Use muted playback and a poster for decorative video. Specify the recipe's reduced-motion behavior and test it in the browser.

## Verified price comparison

This comparison uses **Wan 3.0 Prime, text-to-video, 1080p, 30 seconds, 16:9, audio enabled**. Both providers document the model and parameters. Totals are public-list calculations rather than quality tests or observed invoices.

| Provider | Public price per second | 30-second calculation | Condition and source |
|---|---:|---:|---|
| OpenRouter | $0.28 | $8.40 | Public 1080p catalog price and [model page](https://openrouter.ai/alibaba/wan-3.0-prime); audio is documented. |
| Higgsfield | $0.196 | $5.88 | 30% discount advertised until 1 October 2026; the [official page](https://open.higgsfield.ai/models/alibaba/wan-3.0-prime/text-to-video/playground) specifies 1080p and 30 seconds; [parameters](https://open.higgsfield.ai/models/alibaba/wan-3.0-prime/text-to-video/api-reference) include `generate_audio`. |
| Higgsfield, advertised post-promotion price | $0.28 | $8.40 | Future price stated on the same page; recheck when using it. |

**Arithmetic inference:** the observed model prices give a Higgsfield saving of $2.52, or 30%, during this promotion. Actual cost also depends on fees, currency, taxes, and attempts. OpenRouter's credit-purchase fee and Higgsfield's minimum top-up can alter the required payment. A different model or configuration requires a new comparison.

## Convert a clip into a local sequence

This original technical procedure is equivalent to conversion shown in the videos. Use your own or authorized clip. With FFmpeg available, choose a short segment, dimensions, and sampling rate appropriate to the section; inspect sample frames for quality and continuity. [Official FFmpeg manual](https://ffmpeg.org/ffmpeg.html).

PowerShell example with explicit parameters to adapt to the project:

```powershell
$videoFile = 'work/product.mp4'
$frameFolder = 'work/frames'
$sampleRate = 24
$frameWidth = 1280
$frameQuality = 80
$startSeconds = 0
$durationSeconds = 4
if (Test-Path -LiteralPath $frameFolder) {
    throw 'Choose a new directory for this extraction.'
}
New-Item -ItemType Directory -Path $frameFolder -ErrorAction Stop | Out-Null
ffmpeg -i $videoFile -ss $startSeconds -t $durationSeconds -vf "fps=$sampleRate,scale=${frameWidth}:-2" -c:v libwebp -quality $frameQuality "$frameFolder/frame-%04d.webp"
if ($LASTEXITCODE -ne 0) {
    throw 'Correct the frame conversion before continuing.'
}
```

These are example settings. Use a fresh directory for each extraction so its list contains only that conversion's frames. For a cheap trial, reduce duration and size; select final quality and frequency by observing the page. Keep filenames ordered and use the actual number of generated files for the final index.

Map normalized section progress to the canvas index: `Math.round(progress * (frameCount - 1))`. Draw only when the index changes. Before fast scrolling, check loading and decoding of the required images; measure memory and asset size for that sequence. Choose resolution from displayed dimensions, device, and observed result.

Test forward/reverse scrolling, final frame, resizing, and entry into the next section. For reduced motion, use the chosen static image. Test ordinary video playback and a scroll-controlled sequence as distinct behaviors.
