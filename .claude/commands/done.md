---
description: Write the lesson's takeaways and finish it
---

The lesson must be in state `takeaways` (approved by the review). Otherwise tell him what's still missing.

1. Ask for 3–5 takeaways **in his own words**: what he learned, what tripped him up, and one thing he'd do differently next time. Short bullets are fine. Suggest that format, but don't suggest the content.
2. Check each bullet. Is it correct? Is it specific? ("loops are useful" isn't.) If one is wrong or vague, ask a follow-up question so he fixes it himself. At most two rounds; don't rewrite his bullets for him.
3. Write `takeaways.md` in the lesson folder:
   ```
   # <lesson id> <title>

   - his bullets, with only spelling fixed

   ## Tutor notes
   1–3 lines: anything you corrected, and what to watch in the next lessons.
   ```
4. In student git mode, he commits `work/` first. Tell him what's needed; he types the commands.
5. Run `python tools/learn.py done` and pass on its output: time taken against the estimate, lessons done today, and the 15-minute break. If this was his third lesson today, say that today's plan is done.
