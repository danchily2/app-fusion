# Inventory: me-ios

Employee · ios-native · commit `a3600e7d6d89` (shallow clone) · generated 2026-09-28T19:32:43+00:00

Every number below comes from `scripts/inventory.py` and is printed with the rule that produced it. Two numbers made by different rules are different facts: quote the rule with the number.

## Counts

| What | Count | Rule |
| --- | --- | --- |
| sourceFiles | 2066 | non-test .swift, .m and .h files, generated and vendored directories excluded |
| screens | 116 | UIKit view controllers (a class whose superclass ends in ViewController, or ObjC @interface of one) plus TCA features (@Reducer types), outside test paths |
| uikitControllers | 28 | classes whose superclass name ends in ViewController, TableViewController, CollectionViewController, HostingController or PageViewController |
| tcaFeatures | 88 | struct or enum declarations annotated @Reducer |
| swiftuiViews | 291 | structs conforming to View (every View, not only screens) |
| coordinators | 88 | type declarations (class, struct, protocol, enum, actor) whose name contains 'Coordinator', outside test paths |
| requestTypes | 107 | struct/class/enum declarations conforming to a protocol ending in 'Request', in files that mention APIClientRequest |
| endpoints | 85 | distinct normalized paths from resourceName/path/endpoint properties, let-path literals and URL(string:)/appendingPathComponent calls; \(constant) interpolations resolved when the constant has one literal value |
| events | 185 | distinct case names (or raw values) of enums whose name ends in Event, Events, Analytics, AnalyticsEvent or TrackingEvent, plus string literals passed to logEvent/trackEvent/track |
| stringKeys | 927 | keys in .xcstrings catalogs plus keys of .strings files in *.lproj folders (union of locales) |
| locales | 5 | locales present in any string catalog |
| storageKeys | 40 | UserDefaults forKey literals, @AppStorage keys, Realm and SwiftData model classes, Core Data entities, and one row per file using Keychain APIs (one row per distinct kind and key) |
| webLinks | 8 | absolute http(s) URLs opened with URL(string:) outside request types whose path has no /api/, /vN/, /rest/ or /graphql segment (help, legal and marketing pages) |
| testFiles | 1236 | .swift files on test paths |
| maestroFlows | 0 | YAML files containing an appId: header and at least one Maestro command |
| packages | 38 | local Package.swift manifests |
| dependencies | 54 | distinct remote packages pinned in Package.resolved or Podfile.lock |
| targets | 3 | PBXNativeTarget entries in every .xcodeproj except Pods |
| code | 284586 | scc: code lines per language, generated and vendored directories excluded; summed over programming languages only (JSON, YAML, Markdown and other data formats are listed, not counted) |

## Languages

| Language | Files | Code lines |
| --- | --- | --- |
| Swift | 3300 | 284271 |
| JSON | 782 | 96764 |
| Markdown | 80 | 12759 |
| Plain Text | 53 | 4248 |
| YAML | 22 | 1402 |
| Shell | 7 | 202 |
| SVG | 53 | 192 |
| Properties File | 1 | 152 |
| Python | 1 | 113 |
| HTML | 1 | 10 |
| Gemfile | 1 | 7 |
| Objective C | 2 | 6 |

## Strings

927 keys in `xcstrings` (Employee/InfoPlist.xcstrings, Employee/Localizable.xcstrings); source locale `en`.

| Locale | Keys | Missing |
| --- | --- | --- |
| en | 927 | 0 |
| da-DK | 922 | 5 |
| fi-FI | 922 | 5 |
| nb-NO | 922 | 5 |
| sv-SE | 922 | 5 |

## Platform

| Fact | Value |
| --- | --- |
| Bundle / application ids | com.visma.Employee, com.visma.Employee.expense-share-extension, com.visma.vme.payslip, com.visma.vme.payslip.expense-share-extension |
| Minimum OS | ios 18.0 |
| Push | True |
| URL schemes | vismame, vismamedev |
| Associated domains (iOS) | applinks:static.mobileemployee.visma.net, webcredentials:static.mobileemployee.visma.net, applinks:static.mobileemployee.stag.visma.net, webcredentials:static.mobileemployee.stag.visma.net |
| App groups | group.com.visma.vme.payslip.shared, group.com.visma.Employee.shared |
| Privacy manifests | Employee/PrivacyInfo.xcprivacy, ExpenseShareExtension/PrivacyInfo.xcprivacy |
| Permissions | NSCameraUsageDescription, NSFaceIDUsageDescription, NSLocationWhenInUseUsageDescription, NSMicrophoneUsageDescription, NSPhotoLibraryAddUsageDescription, NSPhotoLibraryUsageDescription, NSSpeechRecognitionUsageDescription |
| Extensions | share (ExpenseShareExtension/Info.plist) |
| Targets | ExpenseShareExtension (extension), Employee (app), EmployeeTests (unit-tests) |

## Screens by area

| Area | Screens |
| --- | --- |
| Modules | 98 |
| Employee | 17 |
| ExpenseShareExtension | 1 |

## Endpoints by prefix

| Prefix | Call sites |
| --- | --- |
| employee/api | 96 |

## Analytics events by family

| Family | Entries |
| --- | --- |
| Event | 159 |
| ObserverEvent | 8 |
| PasscodeLockEvent | 6 |
| Analytics | 4 |
| CostUnitsEvent | 3 |
| ReceiptsSyncEvent | 3 |
| LockEvents | 2 |
| ProjectAccountingEvent | 2 |
| SurvicateTriggerEvent | 1 |

## Storage

| Kind | Distinct keys |
| --- | --- |
| realm-model | 37 |
| keychain | 3 |

## Tests

Frameworks: SnapshotTesting, Swift Testing, XCTest. Unit test files: 1236. UI test files: 0. Maestro flows: 0.

## What this scan cannot see

- Endpoints built at runtime (HATEOAS links, server-provided URLs, string concatenation across functions) are not visible to this scan.
- SwiftUI views are listed separately because most are sub-views, not screens; the map step decides which are screens.
