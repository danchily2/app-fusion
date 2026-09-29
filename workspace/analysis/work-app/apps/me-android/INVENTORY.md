# Inventory: me-android

Employee · android-native · commit `bdc1335e0f55` (shallow clone) · generated 2026-09-29T06:27:34+00:00

Every number below comes from `scripts/inventory.py` and is printed with the rule that produced it. Two numbers made by different rules are different facts: quote the rule with the number.

## Counts

| What | Count | Rule |
| --- | --- | --- |
| sourceFiles | 1481 | non-test .kt, .java and .kts files, generated and build directories excluded |
| screens | 61 | classes extending *Activity or *Fragment plus @Composable functions named *Screen/*Page/*Route, outside test source sets |
| endpoints | 83 | distinct normalized paths from Retrofit @GET/@POST/@PUT/@DELETE/@PATCH/@HEAD/@HTTP annotations with a literal path, Ktor client calls and OkHttp .url() literals; const val templates resolved |
| events | 0 | distinct string literals passed to logEvent/trackEvent/track |
| stringKeys | 904 | <string> and <plurals> names in res/values*/ XML (union of locales; values-night and other non-locale qualifiers ignored) |
| locales | 1 | values-<locale> folders holding strings (default counts as one) |
| storageKeys | 14 | SharedPreferences and DataStore key literals, Room @Entity classes, one row per file using EncryptedSharedPreferences or the Android KeyStore (one row per distinct kind and key) |
| webLinks | 1 | absolute http(s) URLs passed to Uri.parse/toUri (help, legal and marketing pages) |
| testFiles | 386 | .kt/.java files under src/test or src/androidTest (or other test paths) |
| maestroFlows | 69 | YAML files under a maestro folder with an appId: header |
| packages | 11 | modules named in include(...) of settings.gradle(.kts) |
| dependencies | 18 | distinct group:artifact coordinates in Gradle files and version catalogs |
| targets | 10 | AndroidManifest.xml files under src/main |
| code | 202469 | scc: code lines per language, generated and vendored directories excluded; summed over programming languages only (JSON, YAML, Markdown and other data formats are listed, not counted) |

## Languages

| Language | Files | Code lines |
| --- | --- | --- |
| Kotlin | 1865 | 201089 |
| JSON | 73 | 65604 |
| Markdown | 72 | 11285 |
| XML | 289 | 8299 |
| YAML | 83 | 2939 |
| Gradle | 16 | 1952 |
| Python | 1 | 593 |
| Prolog | 17 | 499 |
| Shell | 6 | 466 |
| HTML | 1 | 328 |
| Groovy | 1 | 235 |
| TOML | 1 | 223 |

## Strings

904 keys in `android-xml` (payslip/src/main/res/values/nav_arguments.xml, translations/src/main/res/values/faq.xml, translations/src/main/res/values/strings.xml); source locale `default`.

| Locale | Keys | Missing |
| --- | --- | --- |
| default | 904 | 0 |

## Platform

| Fact | Value |
| --- | --- |
| Bundle / application ids | com.visma.vme.payslip |
| Push | True |
| URL schemes | vismame |
| Permissions | com.visma.employee.permission.SHOW_NOTIFICATION, android.permission.INTERNET, android.permission.RECORD_AUDIO, android.permission.USE_BIOMETRIC, android.permission.POST_NOTIFICATIONS, android.permission.VIBRATE, android.permission.CAMERA, android.permission.FOREGROUND_SERVICE, android.permission.ACCESS_NETWORK_STATE, android.permission.ACCESS_FINE_LOCATION, android.permission.ACCESS_COARSE_LOCATI… |
| Exported components | activity .home.MainActivity |

## Screens by area

| Area | Screens |
| --- | --- |
| expense | 22 |
| app | 14 |
| absence | 8 |
| payslip | 5 |
| core | 4 |
| dottie | 4 |
| faq | 3 |
| login | 1 |

## Endpoints by prefix

| Prefix | Call sites |
| --- | --- |
| api/v1 | 66 |
| api/v2 | 25 |
| api/directions | 1 |

## Storage

| Kind | Distinct keys |
| --- | --- |
| room-entity | 14 |

## Tests

Frameworks: Compose UI test, JUnit, Kotest, MockK, Robolectric. Unit test files: 386. UI test files: 0. Maestro flows: 69.

## What this scan cannot see

- Endpoints whose path comes from @Url parameters or runtime values have no literal and are not counted.
- Navigation destinations defined in Compose NavHost builders are found only through *Screen composables.
