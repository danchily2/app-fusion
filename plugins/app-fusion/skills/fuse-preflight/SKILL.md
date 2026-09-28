---
name: fuse-preflight
description: Checks that this machine can analyze the source apps and build the new one. It covers toolchains (Xcode, Node, Android, Maestro), Figma access and its rate limits, source completeness, and the protection of the legacy code. It asks the five questions only a person can answer and writes PREFLIGHT.md. Run it after /app-fusion:fuse.
argument-hint: "<program>"
arguments: program
---

Check whether this environment can analyze the apps of program `$program` and build its new app, and say exactly
what to fix before later steps run into it. Run **every** check even when an early one fails: the point is one
complete readiness report. Scripts are in `${CLAUDE_PLUGIN_ROOT}/scripts/`. Run from the workspace root.

Read `analysis/$program/program.json` and `INTENT.md`. Without `program.json`, stop: the fix is
`/app-fusion:fuse $program --source <app>=<path> ...`. Without `INTENT.md`, say that nobody has recorded what they want
yet, run the checks anyway, and name `/app-fusion:fuse $program` as the step to run before `fuse-assess`. Never modify
anything under `legacy/`.

## Check 0: Ask the person (these answers are not in any repository)

Ask **only** these five questions, with the AskUserQuestion tool (questions 1–4 in one call, 5 in a second). Give
each its own options, one of them "Don't know", and let the person type instead. Run the other checks while the
pop-up is open: none of them needs the answers.

1. **Scope.** Is each app complete in its repository, or does part of it live elsewhere? Examples: a shared design
   system package, a common SDK, a web view served by another team, a backend-for-frontend.
2. **Test environment.** Is there a test backend and test accounts for each app, including one person with both
   roles? Who owns them? May the plugin run the apps against them?
3. **The new app's backend.** Will the new app call the same APIs as today, a new gateway, or a mix? Is any API
   changing during the project?
4. **Constraints.** Is there a release date, a minimum OS, store or brand rules, accessibility requirements, or an
   earlier attempt to merge these apps that we should learn from?
5. **Off limits.** Must anything stay untouched? Examples: a module another team owns, a frozen API contract, the
   analytics event names dashboards depend on.

Write each question under **Answers** in `PREFLIGHT.md` with the answer **verbatim**. With no answer (headless run,
or skipped), write an open item a person must fill in. All five always appear.

## Check 1: Stacks

`python3 "${CLAUDE_PLUGIN_ROOT}/scripts/workspace.py" check $program` gives each app's link, cleanliness and commit.
Report each app's stack and platforms from `program.json` and the build files you see:
- the Xcode project and any workspace, Swift packages, and the Podfile
- `package.json`, the React Native version and the lockfile
- Gradle modules and the Android Gradle plugin

## Check 2: Analysis tools

| Tool | Used by | Without it |
| --- | --- | --- |
| `python3` 3.8+ | every script | nothing deterministic runs (fatal) |
| `git` | links, proof | the "legacy untouched" check cannot run |
| `scc` | assess | lines of code fall back to non-blank line counts |
| `jq` | convenience | none |

## Check 3: Toolchains (presence and versions; build only with consent)

Use `command -v` plus the version flag. What each is for:

- **iOS:** `xcodebuild -version`, and `xcrun simctl list devices available` for an iPhone simulator. `swift --version`,
  plus `pod --version` if an app has a Podfile.
  - `xcodebuild -list -project <proj>` lists schemes read-only.
- **React Native:** `node -v` and the app's package manager (yarn, npm or pnpm, from the lockfile). Check whether
  `node_modules` already exists in the legacy app.
  - Never install into `legacy/`: it writes node_modules, Pods and lock files, and the guard asks before it.
- **Android:** `java -version`, `adb version`, `ANDROID_HOME` or `ANDROID_SDK_ROOT`, and the Gradle wrapper.
- **Maestro:** `maestro --version`. It is used for journey tests on both platforms.
- **Target stack** (`program.json` → `target.stack`, if decided): the same checks for the new app's stack, following
  `${CLAUDE_PLUGIN_ROOT}/references/targets/<stack>.md`.

