---
name: luanti-playbox
description: >
  Run and verify Luanti (Minetest) Lua code in sandboxed Docker servers using
  the playbox CLI. Use when a task needs pure-Lua evaluation, live engine API
  calls (core.*), or load-time mod testing against real Luanti servers.
---

# Playbox: sandboxed Luanti environments for agents

Playbox runs Luanti (formerly Minetest) inside Docker so you can execute Lua
without touching anyone's local installation. All state lives under playbox's
host data dir; worlds and store content are fully separated from any personal
Luanti setup.

Every command prints failures as:

    error: <what failed> (<detail>) -> <exact next command>

Follow the suggested command instead of falling back to ad-hoc shell probing.
Exit codes: `0` pass, `1` test failure or runtime error, `2` usage/infra
problems.

## First-run setup

Run once per machine before live-engine or full-suite usage:

```sh
playbox doctor        # checks Docker, resolves/pulls the engine image
```

Pure Lua needs only Docker. `doctor` reads `min_minetest_version` from a root
`mod.conf` when present; pin otherwise with `playbox doctor --engine-version X.Y.Z`.

## Choose the lightest mode that suffices

| Mode | Command | Use for | Needs |
|------|---------|---------|-------|
| pure Lua | `playbox lua` | pure logic, algorithms, string/table/bit ops | Docker only |
| live engine | `playbox exec` | live engine API (`core.*`) on a warm server | a started world |
| full suite | `playbox run` | structured load-time test suites of one or more mods via mtt | store game + mtt |

If the code does not reference `core.*` or a world's state, use pure Lua.
If you are declaring repeatable, named mtt test cases (timeouts, async
callbacks, many cases at once), use the full suite.
Otherwise use the live engine.

## Pure Lua: `playbox lua`

Evaluates pure Lua in a pinned LuaJIT 2.1 container (same interpreter Luanti
embeds; Lua 5.1 dialect with the `bit` library). No engine context: `core.*`
does not exist here.

```sh
playbox lua -e "print(('abc'):upper())"
playbox lua my_script.lua
```

Exit code mirrors the snippet: `0` success, non-zero on Lua error.

## Live engine: `playbox exec`

Sends a Lua snippet to the Bridge mod inside a running server; the snippet
executes without restarting anything. Warm executions take about 2 seconds.

```sh
playbox exec --auto -e "return core.get_node({x=0,y=1,z=0}).name"
playbox exec my-world -e "return #core.registered_nodes"
playbox exec my-world check.lua
```

Rules:

- Prefer `--auto`: it reuses an idle ephemeral pool world (starting it if
  needed, creating one named like `pb-t1-3` if none exists) and never touches
  your named persistent worlds.
- Results print as JSON. Multiple return values are preserved; functions,
  userdata and threads come back as `<function>`-style reprs.
- Default response timeout is 30 s (`--timeout SECONDS` to change).
- A snippet error prints its message and traceback and exits 1.
- Worlds shut themselves down after ~15 minutes without requests
  (idle shutdown keeps world data); just re-run `playbox exec` afterwards.
  A snippet that blocks for minutes is a wrong fit for this mode anyway;
  move long asynchronous work into mtt cases and run them as a full suite.

## Full suite: `playbox run`

Structured load-time testing for many test cases at once: creates a fresh
throwaway world (`pb-t2-N`, singlenode, creative, no damage), injects your
mods plus the mtt runner and resolved hard dependencies, runs the server to
completion, parses `[mtt]` markers, then removes the world unless told not
to. The Bridge is absent from these worlds, so no idle shutdown can kill a
long suite; mtt owns termination.

```sh
playbox run ./my-mod                       # local folder: current code is copied in
playbox run author/name                    # installed store ref
playbox run ./my-mod --keep                # keep the world for log inspection
playbox run ./my-mod --report results.json # structured JSON results artifact
```

- Tests self-activate when your mod is listed in `mtt_filter` (handled
  automatically) and define `mtt.register(..)` tests. Progress streams to
  the console as tests execute; `--verbose` shows the full server log.
- Missing hard dependencies are reported with the exact `playbox install`
  command to fix each one.
- Exit codes: `0` all registered tests ran and passed, `1` test failure,
  crash, or no tests executed, `2` infra problem (Docker down, missing deps).

### Real players: `--clients N`

When a suite needs connected players, join real headless clients. They have
genuine ObjectRefs (`type(player) == "userdata"`), real positions, movement
and physics, HUD, network and engine C++ paths.

```sh
playbox run ./my-mod --clients 1   # joins real headless client 'client1'
```

Clients join as `client1`..`clientN` by default. Many suites hardcode the
name `player1`; add `--client-prefix player` so slot N joins as `playerN`
and the suite runs unmodified:

```sh
playbox run _local/mymod --clients 1 --client-prefix player
```

