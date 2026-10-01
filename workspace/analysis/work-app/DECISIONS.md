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
| DEC-117 | gap | CAP-014 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-118 | gap | CAP-015 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-119 | gap | CAP-016 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-120 | gap | CAP-018 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-121 | gap | CAP-019 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-122 | gap | CAP-021 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-123 | gap | CAP-022 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-124 | gap | CAP-024 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-125 | gap | CAP-025 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-126 | gap | CAP-026 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-127 | gap | CAP-027 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-128 | gap | CAP-033 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-129 | gap | CAP-034 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-130 | gap | CAP-035 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-131 | gap | CAP-036 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-132 | gap | CAP-037 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-133 | gap | CAP-038 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-134 | gap | CAP-039 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-135 | gap | CAP-040 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-136 | gap | CAP-041 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-137 | gap | CAP-042 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-138 | gap | CAP-043 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-139 | gap | CAP-044 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-140 | gap | CAP-054 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-141 | gap | CAP-056 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-142 | gap | CAP-057 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-143 | gap | CAP-058 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-144 | gap | CAP-059 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-145 | gap | CAP-060 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-146 | gap | CAP-061 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-147 | gap | CAP-062 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-148 | gap | CAP-063 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-149 | gap | CAP-064 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-150 | gap | CAP-065 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-151 | gap | CAP-075 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-152 | gap | CAP-076 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-153 | gap | CAP-083 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-154 | gap | CAP-084 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-155 | gap | CAP-085 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-156 | gap | CAP-088 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-157 | gap | CAP-089 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-158 | gap | CAP-090 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-159 | gap | CAP-091 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-160 | gap | CAP-092 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-161 | gap | CAP-093 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-162 | gap | CAP-094 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-163 | gap | CAP-099 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-164 | gap | CAP-100 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-165 | gap | CAP-101 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-166 | gap | CAP-102 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-167 | gap | CAP-103 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-168 | gap | CAP-104 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-169 | gap | CAP-105 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-170 | gap | CAP-111 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-171 | gap | CAP-117 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-172 | gap | CAP-118 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-173 | gap | CAP-119 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-174 | gap | CAP-122 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-175 | gap | CAP-123 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-176 | gap | CAP-125 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-177 | gap | CAP-126 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-178 | gap | CAP-127 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-179 | gap | CAP-129 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-180 | gap | CAP-132 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-181 | gap | CAP-135 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-182 | gap | CAP-137 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-183 | gap | CAP-138 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-184 | gap | CAP-139 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-185 | gap | CAP-140 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-186 | gap | CAP-141 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-187 | gap | CAP-142 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-188 | gap | CAP-143 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-189 | gap | CAP-144 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-190 | gap | CAP-145 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-191 | gap | CAP-146 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-192 | gap | CAP-147 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-193 | gap | CAP-148 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-194 | gap | CAP-149 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-195 | gap | CAP-156 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-196 | gap | CAP-159 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-197 | gap | CAP-161 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-198 | gap | CAP-162 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-199 | gap | CAP-169 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-200 | gap | CAP-172 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-201 | gap | CAP-173 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-202 | gap | CAP-176 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-203 | gap | CAP-177 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-204 | gap | CAP-178 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-205 | gap | CAP-179 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-206 | gap | CAP-182 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-207 | gap | CAP-183 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-208 | gap | CAP-184 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-209 | gap | CAP-185 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-210 | gap | CAP-190 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-211 | gap | CAP-191 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-212 | gap | CAP-192 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-213 | gap | CAP-193 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-214 | gap | CAP-194 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-215 | gap | CAP-195 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-216 | gap | CAP-196 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-217 | gap | CAP-197 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-218 | gap | CAP-198 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-219 | gap | CAP-199 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-220 | gap | CAP-200 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-221 | gap | CAP-202 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-222 | gap | CAP-203 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-223 | gap | CAP-204 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-224 | gap | CAP-207 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-225 | gap | CAP-209 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-226 | gap | CAP-210 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-227 | gap | CAP-212 | drop | Build from legacy screens (Time and absence); the day-timeline prototype is dropped. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-228 | gap | CAP-213 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-229 | gap | CAP-215 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-230 | gap | CAP-219 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-231 | gap | CAP-220 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-232 | gap | CAP-221 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-233 | gap | CAP-222 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-234 | gap | CAP-223 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-235 | gap | CAP-232 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-236 | gap | CAP-233 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-237 | gap | CAP-234 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-238 | gap | CAP-235 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-239 | gap | CAP-236 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-240 | gap | CAP-237 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-241 | gap | CAP-239 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-242 | gap | CAP-243 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-243 | gap | CAP-244 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-244 | gap | CAP-247 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-245 | gap | CAP-250 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-246 | gap | CAP-251 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-247 | gap | CAP-260 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-248 | gap | CAP-264 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-249 | gap | CAP-268 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-250 | gap | CAP-273 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-251 | gap | CAP-274 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-252 | gap | CAP-275 | carry-as-is | Build from legacy screens: built with the new design system, laid out like today's screens. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-253 | design | J4jjulaLJ4QNzqZ1INWydq:3550:12036 | in-scope | In scope, same as the task detail: variants of the approval task-detail screen; built with it. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-254 | design | J4jjulaLJ4QNzqZ1INWydq:3550:12556 | in-scope | In scope, same as the task detail: variants of the approval task-detail screen; built with it. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-255 | design | J4jjulaLJ4QNzqZ1INWydq:3550:13266 | in-scope | In scope, same as the task detail: variants of the approval task-detail screen; built with it. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-256 | design | J4jjulaLJ4QNzqZ1INWydq:3550:13582 | in-scope | In scope, same as the task detail: variants of the approval task-detail screen; built with it. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-257 | design | J4jjulaLJ4QNzqZ1INWydq:3561:11848 | out-of-scope | Out of scope: blank 'Update payment state' prototype steps in Autopay; nothing to build from them. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-258 | design | J4jjulaLJ4QNzqZ1INWydq:3561:11851 | out-of-scope | Out of scope: blank 'Update payment state' prototype steps in Autopay; nothing to build from them. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-259 | design | J4jjulaLJ4QNzqZ1INWydq:3561:11854 | out-of-scope | Out of scope: blank 'Update payment state' prototype steps in Autopay; nothing to build from them. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-260 | design | J4jjulaLJ4QNzqZ1INWydq:3561:11857 | out-of-scope | Out of scope: blank 'Update payment state' prototype steps in Autopay; nothing to build from them. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-261 | design | J4jjulaLJ4QNzqZ1INWydq:3561:11860 | out-of-scope | Out of scope: blank 'Update payment state' prototype steps in Autopay; nothing to build from them. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-262 | design | J4jjulaLJ4QNzqZ1INWydq:3561:11863 | out-of-scope | Out of scope: blank 'Update payment state' prototype steps in Autopay; nothing to build from them. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-263 | design | J4jjulaLJ4QNzqZ1INWydq:3561:11866 | out-of-scope | Out of scope: blank 'Update payment state' prototype steps in Autopay; nothing to build from them. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-264 | design | J4jjulaLJ4QNzqZ1INWydq:3561:11869 | out-of-scope | Out of scope: blank 'Update payment state' prototype steps in Autopay; nothing to build from them. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-265 | design | J4jjulaLJ4QNzqZ1INWydq:3561:11872 | out-of-scope | Out of scope: blank 'Update payment state' prototype steps in Autopay; nothing to build from them. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-266 | design | J4jjulaLJ4QNzqZ1INWydq:3561:11875 | out-of-scope | Out of scope: blank 'Update payment state' prototype steps in Autopay; nothing to build from them. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-267 | design | J4jjulaLJ4QNzqZ1INWydq:3561:11878 | out-of-scope | Out of scope: blank 'Update payment state' prototype steps in Autopay; nothing to build from them. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-268 | design | J4jjulaLJ4QNzqZ1INWydq:3561:11881 | out-of-scope | Out of scope: blank 'Update payment state' prototype steps in Autopay; nothing to build from them. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-269 | design | J4jjulaLJ4QNzqZ1INWydq:3561:11884 | out-of-scope | Out of scope: blank 'Update payment state' prototype steps in Autopay; nothing to build from them. | Dan-Mihai Cuc | 2026-10-01 |
| DEC-270 | design | J4jjulaLJ4QNzqZ1INWydq:3561:11887 | out-of-scope | Out of scope: blank 'Update payment state' prototype steps in Autopay; nothing to build from them. | Dan-Mihai Cuc | 2026-10-01 |
