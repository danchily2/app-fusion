# work-app: assessment

Generated 2026-09-28 by `fuse-assess`. Sources: vmm (Manager) `develop @ 342cb745f66b`, me-ios (Employee)
`development @ a3600e7d6d89` (shallow clone, so there are no history signals). Counts come from `scripts/inventory.py`
(`apps/<app>/INVENTORY.md`) and `overlap.json`. Descriptions come from six read-only analyst passes: structure, debt and
security for each app. Citations are `path:line`, relative to `legacy/<app>`. Credentials are masked, and the details
are in `SECRETS.local.md`.

## 1. Executive summary

**Manager (vmm)** is a React Native app for iOS and Android. Managers and approvers at Nordic and Dutch Visma customers
use it to approve invoices, workflow tasks and AutoPay payments, handle HR work (employees, dialogues, anniversaries),
read OSR dashboards and work with Business NXT orders, with an AI assistant ("Gaia") across all of it. **Employee
(me-ios)** is a native Swift iOS app. Employees use it for payslips, expenses (receipts, mileage, allowances), calendar
(absence, time, check-in), Dottie HR and personal information, with its own AI assistants. They are about the same size:
218k code lines against 285k (scc, programming languages only). Manager has 63 screens (components registered as
routes) and Employee has 116 (view controllers plus TCA reducers), so the two screen counts come from different rules.
They overlap very little: **5 shared backend endpoints** out of 52 and 85 (normalized paths that match by suffix, with the
same method), all of them session, configuration, Dottie employee or feedback calls, and **122 shared UI strings**
(identical source-locale values of at least 4 characters). Both codebases are well tested but carry heavy structural
debt: four network stacks in Manager, two DI systems and a half-finished UIKit-to-TCA migration in Employee. **The
headline recommendation is a greenfield app that ports capabilities from both.** Neither codebase covers most of the
other's capabilities, and neither is a clean base.

## 2. Side by side

Each rule is abbreviated here. The full rule is in each `INVENTORY.md`. A row whose rules differ between the apps
compares different facts, so read it as orientation, not as a ratio.

| Count | vmm (Manager) | me-ios (Employee) | Rule |
|---|---|---|---|
| Screens | 63 | 116 | vmm: distinct component files registered as a route's component, navigators excluded. me-ios: UIKit view controllers (28) plus TCA `@Reducer` types (88). **Different rules** |
| Routes | 73 | n/a | vmm: distinct route names in `<X.Screen name=…>`. Coordinators do the routing in me-ios (88 coordinator types) |
| Endpoints | 52 (+35 GraphQL ops) | 85 | Distinct normalized paths in non-test code. **Both are undercounts.** vmm misses the AutoPay and OSR REST paths built with `${apiBase.getBaseUrl()}` in axios `makeRequest`. me-ios misses server-provided HATEOAS action URLs (empty `resourceName`) |
| Analytics events | 311 | 185 | vmm: wire values of `*_EVENTS` members (plus 48 literals outside the catalog). me-ios: case names of `*Event(s)`/`*Analytics` enums plus literals passed to track calls |
| String keys | 2158 | 927 | Keys in i18n catalogs, union of locales (vmm: flattened JSON; me-ios: `.xcstrings`) |
| Locales | 6 (da, en, fi, nl, no, sv) | 5 (en, da-DK, fi-FI, nb-NO, sv-SE) | Locale files or folders in the catalog |
| Missing translations | 486 per non-English locale | 5 per non-English locale | Source-locale keys absent from that locale |
| Storage keys | 12 (11 AsyncStorage, 1 Keychain) | 40 (37 Realm models, 3 Keychain) | Storage keys, persisted slices and models, plus one row per file that uses keychain APIs. vmm's persisted Redux state lives in encrypted MMKV, which this count does not itemize |
| Test files | 556 | 1236 | vmm: files on test paths, including mocks and msw handlers. me-ios: `.swift` files on test paths |
| Maestro flows | 10 | 0 | YAML under a maestro folder with an `appId:` header |
| Code lines | 218,386 (TypeScript 211k) | 284,586 (Swift 284k) | scc, programming languages only, generated and vendored code excluded |
| Dependencies | 109 runtime (62 native modules) | 54 remote SPM pins, 38 local packages | package.json runtime deps / Package.resolved |
| Remote-config flags | 15 (Firebase RC) | 2 (LaunchDarkly, per the debt pass) | vmm: keys read with `getValue`/`getBoolean`/… |
| Min OS | iOS 15.1, Android 24 | iOS 18.0 | Build settings / manifest |

