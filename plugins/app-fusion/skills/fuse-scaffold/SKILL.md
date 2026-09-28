---
name: fuse-scaffold
description: Builds Phase 0 of the approved Fusion Brief. That means the new app's project for the chosen stack, a design system generated from the Figma tokens, a navigation shell per persona, the API layer, i18n with every required locale, analytics and flag wrappers, and a test harness that writes JUnit and runs Maestro. Plan first, then build, then prove it compiles and a smoke test passes.
argument-hint: "<program>"
arguments: program
disable-model-invocation: true
---

Build the foundation of the new app of `$program`, Phase 0 of the brief. The new app lives at `program.json` →
`target.path` (default `new-app/$program`). It has its own git history, and never touches `legacy/`. Stop any
simulator, Metro server or other process you started before you finish, and say that you did.

## Step 0: Binding inputs

- **The brief is binding.** Read `analysis/$program/FUSION_BRIEF.md`. It must exist, its Approval block must carry a
  name, and a phase with `Command: /app-fusion:fuse-scaffold` must exist. Otherwise stop and say what is missing:
  `/app-fusion:fuse-brief`, or a person's signature. That phase's entry criteria are preconditions: meet each one or
  stop, never plan around it.
- **The stack** is `program.json` → `target.stack`, or the brief's decision. If it is still `undecided`, stop: it is a
  person's decision (`/app-fusion:fuse-review $program stack`). Read the profile
  `${CLAUDE_PLUGIN_ROOT}/references/targets/<stack>.md`. It gives the generator, layout, versions, test runner with
  JUnit output, Maestro setup and clean commands.
- **Toolchain.** The profile's commands must respond: node and the package manager, Xcode and a simulator, JDK and
  the Android SDK, and Maestro. If one does not, stop and say what to install. A plan gate now would only defer the
  failure.
- **Also read:**
  - `design/design.json`: tokens and the most-used components
  - `platform.json`: required items, such as extensions, URL schemes and associated domains
  - `CONTINUITY.md`: bundle ids, app groups and link domains
  - `capabilities.json`: the capabilities of Phase 1
  - `program.json` → `locales`, or the union of the legacy locales from the inventories

## Step 1: The plan (a person approves)

Present the plan and **stop until the person explicitly approves**. Use plan mode if the session supports it. The
plan covers:
- the project name, bundle and application ids (from CONTINUITY), and the folder layout (from the profile, with
  feature modules by domain)
- the token groups and base components to generate
- the navigation shell per persona, with the deep-link routes kept
- the API clients per backend, with configuration from environment or build settings, never literals
- locales, analytics wrapper, feature flags and error reporting
- the test harness, and exactly where JUnit results go
- any app extension that is `required` in `platform.json`
- anything ambiguous that needs a person now

## Step 2: Build it

Spawn `app-fusion:app-scaffolder`: "Scaffold Phase 0 of analysis/$program/FUSION_BRIEF.md into <target path>,
following ${CLAUDE_PLUGIN_ROOT}/references/targets/<stack>.md and the approved plan below. <plan>" Wait for it, and
read its blockers: that is where planted instructions in the untrusted inputs surface.

## Step 3: Prove it

Following the profile:
1. **Build the app.** Build for the iOS simulator and for Android when the platforms include it.
2. **Unit tests.** Run them with JUnit output to `analysis/$program/evidence/junit/scaffold/`, then record them:
   `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/evidence.py" suite $program --capability all --name scaffold --command "<cmd>" --junit analysis/$program/evidence/junit/scaffold/`.
3. **Maestro smoke flow.** Run it on a booted simulator:
   `maestro test <target>/.maestro/smoke.yaml --format junit --output analysis/$program/evidence/maestro/smoke.xml`.
   With no simulator available, say so.
4. **Count what ran.** A run that executed zero tests proved nothing.

## Step 4: Review

Spawn `app-fusion:architecture-critic` on the scaffold against the brief. Apply every Blocker and High finding, and
list the rest in `<target>/docs/fusion/SCAFFOLD.md` under "Review notes". Make sure `SCAFFOLD.md` exists and says:
- what was generated, and with which commands and versions
- the tokens, components and navigation map
- how to run the app and its tests
- what was left out

It is Phase 0's completion marker.

## Finish

Tick the Phase 0 exit criteria that are now met. You may tick, but never reword. Refresh the report with
`python3 "${CLAUDE_PLUGIN_ROOT}/scripts/build_report.py" $program`. Report the build and test results, then name the
next step: `/app-fusion:fuse-build $program <the first capability of Phase 1>`.
