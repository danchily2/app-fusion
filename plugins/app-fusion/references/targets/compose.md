# Target profile: Jetpack Compose (Android)

Use this profile for `compose`, and for the Android half of `native`. Check the installed tools: `java -version`,
`$ANDROID_HOME`, and the Gradle wrapper of the generated project.

## Create the project

- A Gradle multi-module project with version catalogs (`gradle/libs.versions.toml`), created from the Android Studio
  "Empty Activity" template or an internal template the team uses. It has `:app`, `:core:designsystem`, `:core:network`,
  `:core:data` and `:feature:<domain>` modules.
- The `applicationId`, signing, deep-link hosts and permissions come from CONTINUITY.md and `platform.json`. When the
  new app replaces a legacy Android app in place, it **must** keep that app's application id and signing key.

## Layout

```
app/                         MainActivity, NavHost with role-aware graphs, deep links (intent filters with autoVerify)
core/designsystem/           tokens (Color, Typography, spacing) from design.json, components named as in Figma
core/network/                Retrofit or Ktor clients per backend, base URL from BuildConfig
feature/<domain>/            src/main/.../<capability>/ holds the capability; src/test/ its unit tests
.maestro/                    smoke.yaml, JRN-NNN-<slug>.yaml
docs/fusion/                 SCAFFOLD.md, CAP-NNN.md, i18n-map.json
```

A capability's **module** is `feature/<domain>/src/main/java/<package>/<capability>/` plus its test folder.

## Architecture

ViewModels with `StateFlow`, Hilt for DI, Room or DataStore only where CONTINUITY.md needs local data, and
EncryptedSharedPreferences or the KeyStore for tokens. `res/values*/strings.xml` for every required locale, with
legacy keys mapped in `docs/fusion/i18n-map.json`.

## Tests with JUnit output

Gradle writes JUnit XML natively, to `<module>/build/test-results/test<Variant>UnitTest/TEST-*.xml`. Run
`./gradlew :feature:<domain>:testDebugUnitTest`, then copy that run's XML files into a fresh run folder
(`RUN=$(python3 "${CLAUDE_PLUGIN_ROOT}/scripts/evidence.py" dir <program> suite <CAP>)`) and record the folder. Never
point `evidence.py` at Gradle's own folder: it keeps results from earlier runs.

**Ids in names:** Kotlin backtick names keep them: ``@Test fun `RULE-017 rounds to cents`()`` in a class
`CAP012MileageTest`.

**Clean for verify:** `./gradlew clean`, then the full `test` task.

## Run and screenshot

- `./gradlew :app:installDebug` on a running emulator (`emulator -avd <name>`).
- Maestro flows use `appId: <applicationId>`.
- Screenshots: `adb exec-out screencap -p > <png>`.
