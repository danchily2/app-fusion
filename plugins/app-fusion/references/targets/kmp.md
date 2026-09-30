# Target profile: Kotlin Multiplatform

Use this profile when the brief chose `kmp`: shared business logic in Kotlin, native UIs (SwiftUI on iOS, Compose on
Android), or Compose Multiplatform when the brief says so.

## Layout

- `shared/`: a Gradle KMP module with `commonMain` (domain, rules, API clients with Ktor, persistence with SQLDelight)
  and `commonTest`.
- `iosApp/`: the SwiftUI app, following `references/targets/swiftui.md`, consuming the shared framework.
- `androidApp/`: the Compose app, following `references/targets/compose.md`.

A capability's **module** is its package in `shared/src/commonMain/.../<capability>/`, plus its UI folders in both
apps. The porting notes list all of them.

## Tests with JUnit output

- **Business rules** live in `commonTest` (kotlin.test). They run on the JVM through
  `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/evidence.py" run <program> --capability <CAP> --name unit
  --collect 'shared/build/test-results/**/*.xml' -- ./gradlew :shared:allTests`, which collects the JUnit XML Gradle
  writes under `shared/build/test-results/` during the run.
- **Rule ids** go in the test names: ``fun `RULE-017 rounds to cents`()``.
- **UI tests** follow the per-platform profiles, and Maestro covers the journeys on both apps.
