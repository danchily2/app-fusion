# Journey tests with Maestro

A journey (`JRN-NNN` in `capabilities.json`) becomes one Maestro flow that drives the new app on a simulator or
emulator, as the persona would. Maestro runs the same YAML on iOS and Android, so a flow written against
accessibility ids covers both platforms.

## File and name

`new-app/<program>/.maestro/JRN-NNN-<slug>.yaml`. The journey id is in the file name, so the JUnit report names it.

```yaml
appId: ${APP_ID}
name: JRN-003 Manager approves an absence request from the list
tags: [journey, manager, CAP-014, CAP-015]
env:
  USER: ${MANAGER_USER}
  PASSWORD: ${MANAGER_PASSWORD}
---
- launchApp: { clearState: true }
- runFlow: flows/sign-in.yaml
- tapOn: { id: "tab-approvals" }
- assertVisible: { id: "approval-list" }
- tapOn: { text: "Absence .*" }
- tapOn: { id: "approve-button" }
- assertVisible: "Approved"
- assertNotVisible: { id: "approval-item-${REQUEST_ID}" }
- takeScreenshot: ../analysis/<program>/evidence/shots/CAP-014/approved
```

## Rules

- **Assert outcomes, not screens.** The item leaves the list, the total shows 147.00 kr, the status reads Approved.
- **Test accounts only**, passed as `-e` variables (`maestro test -e MANAGER_USER=... flow.yaml`), never written in the
  flow. Use a test backend a person named in PREFLIGHT.md.
- **Accessibility ids** (`testID` in React Native, `.accessibilityIdentifier` in SwiftUI, `Modifier.testTag` in
  Compose) are the contract between flows and code. Keep them identical across platforms.
- **Deep links:** `- openLink: vismamanager://approvals/123` checks that a legacy link still lands on the right screen.
  The link table is in CONTINUITY.md.
- **Legacy baseline (optional):** a legacy app's own Maestro flows (vmm has `.maestro/`) show how the journey works
  today. Read them, never edit them, and do not expect them to pass against the new app.

## Run with a JUnit result

```bash
maestro test new-app/<program>/.maestro/JRN-003-approve-absence.yaml \
  -e APP_ID=<bundle or application id> -e MANAGER_USER=... -e MANAGER_PASSWORD=... \
  --format junit --output analysis/<program>/evidence/maestro/JRN-003.xml
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/evidence.py" journey <program> --journey JRN-003 \
  --flow new-app/<program>/.maestro/JRN-003-approve-absence.yaml \
  --junit analysis/<program>/evidence/maestro/JRN-003.xml --device "iPhone 17 (iOS 26)"
```

Boot the device first (`xcrun simctl boot "iPhone 17"`, or `emulator -avd <name>`) and install the app. Stop the
simulator or emulator you started when the run ends.
