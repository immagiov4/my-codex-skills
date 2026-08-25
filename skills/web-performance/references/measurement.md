# Measure web performance

Use this reference for a live capture or an artifact-based audit.

## Pick the strongest available evidence

Check sources in this order:

1. Existing repository scripts, performance tests, budgets, and build analyzers.
2. User-provided Lighthouse, PageSpeed Insights, CrUX, or performance-trace artifacts.
3. Browser controls that can record network activity, runtime traces, screenshots, or user flows.
4. A local Lighthouse CLI run when Chrome or Chromium and the required package are already available, or when installing the package is authorized.
5. Build output and source inspection when runtime evidence is unavailable.

Do not claim that a tool exists until you have discovered it in the active environment.

## Capture a Lighthouse report

Prefer the repository's command. A typical standalone command is:

```bash
npx lighthouse <url> --output=json --output-path=./lighthouse-report.json --chrome-flags="--headless"
```

Do not download packages silently when the environment restricts network access or installations. Store temporary reports outside the repository unless the user asked to keep an artifact.

Record the commit, URL, build mode, cache state, Lighthouse version, emulation settings, and relevant browser version. A development build is not a production-performance baseline unless the user explicitly wants development-loop performance.

## Capture runtime behavior

Use a representative user flow. Record page load separately from interaction work when both matter.

Inspect:

- the network waterfall, redirects, transfer sizes, compression, caching, and request dependencies;
- main-thread long tasks, scripting, style, layout, paint, and event timing;
- LCP element discovery and loading;
- interaction input delay, processing time, and presentation delay;
- layout-shift sources;
- memory growth only when the symptom suggests a leak or retained work;
- bundle composition and duplicated modules when build output points to JavaScript cost.

CPU and network throttling are models, not physical devices. Keep their settings identical between comparisons and label the result as lab data.

## Interpret Core Web Vitals

Use current authoritative definitions. The published good thresholds are LCP at 2.5 seconds or less, INP at 200 milliseconds or less, and CLS at 0.1 or less. Field classification uses the 75th percentile and separates mobile and desktop traffic.

References:

- [Web Vitals](https://web.dev/articles/vitals)
- [Chrome DevTools Performance panel](https://developer.chrome.com/docs/devtools/performance/overview)
- [Chrome performance insights](https://developer.chrome.com/docs/performance/insights)

Do not apply a Lighthouse score, bundle-size limit, API latency limit, or memory budget as a product gate unless the project or user defines it.

## Compare a change

Keep the command and conditions fixed. Run enough samples to see whether normal variation is larger than the apparent improvement. Compare the distribution and individual runs, not only a rounded mean.

Record each experiment:

```text
Hypothesis:
Baseline and variation:
Change:
Result and variation:
Correctness checks:
Verdict: keep, remove, or inconclusive
```

If several changes must ship together, isolate their measurements first when practical. Otherwise state that attribution is uncertain.

## Report without measurements

If only source or build artifacts are available:

- leave LCP, INP, CLS, and runtime timings as `not measured`;
- label each finding `potential impact`;
- cite the file and mechanism that creates the risk;
- name the exact capture or artifact needed to verify it.