## 3. Each app

### 3.1 vmm: Manager (React Native, iOS + Android)

**Purpose and users.** Managers and approvers. Tabs are built at runtime from the user's roles
(`src/configs/navConfig/navConfig.tsx:50-57,91-96`), and a user with no roles lands in `NoRolesStack` (`:184`).

**Areas**

| # | Area | Screens (nav file) | Endpoints / backend |
|---|---|---|---|
| 1 | Auth / login | LoginSelect, WebviewModal (`src/configs/navConfig/auth/AuthNavConfig.tsx:16-26`) | Visma Connect OIDC with PKCE, client `vismamanager` (`src/services/apiManagerConnect/apiManagerConnect.ts:59,100-121`) |
| 2 | Approval (invoices, workflow tasks) | Approval, ApprovalTask, ProcessTask, Voucherlines, Compello lines, financial lines editor (`ApprovalNavConfig.tsx:63-173`) | `approval/rest/my-tasks`, `tasks/{id}/approve\|reject\|forward\|review` (`queryEndpointsApproval.ts:315-339`); `financials/*`; Compello posting lines |
| 3 | AutoPay (payment approval) | Home, InvoiceDetails, OverviewDetails, WarningsOverview, ApproveTransaction (`AutopayNavConfig.tsx:43-86`) | `autopay/transaction/*` (`src/services/apiAutopay/apiAutopay.ts:55-312`), BankID/2FA via WebView |
| 4 | HRM: employees | HrmScreen, EmployeeDetail, DottieEmployeeDetail, edit personal/address/child/emergency, EmployeeCalendar (`HrmNavConfig.tsx:106-190`) | `employee/companies/employees`; `api/v2/dottie/employee/{id}` on `mobileemployee.visma.net` (the Employee backend) |
| 5 | HRM: dialogues and wage runs | DialogueDetails, Create, Splits (`HrmNavConfig.tsx:221-266`) | `dialogue/companies/{c}/dialogues/…` (`queryEndpointsDialogue.ts`, 1977 lines) |
| 6 | Anniversary bot | HrmBotGenerateMessage, GeneratingFinished (`CommonScreensNavConfig.tsx:391-400`) | `hrm/anniversary` |
| 7 | OSR financial dashboards | Dashboard, ElementDetails, CustomerTenant (`OsrNavConfig.tsx:36-65`) | `osr/context`, `osr/dashboards/*` (`src/services/apiOSR/apiOSR.ts:24-157`) |
| 8 | Business NXT | 13 screens: Hub, Orders, OrderCreate, Money, OpenEntries… (`BnxtOrdersNavConfig.tsx:79-229`) | GraphQL `business.visma.net/api/graphql` (Apollo); dark-shipped behind a dev-tools flag (`navConfig.tsx:55-57`) |
| 9 | Gaia AI assistant | GaiaChat, ChatHistory, Conversations, Capabilities (`CommonScreensNavConfig.tsx:320-351`) | `api.assistant.vsn.dev` conversations / agent threads (AG-UI streaming) |
| 10 | Start / home and search | StartScreen, HomeSearch | Aggregates the other areas |
| 11 | Settings, feedback, surveys, user testing | Settings, ToS, Licenses, Privacy, DevTools, Feedback, 4 UserTesting screens | `keys/{name}`, Survicate, Wootric, Airtable, Seatable |

**Architecture.**

- **Navigation.** React Navigation 7 with a login gate and a custom bottom tab bar of native stacks. There is no
  `linking` config (`navConfig.tsx:177-188`).
