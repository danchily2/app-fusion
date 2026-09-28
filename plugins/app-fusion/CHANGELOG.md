# Changelog

A release gets a new number in `.claude-plugin/plugin.json`. Claude Code only offers an update when that number
changes.

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
