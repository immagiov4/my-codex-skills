# Decodo research access

Use Decodo first for public social discovery and extraction, then follow the authenticated Chrome research scope in [Maintain the collection](maintenance.md#discover) when returned content is insufficient. Read [the official CLI documentation](https://github.com/Decodo/cli) and inspect target-specific help before choosing parameters. The maintained [official SDK target catalog](https://github.com/Decodo/sdk-python#social-media) also lists `instagram_graphql_profile`; actual target and plan support must be tested.

## Credentials and local execution

On Windows, store the Web Data API key or legacy Basic authentication token as a SecureString exported with `Export-Clixml` at `$CODEX_HOME/private/decodo-token.clixml`. Capture it through a masked local input, outside chat and source control. Windows encrypts this value for the same user and machine; a task running under another identity needs its own credential provision. Keep this file outside the collection. On other hosts, supply `DECODO_AUTH_TOKEN` to the official CLI through the host's secret mechanism.

Install the official CLI into the Codex tools directory, using a reviewed version. The initial integration uses `@decodo/cli@3.0.0`:

```powershell
npm install --prefix "$env:CODEX_HOME/tools/decodo" @decodo/cli@3.0.0 --no-audit --no-fund
```

Run [the Windows wrapper](../scripts/decodo.ps1) from PowerShell; it decrypts the token into the CLI child environment, preserves the CLI exit status, and restores the previous environment value:

```powershell
& ./scripts/decodo.ps1 -CliArgs @('youtube-search', '--help')
& ./scripts/decodo.ps1 -CliArgs @('youtube-search', 'website animation design', '--full', '-o', 'work/youtube-search.json')
```

These paths assume the current directory is the skill folder. Save research responses in the task's private scratch directory rather than the public skill. Keep credentials out of command arguments and diagnostic output.

## Prove each research path

After credentials are configured, execute a real YouTube discovery query, inspect returned videos, and retrieve relevant metadata or subtitles for a selected candidate. Inspect `targets` and target-specific help for public social extraction, then inspect the actual returned content. The installed CLI 3.0.0 lists TikTok and YouTube targets but does not expose `instagram-graphql-profile`; its bundled official TypeScript SDK 2.7.0 does include `instagram_graphql_profile`. The wrapper's request-file mode uses that official SDK and the CLI's credential-type detection:

```powershell
# profile-request.json contains: {"target":"instagram_graphql_profile","query":"setupsai"}
& ./scripts/decodo.ps1 -RequestFile ./work/profile-request.json -OutputFile ./work/profile-response.json
```

Search indexed public social posts through Decodo search when direct extraction is unavailable. A modern API key enables Web Data search/map/crawl; legacy Basic tokens have a narrower command set, including the traditional Google search target.

Record command, target, observation date, result count or meaningful fields, and any error without credentials. Treat HTTP success, returned login pages, empty results, metadata, transcript text, and observed motion as separate evidence. Publish a new recipe only with the evidence required by the maintenance procedure.

The latest Basic-token probes, on 2026-10-19, returned 20 `youtube-search` results each for website animation tools and Adrien AI Designer, using `--upload-date this_week`. The latter contained the already cataloged `pKO8BFKWET4` as its only matching channel ID; search results establish bounded discovery. Metadata and timed English subtitles for `NZjjmf3I6I4` were usable. Use accepted upload-date values such as `this_week`: the earlier value `month` was rejected.

The Instagram SDK request for `jamux.ai` returned the matching public profile with zero timeline edges; the previous SetupsAI probe had the same limitation. The TikTok target for `beasttechx` returned the matching public identity and a video count in `__UNIVERSAL_DATA_FOR_REHYDRATION__`, with no video entries. These establish profile extraction; post discovery remains pending. Chrome was absent from available browser connections on 2026-10-19, so authenticated visual inspection was unavailable. Public editors remained accessible in the internal browser, where Gradientool PNG and HTML downloads were exercised. See source-coverage.json for the current checkpoint.

The same session's `google-search` and `bing-search` requests for indexed SetupsAI Instagram posts both failed with Decodo's target-scraping error. Treat indexed-social discovery through those targets as blocked until a later successful content-bearing request; use accessible public web search and the proven YouTube discovery path in the meantime.

Authenticated Chrome subsequently exposed SetupsAI's public post grid and reel `DemCV9SP7-w`, whose part 1180 demonstrates SVGConverter. On 2026-10-18, the refresh followed that visual discovery to the official application, converted an original test PNG, and inspected the downloaded SVG. This proves the interactive browser route and the conversion described in [V06](vettoriale.md#v06); each scheduled run still checks its own browser access.

The maintainer authorizes ordinary use of the existing Decodo subscription for this weekly research. Follow the provider's errors and account limits; avoid bulk historical crawling and stop on authentication or quota failures. Report a blocked source accurately and continue useful research through accessible public sources.
