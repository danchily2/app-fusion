---
name: fuse-build
description: Builds one capability into the new app from its three sources of truth. The legacy apps supply the behavior, the Figma screens the UI, and the decisions the scope. Tests come first, then idiomatic code on the design system, then proof that API calls, strings, analytics and journeys still match and that the tests can fail. After a PROVEN pilot and a playbook, whole phases can be ported in batches.
argument-hint: "<program> <CAP-NNN> | <program> --batch <phase-number>"
arguments: program capability
disable-model-invocation: true
---

Build capability `$capability` of `$program` into the new app (`program.json` → `target.path`, default
`new-app/$program`). With `--batch <n>` in `$ARGUMENTS`, go to **Batch mode** at the end. Never touch `legacy/`. Run
every subagent in the foreground and wait for it. Stop any simulator, Metro server or process you started before you
finish, and say so. Scripts are in `${CLAUDE_PLUGIN_ROOT}/scripts/`; the guard hook asks the person before any
command that records a decision, and denies direct edits to what the proof reads.

If `$capability` is empty, take the first capability of the earliest brief phase with `Command: /app-fusion:fuse-build`
that has no `docs/fusion/CAP-NNN.md` in the new app, and say which you picked.

## Step 0: Binding inputs and the plan (a person approves)

- **The brief is binding and approved.** `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/signoff.py" $program show` must say
  the brief is approved, and its approval must cover the phase whose `Capabilities:` include `$capability`. An approval
  for an earlier version of the brief does not count. Meet each entry criterion of that phase, or stop and say which
  is unmet. Never re-plan around one. `docs/fusion/SCAFFOLD.md` must exist in the new app (Phase 0 done).
- **Decisions** (`DECISIONS.json`). Stop, and name the command, when:
  - the capability is `shared-diverged` and has no `conflict` decision (`/app-fusion:fuse-review $program conflicts`);
  - a decision parks it: `conflict: defer`, `gap: defer` or `drop`, `scope: out` or `defer`;
  - it is a `new` (design-only) capability without `scope: in`;
  - it is `gap: design-it` and its screens are not in the design yet.
- **Rules that need a person now.** List the capability's rules (`rules.json`) with a suspected defect or an open
  question, whatever their priority, and every rule conflict inside it that has no decision. The plan asks the person
  about each: keep the legacy behavior (`rule: confirmed`), fix it (`rule: wrong`, with the fix in the note), or talk
  it over first (`discuss`, which blocks this build). A P0 rule under `discuss` is settled here, before any code.
- **Behavior.** The capability's entry in `capabilities.json`: every legacy implementation's screens, files,
  endpoints, events, strings and storage. Its rules come from `rules.json` and `BUSINESS_RULES.md`: honor each
  `wrong` verdict and use the reviewer's note.
