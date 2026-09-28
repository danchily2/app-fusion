---
name: fuse-status
description: Shows where an App Fusion program stands and gives the exact next command. It reports which steps are done, what is stale, the open questions for a person, the plan's approval, and which capabilities are built and proven. Run it any time, especially when unsure what to do next.
argument-hint: "[program]"
arguments: program
---

Report where program `$program` stands, in one screen. This command reads and never modifies, except that it
refreshes `analysis/$program/REPORT.html`.

1. If `$program` is empty, run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/status.py" --list`. With one program, use
   it. With several, ask which one. With none, the answer is
   `/app-fusion:fuse <name> --source <app>=<path> --source <app>=<path>`.
2. Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/status.py" $program` and show its output: the stages, the legacy
   links, capabilities, design coverage, built and proven counts, open questions, the brief's approval, anything
   stale, and the next command.
3. **Secrets hygiene.** Check that `analysis/.gitignore` covers `SECRETS.local.md` and `*.local.patch` (in a git
   repository, `git check-ignore -q analysis/$program/SECRETS.local.md`). If `SECRETS.local.md` exists, confirm it is
   not tracked (`git ls-files --error-unmatch` should fail). If either check fails, say so prominently and recommend
   rotation.
4. **Legacy untouched.** Any app the status shows as CHANGED has local changes in its working tree. Say whether they
   predate the program (compare with `PREFLIGHT.md`). The plugin never writes there, so a change means someone else
   edited it, and the analysis may describe a moving target.
5. Refresh the report: `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/build_report.py" $program`.

End with three lines:
- **Where you are:** the furthest completed step and how much it covers ("mapped, 38 capabilities; 4 of 11 built,
  2 proven").
- **What is stale:** the stale lines, or "nothing".
- **Next command:** the exact command status.py gave, with its one-line reason. Never call a capability done until
  `fuse-verify` says PROVEN and a person has signed. Put `fuse-verify` ahead of building the next capability.
