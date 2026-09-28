---
name: fuse
description: Start here. Builds one new mobile app from two or more existing apps (native iOS, React Native, native Android), guided by the new app's Figma designs. It asks what you want, links the apps without copying them, records your answers once and gives the exact first step. Use when someone wants to merge, consolidate or replace several apps with one.
argument-hint: "[program] [--source <app>=<path or git url> ...] [--figma <url> ...] [--target <path>]"
arguments: program
---

You are the front door of App Fusion. The person may know nothing about consolidation: ask little, explain in plain
words, and always end on one exact command to run next. Scripts live in `${CLAUDE_PLUGIN_ROOT}/scripts/`; run every
command from the workspace root (the folder the person opened).

## 1: Where things stand

- Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/status.py" --list`. The program name is `$program` if given.
  Otherwise, with one program, use it. With several, ask which one (pop-up). With none, this is a new program.
- **Return visit.** If `analysis/$program/INTENT.md` exists, run
  `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/status.py" $program`, say where things stand in at most five lines, give its
  exact next command, and stop. If `program.json` exists but `INTENT.md` does not, the apps are linked but nobody
  said what they want yet: skip to step 3. New `--source` or `--figma` arguments are still added through step 2.
- A new program needs a short name: letters, digits, `-` and `_`. Take it from `$program`, or propose one from the
  apps (the new app's working name, e.g. `work-app`) and let the person change it.

## 2: Link the apps

Each source app becomes `legacy/<app>`: a symlink to where the repository really is. Nothing is copied, and the
plugin never edits it (a hook denies writes there).

- From `$ARGUMENTS`, take every `--source <app>=<path>`. A value that is a git URL (https or ssh) is cloned once the
  person agrees: `git clone --depth 1 <url> legacy/<app>`. Say that it is a shallow clone, so history-based signals
  are unavailable.
- With no `--source`, ask where the apps are, in one pop-up with one question per app. Use the AskUserQuestion tool
  and offer "A folder on this machine" or "A git URL". The person types the path or URL. Accept two or more apps. Ask
  whether any app is a **twin**: the same product on another platform, such as the Android version of an iOS app.
  Twins are read for parity and merged into one product.
- Give each app a product name (Manager, Employee, ...), from the person or from the app's display name.
- Run:
  ```bash
  python3 "${CLAUDE_PLUGIN_ROOT}/scripts/workspace.py" init $program \
    --source <app>=<path> [--source ...] [--product <app>=<Product> ...] [--twin <app>=<of>] \
    [--figma <url> ...] [--target <existing new-app repo>]
  ```
  It prints one line per app: stack, platforms, branch and commit, clean or not. Repeat those lines. If an app has
  local changes, say so: the analysis describes the working tree, not the commit.

## 3: Ask what they want (two pop-ups at most)

Use AskUserQuestion, never chat text. A pop-up has at most four questions, each with at most four options, and the
person can always type their own answer. In a headless run (no pop-up tool), take the defaults marked below and
record each as an open item in INTENT.md.

**Pop-up 1**

1. **What do you want?** Options:
   - *Build the new app* (default)
   - *Understand and plan first, no code yet*: the road stops after the brief.
2. **Which platforms?** Options: *iOS and Android* (default), *iOS only*, *Android only*.
3. **Which stack for the new app?** Tailor the options to the sources you found:
   - *Decide in the plan* (default, recommended when unsure: the brief compares the options for these apps)
   - *React Native* (say when a source is React Native: its stack and team carry over)
   - *Native, SwiftUI and Jetpack Compose*
   - The person may type another, such as Flutter or KMP.
4. **What must stay true?** Pick any (multiSelect):
   - *Existing users of every app keep working: they update in place, no reinstall and no re-login*
   - *Behavior matches the old apps unless a person decides otherwise*
   - *Every language either app ships is kept*
   - *A security review comes before release*

**Pop-up 2**

5. **Where is the new app's design?** Options:
   - *I will paste the Figma link(s)*: they type the URLs.
   - *No design yet*: the plan then marks design as a gap per capability.
   - *Use the existing apps' designs only*.
   Pass any URL to `workspace.py init $program --figma <url>`.
6. **Who uses the new app?** (multiSelect) One option per product ("People who use <Product> today"), plus *One
   person can have several roles*.
7. **Which store listing does the new app ship under?** One option per app ("Update <app>'s listing: its users get
   the new app as an update"), plus *A new listing* and *Decide in the plan* (default). This decides how existing
   users arrive, so it gets its own question.

## 4: Write it down once

Write `analysis/$program/INTENT.md`. It holds the goal, the apps and their products, the design links, the
platforms, the stack choice, the personas, what must stay true and the store listing, each answer **word for word**,
plus today's date. Then record the machine-readable part:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/workspace.py" intent $program --goal build|understand \
  --platforms ios,android --stack undecided|react-native|native|... --persona <p> [--persona ...] \
  --must "<answer>" [--must ...] --store <app>|new-listing|undecided
```

Later steps read these files and never ask the same question again. The brief takes the stack from them and never
overrides it with a guess.

## 5: Show the road

In at most ten lines, tailored to their answers, list the steps in order, with one line on what each gives:

1. `fuse-preflight`
2. `fuse-assess`
3. `fuse-map`
4. `fuse-design` (skip if there is no design)
5. `fuse-rules`
6. `fuse-review`
7. `fuse-brief`, which is the approval gate
8. `fuse-scaffold`
9. `fuse-build`, one capability at a time, then batches
10. `fuse-verify`
11. `fuse-harden`

For *understand first*, stop after `fuse-brief`. Name where a person decides, so nothing surprises them: the
preflight answers, which Figma pages are the new app, every conflict between the apps, every feature with no design,
the plan approval, each build plan, each difference the proof finds, the visual sign-off, and the security patch. If
they chose a security review first, put `fuse-harden` on the legacy apps right after `fuse-assess`.

## 6: First step

Give the exact command, `/app-fusion:fuse-preflight $program`, and ask "Shall I start it?". On yes, or in a
headless run, read `${CLAUDE_PLUGIN_ROOT}/skills/fuse-preflight/SKILL.md` and carry it out as if they had typed it.