- **UI.** Its screens come from `traceability.json`. For each screen, get a build-ready spec from
  `app-fusion:design-analyst`: "Spec screen <fileKey>:<nodeId> for <stack> using the design system in <target>/src
  (or the profile's path). Use the cache under analysis/$program/design/ first. Budget: <n> Figma calls." The analyst
  has no shell and writes nothing: save any `get_design_context` output it returns to
  `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/figma_index.py" path $program <fileKey> <nodeId> context`, record the calls
  with `figma_index.py budget $program --spend <n>`, and run `figma_index.py build $program`. The texts of a built
  screen come from its design context.
- **Stack profile.** `${CLAUDE_PLUGIN_ROOT}/references/targets/<stack>.md`. Also read `analysis/$program/PLAYBOOK.md`
  when it exists.

Present the plan and **stop until the person approves** (plan mode if available). The plan covers:
- the module path and the files to create
- which legacy behavior is kept, from which app, and under which decision
- the P0 and P1 rules and the tests that pin them, and the rules above that need the person's answer
- the endpoints the new code calls, any backend move for `docs/fusion/api-map.json`, and any difference that needs an
  `api` decision
- the string keys, mapped or new, and any key to drop (a `strings: drop` decision); the events kept or renamed (the
  program's `analytics:taxonomy` decision says whether renames are allowed)
- the journeys through the capability and their Maestro flows
- where the design and the legacy app disagree (a person's call)

Record the person's answers about rules, drops and differences in one JSON list and run
`python3 "${CLAUDE_PLUGIN_ROOT}/scripts/decisions.py" add-json $program <file>`. The guard asks the person to confirm;
a headless run records nothing and says so.

## Step 1: Tests first

Spawn `app-fusion:test-engineer`: "Write the tests for $capability in <target>, following
${CLAUDE_PLUGIN_ROOT}/references/targets/<stack>.md and ${CLAUDE_PLUGIN_ROOT}/references/maestro.md."
- **Unit tests** pin every P0 and P1 rule of the capability with the concrete values of its card. Every test names
  its RULE-NNN, and suites name $capability. A behavior a person redesigned (`design`, `new-spec`) is pinned by a test
  named after its DEC-NNN.
- **One Maestro flow per journey** through the capability, at `<target>/.maestro/JRN-NNN-<slug>.yaml`, run against
  test accounts only.
- **Expected API calls**: the legacy endpoints of the capability.

Show the person the test files and get a yes before going on. In a headless run, record that the yes was not given.

## Step 2: Build it

Spawn `app-fusion:feature-porter` for $capability with the approved plan, or build it yourself following that agent's
rules. The porter writes the module, the key map entries (`docs/fusion/i18n-map.json`, `analytics-map.json`,
`api-map.json`) and `docs/fusion/$capability.md`, whose `## Files`, `## Shared files`, `## Tests` and `## API`
sections the proof reads. It also returns **shared-file needs**, which you apply: routes, shared catalogs, the API
client index and dependencies. Add each shared file you changed to the notes' `## Shared files`.

## Step 3: Prove it, and prove the proof can fail

Iterate on this capability's tests only. Then, in this order:

1. **Canary.** Pick one line of the capability's own code (a file in `## Files`) that a rule depends on, and one
   small change that matters: a threshold by one, a rounding mode, a flipped condition. At most six lines, more than
   whitespace, and one canary at a time in the whole program. Then:
   - `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/canary.py" start $program $capability --file <that file> --change "<what you will break>"`.
     It saves the file and prints a run folder.
   - Make the break with Edit, then run the covering tests **through the canary script**, which executes them itself
     on the broken file and records their result in that run folder:
     `canary.py run $program $capability -- <the profile's test command>` (with `{run}`, `--env` or `--collect` as the
     profile says). Then `canary.py finish $program $capability`. It restores the file byte for byte (never with git,
     so uncommitted work is safe), checks the hash, and records which tests of the capability failed. Tests run any
     other way, or before the break, count for nothing.
   - If the tests could not run, `canary.py abort $program $capability` restores the file without recording.
   - If no test of the capability failed, the tests do not pin the behavior: strengthen them and run a new canary.
2. **The whole suite, last.** Run it through the evidence script, which makes the run folder, executes the profile's
   command itself (no shell) and records the exit code, the output and the JUnit XML it wrote:
   `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/evidence.py" run $program --capability $capability --name unit -- <the
   profile's test command>`. For a native pair (`ios/` and `android/` in the new app), run each half's suite on its
   own, with `--platform ios` and `--platform android` and names such as `unit-ios`: the proof checks each half on its
   own results. Report `tests executed: N` from its output. Zero executed, or only skipped, is not green. A canary
   counts only for tests that pass in this recorded suite. A result recorded by hand (`evidence.py suite`) is a gap,
   never a pass.
3. **Parity checks.** Run them, and fix or take to a person anything they report:
   - `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/api_parity.py" $program --capability $capability`. A missing legacy
     endpoint is fixed, mapped in `api-map.json` for a backend move, or recorded by a person as an `api` decision.
     Never record it yourself.
   - `i18n_parity.py`, `events_parity.py` and `design_text.py`, each with `$program --capability $capability`.
4. **Journeys**, when a simulator is available and the app builds. Install the app and, for each flow and each target
   platform, run Maestro through the evidence script:
   `evidence.py run $program --journey <JRN> --platform <ios|android> --flow <flow> --device "<device>" -- maestro test <flow, relative to the new app> --format junit --output {run}/maestro.xml`.
   Capture one screenshot per designed screen into `analysis/$program/evidence/shots/$capability/` (Maestro
   `takeScreenshot`, or `xcrun simctl io booted screenshot`) and record each with
   `evidence.py shot $program --screen <fileKey>:<nodeId> --capability $capability --app <png>`.

Every recorded result is bound to the content of the files the notes name. Changing any of them after a run makes
that run stale: run and record it again rather than explaining it away.

## Step 4: Notes and review

Complete `docs/fusion/$capability.md`: fill the `## Canary` section from the canary entry in
`evidence/test-runs.json` (what was broken and which tests failed), the executed-test count, and the parity results.
Mask any credential-like literal: the file gets committed.

Then run the reviews:
- If screenshots exist, spawn `app-fusion:ui-conformance-reviewer` on the design and app pairs, and fix every Blocker
  and High.
- Spawn `app-fusion:architecture-critic` on the module, apply every Blocker and High finding, and list the rest in the
  notes.

A change made for a review makes the recorded runs stale. Run Step 3 again for what changed.

## Finish

Refresh the report with `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/build_report.py" $program`. Report the tests run and
passed, the canary result, the four parity verdicts, the journeys run and where everything is. This is your own
evidence. The independent check is `/app-fusion:fuse-verify $program $capability`: it re-runs from clean, and it
comes before building the next capability. After the **pilot** capability is PROVEN, write
`analysis/$program/PLAYBOOK.md` with the recipe that worked (paths, patterns, commands, pitfalls). Batch mode needs it.

---

## Batch mode (`--batch <phase>`)

Run a batch only when all of these hold:
- the pilot capability is **PROVEN** in `VERIFICATION.json`, judged on its current code
- `PLAYBOOK.md` exists
- the brief's approval covers the phase
- the person approved the fan-out in a pop-up that showed the capability count and the agent estimate (about three
  agents per capability)

Take the phase's capabilities that are not built yet and not parked by a decision. Step 0's rule questions come
first, for all of them together, in one round of pop-ups. A capability that depends on another's module (from the
brief's architecture table) names it in `deps`.

**With the Workflow tool**, call it by name. If the tool does not know the name, pass
`scriptPath: "${CLAUDE_PLUGIN_ROOT}/workflows/port-batch.js"` instead:

```
Workflow({
  name: "app-fusion:fuse-port-batch",
  args: { program: "$program", stack: "<stack>", target: "<target path>",
          capabilities: [ {id, name, module: "<module path inside target>", deps: [ids]} ... ] }
})
```

Each agent writes only its own module and notes, and returns shared-file needs, which you apply in order, one
capability at a time, rebuilding after each. The test engineers write unit tests only: after the batch, write the
Maestro flows of the phase's journeys yourself, one at a time, because a journey crosses capabilities. The workflow
stops launching batches when fewer than two thirds of a batch build and pass their tests (a circuit breaker). Then
read `failed` and `playbookGaps`, fix the playbook, and re-invoke with `remaining`, `failed` or `blocked` as returned.
Afterwards, run Step 3 per capability (canary, the suite, parity, journeys), then `fuse-verify` for the phase.
**Without the Workflow tool**, build the capabilities one after another with the single-capability flow above.
