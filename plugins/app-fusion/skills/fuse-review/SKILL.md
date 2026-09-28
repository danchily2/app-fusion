---
name: fuse-review
description: Asks a person the questions only a person can answer in a fusion, and records the answers so the plan and the build honor them. These cover which app's behavior survives where the apps diverge, what happens to features with no design, new designed features, flagged business rules, platform features only one app has, the target stack and the store listing. Writes DECISIONS.json and DECISIONS.md.
argument-hint: "<program> [all|blocking|conflicts|gaps|rules|platform|design|stack|continuity]"
arguments: program scope
---

Ask a person to decide what the plugin may not decide for program `$program`, and record each answer word for word.
This command asks in pop-ups and records answers: it never infers an answer, and it never edits the catalogs.

## 1: What is open

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/decisions.py" open $program --json
```

It lists the open questions, each with `about`, `kind`, `question`, `options` and sometimes `detail`, most important
first. `$scope` narrows them:
- **blocking** (the default): priority 1–2, which covers conflicts, stack, store identity, flagged P0 rules, and
  capabilities with no design.
- **all**: everything.
- a single kind: `conflicts`, `gaps`, `rules`, `platform`, `design`, `stack` or `continuity`.

Say how many questions will be asked (about a minute per ten). If none is open, say so and give the next command.

## 2: Ask

Use the AskUserQuestion tool, never chat text, with at most four questions per call. Each question:
- has the id (`CAP-014`, `RULE-007`, `PLT-012`) as its header
- puts the question and the one-line detail in the text
- uses the listed options, written as plain words. For example, `take:vmm` becomes "Keep vmm's behavior", and
  `both-by-role` becomes "Keep both, per role".

The person can type a note instead of choosing. Keep it in their words. Stop when they say to.

Give context for the heavy questions:
- **Conflicts.** Show the divergence lines from `CAPABILITIES.md` and any conflicting rules from `BUSINESS_RULES.md`.
  If a design screen exists for the capability, say what the design shows: often the design already answers it
  (`design`).
- **Capabilities with no design.** The options:
  - `design-it`: a designer adds it. The build waits.
  - `carry-as-is`: build it with the design system from the legacy screens.
  - `drop`: users lose it, so say who uses it today.
  - `defer`: later phase.
- **The stack.** Summarize the brief's comparison if one exists. Otherwise give the assessment's recommendation with
  its reason. The answer is one of react-native, native, swiftui, compose, flutter, kmp.
- **Store identity.** Explain that the listing kept decides whose users update in place, and whose must move (see
  `${CLAUDE_PLUGIN_ROOT}/references/continuity.md`).

Verdicts the person already typed in the request ("CAP-014 take vmm", "RULE-007 wrong: it truncates on purpose") are
recorded as given, with no pop-up. In a headless run with nothing typed, ask nothing: leave every question open and
say so.

## 3: Record

Write the answers to a JSON list (a file in the session's scratch or temp folder). Each entry is
`{"about": "...", "kind": "...", "choice": "...", "question": "...", "note": "<their words>", "by": "<their name if given>"}`.
Then run:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/decisions.py" add-json $program <that file>
```

The script validates every choice for its kind and refuses an invalid one: fix the entry, never loosen the check.
Stack and store answers are also copied into `program.json` with
`workspace.py intent $program --stack <s>` and `--store <app|new-listing>`. Then refresh what depends on the decisions:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/trace.py" $program        # when traceability.json exists
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/render.py" platform $program
```

## 4: What happens next

Tell the person, in three lines:
- A capability marked `defer` or with an unanswered conflict is not built. The brief lists it as an open question
  and blocks the phase that needs it.
- A rule marked `wrong` is not pinned as the oracle. `discuss` blocks the capability's build until it is settled.
- They can change any answer by running this again, or edit `DECISIONS.json` through this command, never by hand.

Refresh the report. The next command is `/app-fusion:fuse-brief $program`, or run it again if the brief exists,
because the decisions changed.
