---
name: fuse-build
description: Builds one capability into the new app from its three sources of truth. The legacy apps supply the behavior, the Figma screens the UI, and the decisions the scope. Tests come first, then idiomatic code on the design system, then proof that API calls, strings and journeys still match. After a PROVEN pilot and a playbook, whole phases can be ported in batches.
argument-hint: "<program> <CAP-NNN> | <program> --batch <phase-number>"
arguments: program capability
disable-model-invocation: true
---

Build capability `$capability` of `$program` into the new app (`program.json` → `target.path`, default
`new-app/$program`). With `--batch <n>` in `$ARGUMENTS`, go to **Batch mode** at the end. Never touch `legacy/`. Run
every subagent in the foreground and wait for it. Stop any simulator, Metro server or process you started before you
finish, and say so.

If `$capability` is empty, take the first capability of the earliest brief phase with `Command: /app-fusion:fuse-build`
that has no `docs/fusion/CAP-NNN.md` in the new app, and say which you picked.

## Step 0: Binding inputs and the plan (a person approves)

- **The brief is binding.** `FUSION_BRIEF.md` must be approved (the Approval block carries a name), and the phase
  whose `Capabilities:` include `$capability` must exist. Meet each of its entry criteria, or stop and say which is
  unmet. Never re-plan around one. `docs/fusion/SCAFFOLD.md` must exist in the new app (Phase 0 done).
- **Decisions.** Read `DECISIONS.json`.
  - For a `shared-diverged` capability, a `conflict` decision must exist. Without one, stop:
    `/app-fusion:fuse-review $program conflicts`.
  - A `gap: design-it` without screens means the design is not ready. Stop.
  - A P0 rule of the capability marked `discuss` is settled at this gate, before any code.
- **Behavior.** The capability's entry in `capabilities.json`: every legacy implementation's screens, files,
  endpoints, events, strings and storage. Its rules come from `rules.json` and `BUSINESS_RULES.md`: honor each
  `wrong` verdict and use the reviewer's note.
