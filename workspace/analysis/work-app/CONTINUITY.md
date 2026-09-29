# work-app: continuity

How every existing user of **Manager (vmm)** and **Employee (me-ios)** gets into the new app without losing their
sign-in, their data, their notifications or their links. No test in either repository protects this. The brief
(`FUSION_BRIEF.md`) sequences it: its last phase carries it out, and its open questions list every choice below.

Sources: `PLATFORM.md` (PLT ids), `program.json`, `ASSESSMENT.md`, `PREFLIGHT.md`, and the reference checklist
`references/continuity.md`. Facts read from the legacy code for this document are cited `app:path:line`.

**Facts that decide most of this document**

| Fact | vmm (Manager) | me-ios (Employee) | Evidence |
|---|---|---|---|
| Apple team id | `XGSJA98R9R` | `XGSJA98R9R` (the same team) | `DEVELOPMENT_TEAM` in both `project.pbxproj` |
| iOS bundle id (App Store) | `com.visma.vmm` | **`com.visma.vme.payslip`** (AppStore configuration). `com.visma.Employee` is the Debug and Release id | me-ios `Employee.xcodeproj/project.pbxproj`, configuration `AppStore` |
| Android application id | `com.visma.vmm` (`com.visma.vmm.develop` for develop) | none: no Android source was provided | vmm `android/app/build.gradle:129,133` |
| App group | `group.com.visma.vmm` | `group.com.visma.vme.payslip.shared` (App Store), `group.com.visma.Employee.shared` (dev) | PLT-033; me-ios `Employee/Employee.entitlements` |
| Extensions | Notification Service, Notification Content | Share extension (`…payslip.expense-share-extension`) | PLT-006/007/008 |
| Sign-in | Visma Connect OIDC + PKCE, client `vismamanager`, callbacks on `visma-manager.web.app` | Visma Connect, its own client id, callbacks on `static.mobileemployee.visma.net` | ASSESSMENT §4 |
| Tokens at rest | Encrypted MMKV (Redux slices), seed in the Keychain | Keychain (3 items), per account; several accounts at once | ASSESSMENT §3 |
| Minimum OS | iOS 15.1, Android 24 | iOS 18.0 | PLT-002 |

---

## 1. Store identity

`program.json` has `storeIdentity: undecided`. **This is the brief's first open question.**

| Option | Manager users (iOS + Android) | Employee users (iOS) | Consequences |
|---|---|---|---|
| **A. Update of Manager** (`com.visma.vmm` on both stores) | Update in place on both platforms. Keychain, container and ratings stay | Install the new app. Employee is sunset | Employee's device-only data (unsent receipt drafts in Realm) must be flushed **before** the sunset (§3). Every Employee user signs in again |
| **B. Update of Employee** (`com.visma.vme.payslip`) | iOS users install the new app. On Android there is no Employee listing, so Android needs a new listing (or option D) | Update in place. Keychain, app-group container (Realm key, Realm file) and ratings stay | Manager's Play users (the only Android users today) all move to a new listing |
| **C. New listing** on both stores | Install | Install | The cleanest identity. Nobody updates in place, so both apps need a full sunset and **every** user signs in again and loses local data |
| **D. Per platform: iOS as an update of Employee, Android as an update of Manager** | Android users update in place. iOS users install | Update in place | The most in-place updates: only Manager's iOS users install. Both listings are renamed to the new product. One codebase ships two application ids (normal: iOS and Android ids are independent) |

**Recommendation: D, if the active-user numbers confirm it.** The numbers are not in the repositories, so this is
open: ask for monthly active users per app and platform.
- Employees usually outnumber their managers. Employee also holds **device-only data** (unsent receipt drafts in
  encrypted Realm, ASSESSMENT §6 debt 1). An update in place is the only option that keeps that data without an extra
  export step.
- On Android only Manager exists, so updating `com.visma.vmm` costs no Employee user anything.
- Only Manager's iOS users must install. Both apps are on team `XGSJA98R9R`, which makes a guided handoff possible
  (§2 and §7).
- **Flip to A** if Manager's iOS users outnumber Employee's by a wide margin. The rest of this document is written for
  D and notes where A or C changes it.
- **Preconditions for D:**
  - Android in place needs the same signing key for `com.visma.vmm`, or Play App Signing continuity. Who holds the
    key is open.
  - `program.json` takes one app for `storeIdentity`. Record D as `--store me-ios` plus a
    `continuity:store-identity` decision naming `com.visma.vmm` for Android, so the platform-parity check expects
    both ids.