Real clients are containers under Xvfb connecting through a published UDP
port; playbox holds test execution at a gate until all N have joined, and
aborts early (with the client's last log lines) when a client container
dies while connecting.

Playbox resolves the client image for the run's engine version on its own;
do not build or pick one unless you are testing an engine-side hypothesis
(e.g. you patched the engine's C++ and built a debug image to bisect a
suspected upstream bug). `--engine-version` is also rarely needed: the run
resolves the newest stable engine at or above every mod's
`min_minetest_version`, so a floor of 5.10 still picks 5.17 when that image
is already local. Pin a version only when the task targets a specific
engine version.

Clients stay warm between runs; a different `--engine-version` is refused
until stale clients are removed.

Other run flags worth knowing: `--report FILE` writes per-test JSON
results; `--conf KEY=VALUE` writes settings into the test world's config
(e.g. `--conf enable_damage=true` for suites whose tests kill the player).

## Install content first

Mods and games come from the shared store, deduplicated across worlds:

```sh
playbox install author/name          # ContentDB ref (hard deps auto-installed)
playbox install author/name@1.2.0    # pinned release
playbox install https://git../repo.git   # git URL
playbox install https://../pkg.zip       # zip URL
playbox install ./path/to/mod             # local folder
playbox mods list
playbox games list
```

Git/zip/local installs are filed under the `_local` author bucket. The default
game is `devtest`; it must be in the store before creating worlds or using
`--auto` (`playbox install Luanti/devtest` if `playbox games list` lacks it).

A store ref runs the *installed copy*; a local folder argument runs its
*current code*. After editing a mod, either keep passing the folder or
re-run `playbox install <folder>` to refresh the store copy — installing
the same content twice just updates it.

## World hygiene

Check what exists before creating anything:

```sh
playbox worlds list
playbox worlds info <name>
```

- Ephemeral worlds (created by `--auto`, names starting `pb-t1-`/`pb-t2-`)
  are pool-managed: `playbox worlds prune` removes stopped ones unused for
  over 24 h (`--stale-hours HOURS` to adjust), always keeping the most
  recently used one.
- Persistent worlds are never touched by prune. Create them deliberately:
  `playbox worlds create [--game NAME] <name>`.
- If you created or started a *named* world, stop it when done:
  `playbox worlds stop <name>` (data is kept). Remove it explicitly with
  `playbox worlds prune <name>`.
- Do not create new worlds when an existing stopped one fits; start it with
  `playbox worlds start <name>` instead.

## Error recovery pattern

When a command fails, the line after `error:` tells you exactly what to do.
Run that command. Typical loops:

- `world 'x' does not exist` -> `playbox worlds list`, create or use `--auto`.
- `mod 'a/b' is not installed in the store` -> `playbox install a/b`.
- `missing hard dependencies` -> run the printed `playbox install` commands.
- `no response from the bridge within Ns` -> `playbox worlds info <name>`;
  if the world stopped, re-running `playbox exec` restarts it.
- `Docker daemon is not running` -> start Docker Desktop, then re-run.

Only fall back to generic probing after the suggested commands also fail.

## Raw docker access as documented fallback

When playbox does not expose something (log inspection, resource stats), go
through the Docker CLI directly; containers follow fixed names:

```sh
docker logs --tail 100 pb-world-<world-name>
docker ps -a            # leftover containers are named pb-world-<name>
docker inspect pb-world-<world-name>
```

World data lives under the host data dir (`%LOCALAPPDATA%\playbox\worlds\<name>`
on Windows, `$XDG_DATA_HOME/playbox/worlds/<name>` elsewhere; override with
`PLAYBOX_HOME`). Treat those directories as read-only unless playbox itself
manages them.

## devtest quick-reference

The default game ships registries worth knowing about before hand-building
fixtures in Lua:

- **testnodes** (`testnodes:*`): hundreds of nodes covering drawtypes,
  param2 variants, liquids, light, fall damage, and bouncy, climbable,
  slippery, or pointable behavior. Use these when a snippet needs specific
  node properties instead of hand-building nodes.
- **testtools**: tools in group `testtool = 1` (`param2tool`, `node_setter`,
  `remover`, `rotator`, `object_mover`, `entity_scaler`, `branding_iron`,
  `entity_spawner`, `object_editor`). Filter items by `group:testtool`.
- **chest_of_everything**: node + bag tool listing every registered item;
  prefer it over long `/giveme` sequences.
- **callbacks** mod: nodes/items in group `callback_test = 1` log every
  callback invocation. Useful for verifying hook behavior.
- Determinism knobs (world minetest.conf or settings): creative mode +
  `devtest_infplace = auto`; `devtest_v6_mapgen_aliases`,
  `devtest_register_biomes` for flat predictable terrain. Broken or
  intentionally-invalid defs carry group `dummy = 1`; exclude it when
  sweeping item registries.

## Bridge execution semantics

Snippets sent by `playbox exec` are compiled in the global environment with
full `core.*` access, wrapped in a function, and run under `xpcall`:

- Return values survive: `return 1, nil, 3` reports all three.
- Serialization uses `core.write_json`; unserializable values fall back to
  reprs. Errors return `{message, traceback}` and exit code 1.
- Requests queue as files in the world's `bridge/requests` dir; responses land
  in `bridge/responses`. One snippet at a time per poll cycle.
