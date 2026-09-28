# Changelog

A release gets a new number in `.claude-plugin/plugin.json`. Claude Code only offers an update when that number
changes.

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
