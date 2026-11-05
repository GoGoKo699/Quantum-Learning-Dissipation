# Hosted mathematical presentation checks

[Verification](../README.md) · [Workflow](../../.github/workflows/verification.yml)

The read-only workflow runs the scientific suite and a separate Playwright capture of every Markdown page at an exact commit. It compares every mathematical expression with its pinned source, preserves accessible MathML structure, checks display geometry at widths 1440 and 760 pixels, and retains HTML, screenshots, source inventories, and JSON reports as workflow artifacts. No credentials are retained in the checkout and the workflow has only contents-read permission.

The two files in `verification/rendering/` retain a reviewed generic collector and text checker. Their Git blob identities in this repository are `7b37eeafcb78e1437f43e6a922a6449bd337c0ea` and `1fdf964f981ec10358b6455f1da4c86ac82249fa`, respectively. Adding a terminal newline to each exactly reproduces the source-release blobs `bd075f4bc53029230fad1b18c6b07d603d45f44f` and `1d3bf9810d0dfadb844a48b354af80f9b66924bc`; this byte comparison was checked, and no executable statement differs. The pinned dependencies are Playwright 1.56.1 and MathJax-full 3.2.1. Ubuntu 24.04 avoids a demonstrated compatibility failure with a later runner image.

Run from a checkout, after installing those dependencies:

```bash
node verification/rendering/capture_hosted_math.cjs \
  --root . --repository GoGoKo699/Quantum-Learning-Dissipation \
  --revision "$(git rev-parse HEAD)" --output /tmp/qld-hosted-evidence
```

Use an empty output directory and preserve failed runs. Source compilation alone is not a hosted check. A passing report establishes the stated expression and geometry comparisons, not visual approval of the entire layout, proof correctness, priority, or hardware performance. Inspect the saved screenshots and compare the important equations with source separately. Any material source change needs a new revision-bound capture.
