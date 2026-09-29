# Decisions: work-app

What a person decided, in their words. The plan (`fuse-brief`) and the build (`fuse-build`) read these, and only a person changes them. Run `/app-fusion:fuse-review` to answer open questions or change an answer.

| Id | Kind | About | Choice | Note | By | When |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-001 | continuity | continuity:store-identity | new-listing | A new listing on both: a fresh app in both stores; users of both old apps move to it, with a notice and a link in the old apps. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-002 | continuity | continuity:minimum-os | iOS 18, Android 8 (API 26) | iOS 18, Android 8 (API 26): Employee's iOS floor. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-003 | analytics | analytics:taxonomy | new-taxonomy | New event taxonomy: rename events for the new app; each rename is listed in a map, and dashboard owners remap. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-004 | conflict | CAP-001 | take:me-ios | Employee's, for both roles: one month view with me-ios's behavior. Employees see their own calendar; managers open a team member's calendar in the same view. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-005 | conflict | CAP-002 | take:me-ios | Employee's: me-ios's list, both directions, jump to date, formatted durations. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-006 | conflict | CAP-003 | take:me-ios | Employee's: one toolbar toggle, list view first, saved on the device. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-007 | conflict | CAP-004 | take:me-ios | Employee's: me-ios's richer sheet. For a manager viewing a team member, actions follow that manager's rights. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-008 | conflict | CAP-005 | take:me-ios | Employee's: me-ios's filter set, including roster and hide weekends. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-009 | conflict | CAP-001:RULE-010+RULE-147 | take:me-ios | Follow each capability's answer: CAP-001 keeps Employee's (me-ios) behavior, so Employee's rule wins here. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-010 | conflict | CAP-001:RULE-018+RULE-101 | take:me-ios | Follow each capability's answer: CAP-001 keeps Employee's (me-ios) behavior, so Employee's rule wins here. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-011 | conflict | CAP-001:RULE-038+RULE-067 | take:me-ios | Follow each capability's answer: CAP-001 keeps Employee's (me-ios) behavior, so Employee's rule wins here. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-012 | conflict | CAP-001:RULE-045+RULE-047 | take:me-ios | Follow each capability's answer: CAP-001 keeps Employee's (me-ios) behavior, so Employee's rule wins here. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-013 | conflict | CAP-001:RULE-045+RULE-147 | take:me-ios | Follow each capability's answer: CAP-001 keeps Employee's (me-ios) behavior, so Employee's rule wins here. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-014 | conflict | CAP-002:RULE-012+RULE-149 | take:me-ios | Follow each capability's answer: CAP-002 keeps Employee's (me-ios) behavior, so Employee's rule wins here. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-015 | conflict | CAP-002:RULE-142+RULE-149 | take:me-ios | Follow each capability's answer: CAP-002 keeps Employee's (me-ios) behavior, so Employee's rule wins here. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-016 | conflict | CAP-003:RULE-091+RULE-108 | take:me-ios | Follow each capability's answer: CAP-003 keeps Employee's (me-ios) behavior, so Employee's rule wins here. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-017 | conflict | CAP-004:RULE-080+RULE-092:59c3eef8 | take:me-ios | Follow each capability's answer: CAP-004 keeps Employee's (me-ios) behavior, so Employee's rule wins here. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-018 | conflict | CAP-004:RULE-080+RULE-092:7197b4ab | take:me-ios | Follow each capability's answer: CAP-004 keeps Employee's (me-ios) behavior, so Employee's rule wins here. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-019 | conflict | CAP-005:RULE-070+RULE-073:1b1db38e | take:me-ios | Follow each capability's answer: CAP-005 keeps Employee's (me-ios) behavior, so Employee's rule wins here. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-020 | conflict | CAP-005:RULE-070+RULE-073:80eda97e | take:me-ios | Follow each capability's answer: CAP-005 keeps Employee's (me-ios) behavior, so Employee's rule wins here. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-021 | conflict | CAP-005:RULE-073+RULE-110 | take:me-ios | Follow each capability's answer: CAP-005 keeps Employee's (me-ios) behavior, so Employee's rule wins here. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-022 | conflict | CAP-005:RULE-110+RULE-146 | take:me-ios | Follow each capability's answer: CAP-005 keeps Employee's (me-ios) behavior, so Employee's rule wins here. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-023 | platform | PLT-001 | drop | A new listing on both: the new app gets its own bundle and application ids (follows the store-listing answer). | Dan-Mihai Cuc | 2026-09-29 |
| DEC-024 | platform | PLT-002 | keep | iOS 18, Android 8 (API 26). | Dan-Mihai Cuc | 2026-09-29 |
| DEC-025 | platform | PLT-006 | keep | Keep: users keep the rich push views (approval and anniversary pushes). | Dan-Mihai Cuc | 2026-09-29 |
| DEC-026 | platform | PLT-007 | keep | Keep: pushes keep their action buttons. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-027 | platform | PLT-008 | keep | Keep, and fix the lock: receipt sharing stays; the new extension requires the app lock. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-028 | platform | PLT-033 | drop | New groups only: the old ids are not carried over; the new app gets its own group for its extensions. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-029 | platform | PLT-042 | drop | Start clean: users sign in again and data is re-fetched from the server; unsent drafts are lost unless sent first. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-030 | platform | PLT-050 | keep | Keep: one push path for iOS and Android; the backends register the new app's tokens. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-031 | platform | PLT-051 | decide-later | Decide with the stack: the plan picks storage together with the stack. | Dan-Mihai Cuc | 2026-09-29 |
| DEC-032 | platform | PLT-057 | decide-later | Decide with the stack: the plan picks storage together with the stack. | Dan-Mihai Cuc | 2026-09-29 |
