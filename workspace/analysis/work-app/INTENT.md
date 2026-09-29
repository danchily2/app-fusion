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