**Store listing work for every option.**
- Screenshots and text for both personas.
- A privacy nutrition label (App Store) and Data safety form (Play) that are the **union** of both apps' data
  collection, from both privacy manifests (PLT-035, `required`).
- Review notes that explain the consolidation.

## 2. Sign-in and session

The two apps use **different Visma Connect clients**, and a refresh token only works with the client that issued it.
So whether a session survives depends on which client the new app uses.

| Users | With option D | What the new app does |
|---|---|---|
| Employee, iOS (updated in place) | **Keep their session** if the new app uses Employee's Visma Connect client. They re-login once if it uses a new client | On first launch, a run-once migration reads me-ios's Keychain token items for **every signed-in account**. It re-stores them under the new app's keys with `…ThisDeviceOnly` accessibility (fixes CWE-922, ASSESSMENT §6), then deletes the old items |
| Manager, Android (updated in place) | **One re-login.** Their tokens were issued to the `vismamanager` client and live in vmm's encrypted MMKV | On first launch, read nothing from the old MMKV except the signed-in user's email (`loginManager.username`) as a login hint. Then wipe the old MMKV and its Keychain seed |
| Manager, iOS (install) | **One re-login.** Different container. The session cannot carry over | Optional: the sunset update of vmm writes the user's email into a shared Keychain access group on team `XGSJA98R9R`, and the new app reads it as a login hint. Never share tokens this way |

**Exactly what the iOS migration reads (verified in me-ios).**
- Tokens live in two Keychain services:
  - `com.visma.vme.payslip.user` in the app's default access group
    (`legacy/me-ios/Employee/AppDependencies.swift:120-122`);
  - a shared service in access group `group.com.visma.vme.payslip.shared`, the app group id used as a Keychain access
    group (`AppDependencies.swift:113,124-126`). The share extension reads it.
- The passcode is in `com.visma.vme.payslip.passcode` (`AppDependencies.swift:239-241`). It is deleted, never read
  (see App lock).
- `Employee.entitlements` has no `keychain-access-groups` key. So the new iOS target **must** carry the app-group
  entitlement `group.com.visma.vme.payslip.shared`, and keep the same team, or it cannot read the shared items.
  Phase 0 checks this.
- **The erase trap.** me-ios wipes a Keychain service whenever its `UserDefaults.standard` marker is missing
  (`EmployeeCore/Services/StorageService/StorageService.swift:118-127`, `eraseOnFirstInstall`). The new app's
  migration must run **before** any code that could reset UserDefaults. The new app's own storage must not port that
  logic onto the old services.
- The pilot (brief Phase 1) rehearses this on a real App Store build, installing over it with two accounts signed in.

**Client registration (open, a person decides with the Visma Connect owners).** The recommendation is that the new app
uses **Employee's client, extended with the scopes and audiences Manager's backends need**: API Manager `Roles`
and `odp/user/info`, calendarBase, and later Approval, AutoPay, OSR, Dialogue and Gaia. Its redirect URIs are the ones
it already has on `static.mobileemployee.visma.net`. If Visma Connect cannot do that, the new app gets a new client
and **everyone** re-logs once. The new app must also get the `Gsid` session that Manager's APIs expect (vmm
`src/reducers/loginManagerReducer.ts:137`).

**What re-login users see** (a first-launch screen, translated into all six locales):
> **Welcome to <new app name>**
> Visma Manager and Visma Employee are now one app. Sign in with your Visma account to continue. You will find
> everything you used before in this app.

Everyone on Manager's side re-logs once. That breaks INTENT's candidate "update in place without re-login" for them,
so a person must accept it explicitly (a `mustStayTrue` decision).

**Several accounts.** me-ios lets one person be signed in to several accounts and companies at once; vmm has one
account. The migration must carry every me-ios account. Whether the new app keeps multi-account for everyone is a
product decision (open question).

**App lock.** The me-ios passcode is stored unhashed (CWE-256). It is **not migrated**. After the update, a user who
had app lock on is asked once to set Face ID or a new passcode. The old passcode item is deleted.

## 3. Local data

The servers are the source of truth for almost everything, so **re-fetch is the default**. The exceptions are
device-only data and preferences.

