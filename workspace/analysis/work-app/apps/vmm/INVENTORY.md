# Inventory: vmm

Manager · react-native · commit `342cb745f66b` · generated 2026-09-28T19:33:13+00:00

Every number below comes from `scripts/inventory.py` and is printed with the rule that produced it. Two numbers made by different rules are different facts: quote the rule with the number.

## Counts

| What | Count | Rule |
| --- | --- | --- |
| sourceFiles | 1424 | non-test .ts/.tsx/.js/.jsx files outside ios/, android/ and generated or vendored directories |
| routes | 73 | distinct route names (the constant when the name is a constant, else the literal) registered in a <X.Screen name=...> element |
| routeSites | 79 | every <X.Screen name=...> element (one route can be registered in several navigators) |
| screens | 63 | distinct component files registered as a route's component (resolved through the file's imports, tsconfig paths and babel aliases), navigators excluded |
| screenDirFiles | 171 | .tsx/.jsx files under screens/ or src/screens/ (a cross-check, not a screen count) |
| endpoints | 93 | distinct normalized paths from url: properties, RTK Query query: string returns, axios-style <client>.get/post/put/patch/delete calls, fetch() literals and url/path/endpoint variable assignments, in non-test, non-mock files; ${CONSTANT} templates resolved |
| graphqlOperations | 35 | distinct named queries, mutations and subscriptions in gql`` tags and .graphql files |
| events | 311 | distinct wire values of top-level members of *_EVENTS objects (when no catalog exists: distinct literals passed to logEvent/trackEvent/logScreenView) |
| eventCatalogMembers | 313 | top-level members of *_EVENTS objects (two members may share a wire value) |
| eventCallsOutsideCatalog | 48 | distinct literals passed to logEvent/trackEvent/logScreenView that are not a catalog wire value |
| navigators | 6 | route components whose file itself registers routes or creates a navigator (nested stacks and tabs) |
| dynamicRouteSites | 1 | <X.Screen> elements whose name is an expression (route.name, a map over a list), not counted as routes |
| stringKeys | 2158 | keys (nested keys flattened with '.') in i18n JSON catalogs, union of locales |
| locales | 6 | locale files or folders in the i18n catalog |
| storageKeys | 12 | AsyncStorage/MMKV keys (literals, or constants resolved to their literal), redux-persist keys and whitelisted slices, one row per file using keychain or secure-store APIs (one row per distinct kind and key) |
| webLinks | 1 | absolute http(s) URLs passed to Linking.openURL, InAppBrowser.open or openBrowserAsync (help, legal and marketing pages) |
| flags | 15 | distinct remote-config keys read with getValue/getBoolean/getString/getNumber in files that mention remoteConfig |
| testFiles | 556 | files on test paths (__tests__, *.test.*, *.spec.*, mocks, msw handlers) |
| maestroFlows | 10 | YAML files under a maestro folder with an appId: header |
| packages | 62 | runtime dependencies that are React Native native modules (react-native-*, @react-native-*, @react-native-firebase/*, expo-*, ...) |
| dependencies | 109 | runtime dependencies in package.json |
| targets | 4 | native targets in ios/*.xcodeproj plus AndroidManifest.xml files under android/*/src/main |
| code | 218386 | scc: code lines per language, generated and vendored directories excluded; summed over programming languages only (JSON, YAML, Markdown and other data formats are listed, not counted) |

## Languages

| Language | Files | Code lines |
| --- | --- | --- |
| TypeScript | 1897 | 211235 |
| JSON | 58 | 54171 |
| Markdown | 172 | 33355 |
| YAML | 43 | 5513 |
| JavaScript | 74 | 5195 |
| SVG | 268 | 1575 |
| Plain Text | 18 | 1231 |
| Shell | 21 | 825 |
| XML | 29 | 584 |
| JSONL | 10 | 576 |
| Kotlin | 7 | 463 |
| TypeScript Typings | 7 | 358 |

## Strings

2158 keys in `i18n-json` (src/assets/i18n/da.json, src/assets/i18n/en.json, src/assets/i18n/fi.json, src/assets/i18n/nl.json, src/assets/i18n/no.json, src/assets/i18n/sv.json); source locale `en`.

| Locale | Keys | Missing |
| --- | --- | --- |
| da | 1672 | 486 |
| en | 2152 | 6 |
| fi | 1672 | 486 |
| nl | 1672 | 486 |
| no | 1672 | 486 |
| sv | 1672 | 486 |

## Platform

| Fact | Value |
| --- | --- |
| Bundle / application ids | com.visma.vmm, com.visma.vmm.VmmNotificationContent, com.visma.vmm.VmmNotificationService, com.visma.vmm.develop |
| Minimum OS | ios 15.1, android 24 |
| Push | True |
| URL schemes | vismamanager |
| Associated domains (iOS) | applinks:visma-manager.web.app, webcredentials:visma-manager.web.app |
| App link hosts (Android) | visma-manager.web.app |
| App groups | group.com.visma.vmm |
| Background modes | fetch, processing, remote-notification |
| Queried schemes | bankid, itms-apps, netvisor-app |
| ATS exceptions | NSAllowsLocalNetworking (ios/vmm/Info.plist) |
| Privacy manifests | ios/PrivacyInfo.xcprivacy |
| Permissions | NSCalendarsFullAccessUsageDescription, NSCalendarsUsageDescription, NSMicrophoneUsageDescription, NSPhotoLibraryUsageDescription, NSSpeechRecognitionUsageDescription, android.permission.INTERNET, android.permission.USE_FINGERPRINT, android.permission.VIBRATE, android.permission.READ_CALENDAR, android.permission.WRITE_CALENDAR, android.permission.NEARBY_WIFI_DEVICES, android.permission.WRITE_EXTER… |
| Extensions | notification-content (ios/VmmNotificationContent/Info.plist), notification-service (ios/VmmNotificationService/Info.plist) |
| Targets | vmm (app), VmmNotificationContent (extension), VmmNotificationService (extension) |
| Exported components | activity .MainActivity, activity net.openid.appauth.RedirectUriReceiverActivity |
| Remote-config flags | use_snowplow, feature_user_testing_phase, ai_approval_history_system_prompt, ai_approval_history_actions_prompt, ai_approval_system_prompt, ai_approval_actions_prompt, perf_monitoring_enabled, feature_app_rate_run_until, feature_app_rate_show_after_actions, feature_app_rate_reshow_after_dismiss, feature_app_rate_enabled, feature_whats_new_v1, feature_wootric_enabled, feature_wootric_show_after_ac… |

## Screens by area

| Area | Screens |
| --- | --- |
| manager | 18 |
| hrm | 12 |
| common | 10 |
| components | 7 |
| UserTestingRecruitment | 4 |
| autopay | 3 |
| osr | 3 |
| gaia | 2 |
| EmployeeCalendarScreen | 1 |
| FeedbackScreen | 1 |
| StartScreen | 1 |
| TimelineScreen | 1 |

## Endpoints by prefix

| Prefix | Call sites |
| --- | --- |
| approval/rest | 25 |
| dialogue/companies | 21 |
| org/{} | 10 |
| api/v1 | 9 |
| autopay/transactions | 8 |
| users/{} | 5 |
| compello/tenants | 5 |
| api/v2 | 4 |
| devices/{} | 3 |
| survey/user | 3 |
| employee/companies | 3 |
| approval/task | 2 |
| financials/validate | 2 |
| devices/all | 2 |
| approval/process | 2 |
| autopay/transaction | 2 |
| employee/api | 2 |
| osr/context | 2 |
| osr/dashboards | 2 |
| hrm/anniversary | 2 |
| openai/deployments | 1 |
| keys/airtabletoken | 1 |
| v0/appuyx2tqe6ium1pb | 1 |
| autopay/overview | 1 |
| gui/layout | 1 |

## Analytics events by family

| Family | Entries |
| --- | --- |
| APPROVAL_EVENTS | 115 |
| call | 60 |
| HRM_EVENTS | 44 |
| AUTOPAY_EVENTS | 39 |
| APP_EVENTS | 33 |
| GAIA_EVENTS | 29 |
| DIALOGUE_EVENTS | 16 |
| BNXT_ORDERS_EVENTS | 14 |
| START_EVENTS | 10 |
| OSR_EVENTS | 9 |
| NAVIGATION_EVENTS | 4 |

## Storage

| Kind | Distinct keys |
| --- | --- |
| asyncstorage | 11 |
| keychain | 1 |

## Tests

Frameworks: Jest, React Native Testing Library, Maestro. Unit test files: 556. UI test files: 0. Maestro flows: 10.

## Native modules

`@react-native-async-storage/async-storage` ^2.2.0, `@react-native-clipboard/clipboard` ^1.16.3, `@react-native-community/hooks` ^100.1.0, `@react-native-community/netinfo` ^12.0.1, `@react-native-community/push-notification-ios` ^1.11.0, `@react-native-firebase/analytics` ^25.1.0, `@react-native-firebase/app` ^25.1.0, `@react-native-firebase/crashlytics` ^25.1.0, `@react-native-firebase/in-app-messaging` ^25.1.0, `@react-native-firebase/messaging` ^25.1.0, `@react-native-firebase/perf` ^25.1.0, `@react-native-firebase/remote-config` ^25.1.0, `@react-native-masked-view/masked-view` ^0.3.0, `@react-native-voice/voice` patch:@react-native-voice/voice@npm%3A3.2.4#~/.yarn/patches/@react-native-voice-voice-npm-3.2.4-10115bd137.patch, `@react-native/babel-preset` 0.86.2, `@sentry/react-native` ^8.22.0, `react-native-animatable` ^1.4.0, `react-native-app-auth` patch:react-native-app-auth@npm%3A8.4.1#~/.yarn/patches/react-native-app-auth-npm-8.4.1-6859698b6b.patch, `react-native-background-fetch` ^4.2.7, `react-native-blob-util` ^0.24.10, `react-native-bootsplash` 7.3.2, `react-native-calendar-events` ^2.2.0, `react-native-calendars` ^1.1314.0, `react-native-dashed-line` ^1.1.0, `react-native-date-picker` patch:react-native-date-picker@npm%3A5.0.13#~/.yarn/patches/react-native-date-picker-npm-5.0.13-e35e950566.patch, `react-native-device-country` ^2.0.1, `react-native-device-info` ^11.1.0, `react-native-dotenv` ^4.1.1, `react-native-gesture-handler` patch:react-native-gesture-handler@npm%3A2.32.0#~/.yarn/patches/react-native-gesture-handler-npm-2.32.0-22bae10265.patch, `react-native-get-random-values` ^1.11.0, `react-native-haptic-feedback` ^2.3.0, `react-native-image-crop-picker` ^0.51.1, `react-native-image-pan-zoom` ^2.1.12, `react-native-image-zoom-response` ^0.0.1, `react-native-images-to-pdf` patch:react-native-images-to-pdf@npm%3A0.2.1#~/.yarn/patches/react-native-images-to-pdf-npm-0.2.1-a52d1bf9dc.patch, `react-native-inappbrowser-reborn` ^3.7.1, `react-native-keyboard-aware-scroll-view` ^0.9.5, `react-native-keyboard-controller` ^1.22.4, `react-native-keychain` ^10.0.0, `react-native-loading-spinner-overlay` ^3.0.1, `react-native-mmkv` ^4, `react-native-network-logger` ^2.0.1, `react-native-nitro-modules` ^0.36.5, `react-native-notify-kit` ^10.5.0, `react-native-pager-view` ^9.0.4, `react-native-pdf` ^7.0.5, `react-native-permissions` 5.6.1, `react-native-reanimated` ^4.5.3, `react-native-render-html` ^6.3.4, `react-native-safe-area-context` ^5.9.1, `react-native-screens` ^4.27.0, `react-native-share` ^12.3.1, `react-native-snow-bg` https://github.com/danchily2/react-native-snow-bg.git#main, `react-native-svg` ^15.15.5, `react-native-switch-selector` ^2.2.1, `react-native-tab-view` ^4.3.2, `react-native-tiff-converter` 0.0.77, `react-native-toast-message` ^2.4.0, `react-native-url-polyfill` ^4.0.0, `react-native-vector-icons` ^10.3.0, `react-native-webview` ^13.16.0, `react-native-worklets` 0.11.4

## What this scan cannot see

- Routes registered with the static navigation API (createXNavigator({screens: {...}})) or built dynamically are not counted.
- Endpoint paths are relative to whichever base URL the client adds; the parity check matches them by path suffix.
- 1 route(s) name a component that could not be resolved to a file (inline render or re-export).
