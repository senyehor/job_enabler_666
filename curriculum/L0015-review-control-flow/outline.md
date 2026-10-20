# L0015 Outline: Review of conditions and loops

A review lesson: no new concepts. The theory is a short recap that joins L0011-L0014 into one pattern ("read until a stop word, store, then process"), which week 02 (debugging, the number-guessing project) relies on.

## Learning goals (roadmap outcomes being practised)
- **py.conditions**: writes chained conditions (`if/elif/else` with ordered ranges) and uses `and`/`or` to test a range in one `if`.
- **py.while**: writes a loop with a clear exit condition (a sentinel word), and can spot why a loop would never end.
- **py.for**: loops over a list's items, and gets range boundaries right (avoids off-by-one at 60, 70, 80, 90).
- **py.lists-basic**: creates an empty list, appends to it, checks `len()`, and loops over it.

## Key points, in teaching order

1. **`while` vs `for`: pick the loop by what you know.**
   If you don't know how many rounds there will be (until the user says stop, until the balance reaches a goal), use `while`. If you have the items already (a list, a string, a `range`), use `for`. Recall the comment he wrote in L0013 `countdown_for.py`.
   Example idea: "keep asking for a password until it's right" (while) vs "print each letter of a word" (for).

2. **The sentinel loop: read once before the loop, and again at the end of the body.**
   `answer = input(...)` before `while answer != "stop":`, then the same `input` as the last line of the body. If the second `input` is missing, the condition never changes: an infinite loop (L0012's `fix_loop.py`). Converting to `int` happens *inside* the loop, after the stop word is ruled out, because `int("stop")` crashes. `while True` + `break` exists (L0012 aside) but this lesson uses the clear-condition form.
   Example idea: a shopping list: read item names until `end`, append each to `items`, then print `len(items)`.

3. **Collect first, process after: a list between two loops.**
   The `while` loop only gathers values into a list (`[]` before the loop, `.append()` inside). A separate `for` loop afterwards does the work. This separation makes each loop simple, and it's how you can know the count before printing a summary.
   Example idea: read temperatures until `q`, then a `for` loop prints each as `21: warm` / `12: cold`.

4. **Chained conditions: order the `elif`s from the top down.**
   With `>=`, check the highest threshold first; each `elif` then only sees what the earlier ones rejected, so `elif x >= 80` already means "80 to 89". Writing them in the wrong order (`>= 60` first) swallows everything. Boundaries: `>=` includes the number, `>` doesn't; test the exact edges.
   Example idea: wind speed to a label: `>= 60` storm, `>= 40` gale, `>= 20` breezy, else calm. Test 60, 59, 40, 39.

5. **Range checks with `and` / `or`.**
   "Inside the range" is `low <= x and x <= high` (Python also allows `low <= x <= high`). "Outside" is `x < low or x > high`. The two are opposites; `not` turns one into the other. A common bug: `x < 0 and x > 100` is never true.
   Example idea: a valid month number, `1` to `12`: `if month < 1 or month > 12: print("No such month")`.

6. **The empty case and accumulators.**
   Total and counters start at `0` before the `for` loop and update inside it; the average is `total / len(...)` after it. If the list is empty, `len` is 0 and the division crashes with `ZeroDivisionError`, so check `len(...) == 0` first and put everything else under `else`.
   Example idea: average reading time per book from a list of minutes; show `[]` crashing, then the guard.

## Common misconceptions
- "The second `input()` isn't needed, the loop reads it." Without it, `answer` never changes and the loop runs forever.
- "Convert with `int(input(...))` straight away." Then typing the stop word crashes with `ValueError`.
- "`elif` order doesn't matter." With overlapping `>=` ranges, the first true branch wins.
- "`x < 0 and x > 100` catches bad scores." No number is both; it's `or`.
- "`score >= 60` and `score > 60` are the same." 60 itself differs: off by one.
- "A `for` loop over the list can go inside the `while` loop." Then the grades are printed again after every new score.
- "`total / len(scores)` is always safe." Not when the list is empty.

## Check-question ideas
1. Predict the output: `n = 75`, `if n >= 60: print("D")`, `elif n >= 70: print("C")`, `else: print("F")`. Why is `C` never printed, and how do you fix it?
2. Spot the bug: `word = input("Word: ")`, `while word != "stop":`, `    print(len(word))`. What happens when he types `cat`? What line is missing?
3. Explain why: `if temp < -50 and temp > 60: print("Sensor error")` never prints, even for `temp = 99`.
4. Predict: `nums = []`, then `for n in nums: print(n)`, then `print(len(nums))`. Does the loop crash? What does print? What would `sum / len(nums)` do?

## Builds on
- L0011 conditions: `if/elif/else`, `and`/`or`, boundaries, guarding bad input.
- L0012 while-loops: start/condition/step, infinite loops and Ctrl+C.
- L0013 for-loops: `for` over a sequence, accumulators, when `while` fits better.
- L0014 lists-basic: `[]`, `.append()`, `len()`, looping over a list, the empty-list check, average with `:.1f`.
- L0008 / L0009: f-strings with `:.1f`, `input()` returns a `str`.
