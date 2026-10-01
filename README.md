# App Fusion (Claude Code plugin marketplace)

This repository is a Claude Code plugin marketplace with one plugin, **App Fusion**. It builds one new mobile app from
two or more legacy apps (native iOS, React Native, native Android), guided by the new app's Figma designs.

Install it from a local clone:

```
/plugin marketplace add /path/to/app-fusion
/plugin install app-fusion@app-fusion
```

Or try it for one session without installing: `claude --plugin-dir /path/to/app-fusion/plugins/app-fusion`.

In Devin: `devin plugins install danchily2/app-fusion#plugins/app-fusion` (see the plugin README for what differs).

Then open an empty folder for the work and type `/app-fusion:fuse`. The full guide is
[plugins/app-fusion/README.md](plugins/app-fusion/README.md), and the design contract is
[plugins/app-fusion/docs/DESIGN.md](plugins/app-fusion/docs/DESIGN.md).

Development checks:

```
claude plugin validate plugins/app-fusion
python3 -m unittest discover -s plugins/app-fusion/scripts/tests -v
node --test plugins/app-fusion/tests/*.test.mjs
claude plugin eval plugins/app-fusion --scaffold --trust-plugin --allow-tools Bash Write Edit --ablation none
```

The eval cases (`plugins/app-fusion/evals/`) run real headless sessions against tiny fixture apps: the front door,
the next command from `fuse-status`, and the guard refusing an edit to a legacy app. All three score 1.00.