- **State.** Redux Toolkit (`createReducer`) with side effects in redux-observable epics.
- **API layer.** Four stacks run side by side: RTK Query, legacy axios-observable services, Apollo, and AG-UI
  streaming.
- **Persistence.** A custom engine writes whitelisted slices to **encrypted MMKV**, with the seed in the Keychain
  (`src/configs/persistEngine.ts:71-73`).
- **DI.** None. Services use module singletons such as `storeWrapper` (`src/configs/reduxState.ts:170`).

**Platform features users depend on.**

- **Push.** FCM with Notifee action buttons. The standout is **replying to an HR dialogue from the notification**
  (`src/hooks/useNotificationEventHandlers.ts:298-321`). There are two iOS notification extensions, Service and Content,
  with custom approval and anniversary layouts (`ios/VmmNotificationContent/NotificationViewController.swift:99,143`).
- **Links.** Universal and app links on `visma-manager.web.app` serve only as OIDC login and logout callbacks. There are
  no in-app deep links.
- **Other.** BankID scheme query for AutoPay 2FA, device calendar sync, voice input for Gaia, and shake to report.
- **Background fetch looks vestigial.** Native code wires it (`ios/vmm/AppDelegate.mm:78`), but no JS configures it.
  The background push refresh never runs, because `index.js:44` reads the store without `getState()`.
- **Biometrics.** Not used.

### 3.2 me-ios: Employee (Swift, iOS only)

**Purpose and users.** Employees of companies on Visma.net Payslip, Expense and Calendar. Tabs are built from
server-side permissions (`Employee/TabbarUI/TabbarCoordinator.swift:57-70`). One person can be signed in to **several
accounts and companies** at the same time.

**Areas**

| # | Area | Screens / code | Representative endpoints (`/employee/api/v1\|v2/…`) |
|---|---|---|---|
| 1 | Sign-in, accounts, session | `Employee/Accounts/Feature/{Login,AccountManager,UserAccounts}` | Visma Connect (`EmployeeServices/EmployeeAPI/Sources/EmployeeAPI/APIConstants.swift:21-50`); `authorization/currentSession` |
| 2 | Start page (cards, tasks, check-in) | `Employee/StartPage/StartPageViewController.swift` (1342 lines) | Aggregates; `surveys` |
| 3 | Payslips and year-end reports | `Modules/PayslipsFeature/…` | `employees/{id}/payslips`, `Payslip/Export`, `payslips/exportFromAllTenants`, `employees/allreports` |
| 4 | Expenses: receipts, claims, mileage, allowances, climate report | `Modules/EmployeeExpenses/…` | About 40 requests: `expense/inbox`, `expense/claims`, `mileages/calculateRoadToll`, ML `predictExpenseType`, `maps/directions` |
| 5 | Calendar: absence, time, balances, check-in | `Modules/CalendarFeature/…` (UIKit plus TCA), `Employee/CalendarLeftover/` | `employees/{id}/calendar`, `calendar/workshift`, `absenceregistration`, `calendar/checkin` |
| 6 | AI assistants (payslip bot, calendar bot) | `Modules/EmployeeChatBot/…` | `employeeassistant/chat`, `chatbot/predictCalendarRegistration` |
| 7 | Dottie HR: profile, colleagues, documents, benefits | `Modules/DottieFeature/…` | 18 `v2/dottie/…` requests |
| 8 | Personal information, including bank account | `Modules/PersonalInformation/…` | `employees/{id}/EmpMan/employees/me` |
| 9 | Inbox messages and notifications | `Modules/InboxMessages/…` | `notification/inbox/items`, `notification/RegisterDevice` |
| 10 | Settings, security, FAQ, feedback | `Employee/Settings`, `Employee/Security/{Passcode,Biometric}` | `org/{orgId}/license/{featureId}`, `feedback` |
| 11 | Remote control (forced update, banners) | `Modules/RemoteControl/…` | `remoteControl/config`, `v2/Configuration/third-party-keys` |
| 12 | Share extension: receipt capture | `ExpenseShareExtension/ShareReceiptCoordinator.swift:76-326` | Expense requests |

