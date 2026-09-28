---
name: fuse-verify
description: Proves, independently, that built capabilities of the new app keep what the legacy apps did. It re-runs the tests from clean, runs its own canary, the Maestro journeys on every target platform and the API, string, analytics and design-copy parity checks, checks that existing users keep their links, push and identity, and has a script give each capability one verdict (PROVEN, PARTLY PROVEN, NOT PROVEN). With `sign`, a named person signs the proof and the visual conformance.
argument-hint: "<program> [CAP-NNN ...] | <program> sign"
arguments: program
disable-model-invocation: true
---

Re-check, independently, the built capabilities of `$program` (all of them, or the ids after the program name in
`$ARGUMENTS`). With `sign` after the program name, go to **Sign-off** at the end. Run it in a fresh session if you
can: what the build left behind is a claim, and this command re-runs it.

- **A script computes the verdict, not you.** It uses fixed rules, written into its output, and counts tests only
  from result files it parses itself, bound to the content of the code they ran on. Never type a count anywhere.
- Never hand-edit code, tests or results to improve a verdict. Never tick, sign or approve anything a person owns.
- Never touch `legacy/`.
- Before running the app or its tests, read their configuration for the backends they call. If any is not a test
  environment a person named (see `PREFLIGHT.md`), stop and ask.
- Stop every simulator, emulator, Metro server or proxy you started, and say so.
- Scripts are in `${CLAUDE_PLUGIN_ROOT}/scripts/`. If `canary.py status $program` shows a canary still in place, run
  `canary.py abort $program <CAP>` first and say so.

## 1: What is built

Built capabilities are the `docs/fusion/CAP-NNN.md` files in the new app. Name them. If none exists, say so and stop:
the next step is `/app-fusion:fuse-build $program`.

## 2: Tests again, from clean

Follow the stack profile `${CLAUDE_PLUGIN_ROOT}/references/targets/<stack>.md`:
1. Delete build output and test caches (its "clean" commands).
2. `RUN=$(python3 "${CLAUDE_PLUGIN_ROOT}/scripts/evidence.py" dir $program suite verify)`. Run the **full** unit suite
   with JUnit output into `$RUN`, and keep the raw output with `2>&1 | tee $RUN/output.txt`.
3. Record it:
   `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/evidence.py" suite $program --capability all --name verify-unit --command "<cmd>" --junit $RUN --log $RUN/output.txt`.
   For a native pair, run and record each half: `--platform ios --name verify-ios`, then `--platform android --name verify-android`.

A failure caused by this machine is still a failure: say why in `--note`.

## 3: Your own canary, per capability

For each capability:
1. Read the build's canary in `evidence/test-runs.json` (`change` and `diff`), and pick a **different** break on a
   line that matters, in a file of the capability's `## Files`.
2. `canary.py start $program <CAP> --file <file> --change "<what you will break>"`, make the break, run the covering
   tests with JUnit output into the run folder it printed, then `canary.py finish $program <CAP>`. It restores the
   file byte for byte and records the result. If the tests cannot run, `canary.py abort`.

The suite from step 2 stays valid: the restore gives back exactly the code it ran on.

## 4: Journeys and screenshots

On a booted simulator for iOS and an emulator for Android, for every platform in `program.json` → `target.platforms`,
with test accounts only:
1. Build and install the app.
2. Run every Maestro flow of the journeys through the capabilities being verified:
   `RUN=$(evidence.py dir $program journey <JRN> --platform <p>)`, `maestro test <flow> --format junit --output $RUN/maestro.xml`,
   then `evidence.py journey $program --journey <JRN> --platform <p> --flow <flow> --junit $RUN --device "<device>"`.
3. Capture a screenshot of each designed screen and record each with `evidence.py shot ...`.

With no simulator or emulator for a platform, say so. The journeys check is then a gap for it, not a pass.

## 5: Parity, continuity, then the verdict

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/api_parity.py" $program
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/i18n_parity.py" $program
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/events_parity.py" $program
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/design_text.py" $program
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/platform_parity.py" $program
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/fusion_proof.py" $program [CAP-NNN ...]
```

`fusion_proof.py` writes `VERIFICATION.md` and `VERIFICATION.json`. Every run judges every built capability, so a
change for one (a shared catalog, a decision) shows in the others; the ids you give only choose what it prints and its
exit code. Exit code 1 only means that something asked about is not PROVEN.

Show the person:
- the verdict per capability, and the reasons **word for word**
- platform continuity for existing users (links, schemes, push, notification categories, extensions, groups, the
  store identity)
- "What this does not prove"

Never soften a reason or change a verdict. If you think a rule of the script is wrong, say so and leave the file as
it is.

## 6: Visual review

Spawn `app-fusion:ui-conformance-reviewer` on each designed screen's pair: the Figma shot and the app screenshot.
Write its tables to `analysis/$program/VISUAL_REVIEW.md` (the proof's own files are written only by its script). The
person compares the pairs in `REPORT.html` (Design tab) and signs with `/app-fusion:fuse-verify $program sign`.

## Finish

Refresh the report with `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/build_report.py" $program`, then turn each non-PROVEN
reason, in order, into a command:
- a failing test or parity difference → `/app-fusion:fuse-build $program <CAP>`
- a missing decision → `/app-fusion:fuse-review $program`
- a journey that waits for a capability not built yet → build that capability; the verdict follows
- a machine limit → run where the tool works, then verify again
- a P0 or P1 rule named by no passing test → the test that pins it must run and pass

**PROVEN** is evidence, not approval: a named person signs. After that come the brief's next capability or phase,
and finally `/app-fusion:fuse-harden $program`.

---

## Sign-off (`sign`)

Only a person signs, and only with their own name.
1. Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/signoff.py" $program show` and read `VERIFICATION.md`. Show the person
   the verdicts that are current (a verdict judged on code that has changed since cannot be signed: verify again).
2. Ask with AskUserQuestion which capabilities they sign the **proof** of (multiSelect over the PROVEN ones), and for
   their name (they type it). A PARTLY PROVEN capability is signed only with their reason for accepting its open
   checks, in their words; a NOT PROVEN one never.
3. Ask the same for **visual conformance**, over the capabilities with a design screen and a recorded app screenshot,
   after they compared the pairs in `REPORT.html`.
4. Record each with `signoff.py $program proof --by "<their name>" --caps <ids> [--accept "<their reason>"]` and
   `signoff.py $program visual --by "<their name>" --caps <ids>`. The guard asks them to confirm each command.
   In a headless run, sign nothing and say so.
5. Run `fusion_proof.py $program` once more, so `VERIFICATION.md` shows the sign-offs, and refresh the report.

A sign-off binds to the verdict, the code and the screenshots it covers. When any of them changes, it no longer
counts, and `fuse-status` asks for a new one.