| App | Store | Contents | Choice | Who loses what |
|---|---|---|---|---|
| me-ios | Encrypted **Realm**, 37 models, in app group `group.com.visma.vme.payslip.shared`, key in the Keychain (PLT-057, PLT-042) | Caches of server data, **plus unsent receipt drafts and captures that exist only on the device** | **Caches: drop and re-fetch.** **Unsent drafts: flush first, then import once as a fallback.** (1) A last me-ios update, shipped before the new app, uploads every unsent draft and shows what could not be sent. (2) Under option D, the new app's first launch also opens the Realm read-only, if it still exists, and imports any drafts left, before deleting the file and its key. Realm silently deletes data on errors (`RealmService.swift:47,101-106`), so the import runs read-only and never deletes before a successful import | Under A or C: any draft not flushed before the sunset is lost. The sunset notice says so |
| me-ios | UserDefaults (PLT-066) | Calendar view mode, filter toggles, balance options | Migrate on first launch (D). They map onto the new calendar settings for CAP-003/005 | Under A or C: preferences reset to defaults |
| me-ios | Keychain (3 items) | Tokens per account, Realm key, passcode | Tokens migrate (§2). Realm key used once for the import, then deleted. Passcode deleted | none |
| vmm | Encrypted **MMKV**, persisted Redux slices, seed in the Keychain (PLT-051) | Session, settings: calendar view mode, hide weekends, week numbers, the three filters, `calendarSync` (PLT-061) | On Android (D): read the calendar settings once and map them onto CAP-003/005. Read the email as a login hint, then wipe the rest. On iOS: nothing (different container) | iOS Manager users: calendar preferences reset. The conflicts on the default view and week numbers (BUSINESS_RULES, CAP-003/005) decide the new defaults |
| vmm | AsyncStorage (11 keys) | Mostly UI flags and legacy persist import | Drop | none |
| vmm | **Device calendars created by calendar sync** (CAP-007, PLT-058) | The Birthdays and Anniversaries calendars, written into the phone's own calendar | They outlive the app. If CAP-007 is kept, the new app finds these calendars by name and adopts them. If it is dropped, the sunset vmm update removes them and says so. Otherwise the phone keeps stale events forever | Users of a feature that is dev-flagged today (PLT-059), so probably few |

**Unsent offline work must be gone before the old app stops working.** Only me-ios has any: receipt drafts. Neither
app queues check-ins or registrations offline in the mapped code.

## 4. Push

| Item | vmm | me-ios | New app |
|---|---|---|---|
| Transport | FCM (`@react-native-firebase/messaging`), both platforms (PLT-050) | APNs, registered per account (`MultiAccountPushManager`) with `notification/RegisterDevice` | FCM on both platforms, plus an APNs token registered with the Employee backend per account. After sign-in, the app registers with **both** backends, for the roles the person has |
| Types | Approval (with approve/reject actions), anniversary, HR dialogue (reply from the notification) | New payslip, new year-end report, **timesheet reminder** (relates to CAP-020), generic | Every type the brief keeps. Each type's tap goes to the new route for it (route table in §5) |
| Categories and channels (PLT-079, `required`) | 5 iOS categories (`APPROVAL_*`, `DIALOGUE_CATEGORY`, `ANNIVERSARY_CATEGORY`), Android channels `high-priority`, `fcm_fallback_notification_channel` | none declared | Declared with the same identifiers so that server payloads keep working |
| Extensions | Notification Service + Notification Content (custom approval and anniversary layouts) (PLT-006/007) | none | Kept with their capabilities. Both extensions are native Swift in any stack |

**Two dependencies to settle before any push work (brief Phase 0 and Phase 4 entry criteria).**
- **One Firebase project.**
  - vmm uses a static Firebase config.
  - me-ios loads its Firebase config at runtime from `third-party-keys` (`Employee/Services/ThirdPartyKeys/FirebaseKeyInitializer.swift:19-25`).
  - The new app's iOS id (`com.visma.vme.payslip` under D) and Android id must both be registered in the project the
    Manager push backend sends through. Otherwise Manager notifications never reach iOS.
  - The config is static, so crashes before sign-in are reported.
- **Employee push on Android.**
  - me-ios registers with `notification/RegisterDevice` and a hard-coded `family: 0`
    (`Employee/PushNotifications/PushNotificationService.swift:49`). Nothing shows that the Employee backend can send
    through FCM to Android.
  - The backend owner confirms it before the timesheet reminder (CAP-020) is built.

**Extension ids under D.** vmm's Notification Service and Content extensions become
`com.visma.vme.payslip.<extension>`, with new provisioning profiles. Their app group moves from `group.com.visma.vmm`
to the new app's group.