**Optional build smoke test** (ask first; it can take 10+ minutes). Build one legacy iOS app for the simulator into a
scratch folder: `xcodebuild ... -sdk iphonesimulator -derivedDataPath "$(mktemp -d)" build`. It writes only there
and to the shared SPM and Xcode caches. A React Native build needs its dependencies installed, which writes into the
app, so only offer it in a scratch copy (`rsync -a --exclude node_modules --exclude Pods legacy/<app>/ <scratch>/`).
A red build is a finding, not a blocker: the proof then compares the new app with the recorded legacy behavior,
rules and API use, not with a running legacy app.

## Check 4: Source completeness

Look for the equivalents of missing includes:
- `.gitmodules` entries whose folders are empty
- private package registries (`.npmrc` registry lines, Package.resolved or Podfile.lock pins from private hosts)
  that the new app will also need
- generated code referenced but absent: GraphQL codegen output, SwiftGen or R.swift output, OpenAPI clients
- design-system packages (Gaia or similar) and where they come from
- a shallow clone (`git rev-parse --is-shallow-repository`), which means no change history

## Check 5: Figma

Check each part and record what you find:
- **Connection.** Is a Figma MCP server connected? Look for a `get_metadata` or `get_screenshot` tool from any server
  (the claude.ai Figma connector, the Figma desktop server or a remote Figma server).
- **Seat and limits.** Call `whoami`, which is exempt from rate limits, and report the plans and seats. Read limits
  follow the seat:

  | Seat | Figma read calls |
  | --- | --- |
  | Enterprise Dev or Full | 600 a day, 20 a minute |
  | Organization or Professional Dev or Full | 200 a day, 10–15 a minute |
  | View or Collab | 6 a month |

  With a View or Collab seat, say plainly that MCP ingestion is not viable. Recommend a Dev seat, or the REST path.
- **REST path.** Is `FIGMA_TOKEN` set in this shell (`[ -n "$FIGMA_TOKEN" ]`, never print it)? If so,
  `scripts/figma_rest.py` reads the whole file in a few requests.
- **Design files.** For each Figma file in `program.json`, one `get_metadata` without a node id lists its pages.
  Save the response to the path `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/figma_index.py" path $program <fileKey> pages pages`
  prints, run `figma_index.py pages $program <fileKey> <that file> --name "<file name>"`, and record the spend with
  `figma_index.py budget $program --spend 1`. A permission error means the person's Figma account cannot open the
  file: say which account `whoami` reported.

## Check 6: Overlap and boundaries

- Do the apps share code: a common package, a git submodule, the same design-system library? Shared code is a merge
  opportunity. List it.
- Does one repository hold more than one app (a monorepo)? Then the link must point at the right folder.

## Check 7: Is the legacy code protected?

`python3 "${CLAUDE_PLUGIN_ROOT}/scripts/workspace.py" guard $program` reads the permission deny rules (read-only: never
edit a settings file) and prints the snippet to add when the links or their real paths are not covered. Also say
whether the plugin's guard hook is active (the plugin option `guard` is on by default).

Status is ✅ or ⚠️, never ❌. Say plainly what the rules and the hook cover: Claude's file tools and the shell commands
they recognize. They do not cover a script that opens files itself. A read-only mount is the hard guarantee.

## Report

Write `analysis/$program/PREFLIGHT.md`:
1. The **Answers** (verbatim) and the Check 6 findings.
2. One table row per check with ✅, ⚠️ or ❌, what was found, and the fix for anything not green.
3. Readiness per later step:
   - `fuse-assess` and `fuse-map`: Checks 1–2.
   - `fuse-design`: Check 5.
   - `fuse-rules`: Checks 1–2.
   - `fuse-brief`: the discovery files only.
   - `fuse-scaffold` and `fuse-build`: Check 3 for the target stack, a simulator, and Maestro for journeys.
   - `fuse-verify`: the same, plus Check 7.

Print the table in the session too, then refresh the report with
`python3 "${CLAUDE_PLUGIN_ROOT}/scripts/build_report.py" $program`. This is a convenience: if it fails, say so in one
line and carry on. End with the single most important fix if anything is red, and the next step:
`/app-fusion:fuse-assess $program`.
