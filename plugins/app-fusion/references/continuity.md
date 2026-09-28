# Continuity: getting every legacy app's users into the new app

No test in any repository protects existing users. This checklist does, and `fuse-brief` turns it into
`CONTINUITY.md`.

## 1. Store identity (decide first)

| Option | Users of app A | Users of app B | Notes |
| --- | --- | --- | --- |
| New app ships as an **update of A** (A's bundle id, team and listing) | get it as an update: Keychain, app container, push registration and ratings stay | must install it; B is sunset | usually best when A has more users or better ratings |
| New app ships as an **update of B** | must install it | get it as an update | the mirror image |
| **New listing** | install it | install it | cleanest identity; both apps are sunset; nobody updates in place |

- An iOS update in place needs the **same bundle id and team id**.
- An Android update in place needs the **same application id and signing key** (or Play App Signing continuity).
- A different team or key means a new app for the store, and for the Keychain.

## 2. Sign-in and session

- **Updated app:** the Keychain items and the app container survive. Keep the token keys, or migrate them on first
  launch in code that runs once.
- **Other app's users:** the session does not carry over unless both apps share a **keychain access group** under the
  same team (iOS) or use account transfer (Android backup, or a server-issued one-time transfer). Otherwise it is one
  re-login: say so in the plan, and write the message users see.
- **SSO:** check the redirect URI scheme. The new app must register the scheme the identity provider knows, or the
  provider needs a new client registration.

## 3. Local data

List each app's local storage from `PLATFORM.md` (Realm, Core Data, AsyncStorage, MMKV, UserDefaults,
SharedPreferences, files). For each store, choose one:
- **Re-fetch:** the server is the source of truth. This is the usual choice and the cheapest.
- **Migrate on first launch:** only for the updated app, whose container is kept.
- **Move through an app group:** same team only. The old app writes an export into the group container, and the new
  app imports it.
- **Drop:** say who loses what, for example drafts or offline queues.

Unsent offline work (drafts, queued expense claims, check-ins) must be flushed or migrated **before** the old app
stops working. Plan an update of the old app that sends it.

## 4. Push notifications

- Device tokens are per app id. The new app registers on first launch after sign-in, and the backend maps tokens to
  users and roles.
- Tokens of the sunset app keep receiving until the backend drops them: plan the backend cut.
- Notification service and content extensions (rich push, grouping), actionable categories and deep-link payloads
  must exist in the new app for every notification type the brief keeps (`PLATFORM.md` extensions).

## 5. Links

- **Universal links (iOS)** need `applinks:<domain>` in the entitlements, and the domain's
  `/.well-known/apple-app-site-association` must list the new app's `teamId.bundleId` with the paths. **App links
  (Android)** need intent filters with `autoVerify` and `/.well-known/assetlinks.json` with the new signing
  certificate. Do this for **every** legacy domain whose links exist in emails, notifications or documents.
- **Custom URL schemes** (`vismamanager://`, `vismame://`): the new app registers each one it keeps. On iOS, two
  installed apps claiming one scheme is undefined behaviour, so the sunset app must drop it.
- **Paths:** keep a route table from legacy paths to new routes. The deep-link tests (Maestro `openLink`) use it.

## 6. Analytics, crash reporting and flags

- Event wire names are a contract with dashboards. Keep them unless a decision renames them, and record renames in
  `docs/fusion/analytics-map.json`.
- **User id continuity:** keep the same analytics user id where the backend identity is the same, and add a `source_app`
  property during the transition.
- **Crash reporting:** decide the project (one of the old ones, or new). Upload symbol maps for release builds.
- **Remote config and feature flags:** carry over the keys still in use (`PLATFORM.md` flags). Use a flag per migrated
  capability so it can be switched off.

## 7. Sunset of the other app

Sequence the steps, with no dates:
1. An update of the old app with an in-app notice and a deep link to the new app (store link, or universal link).
2. Flush offline work (section 3).
3. A server-side soft block, then a forced update screen.
4. Removal from sale.
5. Backend cleanup: push tokens, and API clients whose last user is gone.

Measure adoption before each step, with analytics `source_app` and active users per app.

## 8. Rollout

- TestFlight and Play internal testing with users who have each role, and one user who has several.
- Staged rollout (phased release on iOS, percentage rollout on Play), plus feature flags per capability.
- Store listing: screenshots and text for both personas, a privacy nutrition label that is the **union** of both apps'
  data collection (from their privacy manifests), and review notes explaining the consolidation.