**Architecture.**

- **Navigation.** A UIKit coordinator tree: Root, then Main, then Tabbar (`Employee/SceneDelegate.swift:107-116`).
- **State.** Hybrid. There are 88 TCA features hosted in coordinators and 28 UIKit/MVVM controllers. The team's rule is
  that new code uses TCA.
- **API layer.** `APIClientRequest` structs on Alamofire, plus HATEOAS action links for many writes
  (`EmployeeServices/Calendar/Sources/Calendar/Request/Absence/UpdateAbsence.swift:25-31`).
- **Persistence.** **Encrypted Realm** with 37 models, and the key in the Keychain. The passcode repository is also
  here.
- **DI.** Swinject and SwinjectStoryboard (`Employee/AppDependencies.swift`, 1495 lines, 162 registrations) run
  alongside TCA `@Dependency`.
- **Modules.** 38 local SwiftPM packages.
- **Third-party SDK keys.** They come from the backend at runtime, not from the repo.

**Platform features users depend on.**

- **Push.** Four event types (`Employee/PushNotifications/PushNotificationHandlingService.swift:20-30`): new payslip,
  new year-end report, timesheet reminder, generic. Registration is per account (`MultiAccountPushManager`).
- **Share extension.** Receipt capture from Photos or Files. It shares tokens and the Realm key through app group
  `group.com.visma.vme.payslip.shared`.
- **App lock.** Face ID plus a custom passcode, triggered after 15 s in the background, and an app-switcher blur
  (`Employee/SceneDelegate.swift:75-95`).
- **Other permissions.** Camera with receipt crop (WeScan fork), location for mileage (Google Maps and Places), and
  voice for the assistant.
- **Deep links are stubbed.** `scene(_:openURLContexts:)` is empty (`SceneDelegate.swift:98-99`). The associated domains
  exist for the OAuth callback.
- **Background modes.** None.

## 4. Overlap

- **Shared backend endpoints (5).** Rule: normalized paths match by segment suffix and the methods agree.

  | vmm | me-ios |
  |---|---|
  | `GET /api/v1/authorization/currentsession` | `GET /employee/api/v1/authorization/currentsession` |
  | `GET /api/v2/configuration/third-party-keys` | `GET /employee/api/v2/configuration/third-party-keys` |
  | `GET /api/v2/dottie/employee/{}` | `GET /employee/api/v2/dottie/employee/me` |
  | `GET /api/v2/dottie/employees/possible-quick-filters` | `GET /employee/api/v2/dottie/employees/possible-quick-filters` |
  | `POST /employee/api/v1/feedback` | `POST /employee/api/v1/feedback` |

  The products already meet on **the Mobile Employee backend (`mobileemployee.visma.net`) and Dottie HR**. Manager calls
  the Employee API for the session, third-party keys, Dottie employee detail and feedback. Everything else Manager does
  (approval, AutoPay, dialogue, OSR, Business NXT, Gaia) runs on other backends. So a merged app talks to at least
  six backend families, and the Mobile Employee API is the natural shared core.
- **Shared UI copy.** 122 distinct source-locale strings (normalized, at least 4 characters) appear in both apps, out of
  1836 in vmm and 839 in me-ios.
- **Locales.** Both apps have da, en, fi, nb/no and sv. Only vmm has **nl**. The union is 6 languages, and the new app
  must keep nl for Manager's Dutch users. vmm has 486 keys missing in each non-English locale, so it ships
  English fallbacks today.
- **Design system and packages.** Nothing is shared. Employee has `Modules/EmployeeUIComponents`, and Manager has
  in-app themes (`AppTheme.tsx`) with styled-components. Both use Firebase, Snowplow and Survicate, and each also has
  vendors of its own: Sentry, Wootric, Airtable and Seatable in vmm; LaunchDarkly and Google Maps in me-ios.
- **Identity.** Both apps sign in with Visma Connect OIDC and PKCE, but they use different client IDs and different
  callback domains.

