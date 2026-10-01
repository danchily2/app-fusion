# Changelog

A release gets a new number in `.claude-plugin/plugin.json`. Claude Code only offers an update when that number
changes.

## Unreleased

- **Runs in Devin.** Devin loads the Claude Code layout as it is; what it names differently is now handled. The guard
  hook matches Devin's tools too (`edit`, `write`, `notebook_edit`, every file an `apply_patch` adds, updates, deletes
  or moves to, `exec` in its `workdir`, and the text `write_to_process` types into a shell), finds the project and the
  plugin from `DEVIN_PROJECT_DIR` and `DEVIN_PLUGIN_ROOT`, and turns off with `APP_FUSION_GUARD=false` where plugin
  options do not exist. A session-start hook, silent under Claude Code, tells a Devin agent the plugin's folder for
  `${CLAUDE_PLUGIN_ROOT}`, the Devin names of the tools the skills mention, the path to take without the Workflow
  tool and the Figma budget default. `workspace.py guard <program> --agent devin` reads and prints Devin's
  `.devin/config.json` `Write(...)` deny rules, which fuse-preflight Check 7 uses in Devin.

## 0.3.0

From a third review, of the proof and the guard, and from the work-app run with three apps.

- **The scripts run the tests.** The proof trusted any JUnit file inside the workspace, so a result file written by
  hand yielded PROVEN. `evidence.py run` now executes the test command itself (no shell: the runner and its
  arguments; `{run}` and `FUSION_RUN_DIR` name the fresh run folder; `--env` for the runner's environment;
  `--collect` for runners that write elsewhere, taking only files the run created or changed, an `.xcresult`
  converted) and records the exit code, stdout, stderr and the JUnit XML the command produced. Shells, file copiers,
  archivers, `sleep`, `git` and inline code are refused as the test command. `canary.py run` does the same for the
  canary's tests, in a `tests/` folder below the run so a runner that empties its output folder never reaches the
  saved copy, and remembers the hash of the file they ran on, so `finish` knows whether they saw the break. The proof
  counts only executed suites, journeys and canaries; a result recorded by hand (`evidence.py suite`, `journey`) is
  kept but listed as a gap with the command that fixes it. Every skill and stack profile gives the `run` commands.
- **The canary cannot destroy the file it protects.** The saved copy is read-only, verified when made, and its hash
  is checked before any restore; on a mismatch the file is left as it is and the message says how to restore it.
- **A guard that reads the shell like a shell.** Operators and new lines split commands, shell keywords are stepped
  over so loop bodies are read, `cd` and `pushd` move the folder for what follows, every redirect form counts (`>|`,
  `2>`, `&>` too), `sh -c`, `bash -lc` and `eval` are read inside, a script a shell or an interpreter runs is read when
  it lies outside the plugin, a script piped into a shell is asked about, heredocs and inline code are scanned for
  the paths they open and whether they write or spawn a process (reads pass), `xargs` follows the pipe, `find -exec`
  is read for its command, and `dd`, `curl`, `tar`, `find -delete`, `sed -i`, `perl -pi`, package managers (a bare
  `yarn` too), build tools, formatters with `--fix` or `--write`, `patch` and git name their targets through their
  options. The folders that hold the proof's inputs (`analysis/<program>`, `evidence/`, `design/`) and any folder above
  them are denied to removing and moving commands, and test-result run folders are no longer shell-writable
  (`evidence.py run` writes them). A write whose target the guard cannot resolve is asked, never silently allowed,
  when the command names a judged file, `analysis/`, `legacy/` or a source app's real path. Git commands that can
  rewrite decisions, sign-offs or evidence are asked in the repository that holds the analysis folder, and pass in
  the new app's own repository; reads, commits and `switch -c` pass. Zipping the analysis folder into `/tmp`,
  `find -exec wc` and `json.dump` to standard output pass. Paths fold case on macOS and Windows. `hooks/guard.sh`
  runs the script on every matched call, so the workspace is found when Claude was started above or inside it, and a
  malformed `program.json` leaves the `legacy/` links protected.
- **A signature carries a person's name.** `signoff.py` and `decisions.py` refuse a `--by` that is empty, a
  placeholder, or the name of a model or an assistant, and accept a person's name in any script; the guard also asks
  when the recording scripts run as a module, from inline code, or with a variable for the subcommand.
- **Twins are one product in the rules.** The conflict judge runs only for capabilities with rules from two or more
  products, so a twin's platform-parity differences no longer land in the questions a person must settle.
- **The design analyst sees the official Figma plugin.** Its read tools (`mcp__plugin_figma_figma__*`) are listed, so
  the analyst no longer launches blind under the usual setup.
- **Arguments read right.** `fuse --source ...` without a name and `fuse-build <program> --batch <n>` no longer hand
  a flag to the skill as the program or capability name.
- **A headless first run no longer locks the intent.** Its documented defaults are marked `OPEN:` in INTENT.md, the
  next visit with pop-ups asks exactly those, and `fuse-status` points at `fuse <program>` until a person has
  answered, before the brief is written.

Earlier runs' suites, journeys and canaries were recorded by hand: record them again with `evidence.py run` and
`canary.py run`, or the proof lists them as gaps.

## 0.2.0

From an adversarial review of 0.1.0 and a trial on two production apps.

