---
name: fuse-assess
description: Answers "what are we dealing with?" for every source app, side by side. It covers the deterministic inventory (screens, routes, endpoints, events, strings, storage, platform features, dependencies, tests, each count with its rule), architecture, technical debt, inherited security risks, overlap between the apps, and a recommended fusion strategy. Writes ASSESSMENT.md.
argument-hint: "<program>"
arguments: program
---

Assess the source apps of `$program` so an engineering lead can take a fact-based picture into a planning meeting.
Read `analysis/$program/program.json`, `INTENT.md` and `PREFLIGHT.md` first. If `program.json` is missing, stop: the
fix is `/app-fusion:fuse $program`. Never modify `legacy/`. Run every subagent in the foreground and wait for its
result: never end your turn while one is still running.

## Step 1: Deterministic inventory

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/inventory.py" $program --all
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/render.py" overlap $program
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/render.py" platform $program
```

These write `apps/<app>/inventory.json`, `strings.json` and `INVENTORY.md`, then `overlap.json` (shared backend
endpoints, shared UI copy, locales) and `platform.json` with `PLATFORM.md`. **Every count is printed with its rule.**
Quote the rule with any number you repeat, because two numbers made by different rules are different facts. An app
whose stack has no extractor (Flutter, a hybrid web shell) exits with code 3: give it to an analyst agent in Step 2
and say the inventory is model-derived.

## Step 2: Read each app (subagents in parallel, one of each per app)

Choose the analyst by stack: `app-fusion:ios-analyst`, `app-fusion:rn-analyst` or `app-fusion:android-analyst`.

1. **Analyst: structure.** "Read legacy/<app>, starting from analysis/$program/apps/<app>/INVENTORY.md. Say what the
   app is for and who uses it. Name its 5–12 functional areas (the screens, files and endpoints of each, as a table)
   and the architecture (navigation, state, API layer, persistence, DI). Describe the platform features it depends on
   (push, links, extensions, background work, biometrics) with evidence. Say what is unusual about it. Return
   markdown with `path:line` citations, and end with Confidence & gaps."
2. **Analyst: debt and risks.** "Identify the technical debt in legacy/<app> that matters for a rebuild, and return
   the top 8 with `path:line`. Cover deprecated APIs and SDKs, code duplicated across layers, god objects, missing
   error handling, hard-coded config, dead features, and anything the new app must not copy. Mask any credential."
3. **`app-fusion:security-auditor`.** "Quick inherited-risk pass on legacy/<app> for the new app's planning: secrets
   in source or config, insecure storage of tokens or personal data, network exceptions, unvalidated deep links,
   exported components. Return the top 10 as a CWE-tagged table with `path:line` and severity. Mask every credential
   as `file:line` plus a 2–4 character preview."

Wait for all of them.

## Step 3: Secrets first

If any agent found a credential, make sure `analysis/.gitignore` holds `SECRETS.local.md` and `*.local.patch` (in a
git repository, check with `git check-ignore -q analysis/$program/SECRETS.local.md`). Write
`analysis/$program/SECRETS.local.md` with, per credential: the masked preview, `file:line`, the type, what it grants,
a guess at production or test, and rotation advice. No shareable file ever holds a raw value.

## Step 4: Write ASSESSMENT.md

`analysis/$program/ASSESSMENT.md`:

1. **Executive summary**, 4–6 sentences: what each app is, for whom, how big, how healthy, how much they overlap
   (from `overlap.json`), and the headline recommendation.
2. **Side by side**: a table of the key counts per app (screens, routes, endpoints, events, string keys, locales,
   storage, tests, Maestro flows, lines of code), each with its rule.
3. **Each app**: purpose and users, areas (the Step 2 table), architecture, and the platform features that users
   depend on.
4. **Overlap**: shared backend endpoints (these show where the products already meet), shared UI copy, the locale
   union and the differences. Also note shared design system or packages.
5. **Platform surface**: point to `PLATFORM.md`, and call out the items only one app has (extensions, background
   modes, URL schemes, app groups). Each is a decision for `fuse-review`.
6. **Technical debt and inherited risks**: top items per app, masked. Point to `SECRETS.local.md` when it exists.
7. **Fusion strategy (recommendation)**: one of these, with a one-paragraph rationale grounded in the numbers:
   - **Grow one app into the new app**: when one source's stack is the likely target and it covers most
     capabilities. Its codebase becomes the base, and the other app's capabilities are ported in.
   - **Greenfield new app, porting capabilities from both**: when neither codebase should be the base, for example
     because of heavy debt, a different target stack, or the new design replacing most UI.
   - **Native pair**: SwiftUI and Compose side by side, when platform features dominate.

   The stack itself is decided in the brief (`INTENT.md` may already fix it). State plainly that this is a
   recommendation.
8. **Documentation gaps**: the top five things a new engineer would need explained about each app.

## Finish

Refresh the report with `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/build_report.py" $program` (a convenience: if it
fails, say so in one line and carry on). Tell the person where `ASSESSMENT.md` and `REPORT.html` are. The next step
is `/app-fusion:fuse-map $program`.
