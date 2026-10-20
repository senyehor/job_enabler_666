---
description: Get the current task reviewed
---

1. Run `python tools/learn.py review-start`. If it fails, explain why in plain words. For example, if he hasn't finished the theory yet, or in student git mode he must commit his work first (help him with the commands, but he types them).
2. Launch the `reviewer` subagent. Pass it the JSON output from step 1 in full, plus anything he asked to have checked. Wait for it to finish.
3. Run `python tools/learn.py review-record`. If it rejects the review file's format, fix `reviews/round-N.json` (you may edit files in `reviews/`) and run it again. Never change the verdict yourself.
4. Present the review from `reviews/round-N.md`:
   - The verdict and the test result, in one line.
   - 1–2 specific things he did well.
   - The issues, most severe first. Each one gets the explanation and the hint at the level the reviewer chose. **Never the fixed code.**
   - Nits go under "for next time". He doesn't need to fix them.
5. Next:
   - **changes_requested**: he fixes them and runs `/review` again.
   - **approved**: ask him to explain, in his own words, the part of his code the reviewer flagged in `Explain back`. If his explanation is off, correct it gently. Then continue with `/done`.