- **Evidence you cannot game by accident.** Results are bound to content, not file times: every recorded run keeps the
  SHA-256 of its result files and of the capability's code. A `git checkout`, a restore or a copy no longer makes
  fresh results look stale, an edited result file is rejected, and a code change makes old results stop counting.
  Each run gets its own folder. `evidence/test-runs.json` is now version 2; record earlier runs again.
- **A canary that cannot hurt your work.** `scripts/canary.py` saves the file it breaks and puts back the exact bytes,
  never with git, so uncommitted work is safe and nothing stays broken. It refuses test files and a break that was
  never made, and it counts only failures of the capability's own tests that passed on the real code.
- **Verdicts that stay put.** Verifying one capability keeps the others' verdicts; `fuse-status` no longer bounces
  between two capabilities, and it moves on to build what a shared journey waits for instead of looping.
- **Sign-offs a person owns.** The brief's approval (`fuse-brief <program> approve`, with the phases it covers) and the
  proof and visual sign-offs (`fuse-verify <program> sign`) live in `SIGNOFF.json`, bound to what was signed. A
  changed brief, verdict or screenshot needs a new signature.
- **Decisions honored in the proof.** `take:<app>` leaves out the other app's rules; `design` and `new-spec` need a
  test named after the decision; P1 rules are pinned as well as P0; a suspected legacy defect needs a person's keep or
  fix. Every question has its own key, so a rule conflict no longer overwrites the capability's conflict.
- **No self-granted exemptions.** A dropped string key, a renamed or dropped analytics event, and an API difference
  each need a person's decision. Design sample data is recorded in the design step, not by the build. A check is n/a
  only when the capability's own legacy files agree that there is nothing to compare. No design by intent is n/a.
- **Continuity for existing users.** New `platform_parity.py`: the store listing's bundle id, link domains, URL schemes,
  push, notification categories and channels (now extracted), app extensions, keychain and app groups, locales. New
  `events_parity.py`: analytics event names per capability. Platform items users depend on now block the plan.
- **Per platform.** Journeys are recorded and checked for every target platform; a native pair is checked per half.
- **Stable ids across re-runs.** A renamed capability keeps its id by its evidence; an id still in use that leaves the
  map is reported, and `map_aliases.json` carries it over. Designed features keep their screens and need a person's
  scope decision.
- **The guard protects the judge.** File edits to decisions, sign-offs, verdicts, catalogs and evidence are denied;
  recording a person's answer asks that person. The design analyst has an allowlist of Figma read tools and nothing
  else. The review, brief, build and verify commands can only be started by a person.
- **A second review, of these fixes.** Every run now judges every built capability, so a change made for one shows in
  the others. A signed, accepted PARTLY PROVEN capability no longer holds up the status. Ticking a met criterion in
  the brief keeps its approval. A rule-conflict decision wins over the capability's for its rules. A removed result
  file counts as tampering. The canary allows one break at a time, in the capability's own files, of at most six real
  lines, credited only from its own run folder. Parity results merge per capability. Parked capabilities leave their
  journeys. A native pair is judged per half, and platform continuity per platform, with a store listing per platform
  (`--store ios=me-ios,android=vmm`). Rule ids survive a reworded re-run, a conflict whose rule names do not resolve is
  still asked, and a person's own drop no longer blocks a re-map. The guard also protects `program.json`, asks before
  `workspace.py intent`, refuses shell writes to the proof's inputs, and protects a snapshot's source.
- **Smaller fixes.** Locales keep script and region where users differ (zh-Hans and zh-Hant, pt-BR and pt) and read
  Base as the source language; design-copy templates match whole words; screen texts come from the design context
  when cached; a rules slice no longer overwrites the map's arguments; a React Native app's native code is sharded;
  an app without an extractor no longer stops the others' inventory; endpoint literals and HAR recordings are
  sanitized; `goal: understand` stops at the approved brief; a legacy scan no longer counts as the new app's.

## 0.1.0

- **A front door.** `/app-fusion:fuse` asks what you want once, links two or more apps without copying them, and
  gives the exact first command.
- **Inventories that carry their rules.** Native iOS, React Native and native Android apps are scanned
  deterministically: screens, routes, endpoints (constants resolved), analytics, strings, storage, platform features,
  dependencies and tests. Each count is printed with the rule that produced it.
- **Capability map.** It lists what people can do in any app, merged across apps and classified as unique,
  shared-same or shared-diverged, with each app's evidence. Every capability is re-checked by a referee agent. It
  also produces persona journeys and a platform matrix.
- **Design trace.** Figma is read within a call budget, and every response is cached. Figma REST is available as an
  accelerator. Each screen is traced to the capabilities it serves. The gaps (features with no design, designs with
  no feature) become decisions.
- **Decisions and an approved plan.** A person decides conflicts, gaps, flagged rules, platform items, the stack and
  the store identity. The Fusion Brief and the continuity plan are a gate: nothing is built before they are approved.
- **Build and proof.** Capabilities are built tests-first. A script gives one verdict per capability from nine
  checks: built, tests ran, rules traced, journeys, API parity, strings, design copy, canary, legacy untouched.
- **Safety.** A legacy write guard hook, secrets quarantine, untrusted-content discipline in every agent and workflow,
  and read-only Figma.
