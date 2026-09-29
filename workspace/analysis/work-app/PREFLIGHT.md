# work-app: preflight

Run: 2026-09-28, headless (no pop-up tool), so the five questions below are unanswered open items.

## Answers

1. **Scope.** Is each app complete in its repository, or does part of it live elsewhere (shared design system, common
   SDK, web view from another team, backend-for-frontend)?
   **OPEN: a person must answer.**
2. **Test environment.** Is there a test backend and test accounts for each app, including one person with both
   roles? Who owns them? May the plugin run the apps against them?
   **OPEN: a person must answer.**
3. **The new app's backend.** Same APIs as today, a new gateway, or a mix? Is any API changing during the project?
   **OPEN: a person must answer.**
4. **Constraints.** Release date, minimum OS, store or brand rules, accessibility requirements, earlier merge attempts?
   **OPEN: a person must answer.** Seen in code: Manager's iOS minimum is 15.1, Employee's is 18.0.
5. **Off limits.** Anything that must stay untouched (another team's module, a frozen API contract, analytics event
   names dashboards depend on)?
   **OPEN: a person must answer.**

## Overlap and boundaries (Check 6)

- No shared code between the repositories: no submodules, no common package. Each app is its own repository (not a
  monorepo), and the links point at the repository roots.
- **Shared third-party services** (merge opportunities, plus continuity items for the brief): Firebase (analytics,
  crashlytics, messaging, remote config), Snowplow analytics and Survicate surveys are in both apps. Manager also has
  Sentry and Apollo GraphQL. Employee also has LaunchDarkly, Realm, TCA and Google Maps.
- Identifiers: Manager `com.visma.vmm` (iOS and Android; Android develop `com.visma.vmm.develop`). Employee
  `com.visma.Employee`, plus a share extension, and a second extension id `com.visma.vme.payslip.expense-share-extension`.
- Design systems: Employee has its own `Modules/EmployeeUIComponents` package, and Manager has themes in the app
  (`AppTheme.tsx`, `custom-icons`). They are not shared.

## Checks

| # | Check | Status | Found | Fix |
|---|---|---|---|---|
| 0 | Questions for a person | ⚠️ | 5 of 5 unanswered (headless run) | Answer them (see above) before `fuse-brief` |
| 1 | Stacks | ✅ | **vmm (Manager):** React Native 0.86.0, React 19.2.7, yarn (yarn.lock), iOS `vmm.xcworkspace` + Podfile, Android AGP 8.12.0, Gradle 9.3.1, one module `:app`. **me-ios (Employee):** native Swift, `Employee.xcodeproj` (no workspace, no Podfile), SPM (56 pins), 16 local packages under `Modules/`, share extension. Both links clean, at the recorded commit | none |
| 2 | Analysis tools | ✅ | python3 3.14.7, git 2.53.0, scc 4.1.0, jq | none |
| 3 | Toolchains | ✅ | Xcode 26.2, Swift 6.2.3, CocoaPods 1.13.0, iPhone 17 Pro simulators; Node 22.22.0, yarn 1.22.22 (the lockfile is Yarn Berry format, so Corepack gives the pinned version); Java 17.0.8, adb 1.0.41, Android SDK at `~/Library/Android/sdk`; Maestro 2.3.0. Target stack undecided, so no target-specific check | Build smoke test not run (it needs consent; offer it in an interactive run) |
| 4 | Source completeness | ⚠️ | **me-ios is a shallow clone**, so there is no change history (churn and ownership signals are unavailable). vmm: `node_modules` and `Pods` are absent, so the iOS and Android builds cannot run until dependencies are installed (never inside `legacy/`). Apollo codegen output in `src/gql/` is present. All registries are public; one fork: `Visma-Mobile-Employee/WeScan` on GitHub. No submodules | For history: `git -C /Users/vismaemployee/Downloads/me-ios fetch --unshallow` (optional) |
| 5 | Figma | ⚠️ | Claude.ai Figma connector connected. `whoami`: Dan-Mihai Cuc. **Dev seat on "Visma Software" (enterprise: 600 reads a day, 20 a minute)**; View seats on "Visma" (org) and a Starter team (6 reads a month). `FIGMA_TOKEN` not set. **No Figma file recorded for work-app** | Add the new app's design: `python3 "…/scripts/workspace.py" init work-app --figma <url>`. The file must belong to the Visma Software plan: with a View seat, MCP ingestion is not viable. Or set `FIGMA_TOKEN` for the REST path |
| 6 | Overlap | ✅ | Separate repos, shared SDK vendors, no shared code (see above) | none |
| 7 | Legacy protection | ✅ | Deny rules in `.claude/settings.json` cover `legacy/**` and both real paths. The plugin's guard hook is on by default. They cover Claude's file tools and the shell commands they recognize, not a script that opens files itself. A read-only mount is the hard guarantee | Optional: mount the sources read-only |

## Readiness per step

| Step | Ready? | Why |
|---|---|---|
| `fuse-assess`, `fuse-map` | ✅ | Checks 1–2 green (me-ios has no history signals) |
| `fuse-design` | ⚠️ | Connected with a Dev seat, but no Figma file is recorded yet |
| `fuse-rules` | ✅ | Checks 1–2 green |
| `fuse-brief` | ⚠️ | Needs the discovery files, and it needs the five answers above to be sound |
| `fuse-scaffold`, `fuse-build` | ✅ (tools) | Xcode, simulator, Node, Android SDK and Maestro are all present. The target stack check comes once it is decided |
| `fuse-verify` | ✅ (tools) | As above, plus Check 7 green |
