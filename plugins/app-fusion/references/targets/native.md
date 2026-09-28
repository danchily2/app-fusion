# Target profile: native pair (SwiftUI + Jetpack Compose)

Two projects side by side under the new app root:

```
new-app/<program>/
  ios/        the SwiftUI app: references/targets/swiftui.md
  android/    the Compose app: references/targets/compose.md
  .maestro/   one flow per journey, shared by both platforms where the accessibility ids match
  docs/fusion/SCAFFOLD.md, CAP-NNN.md, i18n-map.json   one set for both platforms
```

- **One capability, two modules.** A capability's porting notes list the files of both platforms under `## Files`,
  and its tests name the same CAP and RULE ids on both. The proof then judges the capability once, over both platforms'
  results.
- **Keep the platforms in step.** Build a capability on both platforms in the same phase, or state in the brief which
  platform leads and when the other follows. A capability built on one platform only is PARTLY PROVEN at best.
- **Share the definitions, not the code.** One token export feeds both design systems, one string key set feeds both
  catalogs (a generator writes `Localizable.xcstrings` and `strings.xml` from one source), and one API contract
  (OpenAPI when the backend has one) generates both clients.
- **Maestro flows** are written once, with `appId` set per platform through `-e APP_ID=...` or two small wrappers,
  and accessibility ids that are the same on both platforms.
