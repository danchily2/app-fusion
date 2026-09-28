---
name: fuse-verify
description: Proves, independently, that built capabilities of the new app keep what the legacy apps did. It re-runs the tests from clean, runs its own canary, the Maestro journeys and the API, string and design-copy parity checks, and has a script give each capability one verdict (PROVEN, PARTLY PROVEN, NOT PROVEN). A person signs visual conformance from side-by-side screenshots.
argument-hint: "<program> [CAP-NNN ...]"
arguments: program
disable-model-invocation: true
---

Re-check, independently, the built capabilities of `$program` (all of them, or the ids after the program name in
`$ARGUMENTS`). Run it in a fresh session if you can: what the build left behind is a claim, and this command re-runs it.

- **A script computes the verdict, not you.** It uses fixed rules, written into its output, and counts tests only
  from result files it parses itself. Keep the JUnit result or raw log of every run. Never type a count anywhere.
- Never hand-edit code, tests or results to improve a verdict. Never tick or approve anything a person owns.
- Never touch `legacy/`.
- Before running the app or its tests, read their configuration for the backends they call. If any is not a test
  environment a person named (see `PREFLIGHT.md`), stop and ask.
- Stop every simulator, emulator, Metro server or proxy you started, and say so.

## 1: What is built

Built capabilities are the `docs/fusion/CAP-NNN.md` files in the new app. Name them. If none exists, say so and stop:
the next step is `/app-fusion:fuse-build $program`.

## 2: Tests again, from clean

Follow the stack profile `${CLAUDE_PLUGIN_ROOT}/references/targets/<stack>.md`:
1. Delete build output and test caches (its "clean" commands).
2. Run the **full** unit suite with JUnit output to `analysis/$program/evidence/junit/verify/`, and keep the raw
   output with `2>&1 | tee analysis/$program/evidence/logs/verify-unit.txt`.
3. Record it:
   `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/evidence.py" suite $program --capability all --name verify-unit --command "<cmd>" --junit analysis/$program/evidence/junit/verify/ --log analysis/$program/evidence/logs/verify-unit.txt`.

A failure caused by this machine is still a failure: say why in `--note`.

## 3: Your own canary, per capability

For each capability:
1. Pick a **different** break than the build's canary (read its notes), on a line that matters.
2. Run the covering tests with JUnit to `analysis/$program/evidence/canary/<CAP>/`, then restore the file with
   `git -C <target> checkout -- <file>` and confirm it is clean.
3. Record it with `evidence.py canary $program --capability <CAP> --change "<what you broke>" --junit analysis/$program/evidence/canary/<CAP>/`.

## 4: Journeys and screenshots

On a booted simulator (and an emulator for Android when the platforms include it), with test accounts only:
1. Build and install the app.
2. Run every Maestro flow of the journeys through the capabilities being verified, with JUnit output. Record each
   with `evidence.py journey ...`.
3. Capture a screenshot of each designed screen. Record each with `evidence.py shot ...`.

With no simulator, say so. The journeys check is then a gap, not a pass.

## 5: Parity, then the verdict

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/api_parity.py" $program
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/i18n_parity.py" $program
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/design_text.py" $program
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/fusion_proof.py" $program [CAP-NNN ...]
```

`fusion_proof.py` writes `VERIFICATION.md` and `VERIFICATION.json`. Its exit code 1 only means that something is not
PROVEN.

Show the person:
- the verdict per capability, and the reasons **word for word**
- "What this does not prove"
- the blank sign-off block

Never soften a reason or change a verdict. If you think a rule of the script is wrong, say so and leave the file as
it is.

## 6: Visual conformance (a person signs)

Spawn `app-fusion:ui-conformance-reviewer` on each designed screen's pair: the Figma shot and the app screenshot.
Add its tables to `VERIFICATION.md` under "Visual review". The person compares the pairs in `REPORT.html` (Design tab)
and signs the Visual conformance line. You never sign.

## Finish

Refresh the report with `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/build_report.py" $program`, then turn each non-PROVEN
reason, in order, into a command:
- a failing test or parity difference → `/app-fusion:fuse-build $program <CAP>`
- a missing decision → `/app-fusion:fuse-review $program`
- a machine limit → run where the tool works, then verify again
- a P0 rule named by no passing test → the test that pins it must run and pass

**PROVEN** is evidence, not approval. A named person signs `VERIFICATION.md`. After that come the brief's next
capability or phase, and finally `/app-fusion:fuse-harden $program`.
