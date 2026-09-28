# Target profile: SwiftUI (iOS)

Use this profile for `swiftui`, and for the iOS half of `native`. Check the installed toolchain first:
`xcodebuild -version` and `swift --version`.

## Create the project

- An Xcode app project (one `.xcodeproj`, no workspace needed) plus local Swift packages for the features. This is the
  shape of a modular native app such as me-ios: `Modules/<Feature>/Package.swift` and
  `Services/<Service>/Package.swift`. Generate the project with XcodeGen (`project.yml`) or Tuist when the team uses
  one, else create it in Xcode once and commit it.
- The bundle id, app groups, keychain access group, associated domains and extension targets come from CONTINUITY.md
  and `platform.json`. When the new app replaces a legacy iOS app in place, it **must** use that app's bundle id and
  team so users update and keep their Keychain items.

## Layout

```
App/                      @main App, root coordinator or router, role-aware TabView, deep-link handling
Modules/<Feature>/        one package per domain; Sources/<Feature>/<Capability>/ holds the capability, Tests/ its tests
Services/<API>/           API client packages (request types with path + method), persistence, analytics, flags
DesignSystem/             tokens (Color, Font, spacing) generated from design.json, components named as in Figma
Extensions/               notification service, share, widgets (only those platform.json keeps)
.maestro/                 smoke.yaml, JRN-NNN-<slug>.yaml
docs/fusion/              SCAFFOLD.md, CAP-NNN.md, i18n-map.json
```

A capability's **module** is `Modules/<Feature>/Sources/<Feature>/<Capability>/` plus its tests folder.

## Architecture

- TCA when a legacy app already uses it and the team knows it. Otherwise use Observation (`@Observable` models) with
  `NavigationStack`.
- Dependencies are struct-based clients with live, preview and test values.
- String Catalogs (`Localizable.xcstrings`) for every required locale. New keys are domain-prefixed. Legacy keys are
  mapped in `docs/fusion/i18n-map.json`.

## Tests with JUnit output

Tests use Swift Testing (`import Testing`). XCTest is fine where it already exists.

**Put the id in the function or type name, and in the display name:**
- `@Suite("CAP-012 mileage") struct CAP012MileageTests`
- `@Test("RULE-017 rounds to cents") func rule017_roundsToCents()`

Xcode's result bundle keeps display names, but `swift test`'s xUnit file keeps only function and type names.

Choose the route by what you are testing:
- **Packages** (fast; use it for a capability's module): `swift test --package-path Modules/<Feature> --parallel
  --xunit-output analysis/<program>/evidence/junit/<CAP>/unit.xml`.
  - XCTest results go to `unit.xml`. The `--parallel` flag is required, or no XCTest file is written.
  - Swift Testing results go to `unit-swift-testing.xml`, with no display names.
  - Record both files.
- **The app scheme:** `xcodebuild test -project <App>.xcodeproj -scheme <App> -destination 'platform=iOS
  Simulator,name=iPhone 17' -resultBundlePath <out>.xcresult`, then
  `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/xcresult_junit.py" <out>.xcresult analysis/<program>/evidence/junit/<CAP>/app.xml`.
  The converter keeps display names and node identifiers.
- `xcodebuild` returns 65 when a test fails. That is expected, and the result bundle is still written.

**Clean for verify:** delete the derived data you use (`-derivedDataPath <dir>`, then `rm -rf <dir>`) and every
`.build/` folder of the packages, then run the full test plan.

## Run and screenshot

- Build for the simulator, install and launch: `xcrun simctl install booted <App>.app` and
  `xcrun simctl launch booted <bundle id>`.
- Maestro flows use `appId: <bundle id>`. See `references/maestro.md`.
- Screenshots: `xcrun simctl io booted screenshot <png>`.

## Design system from Figma

Generate from `design.json` tokens:
- `Color` extensions or an asset catalog with light and dark variants when the Figma variables have modes
- `Font` styles with Dynamic Type (`relativeTo:`)
- spacing constants

Name components after the Figma components (Code Connect can map them later). A literal `Color(red:...)` in a feature
is a review finding.