- **UI.** Its screens come from `traceability.json`. For each screen, get a build-ready spec from
  `app-fusion:design-analyst`: "Spec screen <fileKey>:<nodeId> for <stack> using the design system in <target>/src
  (or the profile's path). Use the cache under analysis/$program/design/ first. Budget: <n> Figma calls." Save any
  `get_design_context` output it returns to
  `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/figma_index.py" path $program <fileKey> <nodeId> context`, record the calls
  with `figma_index.py budget $program --spend <n>`, and run `figma_index.py build $program`. The texts of a built
  screen come from its design context.
- **Stack profile.** `${CLAUDE_PLUGIN_ROOT}/references/targets/<stack>.md`. Also read `analysis/$program/PLAYBOOK.md`
  when it exists.

Present the plan and **stop until the person approves** (plan mode if available). The plan covers:
- the module path and the files to create
- which legacy behavior is kept, from which app, and under which decision
- the rules and the tests that pin them
- the endpoints the new code calls, and any difference that needs an `api` decision
- the string keys, mapped or new, and the events kept
- the journeys through the capability and their Maestro flows
- where the design and the legacy app disagree (a person's call)

## Step 1: Tests first

Spawn `app-fusion:test-engineer`: "Write the tests for $capability in <target>, following
${CLAUDE_PLUGIN_ROOT}/references/targets/<stack>.md and ${CLAUDE_PLUGIN_ROOT}/references/maestro.md."
- **Unit tests** pin each rule of the capability with the concrete values of its card. Every test names its
  RULE-NNN, and suites name $capability.
- **One Maestro flow per journey** through the capability, at `<target>/.maestro/JRN-NNN-<slug>.yaml`, run against
  test accounts only.
- **Expected API calls**: the legacy endpoints of the capability.

Show the person the test files and get a yes before going on. In a headless run, record that the yes was not given.

## Step 2: Build it

Spawn `app-fusion:feature-porter` for $capability with the approved plan, or build it yourself following that agent's
rules. The porter writes the module, the i18n key map entries (`docs/fusion/i18n-map.json`) and
`docs/fusion/$capability.md` (its `## Files` section names every new file in backticks). It also returns
**shared-file needs**, which you apply: routes, shared catalogs, the API client index and dependencies.

## Step 3: Prove it, and prove the proof can fail

Iterate on this capability's tests only, then run the whole suite once before Step 4.

1. **Unit tests** with JUnit output (the profile's command) to `analysis/$program/evidence/junit/$capability/`, then
   record them:
   `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/evidence.py" suite $program --capability $capability --name unit --command "<cmd>" --junit analysis/$program/evidence/junit/$capability/`.
   Report `tests executed: N`. Zero executed, or only skipped, is not green.
2. **Canary.** Break the capability's code in one small way that matters: a threshold by one, a rounding mode, a
   flipped condition. Run the covering tests with JUnit to `analysis/$program/evidence/canary/$capability/`, confirm
   at least one fails, then restore the file with `git -C <target> checkout -- <file>` and confirm the suite is green
   again. Record it with
   `evidence.py canary $program --capability $capability --change "<what you broke>" --junit analysis/$program/evidence/canary/$capability/`.
   If nothing failed, the tests do not pin the behavior. Strengthen them before going on.
3. **Parity checks.** Run the three scripts, and fix or take to a person anything they report:
   - `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/api_parity.py" $program --capability $capability`. A missing legacy
     endpoint is fixed, or recorded by a person as an `api` decision through `/app-fusion:fuse-review`. Never record
     it yourself.
   - `i18n_parity.py $program --capability $capability` and `design_text.py $program --capability $capability`.
4. **Journeys**, when a simulator is available and the app builds. Install the app and run each flow:
   `maestro test <flow> --format junit --output analysis/$program/evidence/maestro/<JRN>.xml`. Record each run with
   `evidence.py journey $program --journey <JRN> --flow <flow> --junit <xml> --device "<device>"`. Capture one
   screenshot per designed screen into `analysis/$program/evidence/shots/$capability/` (Maestro `takeScreenshot`, or
   `xcrun simctl io booted screenshot`). Record each with
   `evidence.py shot $program --screen <fileKey>:<nodeId> --capability $capability --app <png>`.

## Step 4: Notes and review

Complete `docs/fusion/$capability.md`: fill the `## Canary` section and the executed-test count, and link the parity
results. Mask any credential-like literal: the file gets committed.

Then run the reviews:
- If screenshots exist, spawn `app-fusion:ui-conformance-reviewer` on the design and app pairs, and fix every Blocker
  and High.
- Spawn `app-fusion:architecture-critic` on the module, apply every Blocker and High finding, and list the rest in the
  notes.

## Finish

Refresh the report with `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/build_report.py" $program`. Report the tests run and
passed, the canary result, the three parity verdicts, the journeys run and where everything is. This is your own
evidence. The independent check is `/app-fusion:fuse-verify $program $capability`: it re-runs from clean, and it
comes before building the next capability. After the **pilot** capability is PROVEN, write
`analysis/$program/PLAYBOOK.md` with the recipe that worked (paths, patterns, commands, pitfalls). Batch mode needs it.

---

## Batch mode (`--batch <phase>`)

Run a batch only when all of these hold:
- the pilot capability is **PROVEN** in `VERIFICATION.json`
- `PLAYBOOK.md` exists
- the person approved the fan-out in a pop-up that showed the capability count and the agent estimate (about three
  agents per capability)

Take the phase's capabilities that are not built yet. A capability that depends on another's module (from the brief's
architecture table) names it in `deps`.

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
capability at a time, rebuilding after each. The workflow stops launching batches when fewer than two thirds of a
batch build and pass their tests (a circuit breaker). Then read `failedUnits` and `playbookGaps`, fix the playbook,
and re-invoke with `remaining`, `failed` or `blocked` as returned. Afterwards, run Step 3 per capability (canary,
parity, journeys), then `fuse-verify` for the phase. **Without the Workflow tool**, build the capabilities one after
another with the single-capability flow above.
