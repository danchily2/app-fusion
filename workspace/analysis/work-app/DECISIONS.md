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
| DEC-033 | conflict | CAP-047 | take:vmm | Manager's Gaia, for everyone: one general assistant; Employee's payslip/calendar questions become contexts of it. Keep Employee's server-side rating, which Gaia lacks. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-034 | conflict | CAP-048 | take:vmm | Manager's Gaia, for everyone: one general assistant; Employee's payslip/calendar questions become contexts of it. Keep Employee's server-side rating, which Gaia lacks. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-035 | conflict | CAP-053 | take:vmm | Manager's Gaia, for everyone: one general assistant; Employee's payslip/calendar questions become contexts of it. Keep Employee's server-side rating, which Gaia lacks. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-036 | conflict | CAP-054 | take:vmm | Manager's Gaia, for everyone: one general assistant; Employee's payslip/calendar questions become contexts of it. Keep Employee's server-side rating, which Gaia lacks. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-037 | conflict | CAP-059 | take:vmm | Manager's Gaia, for everyone: one general assistant; Employee's payslip/calendar questions become contexts of it. Keep Employee's server-side rating, which Gaia lacks. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-038 | conflict | CAP-066 | take:vmm | Manager's Gaia, for everyone: one general assistant; Employee's payslip/calendar questions become contexts of it. Keep Employee's server-side rating, which Gaia lacks. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-039 | conflict | CAP-197 | new-spec | Employee's, plus Manager's extras: multi-account sign-in from Employee; keep Manager's no-roles screen and web-session logout. A new listing needs a new redirect link either way. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-040 | conflict | CAP-199 | new-spec | Employee's, plus Manager's extras: multi-account sign-in from Employee; keep Manager's no-roles screen and web-session logout. A new listing needs a new redirect link either way. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-041 | conflict | CAP-200 | new-spec | Employee's, plus Manager's extras: multi-account sign-in from Employee; keep Manager's no-roles screen and web-session logout. A new listing needs a new redirect link either way. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-042 | conflict | CAP-201 | new-spec | Employee's, plus Manager's extras: multi-account sign-in from Employee; keep Manager's no-roles screen and web-session logout. A new listing needs a new redirect link either way. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-043 | conflict | CAP-209 | new-spec | Employee's, plus Manager's extras: multi-account sign-in from Employee; keep Manager's no-roles screen and web-session logout. A new listing needs a new redirect link either way. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-044 | conflict | CAP-176 | both-by-role | Register with both, per role: the device registers with each backend for the roles the user has, and unregisters from both on sign-out. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-045 | conflict | CAP-177 | both-by-role | Register with both, per role: the device registers with each backend for the roles the user has, and unregisters from both on sign-out. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-046 | conflict | CAP-124 | both-by-role | Both, per role: managers keep the HRM directory of their companies; employees keep the colleague directory. One shared, localized profile screen. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-047 | conflict | CAP-125 | both-by-role | Both, per role: managers keep the HRM directory of their companies; employees keep the colleague directory. One shared, localized profile screen. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-048 | conflict | CAP-126 | both-by-role | Both, per role: managers keep the HRM directory of their companies; employees keep the colleague directory. One shared, localized profile screen. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-049 | conflict | CAP-129 | both-by-role | Both, per role: managers keep the HRM directory of their companies; employees keep the colleague directory. One shared, localized profile screen. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-050 | conflict | CAP-067 | both-by-role | Tabs per role: each person sees the areas of their roles; someone with both gets both sets under one shell (the plan's role matrix decides the order). | Dan-Mihai Cuc | 2026-10-01 |
| DEC-051 | conflict | CAP-078 | take:vmm | Manager's: richer feedback context, remotely tuned rating prompt and announcements, without an app release. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-052 | conflict | CAP-098 | take:vmm | Manager's: richer feedback context, remotely tuned rating prompt and announcements, without an app release. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-053 | conflict | CAP-100 | take:vmm | Manager's: richer feedback context, remotely tuned rating prompt and announcements, without an app release. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-054 | conflict | CAP-101 | take:vmm | Manager's: richer feedback context, remotely tuned rating prompt and announcements, without an app release. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-055 | conflict | CAP-108 | take:vmm | Manager's: in-app language choice and synced appearance follow the user across devices; one update check. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-056 | conflict | CAP-109 | take:vmm | Manager's: in-app language choice and synced appearance follow the user across devices; one update check. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-057 | conflict | CAP-110 | take:vmm | Manager's: in-app language choice and synced appearance follow the user across devices; one update check. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-058 | conflict | CAP-113 | take:vmm | Manager's: in-app language choice and synced appearance follow the user across devices; one update check. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-059 | conflict | CAP-114 | take:vmm | Manager's: in-app language choice and synced appearance follow the user across devices; one update check. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-060 | conflict | CAP-115 | take:vmm | Manager's: in-app language choice and synced appearance follow the user across devices; one update check. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-061 | conflict | CAP-118 | take:vmm | Manager's: in-app language choice and synced appearance follow the user across devices; one update check. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-062 | conflict | CAP-120 | take:vmm | Manager's: in-app language choice and synced appearance follow the user across devices; one update check. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-063 | conflict | CAP-119 | take:vmm | Yes, Manager's way: encrypted local state restored on launch. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-064 | conflict | CAP-144 | take:me-ios | iOS behavior: me-ios is the more complete twin in the map; Android follows it. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-065 | conflict | CAP-145 | take:me-ios | iOS behavior: me-ios is the more complete twin in the map; Android follows it. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-066 | conflict | CAP-146 | take:me-ios | iOS behavior: me-ios is the more complete twin in the map; Android follows it. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-067 | conflict | CAP-178 | take:me-ios | iOS behavior: me-ios is the more complete twin in the map; Android follows it. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-068 | conflict | CAP-198 | take:me-ios | iOS behavior: me-ios is the more complete twin in the map; Android follows it. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-069 | conflict | CAP-238 | take:me-ios | iOS behavior: me-ios is the more complete twin in the map; Android follows it. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-070 | scope | CAP-087 | out | Merge them: a duplicate of CAP-201, which is kept and built. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-071 | conflict | CAP-087 | defer | Merge them: a duplicate of CAP-201, which is kept and built. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-072 | scope | CAP-121 | out | Merge them: a duplicate of CAP-209, which is kept and built. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-073 | conflict | CAP-121 | defer | Merge them: a duplicate of CAP-209, which is kept and built. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-074 | scope | CAP-107 | out | Merge them: a duplicate of CAP-113 and CAP-115, which is kept and built. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-075 | conflict | CAP-107 | defer | Merge them: a duplicate of CAP-113 and CAP-115, which is kept and built. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-076 | platform | PLT-094 | keep | Keep all 17: they are what makes push work for existing flows; the new app rebuilds each. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-077 | platform | PLT-095 | keep | Keep all 17: they are what makes push work for existing flows; the new app rebuilds each. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-078 | platform | PLT-150 | keep | Keep all 17: they are what makes push work for existing flows; the new app rebuilds each. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-079 | platform | PLT-151 | keep | Keep all 17: they are what makes push work for existing flows; the new app rebuilds each. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-080 | platform | PLT-208 | keep | Keep all 17: they are what makes push work for existing flows; the new app rebuilds each. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-081 | platform | PLT-209 | keep | Keep all 17: they are what makes push work for existing flows; the new app rebuilds each. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-082 | platform | PLT-219 | keep | Keep all 17: they are what makes push work for existing flows; the new app rebuilds each. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-083 | platform | PLT-220 | keep | Keep all 17: they are what makes push work for existing flows; the new app rebuilds each. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-084 | platform | PLT-221 | keep | Keep all 17: they are what makes push work for existing flows; the new app rebuilds each. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-085 | platform | PLT-222 | keep | Keep all 17: they are what makes push work for existing flows; the new app rebuilds each. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-086 | platform | PLT-246 | keep | Keep all 17: they are what makes push work for existing flows; the new app rebuilds each. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-087 | platform | PLT-330 | keep | Keep all 17: they are what makes push work for existing flows; the new app rebuilds each. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-088 | platform | PLT-331 | keep | Keep all 17: they are what makes push work for existing flows; the new app rebuilds each. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-089 | platform | PLT-351 | keep | Keep all 17: they are what makes push work for existing flows; the new app rebuilds each. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-090 | platform | PLT-371 | keep | Keep all 17: they are what makes push work for existing flows; the new app rebuilds each. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-091 | platform | PLT-372 | keep | Keep all 17: they are what makes push work for existing flows; the new app rebuilds each. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-092 | platform | PLT-390 | keep | Keep all 17: they are what makes push work for existing flows; the new app rebuilds each. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-093 | platform | PLT-114 | keep | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a behavior users notice: kept) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-094 | platform | PLT-171 | keep | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a behavior users notice: kept) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-095 | platform | PLT-174 | keep | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a behavior users notice: kept) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-096 | platform | PLT-212 | keep | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a behavior users notice: kept) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-097 | platform | PLT-213 | keep | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a behavior users notice: kept) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-098 | platform | PLT-273 | keep | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a behavior users notice: kept) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-099 | platform | PLT-287 | keep | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a behavior users notice: kept) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-100 | platform | PLT-338 | keep | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a behavior users notice: kept) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-101 | platform | PLT-364 | keep | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a behavior users notice: kept) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-102 | platform | PLT-365 | keep | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a behavior users notice: kept) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-103 | platform | PLT-379 | keep | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a behavior users notice: kept) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-104 | platform | PLT-399 | keep | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a behavior users notice: kept) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-105 | platform | PLT-408 | keep | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a behavior users notice: kept) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-106 | platform | PLT-415 | keep | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a behavior users notice: kept) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-107 | platform | PLT-101 | decide-later | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a storage engine: chosen with the stack) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-108 | platform | PLT-120 | decide-later | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a storage engine: chosen with the stack) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-109 | platform | PLT-129 | decide-later | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a storage engine: chosen with the stack) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-110 | platform | PLT-157 | decide-later | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a storage engine: chosen with the stack) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-111 | platform | PLT-286 | decide-later | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a storage engine: chosen with the stack) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-112 | platform | PLT-358 | decide-later | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a storage engine: chosen with the stack) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-113 | platform | PLT-378 | decide-later | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a storage engine: chosen with the stack) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-114 | platform | PLT-382 | decide-later | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a storage engine: chosen with the stack) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-115 | platform | PLT-130 | drop | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a migration of old data: not needed when starting clean) | Dan-Mihai Cuc | 2026-10-01 |
| DEC-116 | platform | PLT-343 | drop | Rebuild what users notice: keep the behaviors, drop the old stores and migrations; the engine is chosen with the stack. (a migration of old data: not needed when starting clean) | Dan-Mihai Cuc | 2026-10-01 |
