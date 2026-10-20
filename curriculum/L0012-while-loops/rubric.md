# L0012 rubric: Repeating with while loops

## Must-have
- [py.while] `countdown.py` uses a `while` loop with a start value, a condition that stops at 1 (prints 5..1, no 0) and a step inside the body.
- [py.while] `savings.py` loops while the balance is below the goal, adds one year's interest and 1 to a year counter each round, and prints the result once, after the loop.
- [py.while] `fix_loop.py` ends and prints `Total: 15`. The fix is the missing `count = count + 1` inside the loop body, and the comment says that `count` never changed, so the condition stayed True.
- [py.conditions] `countdown.py` rejects a start below 1 with the message, and prints nothing else.
- [py.conditions] `savings.py` checks for a rate of 0 or less before looping, so it can never hang.
- [py.io] Inputs are converted (`int` for the countdown, `float` for savings), using the prompts from the task.
- [py.arithmetic] Interest is `balance * rate / 100` added to the balance. The final balance is printed with 2 decimals.

## Likely mistakes

1. **Off-by-one: prints 0 or stops at 2** (py.while, major)
   - Where: look at the `while` line in `countdown.py` and run it with 3.
   - Concept: the condition is checked before every round. `n > 0` and `n >= 1` both stop after 1. `n >= 0` lets 0 through, and `n > 1` stops before 1.
   - Example: `x = 4` / `while x > 2: print(x); x = x - 1` prints 4 and 3. What would change with `>=`?

2. **Step outside the loop body, or missing** (py.while, major)
   - Where: check the indentation of the line that changes `n` (or `years`/`balance`).
   - Concept: only the indented lines repeat. A step after the loop never runs while the loop is going, so the condition stays True forever.
   - Example: `lives = 3` / `while lives > 0:` / `print("playing")` followed by an unindented `lives = lives - 1` never stops. Indent it and it runs 3 times.

3. **Printing the result inside the loop** (py.while, minor)
   - Where: where does `Years needed:` get printed in `savings.py`?
   - Concept: the body runs once per round. Anything that should appear once, after the answer is known, goes after the loop (unindented).
   - Example: a snail climbing 3 m/day up a 20 m well. Print `days` after the loop, not on every day.

4. **No guard for a 0% rate, so savings.py hangs** (py.conditions, major)
   - Where: run `savings.py` with rate 0 and a goal above the balance.
   - Concept: if nothing can make the condition False, the loop never ends. Check for that case with an `if` before the loop.
   - Example: "how many steps of size s to walk 10 m": if `s <= 0`, print a message instead of looping.

5. **`balance + balance * rate / 100` calculated but not stored** (py.while / py.arithmetic, major)
   - Where: the line inside the loop that should grow the balance.
   - Concept: an expression on its own line calculates a value and throws it away. You need `balance = ...` so the condition sees the new value.
   - Example: `n - 1` vs `n = n - 1` in a tiny loop. Print `n` after each to see the difference.

6. **Using `!=` or `==` instead of `<` in the savings condition** (py.while, minor)
   - Where: the `while` line in `savings.py`.
   - Concept: the balance almost never equals the goal exactly, so `!=` jumps past it and keeps going forever. `<` stops as soon as the goal is reached or passed.
   - Example: `total = 0` / `while total != 10: total = total + 3` never stops (9, 12, ...).

7. **Forgetting `float()`/`int()` on input** (py.io, minor)
   - Where: the error message (a `TypeError` mentioning `str`) and the `input` lines.
   - Concept: `input()` always returns a string. Convert it before comparing or doing maths.
   - Example: `"5" < 3` fails, and `int("5") < 3` works.

## Don't nitpick
- Using `while` where `for`/`range` would be shorter. `for` is the next lesson (L0013).
- Not using functions, constants or `break`. None of those are taught yet, and `break` is only an aside.
- Not handling non-numeric input (no `try/except` yet).
- Exact message wording, spacing, `print("Years needed:", years)` vs an f-string, `n -= 1` vs `n = n - 1`.
- Variable names, as long as they're readable.

## Explain back
Ask him to walk through the `savings.py` loop for 200 / 10% / 300, round by round: what the balance and year counter are after each round, and why the loop stops after year 5 and not earlier or later. Then ask what would happen with a 0% rate if his `if` check weren't there.
