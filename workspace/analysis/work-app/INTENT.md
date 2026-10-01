# work-app: intent

Recorded: 2026-09-28. Headless run (no pop-up tool was available), so every answer below is the documented default,
not a person's words. Each one is listed under **Open items** so a person confirms or changes it.

## Apps

| App | Product | Stack | Platforms | Branch @ commit | Path |
|---|---|---|---|---|---|
| vmm | Manager ("Visma Manager") | React Native | iOS, Android | develop @ 342cb745f66b (clean) | /Users/vismaemployee/Downloads/vmm |
| me-ios | Employee | Native iOS (Swift) | iOS | development @ a3600e7d6d89 (clean, shallow clone) | /Users/vismaemployee/Downloads/me-ios |

Twins: none (Manager and Employee are different products).

## Answers

1. **What do you want?** Build the new app *(default)*
2. **Which platforms?** iOS and Android *(default)*
3. **Which stack for the new app?** Decide in the plan *(default)*. Note: vmm is React Native, so its stack and team
   could carry over; the brief compares the options.
4. **What must stay true?** No answer given *(no default)*.
5. **Where is the new app's design?** No answer given; no Figma links recorded. Treated as *No design yet* until a
   person says otherwise, so the plan marks design as a gap per capability.
6. **Who uses the new app?** People who use Manager today; People who use Employee today *(one per product)*.
   Whether one person can have several roles: not answered.
7. **Which store listing does the new app ship under?** Decide in the plan *(default)*

## Open items

- Confirm the goal (build vs. understand and plan first).
- Confirm the platforms (iOS and Android).
- Confirm the stack stays "decide in the plan".
- Pick what must stay true: users update in place without reinstall or re-login; behavior matches the old apps
  unless a person decides otherwise; every shipped language is kept; a security review comes before release.
- Give the new app's Figma link(s), or confirm there is no design yet.
- Confirm the personas, and whether one person can be both a manager and an employee.
- Choose the store listing: update vmm's, update me-ios's, a new listing, or decide in the plan.
- me-ios is a shallow clone: history-based signals (churn, ownership) are unavailable for it.

## Answers given in the terminal, 2026-09-29 (Dan-Mihai Cuc)

Recorded as DEC-001 to DEC-032 in DECISIONS.json; the words below are the options chosen or typed.

- **Design:** "https://www.figma.com/proto/J4jjulaLJ4QNzqZ1INWydq/manployee-design … here is the proposed design, but
  plugin should work with other design as well". The file sits in the Visma plan, on a View seat (6 MCP reads a
  month), so the design step reads it through the REST API with a FIGMA_TOKEN.
- **Stack:** "Decide in the plan".
- **Store listing:** "A new listing on both".
- **Next step:** "Map all of both apps first", with me-android added: "Yes, clone it from GitHub".
- **Calendar (CAP-001 to CAP-005):** Employee's behavior every time ("Employee's, for both roles" for the month view).
- **The 14 rule differences inside them:** "Follow each capability's answer".
- **Analytics:** "New event taxonomy".
- **Data on the device:** "Start clean".
- **Notification service and content extensions:** "Keep". **Share extension:** "Keep, and fix the lock".
- **App groups:** "New groups only". **Firebase Cloud Messaging:** "Keep". **MMKV and Realm:** "Decide with the stack".
- **Minimum OS:** "iOS 18, Android 8 (API 26)". **The 60 minor platform items:** "Leave them to the plan".
- **Push the answers to GitHub:** "Yes, push them".

## Answers given in the terminal, 2026-10-01 (Dan-Mihai Cuc), after the full map

Recorded as DEC-033 to DEC-116. Options chosen, word for word:
- **AI assistant (6):** "Manager's Gaia, for everyone". **Sign-in and accounts (5):** "Employee's, plus Manager's extras".
- **Push (2):** "Register with both, per role". **People directory (4):** "Both, per role". **Tabs:** "Tabs per role".
- **Help, feedback, What's New (4):** "Manager's". **Settings and legal (8):** "Manager's". **App state:** "Yes, Manager's way".
- **Employee iOS vs Android differences (6):** "iOS behavior". **Duplicates (3):** "Merge them".
- **Push mechanics (17):** "Keep all 17". **Storage and housekeeping (24):** "Rebuild what users notice".

## Design gaps, answered in the terminal 2026-10-01 (Dan-Mihai Cuc)

- **All 136 capabilities with no screen:** "Build from legacy screens" (every domain); the day-timeline prototype is dropped.
- **14 blank Autopay prototype frames:** "Out of scope". **4 invoice task frames:** "In scope, same as the task detail".
