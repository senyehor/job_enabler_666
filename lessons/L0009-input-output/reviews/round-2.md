# Review round 2: approved

Tests: 7 passed, 0 failed

## What's good
- You fixed both issues from round 1 exactly as asked. Line 15 is now one `print` call with five values: the word `'Recap'` and the four amounts. `sep=' | '` puts the bars between all of them, so the line comes out as `Recap | 47.60 | 9.52 | 57.12 | 19.04`. No `|` is typed into a string by hand.
- Lines 16-17 split the share line into two prints, and the first one has `end=''`. You put the space inside the text (`'Each person pays: '`), so the amount doesn't stick to the colon. In the check questions you thought `end=` carried over to the next print. Here you used it correctly: it only changes how the first print finishes its line.

## Issues
None.

## For next time
- `work/tip.py:15` and `:16`: `f'Recap'` and `f'Each person pays: '` have no `{}` in them, so the `f` does nothing. A plain `'Recap'` is enough. Use `f` only when there's something inside braces.
- `work/tip.py:11`: `print('')` still works, but a plain `print()` does the same thing.
- Optional: the stretch goal (columns lined up with widths like `:<8` and `:>8.2f`) is still open.

## Explain back
Point at line 3, where the bill becomes a number. What type does `input()` give you before `float(...)` runs, and what type do you have after it? What would happen with `47.60` if you had used `int` there? Then look at line 15: if you removed `sep=' | '`, what would `print` put between `Recap` and the amounts?