**Tokens.** Tokens are per app id.
- Under D, APNs tokens of `com.visma.vme.payslip` and FCM tokens of `com.visma.vmm` (Android) usually stay valid
  across the update. The new app still re-registers after sign-in, because the registration payload and role mapping
  change.
- Tokens of **vmm on iOS** keep receiving until the backend drops them. A person with both roles and both apps would
  get Manager notifications twice. **Mitigation:**
  - The backend de-duplicates by user and device vendor id.
  - The sunset update of vmm unregisters its token once the user has signed in to the new app. That sign-in is
    visible to the backend.
- **Backend cut:** after the vmm iOS removal step (§7), the Manager push backend drops vmm iOS tokens.

**Security fix carried in.** The exported Android `MainActivity` accepts forged notification-action extras
(CWE-926/940, ASSESSMENT §6). The new app handles notification actions only from its own notification intents
(`PendingIntent` with `FLAG_IMMUTABLE`, activity not exported for that action).

## 5. Links

Neither app has in-app deep links today: vmm has no `linking` config, and me-ios's `openURLContexts` is empty.
So **no email or document links point into either app**. What must keep working is sign-in callbacks and AutoPay
2FA.

| Link | Legacy | New app | Action |
|---|---|---|---|
| `applinks:` / `webcredentials:` `static.mobileemployee.visma.net` (+ `.stag`) (PLT-004) | me-ios OAuth callback | **Claimed.** It is the redirect of the recommended client | The domain's `/.well-known/apple-app-site-association` lists `XGSJA98R9R.com.visma.vme.payslip` (unchanged under D). Add `assetlinks.json` for Android `com.visma.vmm` with its signing certificate |
| `applinks:` / `webcredentials:` `visma-manager.web.app` (PLT-004) | vmm OIDC login and logout callbacks (`/connect-login`, `/connect-logout`, vmm `apiManagerConnect.ts:55,57`), **AutoPay 2FA redirect** | **Claimed for the AutoPay 2FA paths only**, when AutoPay is built | The AASA `components` are **scoped by path**. `/connect-login` and `/connect-logout` stay exclusive to `XGSJA98R9R.com.visma.vmm` until sunset step 6. If the new app claimed them while vmm iOS is installed, vmm's sign-in callback would open the new app, and vmm users could not sign in during the sunset. Only the 2FA paths list the new app's id. Android: verify the hosted `assetlinks.json` lists `com.visma.vmm` with the Play App Signing certificate. It is on the server and cannot be checked from the repositories |
| Scheme `vismame`, `vismamedev` (PLT-005) | me-ios OAuth callback | Kept (`vismame`) while the Employee client still has it as a redirect URI. `vismamedev` only in dev builds | Under D there is no clash, because me-ios is replaced |
| Scheme `vismamanager` (PLT-005) | vmm OAuth leftover | **Dropped** (security pass: unused scheme, CWE-939) | While vmm is installed on iOS, two apps must never claim one scheme. The new app does not |
| BankID scheme query | vmm AutoPay 2FA | Kept with AutoPay (`LSApplicationQueriesSchemes`) | none |

**Route table.** The new app gets a `linking` config from day one (Phase 0). It holds a route for each
notification type and for "open the new app" from the sunset notice. Maestro `openLink` flows test it.

## 6. Analytics, crash reporting and flags

- **Event wire names are kept** unless a decision says otherwise (`analytics:taxonomy`). vmm has 311 catalog events
  plus 48 literals; me-ios has 185. The calendar slice's events are listed per capability in `capabilities.json` and
  checked by `events_parity.py`. Renames go into `docs/fusion/analytics-map.json`.
- **Destinations.**
  - Snowplow is in both apps (PLT-038). Keep it, with the event names of the app each capability came from.
  - Firebase Analytics is in vmm (PLT-037). me-ios turns it off (`Employee/Services/FirebaseService.swift:42-44`).
  - Which one dashboards read is open (ASSESSMENT §8, vmm gap 1).
- **User id.**
  - Both apps sign in to the same Visma Connect identity. The new app uses the **Connect user id** as the analytics
    user id: me-ios `connectUserId` from `currentSession`, and the vmm equivalent from `odp/user/info`.
  - It adds `source_app` (`manager` or `employee`, from the persona of the screen) and `migrated_from`
    (`vmm`, `me-ios` or `none`, set once at first launch) during the transition.
  - Whether dashboards can follow users across that change is open.