## 5. Platform surface

The full matrix of 44 items is in `PLATFORM.md`. These items exist in only one app, and each needs a decision in
`fuse-review`:

| Item | Only in | Why it matters |
|---|---|---|
| Notification Service and Content extensions (PLT-006/007) | vmm | Rich approval and anniversary notifications, and dialogue reply from the notification |
| Share extension (PLT-008) | me-ios | Receipt capture from other apps, a core expense flow |
| Background modes `fetch`, `processing`, `remote-notification` (PLT-009) | vmm | Mostly vestigial (see 3.1), but `remote-notification` supports push refresh |
| URL schemes `vismamanager` vs `vismame`/`vismamedev` (PLT-005) | each | Both are OAuth leftovers or callbacks. The security pass advises dropping `vismamanager` |
| Associated domains `visma-manager.web.app` vs `static.mobileemployee.visma.net` (PLT-004) | each | OAuth callbacks. AutoPay 2FA also redirects through `visma-manager.web.app` |
| App groups `group.com.visma.vmm` vs `group.com.visma.vme.payslip.shared` (PLT-033) | each | Existing tokens, the Realm key and Realm data live in me-ios's group. Continuity depends on it |
| Calendar permission (PLT-010/011), BankID scheme query | vmm | Calendar sync and AutoPay 2FA |
| Camera, location, Face ID (PLT-012–014) | me-ios | Receipts, mileage, app lock |
| Android permissions (PLT-019–032) | vmm | Only vmm is on Android today, and `QUERY_ALL_PACKAGES` and `WRITE_EXTERNAL_STORAGE` need justification |
| Min OS: iOS 15.1 vs 18.0 (PLT-002) | each | The new app's floor decides who can upgrade |
| Remote config: Firebase RC (15 keys) vs LaunchDarkly | each | Pick one flag system |
| Legacy bundle ID `com.visma.vme.payslip` | me-ios | Probably Employee's App Store ID. It constrains the store-listing decision |

## 6. Technical debt and inherited risks

The credentials are listed, masked, in **`SECRETS.local.md`** (local only; ignored by `analysis/.gitignore`). None of
them is a hard-coded private secret. The Firebase client keys and Sentry DSNs are committed to vmm, the Fastfile
holds a CI keychain password (`te…`), and vmm serves Airtable and Seatable write tokens to devices from the backend.

### vmm: debt (top 8)

1. **Four network stacks, six copy-pasted axios wrappers and three separate 401 paths.** The stacks are in
   `src/services/apiBase.ts:178-208`, `apolloClient.ts:81` and `queryApi.ts:169`. Build one client and one auth
   interceptor, and do not port the RxJS layer.
2. **Environment config hard-coded in 6 places and switchable at runtime.** For example `apiBase.ts:28-37`. `.env` is
   tracked and defaults to stage.
3. **Airtable and Seatable write tokens are served to devices** (`src/services/apiAirtable/apiAirtable.ts:16-27`). Do
   not copy this.
4. **The request error log may keep auth headers and is persisted** (`apiBase.ts:195-205`,
   `src/reducers/featureReducer.ts:196`). A 403 is treated as token expiry, and there are 38 swallow sites.
5. **Global `storeWrapper` is used from services at 136 sites, plus god objects.** Examples are `src/utils/utils.ts`
   (966 lines, imported by 90 files) and `src/hooks/useGaiaChat.ts` (1344 lines).
6. **Deprecated or duplicate dependencies.** These include moment, crypto-js, an RC-pinned redux-observable, an archived
   push-notification-ios, a snow-bg fork on a personal GitHub, 5 yarn patches, and msw and reactotron in runtime
   dependencies.
7. **Duplicate vendors.** Firebase plus Snowplow, Survicate plus Wootric, and Airtable plus Seatable. There are also 48
   event literals outside the catalog.
8. **LLM system prompts are owned by the client and overridable through Remote Config**
   (`src/consts/approvalPrompts.ts`). Do not copy this.

### vmm: inherited security risks (top items; none Critical)

