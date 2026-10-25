# L0007 Arithmetic and operators

- I learned that `*` multiplies, `/` divides, `**` powers. The order of the counting process is like in school math, but with the exception that `**` goes from right to left.
- I learned the priority: 1. `()` 2. `**` 3. `* /` 4. `+ -`.
- In `x // y` I check how many times `y` fits into `x`: `9 // 2 = 4`. And `%` checks for leftovers, so `9 % 2 = 1`.
- I applied my new knowledge on variables: I converted seconds to full hours with `hours = total_seconds // 3600`.
- I tripped on math in general. Doing all those calculations in my head was very hard, and I made a couple of mistakes before running the code. Then I double-checked and corrected myself.
- Next time I will use a calculator for the arithmetic.

## Tutor notes
- All 3 check questions right first try; all 8 predictions right; approved round 1 (one minor: hard-coded "10 weeks" in a label). Explain-back of `(total_seconds % 3600) // 60` was correct, but he didn't say what skipping `%` gives (164); I supplied it.
- His priority list leaves `//` and `%` off level 3 (asked once, he explained what they do but didn't place them). Check where he puts `//` and `%` next time precedence comes up.
- Ran ~127 min vs 65 estimated, again roughly 2x. Said mental arithmetic was the hard part, not the Python rules.