- **Crash reporting.**
  - vmm has both Sentry and Crashlytics (PLT-045/046), and me-ios has firebase-ios-sdk. Pick one project for the
    new app (open question).
  - Upload dSYMs and Hermes source maps for every release build.
- **Flags.**
  - Firebase Remote Config (vmm, 15 keys) against LaunchDarkly (me-ios, 2 keys). Pick one (open question).
  - Carry over only keys still in use.
  - Add one kill-switch flag per migrated capability.
  - Never carry the LLM system prompts that vmm lets Remote Config override (ASSESSMENT §6, vmm debt 8).
- **Surveys.**
  - Survicate is in both apps (PLT-048). Keep one workspace, with the persona as an attribute.
  - Wootric (vmm only) is a duplicate vendor, so decide whether it goes.

## 7. The other app's sunset

Under D the app that is sunset is **Manager on iOS** (under A: Employee on iOS; under C: both apps on every
platform). The steps come in order, with no dates. Before each step, measure adoption with `migrated_from` and active
users per app.

These updates change the legacy apps. This program never edits them, so their own teams ship them. The brief's
**Phase 8** (legacy app releases) tracks them from the end of the pilot, because they need lead time and adoption.

1. **Pre-cutover update of the app being replaced in place (Employee iOS under D).**
   - It flushes unsent receipt drafts (§3) and makes sure every account's token is in the Keychain items the
     migration reads.
   - It ships **before** the new app's first store release. It must reach the adoption threshold recorded in the
     `continuity:legacy-releases` decision. me-ios's server-driven forced update (`remoteControl/config`) pushes
     stragglers to it.
2. **The new app ships as the update** (Employee iOS listing, Manager Play listing).
   - Staged rollout: phased release on iOS, percentage rollout on Play.
   - A kill-switch flag per capability.
3. **Sunset update of vmm on iOS.**
   - An in-app notice with a link to the new app's App Store page.
   - It unregisters vmm's push token once the user has signed in to the new app (§4).
   - It removes the synced device calendars, or leaves them for the new app to adopt (§3).
   - Optionally, a login hint in the shared Keychain group (§2).
4. **Soft block, then forced update screen** in vmm iOS, served from the server (vmm's remote config), pointing to the
   new app.
5. **Removal from sale** of vmm iOS.
6. **Backend cleanup.**
   - Drop vmm iOS push tokens.
   - Retire the `vismamanager` Visma Connect client once no active user has it.
   - Remove `XGSJA98R9R.com.visma.vmm` from the `visma-manager.web.app` AASA.

**Android Employee.** `ASSESSMENT.md` §8 asks whether an Android Employee app exists outside the provided sources. If
it does, it is a third legacy app with its own users. This plan does not cover it until it is added to the program.

## Rollout (people carry it out)

- **Test groups.** TestFlight and Play internal testing with at least:
  - an employee-only account
  - a manager-only account (HRM, approval)
  - **one person who is both**
  - one me-ios user with several accounts
- **Test updates in place with real old builds.**
  - Install the current App Store Employee build, sign in with two accounts, leave a receipt draft unsent, then
    install the new build over it.
  - Do the same with the current Play Manager build on Android.

## Open continuity choices (also in the brief's Open Questions)

- [ ] Store identity (A, B, C or D). Needs active users per app and platform.
- [ ] Who holds the Android signing key for `com.visma.vmm`, and whether Play App Signing is on.
- [ ] Visma Connect client: extend Employee's client with Manager's scopes, or register a new one. Also where `Gsid`
      comes from for the new app.
- [ ] Multi-account for everyone, or only for former Employee users.
- [ ] Backend support for server-side receipt drafts, so the flush in §7 step 1 has somewhere to send them.
- [ ] Push: backend de-duplication by user and device, and the Manager push registration endpoint (not in the mapped
      slice).
- [ ] Analytics: Firebase Analytics or Snowplow for dashboards, the user id, and the crash reporting project.
- [ ] Flags: Firebase Remote Config or LaunchDarkly.
- [ ] One Firebase project for both new app ids, and Employee push delivery to Android.
- [ ] Owners and adoption thresholds of the Employee pre-cutover update and the vmm sunset update.
- [ ] Accept one re-login for Manager users (`mustStayTrue`).
- [ ] Minimum iOS version (Manager supports 15.1, Employee 18.0). Manager iOS users below the new floor cannot install.
- [ ] Does an Android Employee app exist?
