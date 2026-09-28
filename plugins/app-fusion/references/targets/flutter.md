# Target profile: Flutter

Use this profile when the brief chose `flutter`. Check the installed tools first: `flutter --version` and
`flutter doctor`.

## Project and layout

Create the project with
`flutter create --org <reverse-domain> --project-name <app> --platforms ios,android new-app/<program>`. Take the
bundle and application ids from CONTINUITY.md (keep a legacy app's ids to update it in place).

Code lives under `lib/`:
- `app/`: the router (go_router) with role-aware shells and deep links
- `features/<domain>/<capability>/`: a capability's **module**, with its tests in `test/features/<domain>/<capability>/`
- `design_system/`: `ThemeData` and token classes generated from design.json
- `api/`, `l10n/` (ARB files per locale, gen-l10n), `analytics/`, `flags/`

Native extensions (notification service, share) are still Swift and Kotlin targets under `ios/` and `android/`.

## Tests with JUnit output

Take a fresh run folder (`RUN=$(python3 "${CLAUDE_PLUGIN_ROOT}/scripts/evidence.py" dir <program> suite <CAP>); OUT="$PWD/$RUN"`),
then run `flutter test --machine test/features/<domain>/<capability> | tojunit > "$OUT/unit.xml"` inside the app.
`tojunit` comes from the junitreport package: `dart pub global activate junitreport`.

Put ids in the group and test names: `group('CAP-012 mileage', ...)` and `test('RULE-017 rounds to cents', ...)`.

To clean for verify, run `flutter clean`, then the full `flutter test --machine`.

Maestro drives Flutter apps through semantics labels (`Semantics(identifier: ...)`).
