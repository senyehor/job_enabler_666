# L0007 Rubric: Arithmetic and operators

## Must-have
- [py.arithmetic] Part 1 prints all 8 expressions with a label, using the real expression after the comma (not a typed-in answer): `2 + 3 * 4`, `(2 + 3) * 4`, `20 - 10 - 5`, `2 ** 3 ** 2`, `7 / 2`, `7 // 2`, `7 % 2`, `6 / 2`.
- [py.arithmetic] Every Part 1 line has a `# predict:` comment above it, and wrong predictions are corrected, not deleted. This is the main evidence that he understands precedence and int vs float, so read the corrections.
- [py.arithmetic] Workout time is computed with `//` and `%` from `total_seconds`: `2 h 44 min 36 s`.
- [py.arithmetic] The average uses brackets around the sum and `/`: `6.5`. The whole-km version uses `//`: `6`.
- [py.arithmetic] Points use `**`: `start_points * 2 ** weeks` gives `51200`.
- [py.variables] The raw data lives in named variables, and every Part 2 result is computed from them. Changing `total_seconds` alone changes the workout line.
- [py.values] The script runs from `work/` with `python calculator.py` without crashing.

## Likely mistakes

1. **Average without brackets: `run1 + run2 + run3 + run4 / 4`** (py.arithmetic, major)
   - Where: "Look at the line where you compute the average. Which numbers actually get divided by 4?"
   - What: `/` binds tighter than `+`, so only the last run is divided. See "Operator precedence and brackets" in theory.
   - How: compare `print(2 + 4 / 2)` with `print((2 + 4) / 2)`.

2. **Minutes computed as `total_seconds // 60` (gives 164) or seconds as `total_seconds % 3600`** (py.arithmetic, major)
   - Where: "Check: does `hours * 3600 + minutes * 60 + seconds` give back 9876, and is `minutes` under 60?"
   - What: after taking out the hours, you work with what's left over (`%`), not the original total.
   - How: 200 minutes: `200 // 60` is 3 hours, `200 % 60` is 20 minutes. Now try 1000 days into weeks and days.

3. **Typed-in results, e.g. `print("Workout time:", 2, "h", 44, ...)` or `points = 51200`** (py.variables, major)
   - Where: "Change `total_seconds` to 5000 and run it. Did the workout line change?"
   - What: results must be computed from the variables (requirement 8).
   - How: `price = 3`, `count = 4`, `total = price * count` instead of `total = 12`.

4. **Uses `^` for power, or writes `(start_points * 2) ** weeks`** (py.arithmetic, major)
   - Where: "Your points line: is that number believable for 10 weeks of doubling 50?"
   - What: power is `**`, and `**` goes before `*`, so `start_points * 2 ** weeks` already does the right thing.
   - How: `3 * 2 ** 2` is `12`, `(3 * 2) ** 2` is `36`.

5. **Predictions written after running, or wrong ones deleted** (py.arithmetic, minor; major if all 8 are perfect and it seems unlikely)
   - Where: "Which of your predictions were wrong? Where is the correction?"
   - What: the point of Part 1 is comparing expectation with reality (requirement 3).
   - How: `# predict: 4  WRONG: actually 4.0, because / always gives a float`.

6. **Label doesn't match the expression, e.g. `print("7 / 2 =", 7 // 2)`** (py.arithmetic, minor)
   - Where: point to the line whose label and expression differ.
   - What: the label is only text; Python computes what's after the comma.
   - How: `print("10 / 4 =", 10 / 4)` vs `print("10 / 4 =", 10 // 4)`: run both.

7. **Correction for `2 ** 3 ** 2` says "left to right gives 64"** (py.arithmetic, minor)
   - Where: "Read your correction for the `**` line again. Which `**` happens first?"
   - What: `**` goes right to left. See precedence in theory.
   - How: `2 ** 2 ** 3` is `2 ** 8`, which is `256`, not `4 ** 3`.

## Do not nitpick
- Spacing in the output or the labels, extra blank lines, extra headings like `--- Part 2 ---`.
- Variable names, as long as they're readable (`run1` and `distance_1` are both fine).
- Not rounding `6.5` or other floats: `round()` and formatting aren't taught yet.
- Anything not taught yet: f-strings, `input()`, `if`, loops, functions, `divmod`, `math`. Don't suggest them.
- PEP 8 details beyond basic readability (spaces around operators are nice, but don't insist).

## Explain back
Ask him to walk through how he got minutes from `total_seconds`: why `%` before the second `//`, and what `9876 % 3600` means in plain words. Then ask why `6 / 2` printed `3.0` and not `3`.
