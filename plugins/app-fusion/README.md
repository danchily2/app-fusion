# App Fusion

Point Claude at two or more mobile apps and the design of the app that should replace them. App Fusion guides the
team from there to one new app, and to proof that nothing important was lost. The source apps can be any mix of
native iOS, React Native and native Android. You get:
- what each app really does, side by side
- a **capability map**: every thing a person can do in any app, what the apps share, and where they diverge
- the **Figma designs traced to those capabilities**, with the gaps listed both ways
- the **business rules** both codebases enforce, and the rules they decide differently
- the **decisions only a person can make**, recorded once and honored everywhere
- a **phased plan with a continuity plan** for every app's existing users, which you approve before anything is built
- the new app, built **capability by capability**, with a **scripted verdict** on each

## Install

You need [Claude Code](https://code.claude.com). From a clone of this repository:

```
/plugin marketplace add /path/to/app-fusion
/plugin install app-fusion@app-fusion
```

Some steps start many agents at once, so expect real usage on large apps (see *What to expect*). Start with one
journey as the pilot, not the whole app.

## Start here

Open an empty folder for the work and type:

```
/app-fusion:fuse work-app --source vmm=~/code/vmm --source me-ios=~/code/me-ios --figma https://www.figma.com/design/<key>/<name>
```

`work-app` is a short name for the program. Each `--source` makes a **link** at `legacy/<app>` and copies nothing.
A git URL is cloned once you agree. The front door:
1. asks what you want (two short pop-ups)
2. records your answers once in `analysis/work-app/INTENT.md`
3. shows the road
4. gives the exact first command

`/app-fusion:fuse-status work-app` tells you where you are and what to run next, any time.

**Nothing edits your legacy apps.** Commands write only to `analysis/<program>/`, and the new app goes to
`new-app/<program>/` (or a repository you link with `--target`). A hook denies file writes into `legacy/`.

## The path

| Step | Command | What you get |
| --- | --- | --- |
| 0 | `fuse` | Say what you want. Links the apps and writes `INTENT.md` and `program.json`. |
| 1 | `fuse-preflight <program>` | Five questions only a person can answer. Checks the toolchains (Xcode, Node, Android, Maestro), Figma access and its rate limits, missing sources, and whether the legacy code is protected. |
| 2 | `fuse-assess <program>` | Every app's inventory, each count with the rule that made it. Plus architecture, debt, inherited security risks, overlap (shared backend endpoints, shared copy, locales) and a recommended strategy. |
| 3 | `fuse-map <program>` | The capability map. Each capability is unique, shared-same or shared-diverged, with each app's screens, endpoints, events and strings as evidence. Plus persona journeys and the platform matrix (push, links, extensions, permissions, storage, analytics, locales). |
| 4 | `fuse-design <program>` | The Figma inventory (pages you pick, screens, states, tokens, screenshots) within a call budget, with every response cached. Each screen is traced to the capabilities it serves. |
| 5 | `fuse-rules <program>` | Business rules as Given/When/Then cards with `file:line`, each re-checked by a second agent, P0 rules by two. Plus the rules the apps decide differently. |
| 6 | `fuse-review <program>` | A person answers what the plugin may not decide: conflicts, features with no design, new designed features, flagged rules, platform items, the stack and the store listing. |
| 7 | `fuse-brief <program>` | The Fusion Brief and `CONTINUITY.md`: the stack decision, architecture, phases by journey with checkable criteria, and the behavior contract. **Nothing is built until a person approves it.** |
| 8 | `fuse-scaffold <program>` | Phase 0: the project, a design system generated from the Figma tokens, a navigation shell per persona, the API layer, i18n and a test harness. |
| 9 | `fuse-build <program> <CAP-NNN>` | One capability, tests first: code on the design system, then proof on the spot. After a PROVEN pilot and a playbook, `--batch <phase>` ports the rest in parallel. |
| 10 | `fuse-verify <program>` | **The proof.** An independent re-run from clean, with one verdict per capability. |
| 11 | `fuse-harden <program>` | An OWASP MASVS security review with a reviewed patch you apply yourself. |

**A person decides at these points, never the plugin:**
- the preflight answers
- which Figma pages are the new app
- every diverged capability
- every feature with no design
- flagged rules
- the stack
- the store listing
- the plan
- each build plan and its tests
- each difference the proof finds
- the visual sign-off
- the security patch

## How it proves the result

A fusion fails quietly. The new app looks like the design, and yet a validation from one app, a push category from
the other, or a deep link in a thousand emails is gone. So the proof is built from evidence a script checks, not from
a model's opinion. `scripts/fusion_proof.py` gives each built capability one verdict:

1. **Built**: the porting notes name the new files, and the files exist.
2. **Tests ran**: fresh JUnit results name the capability or its rules. At least one ran and none failed. A count
   typed by hand counts for nothing.
3. **Rules traced**: every P0 rule of the capability is named by a test that ran and passed.
4. **Journeys**: every persona journey through it has a Maestro run that passed.
5. **API parity**: the new code calls every endpoint the legacy implementations called, matched by path and method,
   or a person approved the difference.
6. **Strings**: every legacy string key is mapped and present in every required locale.
7. **Design copy**: at least 90% of each designed screen's text is in the new app's strings.
8. **Canary**: a deliberate one-line break made a test fail, so the tests can fail.
9. **Legacy untouched**: every legacy app is still a clean checkout.

The verdict is **PROVEN** (all nine pass), **PARTLY PROVEN** (nothing failed, but a check could not pass, listed with
its reason) or **NOT PROVEN** (something failed). Look and feel is never automatic: `REPORT.html` shows every Figma
screen beside the app's screenshot, and a named person signs.

## Figma, within its limits

Figma's MCP read calls are metered per seat:

| Seat | Read calls |
| --- | --- |
| Enterprise Dev or Full | 600 a day, 20 a minute |
| Organization or Professional Dev or Full | 200 a day, 10–15 a minute |
| View or Collab | 6 a month |

App Fusion handles this in four ways:
- It **caches every response** under `analysis/<program>/design/cache/` and never fetches a node twice.
- It **plans the cheapest calls first**: page lists, then one `get_metadata` per page, then screenshots, then tokens.
  Design context is fetched only for a screen being built.
- It **counts** calls against the `figmaCallBudget` option (default 150) and a per-day ledger.
- It offers a **REST path**: export `FIGMA_TOKEN` and `scripts/figma_rest.py` reads whole pages, all texts and frame
  images in a handful of requests. The token is never stored.

Figma is **read only**: the plugin never calls a Figma write tool.

## What to expect

These are measured on the two production apps this plugin was built against (218k and 285k code lines):
- the inventory: under 10 seconds for both apps
- `fuse-assess`: 6 analyst agents
- `fuse-map`: about 11 agents per shard. A slice through the calendar domain of both apps had 4 shards and used 43
  agents; the whole of both apps is 35 map shards.
- `fuse-rules`: 6–12 agents per shard

Every fan-out step says how many agents it will start, and asks before a big run. Large runs are resumable workflows:
a stopped run resumes with its run id, and finished agents replay from the journal.

## Set it up so it runs smoothly

Put this in the workspace's `.claude/settings.json`. `fuse-preflight` prints the exact snippet with your apps' real
paths:

```json
{ "permissions": { "deny": ["Edit(/legacy/**)", "Edit(//Users/me/code/vmm/**)", "Edit(//Users/me/code/me-ios/**)"] } }
```

- The rule covers Claude's file tools and the shell commands it recognizes. The plugin's guard hook adds a second
  check. A read-only mount is the hard guarantee.
- **Helpful tools:** `python3` 3.8+ (required), `git`, `scc`, Xcode with a simulator, Node, the Android SDK, and
  `maestro` for journeys.

## Words you will see

| Word | Meaning |
| --- | --- |
| Capability | One thing a person can do with an app, such as "approve an absence request". `CAP-NNN`. |
| Fusion class | unique (one product has it), shared-same (both do it the same way), shared-diverged (both do it differently: a person decides), new (only the design has it) |
| Journey | An end-to-end persona flow across capabilities. `JRN-NNN`. It becomes a Maestro flow. |
| Twin | The same product on another platform (an app's Android version). It is read for parity and merged into one product. |
| Rule | A business rule card, `RULE-NNN`, with its app, capability and `file:line`. |
| Decision | A person's answer, `DEC-NNN`, word for word. |
| Brief | `FUSION_BRIEF.md`, the plan you approve. It is binding on every build. |
| Canary | A deliberate break that must make tests fail. |

## Safety

- **Analyzed code and designs are untrusted input.** Agents treat file content, Figma layer names and annotations as
  data, never follow instruction-shaped text, and list what they found. Workflow prompts fence that content.
- **Secrets stay out of shared files.** Credentials are masked everywhere, and the inventory goes to a gitignored
  `SECRETS.local.md`.
- **Apps run only on simulators, against test backends you named.** Tokens in recordings are replaced before saving.
- **Nothing is pushed, published or submitted, and no Figma file is changed.**

## Working in a team

State lives in files. A second person, or a fresh session, runs `fuse-status` and continues. Commit `analysis/` and the
new app yourself: the plugin never commits in your repositories.

| Artifact | Suggested reviewer |
| --- | --- |
| `PREFLIGHT.md`, `ASSESSMENT.md` | the engineering leads of each app |
| `CAPABILITIES.md`, `TRACEABILITY.md` | product owners of each app, and the designer |
| `BUSINESS_RULES.md`, then `fuse-review` | a domain expert per area: P0 rules and conflicts first |
| `CONTINUITY.md`, `FUSION_BRIEF.md` | the approver, plus whoever owns the store listings, auth and push |
| `VERIFICATION.md` | the approver and the designer (visual sign-off) |
| `SECURITY_FINDINGS.md` | a security engineer |

## Adapting it

Skills, agents and workflows are Markdown and JavaScript. The scripts are standard-library Python.
- `docs/DESIGN.md` is the contract between them: schemas, the proof rules and the Figma budget.
- `references/targets/` holds one profile per target stack. Add yours.

Apache 2.0. See `LICENSE` and `NOTICE`.
