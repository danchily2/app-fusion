---
name: fuse-rules
description: Mines the business rules both apps enforce on the client (validations, calculations, eligibility and role visibility, status lifecycles, formatting and rounding, offline and retry policies) into Given/When/Then cards with file:line citations, each tied to its app and capability and re-checked by a second agent. It also finds rules the two apps decide differently. Writes BUSINESS_RULES.md, DATA_OBJECTS.md and rules.json.
argument-hint: "<program> [--app APP] [--pattern GLOB]"
arguments: program
---

Extract the business rules of the source apps of `$program`: the decisions the code makes that users rely on, and
that silently change when two apps become one. Prioritize calculations, validations, eligibility and visibility by
role, status lifecycles and formatting over plumbing.

Needs the inventories. The capability map (`capabilities.json`) is strongly recommended: rules are attached to
capabilities, and conflicts are found per shared capability. Never modify `legacy/`. Run every subagent in the
foreground and wait for it.

## 1: Shards

Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/shard.py" $program --for rules [--app <app>] [--pattern <glob>]`. Run it
again even when `shards.json` exists, so `workflow-args.rules.json` carries the current capability ids from
`capability_index.json`; `--for rules` leaves the map's arguments as they are. Rules use **every** shard, including
logic (services, reducers, utils) and a React Native app's native code, because that is where validation and
calculation live.

## 2: Estimate, ask if large, launch

The fan-out is one extractor per shard, one citation referee per rule, two judges per P0 rule, and one conflict judge
per shared capability, so the count follows how many rules the code holds. Measured on two production apps, a 4-shard
calendar slice produced 153 rules and used 171 agents, about 43 per shard (about $5 per shard); plumbing-heavy code
needs far fewer. Say the estimate. With more than 10 shards, ask first (AskUserQuestion): "Run all N", "Only a slice
(an app or a pattern)", "Cancel". A run is capped at 1,000 agents, so split into parts of at most about 20 shards,
run them one after another, and merge.

**With the Workflow tool** (this command authorizes it), call it by name. If the tool does not know the name, pass
`scriptPath: "${CLAUDE_PLUGIN_ROOT}/workflows/extract-rules.js"` instead:

```
Workflow({
  name: "app-fusion:fuse-extract-rules",
  args: <the JSON object in analysis/$program/workflow-args.rules.json, passed as it is>
})
```

Each extractor reads its shard file and `capability_index.json` itself, so the call carries ids and paths only.

Record the Run ID. If the run stops without a result, **resume, never restart**: identical `name` and `args` plus
`resumeFromRunId`. A completed run with `rerunShards` is rendered as it is. Then offer one follow-up run on those
shards, and merge the rules, de-duplicating by `app`, `source` file and name.

**Without the Workflow tool**, give one `app-fusion:business-rules-extractor` per group of shards, at most 6 at once,
the capability list and the card format of `RULE_SCHEMA` in `workflows/extract-rules.js`. Then verify before you
write: read each cited line yourself, and drop any rule supported only by a comment or a string. For each
shared-diverged or shared-same capability with rules from two apps, compare them yourself and list the conflicts.

## 3: Render

Save the returned object as `analysis/$program/rules_result.json` and run:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/render.py" rules $program
```

This writes:
- `BUSINESS_RULES.md`: the summary table, the cross-app conflicts, cards by category (headings exactly
  `### RULE-NNN: <name>`), rules needing an owner's confirmation, instruction-shaped text found, and coverage gaps.
- `DATA_OBJECTS.md`.
- `rules.json`, with stable ids: a rule keeps its RULE id across re-runs.

## Finish

Report:
- total rules, by category and priority
- how many are flagged for a person, by priority: P0 rules with any doubt block the plan; P1 and P2 rules with a
  suspected defect or a question are asked when their capability is built. Say plainly when there is no P0 rule
  at all: the proof pins the P1 rules as well, but only P0 rules get the two-judge panel
- the rules no capability owns: each P0 one is a question (`attach`)
- the cross-app conflicts, by capability
- how many candidates the referees rejected (the quality the verification bought)

Refresh the report with `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/build_report.py" $program`. The next step is
`/app-fusion:fuse-review $program`: every conflict and every flagged P0 rule is a question only a person can answer.
