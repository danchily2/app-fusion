---
name: fuse-brief
description: Writes the Fusion Brief, the phased plan an approver signs before anything is built. It covers the target stack decision, the architecture of the new app, the role matrix, the continuity plan for every legacy app's users (store listing, data, sessions, push, links, analytics), phases by journey with checkable entry and exit criteria, the behavior contract and the open questions. Writes CONTINUITY.md and FUSION_BRIEF.md, then stops. With `approve`, a named person approves it.
argument-hint: "<program> [approve]"
arguments: program
disable-model-invocation: true
---

Synthesize everything under `analysis/$program/` into the **Fusion Brief**: the one document an approver signs and
engineering executes. Nothing is built before it is approved. With `approve` after the program name in
`$ARGUMENTS`, skip to **Approval** at the end.

## Inputs

**Required:**
- `program.json` and `INTENT.md`
- `ASSESSMENT.md` and `PLATFORM.md` (from `fuse-assess`)
- `capabilities.json` and `CAPABILITIES.md` (from `fuse-map`)
- `rules.json` and `BUSINESS_RULES.md` (from `fuse-rules`)

If one is missing, say which and stop.

**Read when present:**
- `PREFLIGHT.md`: the person's answers bind the plan.
- `traceability.json` and `TRACEABILITY.md`: without them, every capability is "no design" and the brief says so.
- `DECISIONS.json` and `DECISIONS.md`.
- `overlap.json` and `design/design.json`.
- `${CLAUDE_PLUGIN_ROOT}/references/continuity.md`, and the target profile
  `${CLAUDE_PLUGIN_ROOT}/references/targets/<stack>.md` once the stack is known.

**The person's words bind the plan.** Never override `INTENT.md`, a preflight answer or a decision with a guess.
- A capability with an undecided conflict, or a `discuss` rule, is **blocked**. List it under Open Questions and in
  its phase's entry criteria, and never plan around it.
- A capability decided `drop` is out of scope and listed as such, with the users who lose it.
- A `defer` capability goes to a later phase.

**Staleness.** If any input is newer than an existing brief, regenerating is justified. If the brief is newer than
every input, ask what changed before writing. Put the input timestamps in the brief's header.

## CONTINUITY.md (write this first)

Existing users are the one thing no test in the repositories protects. For each legacy app, using `PLATFORM.md`,
`program.json` (`storeIdentity`) and the references, cover:

1. **Store identity.** Which listing and bundle or application id the new app ships under. Whose users get it as an
   update, and whose must install it. With `storeIdentity: undecided`, give the options and a recommendation, and make
   it the brief's first open question.
2. **Sign-in and session.** Can the session carry over? Keychain access groups need the same team id, and the
   updated app keeps its container. Otherwise it is a one-time re-login, and the plan says how the message reads.
3. **Local data.** What each app stores locally (`PLATFORM.md` storage items: Realm, AsyncStorage, MMKV, UserDefaults,
   Core Data) and whether it must move. Moving it goes through app-group containers or server-side restore. Dropping
   it means it is re-fetched.
4. **Push.** Tokens are per app id: when and how the new app registers. What happens to notifications sent to the
   old app's tokens, and which notification extensions the new app needs.
5. **Links.** Universal and app links, and URL schemes, of every legacy app (from `PLATFORM.md`). The new app claims
   them (AASA and assetlinks files on each domain) or they redirect. Old links in emails keep working.
6. **Analytics and crash reporting.** Event wire names are kept unless a decision says otherwise, because dashboards
   depend on them. Cover user ids across apps, and which projects the new app reports to.
7. **The other app's sunset.** In-app notice, deep link to the new app, forced update, removal from the store. The
   plan sequences these; it states no dates.

## FUSION_BRIEF.md

1. **Objective.** One paragraph: from which apps, to what, for whom, and why now (from INTENT and ASSESSMENT).

2. **Target stack decision** (an ADR).
   - **Context:** the sources' stacks, team skills from PREFLIGHT, and the native features in use (extensions,
     background modes).
   - **Options:** two to four, each with its trade-offs for *these* apps: reuse of a source's code, platform features,
     performance, hiring and team.
   - **Decision:** from `program.json` or DECISIONS when set, else a clearly marked **Recommendation** that the
     approval confirms.

3. **Target architecture.**
   - A Mermaid C4 container diagram: the app, its modules, the backends and third-party SDKs.
   - The module map: domains to feature modules, following capabilities, never the old apps' folders.
   - The navigation shell per persona: roles and entry points, and a person with both roles.
   - **The role matrix.** Each legacy app served one role, so no legacy code says who sees what in the merged app.
     A table from capability to the personas who see it, with what decides a person's role (a claim in the token, a
     tenant setting, an API call). A capability visible to a role that never had it is a decision, listed under Open
     Questions (`roles` decisions record the answers). The tests include a negative case per role: an employee-only
     account never reaches approvals.
   - Shared foundations: the design system from the Figma tokens, one API client per backend, auth, storage,
     analytics, flags, i18n with the union of locales.
   - A table from capability to new module to legacy implementations.