| Sev | CWE | Where | Risk |
|---|---|---|---|
| High | CWE-926/940 | `android/app/src/main/AndroidManifest.xml:60-66`, `MainActivity.kt:43-115`, `src/utils/notifications/dialogueReply.ts:26-62` | The exported `MainActivity` accepts forged "notification action" extras. Another app can post a dialogue reply as the manager |
| Medium | CWE-312/522 | `src/utils/encryption.ts:98-110` | The MMKV key falls back to plaintext AsyncStorage when the Keychain fails, which exposes the tokens |
| Medium | CWE-598 | `apiManagerConnect.ts:473-499` | `id_token_hint` goes to the external browser, and logout counts as a success on any URL |
| Medium | CWE-200 | `ios/GoogleService-Info.plist:16,40` | Committed Firebase config including a Realtime Database URL. The database rules have not been checked |
| Low | CWE-312, 319, 489, 939, 20, 1395 | See the security pass | Push payload stored in plaintext; loopback cleartext allowed in release; Reactotron a runtime dependency; unused OAuth scheme; AutoPay WebView success check uses `includes()`; `yarn npm audit` found 2 critical and 75 high (build tooling), R8 off |

### me-ios: debt (top 8)

1. **Realm deletes local data silently on errors** (`EmployeeServices/EmployeeDatabase/Sources/EmployeeDatabase/RealmService.swift:47,101-106`).
   Unsent receipt drafts exist only on the device. The new app needs a safe one-time import.
2. **Two DI systems with 398 force-unwrapped `resolve(...)!`** (`Employee/AppDependencies.swift`).
3. **God objects.** `ReceiptDetailViewController.swift` has 2780 lines, `ExpenseMileageViewModel.swift` 2348 and
   `StartPageViewController.swift` 1342, and business rules live in UI classes.
4. **Implicit cross-screen refresh through NotificationCenter** (87 uses; `AppMessage` in
   `EmployeeServices/EmployeeResources/Sources/EmployeeResources/AppConstants.swift:12-22`).
5. **The same domain model is written three or more times.** Receipt exists as an API DTO, a Realm object and a mutable
   view model.
6. **Deprecated or abandoned SDKs.** Realm (deprecated by MongoDB), Swinject and SwinjectStoryboard, a WeScan fork,
   OAuthSwift, and unused pins. There are also deprecated SwiftUI APIs, including 18 `NavigationView`.
7. **Hard-coded environment config, switchable through UserDefaults and launch arguments**
   (`EmployeeServices/EmployeeCore/Sources/EmployeeCore/Utils/CoreUtils.swift:110-122`).
8. **A partial migration left behind.** `Employee/CalendarLeftover/` is still wired, there are 48 storyboards and xibs,
   and `fatalError` stands in for abstract methods.

### me-ios: inherited security risks (top items; none Critical)

| Sev | CWE | Where | Risk |
|---|---|---|---|
| High | CWE-288 | `ExpenseShareExtension/ShareReceiptCoordinator.swift:83-96,125` | The share extension skips the app lock. From an unlocked phone, someone can submit receipts as the user |
| Medium | CWE-922 | `EmployeeServices/EmployeeCore/Sources/EmployeeCore/Services/CryptoService/CryptoService.swift:105`, `StorageService.swift:31,43` | Keychain items use `AfterFirstUnlock` without `ThisDeviceOnly`, so tokens and the DB key survive a restore to another device |
| Medium | CWE-459 | `Employee/Services/AppStateService.swift:86-97` | Logout does not wipe the user's Realm DB or its key |
| Medium | CWE-311 | `RealmService.swift:66-68` | Realm encryption fails open, because the key check is an `assert` that is stripped in Release |
| Medium | CWE-603/256 | `Employee/Security/Passcode/Protocols/SecureAppPasscodeRepository.swift:59-73` | The app lock covers only the UI. The PIN is stored unhashed next to the attempt counter |
| Medium | CWE-1104 | `Package.resolved` | Realm is the store for all local PII, and its SDK is deprecated |
| Low | CWE-783, 295, 489, 798 | See the security pass | Operator-precedence bug in the OAuth callback check; no certificate pinning; hidden gesture switches to staging in Release; Fastfile keychain password |

