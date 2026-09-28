---
max_turns: 60
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, AskUserQuestion, Agent]
runs: 2
---

/app-fusion:fuse work --source mgr=./src-mgr --source emp=./src-emp
