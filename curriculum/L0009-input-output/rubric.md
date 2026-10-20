# L0009 Rubric: Talking to the user: print and input

## Must-have
- [py.io] Reads the bill, tip percent and number of people with `input()`, in that order, with a readable prompt for each.
- [py.values] Converts each answer before using it: `float` for the bill, `int` for the percent and people. (`float` for the percent is fine too.)
- [py.arithmetic] Tip = bill * percent / 100, total = bill + tip, share = total / people, each stored in a named variable.
- [py.strings-basic] The bill, tip and total lines use f-strings with `:.2f`.
- [py.io] The `Recap` line comes from one `print` call with several values and `sep=" | "`, not from `|` typed into a string.
- [py.io] `Each person pays:` and the share come from two `print` calls, the first with `end=` (e.g. `end=" "`).
- [py.io] Runs from `work/` with `python tip.py` and doesn't crash on a bill with cents like `47.60`.

## Likely mistakes

1. **Uses the `input()` result without converting it** (py.io, major)
   - Where: "Run it and look at the last line of the error. Which line is it on, and what types does it mention?"
   - What: `input()` always returns a `str`, even when you type digits. See "input always gives text" in theory.md.
   - How: `n = input("Number: ")`, type `4`, then `print(n * 2)`. What do you get, and what changes with `int(n) * 2`?

2. **Converts the bill with `int()`** (py.values, major)
   - Where: "Try your program with a bill of `47.60`. What does the error say?"
   - What: `int()` only accepts whole-number text. Money has cents, so it needs `float()` (L0004 conversions).
   - How: compare `int("3")`, `float("3")` and `int("2.5")` in a scratch file.

3. **Converts into a new variable but then calculates with the old string** (py.io, major)
   - Where: "Find the line that crashes. Which variable is used there, the text one or the number one?"
   - What: `int(x)` makes a new value; it doesn't change `x` unless you assign the result.
   - How: `age_text = input("Age: ")`, `age = int(age_text)`, then compare `print(age_text + 1)` with `print(age + 1)`.

4. **Wrong tip formula: forgets `/ 100`, or uses `%` as "percent"** (py.arithmetic, major)
   - Where: "With a bill of 100 and 10 percent, what tip does your program print? What should it be?"
   - What: a percent is "per hundred", so 10 percent of 100 is `100 * 10 / 100`. In Python, `%` is the remainder operator (L0007), not percent.
   - How: work out 25 percent of 80 by hand, then write it as a Python expression.

5. **Types the separators by hand instead of using `sep`** (py.io, minor)
   - Where: "Look at your Recap line. Where do the `|` characters come from?"
   - What: `sep=` sets what `print` puts between its values. See "print options" in theory.md.
   - How: `print(2026, 10, 20, sep="-")` prints `2026-10-20`.

6. **Share shows as 36.666666666666664, or recap values have long decimals** (py.strings-basic, minor)
   - Where: "Run it with 100, 10 and 3. How many decimals does the share have, in both places it's printed?"
   - What: format money with `:.2f` inside an f-string (L0008). Each value passed to the recap `print` can be its own f-string.
   - How: `print(f"{10 / 3:.2f}", f"{0.1 + 0.2:.2f}", sep=" / ")`.

7. **`end` written wrongly: `print("Each person pays:" end=" ")` or `print(..., end)`** (py.io, minor)
   - Where: "Read the error line. What's between the text and `end`?"
   - What: options like `end=` go after the values, with a comma before them, in `name=value` form.
   - How: `print("Loading", end="")`, then `print("... done")`.

8. **`end=""` with no space, so it prints `Each person pays:19.04`** (py.io, nit)
   - Where: "Look closely at the gap before the amount."
   - What: `end` replaces the newline with exactly what you give it, nothing more.
   - How: compare `print("a", end="")` + `print("b")` with `print("a", end=" ")` + `print("b")`.

## Do not nitpick
- Exact prompt and label wording, spacing, alignment, empty lines. The tests only care about the numbers and the two special lines.
- Putting the conversion on the same line (`float(input(...))`) vs a separate line. Both are fine.
- Using `float` for the tip percent.
- No checks for bad input (zero people, letters, negative bill). He has no `if` yet (L0011). Don't suggest `if` or `try/except`.
- Not taught yet: `round()`, functions, loops, string methods like `.strip()`. Don't suggest them.
- PEP 8 details beyond basic readability.

## Explain back
Ask him to point at the line where the bill becomes a number and explain what type it was before and after that line, and what would happen with `47.60` if he'd used `int` there. Then ask what `print` would put between the recap values without `sep=" | "`.