## 7. Fusion strategy (recommendation)

**Recommendation: build a greenfield app and port capabilities from both.** This is a recommendation. The stack itself
is decided in `fuse-brief`, and `INTENT.md` leaves it open.

**Rationale.**

- **Neither app covers most of the other's capabilities.** Only 5 of 52 and 85 endpoints match, and all 5 are
  session, config, Dottie or feedback calls. Beyond sign-in and Dottie HR, the capability sets barely overlap: approval,
  AutoPay, OSR and Business NXT on one side; payslips, expenses and calendar on the other.
- **Growing one app would mean porting roughly half the product into it.** Employee is the larger app, with 285k code
  lines and 116 screens by its own rule. It is iOS-only, so it cannot be the base for an iOS and Android target.
- **Manager is cross-platform, but its debt makes it a poor foundation.** It carries four network stacks, a global store
  singleton used from 136 sites, and Redux plus RxJS epics.
- **There is no design yet**, so most of the UI will be new either way.

**Runner-up.** If the brief picks React Native, vmm's toolchain, CI, Maestro flows and team knowledge carry over well.
That makes "greenfield on vmm's stack, reusing its build pipeline and selected modules" a practical middle path. It is
still not "grow vmm", because its architecture should not be the base.

**A native pair is not indicated.** The platform surface is modest: push, one share extension, notification extensions
and app lock. React Native or a native approach can both deliver it.

**Continuity is the hard part, whatever the strategy.**

- Encrypted MMKV (Manager) and encrypted Realm with unsent receipt drafts (Employee) both need a migration path.
- The two app groups and Keychain tags hold existing sessions.
- The OAuth client IDs and callback domains differ between the apps.
- The store-listing decision is open (two bundle IDs, including the legacy `com.visma.vme.payslip`).

## 8. Documentation gaps

**vmm (Manager)**

1. Which duplicate vendors are live in production: Firebase or Snowplow, Survicate or Wootric, Airtable or Seatable.
   Also the meaning of the 15 Remote Config flags.
2. Whether approving or rejecting from a notification without opening the app is supported. The code logs
   "headlessActionDiscarded". Also whether the `index.js:44` background refresh is meant to work.
3. Which backend owns which area, and the auth header scheme each one expects (Bearer plus `Gsid`, `Gsid-v1` for
   downloads). Base URLs are spread across 6 files.
4. The Business NXT area's status: it is dark-shipped behind a dev-tools flag. Also the Gaia front-end tools, meaning
   which actions the AI may take.
5. The persistence migration chain (legacy redux-persist import, then MMKV, then migrations) and what a replacement app
   must read.

**me-ios (Employee)**

1. The store identity: is the App Store build `com.visma.vme.payslip`, and must the new app keep its app group and
   Keychain tags?
2. The HATEOAS action links: which writes use server-provided URLs, and what their contract is.
3. The multi-account and multi-company model: session lifetime, push per account, and context switching.
4. Which `CalendarLeftover` and UIKit paths are still reachable, and which are migration scaffolding.
5. Whether an **Android Employee app** exists elsewhere. The target includes Android, but only iOS source was provided.
   Also whether Firebase analytics is meant to be permanently off (`Employee/Services/FirebaseService.swift:42-44`).

## Confidence & gaps

- **Model-derived.** The area tables, architecture, debt and security findings come from analyst reads, with medium to
  high confidence each. The counts in section 2 are deterministic.
- **Undercounted endpoints.** Both endpoint counts are low for the reasons given in section 2.
- **Unread files.** Deny rules blocked `legacy/vmm/.env`, `src/consts/backendKeys.ts` and `legacy/me-ios/.mcp.json`.
- **Not run.** No builds ran, and no network checks were made, so the Firebase database rules are unverified.
- **No prompt injection.** Neither repo contained instruction-injection text, although both carry `CLAUDE.md` and
  `.claude/` files.