4. **Phased sequence.** Phase 0 is the foundation (`fuse-scaffold`). Phase 1 is a **pilot**: one journey, one to three
   capabilities, chosen to exercise both personas and the riskiest platform feature. Later phases go by journey or
   domain: low-risk and few dependencies first, P0-heavy capabilities once the harness is proven. A last phase covers
   continuity and cutover, which people carry out. Write every phase in exactly this shape, because the build and the
   status read it:

   ```
   #### Phase N — <name>
   Command: /app-fusion:fuse-scaffold | /app-fusion:fuse-build
   Capabilities: CAP-001, CAP-002
   Journeys: JRN-001
   Scale: S | M | L | XL
   Risk: <level>; <top two risks and their mitigations>
   Entry criteria:
   - [ ] <a checkable precondition>
   Exit criteria:
   - [ ] <a checkable condition, such as "fuse-verify reports PROVEN for CAP-001 and CAP-002">
   ```

   - **Scale** is a size relative to the other phases, never a duration. State no weeks, dates or person-months.
   - **Criteria are conditions, never states.** The build commands treat them as binding. They may tick a box or add
     a `Proposed revision:` line, but never reword a criterion.
   - Tell the approver they steer by editing this file.
   - Draw the phases as a Mermaid `flowchart LR` of sequence and dependencies, never a gantt chart.
   - Say that Phase 1 is a pilot and this brief a hypothesis: what the pilot surfaces is expected to revise it.

5. **Business walkthroughs.** For each journey in `capabilities.json`, a short table: persona, the steps in business
   words, today's implementation in each app, and the phase that builds it. This is the section non-technical
   approvers read.

6. **Behavior contract.** What must be proven before each phase ships (the ten checks of `scripts/fusion_proof.py`):
   - the P0 and P1 rules of its capabilities, excluding those marked `wrong` and those of an app a decision did not
     keep; a rule with a suspected legacy defect is decided (keep or fix) in its capability's build plan
   - the `required` and kept platform items (links, schemes, push, notification categories, extensions, groups, the
     store identity), checked for the whole app by `platform_parity.py`
   - each journey, on every target platform
   - API, string and analytics-event parity per capability, and locale coverage
   - the design copy

   Flag any P0 rule below High confidence as needing its owner before its phase starts.

7. **Validation strategy per phase.** Unit tests pinning rules, Maestro journeys on both platforms, the static
   API-parity check (or recorded traffic compared as HAR), i18n parity, design-text parity, a canary, and visual
   sign-off by a person.

8. **Open questions.** Every undecided item, each a checkbox for the approver: stack, store identity, conflicts, gaps,
   discuss rules, and continuity choices.

9. **Approval.** One line: "Approval is recorded in `SIGNOFF.json` by `/app-fusion:fuse-brief $program approve`, and
   binds to this exact text: any later edit to the brief needs a new approval." Never write a name, a date or a
   signature line into the brief yourself.

## Review before you present

Give the draft to `app-fusion:architecture-critic`: "Review analysis/$program/FUSION_BRIEF.md and CONTINUITY.md
against CAPABILITIES.md, PLATFORM.md and DECISIONS.md. Look for continuity holes for either app's users, an unrealistic
pilot, missing NFRs (offline, accessibility, app size, minimum OS), over-engineering, and phase-order mistakes." Apply
every Blocker and High finding, and list the rest in an appendix.

## Finish

Refresh the report with `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/build_report.py" $program`. Present a summary: the
stack decision or recommendation, the phases, the pilot, the top continuity risks and the open questions. Then
**stop: write nothing further.** "No objection" is not approval. The next step is a person running
`/app-fusion:fuse-brief $program approve`.

---

## Approval (`approve`)

Only a person approves, with their own name. Read `FUSION_BRIEF.md` and `CONTINUITY.md`, and show the summary above.
1. **Scope.** Ask with AskUserQuestion what the approval covers: "Every phase", "Phase 0 and Phase 1 only (the pilot)",
   or "Not yet". "Not yet" records nothing: say what they want changed and stop.
2. **What the approval settles.** When `program.json` still has the stack or the store listing undecided, ask each with
   AskUserQuestion, the brief's recommendation first: "Use <stack> (the brief's recommendation)" and the other options;
   for the store listing, each app's listing and "a new listing". Record the answers as decisions
   (`decisions.py add-json`: kind `stack` about `stack`, kind `continuity` about `continuity:store-identity`) and in
   `program.json` (`workspace.py intent $program --stack <s> --store <app|new-listing>`). The guard asks the person to
   confirm each recording command.
3. **The name.** Ask for the approver's name (they type it), then run
   `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/signoff.py" $program brief --by "<their name>" --covers "<all | Phase 0, Phase 1>"`.
   It binds the approval to the brief's current text.

In a headless run, approve nothing and say so. Afterwards the next step is `/app-fusion:fuse-scaffold $program`; when
the approval covers only some phases, `fuse-status` asks for a new approval before the next phase.
