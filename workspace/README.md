# The work-app workspace

The App Fusion analysis of Visma Manager (`vmm`) and Mobile Employee (`me-ios`), so far one slice of both apps: the
calendar, absence and time area (about 24k of 500k code lines). Open `analysis/work-app/REPORT.html` for an overview.

| File | What it holds |
| --- | --- |
| `analysis/work-app/ASSESSMENT.md` | both apps' inventories, architecture, inherited risks, the recommended strategy |
| `analysis/work-app/CAPABILITIES.md` | 29 capabilities of the slice (5 where the apps differ), 8 persona journeys |
| `analysis/work-app/BUSINESS_RULES.md` | 153 rules with Given/When/Then examples, 14 cross-app conflicts |
| `analysis/work-app/PLATFORM.md` | push, links, extensions, notification categories, storage, SDKs of each app |
| `analysis/work-app/CONTINUITY.md`, `FUSION_BRIEF.md` | the draft plan: 10 phases, not approved |

The analysis describes these commits:

| App | Repository | Branch | Commit |
| --- | --- | --- | --- |
| vmm | https://github.com/Visma-Manager/vmm | develop | `342cb745f66b70d9c715244d6d5a937d4e18e6fc` |
| me-ios | https://github.com/Visma-Mobile-Employee/me-ios | development | `a3600e7d6d899ee40044f04fb07bcb5a9e07006f` |

## Continue on another machine

1. Clone both apps at those commits (or at newer ones, then re-run the map for what changed).
2. From this folder, link them. This records nothing new in the analysis except the links:

   ```bash
   python3 ../plugins/app-fusion/scripts/workspace.py init work-app --source vmm=<path to vmm> --source me-ios=<path to me-ios>
   ```

3. Start Claude Code in this folder with the plugin: `claude --plugin-dir ../plugins/app-fusion` (or install it from
   the repository's marketplace), then run `/app-fusion:fuse-status work-app`. It names the next step: today, the
   30 questions only a person can answer (`/app-fusion:fuse-review work-app`).
4. Run `/app-fusion:fuse-preflight work-app` once there: it prints the permission deny rules for that machine's paths.

`legacy/` (the links) and `SECRETS.local.md` (credentials found in the code, masked everywhere else) are never
committed. The next steps are still open: the new app's Figma link, a person's answers, the approval of the brief.
