# Target profile: React Native

Use this profile when the new app's stack is `react-native`. The scaffold, build and verify steps follow it. Check
the current versions before generating: `npm view react-native version` and `npm view @react-native-community/cli version`.
Never copy version numbers from this file without checking them.

## Create the project

- **Bare React Native (the default for a fusion).** Use it when the legacy apps have native extensions (notification
  service or content extensions, share extensions, widgets), app groups or custom native modules. A fusion almost
  always does. Run `npx @react-native-community/cli@latest init <AppName> --directory new-app/<program> --skip-git-init
  --pm <yarn|npm>`, then `git init` inside it. The legacy React Native app's `ios/` and `android/` settings (bundle id,
  capabilities, extensions) are the reference for what the new shell must declare. Copy **settings**, not files.
- **Expo (prebuild)** only when every native need is covered by config plugins and the brief chose it.

## Layout

```
src/
  app/                 navigation shell: root navigator, role-aware tabs (one stack per persona), deep-link config
  features/<domain>/<capability-slug>/   one folder per capability: screens, hooks, state, tests (__tests__/)
  design-system/       tokens.ts (generated from design.json tokens), components/ (Button, Card, ListItem ... named as in Figma)
  api/                 one client per backend (base URL from config), typed endpoints per domain
  i18n/                i18next setup and locales/<lang>.json
  analytics/           track(event, props): legacy wire names kept
  flags/               remote config or feature flags wrapper
  storage/             secure storage (react-native-keychain) for tokens; MMKV for non-sensitive state
.maestro/              smoke.yaml, JRN-NNN-<slug>.yaml
docs/fusion/           SCAFFOLD.md, CAP-NNN.md, i18n-map.json
```

A capability's **module** (the build step's write scope) is `src/features/<domain>/<capability-slug>/`.

## State and data

- Use Redux Toolkit with RTK Query when a legacy React Native app already uses it (keep its patterns). Otherwise use
  TanStack Query for server state plus a small store (Zustand) for client state. Choose one state library, not two.
- Persist only what CONTINUITY.md says must survive, and keep tokens in the Keychain, never in AsyncStorage.

## Tests with JUnit output

Configure jest-junit once in `package.json`:

```json
"jest": { "reporters": ["default", ["jest-junit", { "outputDirectory": "./test-results", "outputName": "junit.xml",
  "classNameTemplate": "{classname}", "titleTemplate": "{title}", "addFileAttribute": "true" }]] }
```

Per run, from the workspace root, take a fresh run folder and pass it as an absolute path (jest runs inside the new
app, so a relative path would land there):

```bash
RUN=$(python3 "${CLAUDE_PLUGIN_ROOT}/scripts/evidence.py" dir <program> suite <CAP>); OUT="$PWD/$RUN"
(cd new-app/<program> && JEST_JUNIT_OUTPUT_DIR="$OUT" JEST_JUNIT_OUTPUT_NAME=unit.xml npx jest src/features/<domain>/<slug> --ci)
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/evidence.py" suite <program> --capability <CAP> --name unit --command "npx jest ..." --junit "$RUN"
```

**Ids in names.** `describe('CAP-012 mileage', ...)` and `it('RULE-017 rounds the allowance to cents', ...)`. jest-junit
keeps both, so the proof finds them.

**Clean for verify:** `rm -rf node_modules/.cache test-results && npx jest --clearCache`, then the full suite with `--ci`.

## Run on devices

- iOS: `npx react-native run-ios --simulator "iPhone 17"` (or build with `xcodebuild` in `ios/` against the
  workspace).
- Android: `npx react-native run-android` on a running emulator.
- Maestro needs the app installed. `appId` is the bundle id (iOS) or application id (Android). See
  `references/maestro.md`.
- Screenshots: `xcrun simctl io booted screenshot <png>`, or `- takeScreenshot: <path-without-extension>` in a flow.

## Design system from Figma

Generate `src/design-system/tokens.ts` from `analysis/<program>/design/design.json` → `tokens`:
- colors keep their Figma variable names in camelCase (`g-surface/primary` becomes `gSurfacePrimary`)
- typography becomes `{ fontSize, fontWeight, lineHeight }` entries
- spacing and radius become numbers

Components take tokens only. A hard-coded color or size in a feature is a review finding.

## i18n

i18next with one JSON file per locale. Keys are new, domain-prefixed names (`approvals.list.title`). Legacy keys are
mapped in `docs/fusion/i18n-map.json` (`"vmm:approval_title": "approvals.list.title"`). The i18n parity check reads
that map, so a missing mapping shows as a missing key.

## Native pieces a fusion usually needs

- Notification service or content extensions and a share extension are Swift targets in `ios/` with an app group
  shared with the app.
- Push: `@react-native-firebase/messaging` or `notifee`, registered after sign-in. Tokens are sent to the backend per
  role.
- Universal and app links need `associated-domains` entitlements for every legacy domain that CONTINUITY.md keeps,
  plus Android intent filters with `autoVerify`.
