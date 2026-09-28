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

Reuse `analysis/$program/shards.json` when it is newer than every inventory. Otherwise run
`python3 "${CLAUDE_PLUGIN_ROOT}/scripts/shard.py" $program [--app <app>] [--pattern <glob>]`. Rules use **every**
shard, including logic (services, reducers, utils), because that is where validation and calculation live.

## 2: Estimate, ask if large, launch

The fan-out is one extractor per shard, one citation referee per rule, two judges per P0 rule, and one conflict judge
per shared capability. Typical counts are 6 to 12 agents per shard. Say the estimate. With more than 25 shards, ask
first (AskUserQuestion): "Run all N", "Only a slice (an app or a pattern)", "Cancel". A run is capped at 1,000 agents,
so split more than about 80 shards into parts of at most 80, run them one after another, and merge.

**With the Workflow tool** (this command authorizes it), call it by name. If the tool does not know the name, pass
`scriptPath: "${CLAUDE_PLUGIN_ROOT}/workflows/extract-rules.js"` instead:

```
Workflow({
  name: "app-fusion:fuse-extract-rules",
  args: {
    program: "$program",
    apps: [ {name, product, stack} ... ],
    shards: [ ... shards.json ... ],
    capabilities: [ {id, name, domain, apps: [<app names that implement it>], fusion} ... ]   // [] if no map yet
  }
})
```

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
- how many are flagged for a person (P0 below High confidence, with a suspected defect or with a question)
- the cross-app conflicts, by capability
- how many candidates the referees rejected (the quality the verification bought)

Refresh the report with `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/build_report.py" $program`. The next step is
`/app-fusion:fuse-review $program`: every conflict and every flagged P0 rule is a question only a person can answer.
