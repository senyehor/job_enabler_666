# L0015 Rubric: Review of conditions and loops

## Must-have
- [py.lists-basic] An empty list is created before reading, and valid scores are added with `.append()`.
- [py.while] Scores are read with a `while` loop whose condition checks for `done`. There is an `input()` before the loop and one at the end of the body, so the loop always ends.
- [py.io] The answer is converted with `int()` only after it's known not to be `done` (inside the loop).
- [py.conditions] The 0-100 check is one `if` using `or` (outside) or `and` (inside), and rejected scores are not appended.
- [py.lists-basic] The empty case is checked with `len(...) == 0` (or similar) before any average, and prints `No scores entered.`
- [py.for] A separate `for` loop *after* the `while` loop prints one `score: letter` line per score, in order.
- [py.conditions] The grade chain is `if/elif/else` ordered so that 90, 80, 70 and 60 land in the higher grade (`>=` from the top down, or equivalent).
- [py.for] Total and pass counter start at 0 before the `for` loop and update inside it; the average is `total / len(...)` with `:.1f`, and `Passed: X of Y` uses `len(...)` for Y.

## Likely mistakes

1. **No `input()` at the end of the while body, so the program hangs after the first score** (py.while, major)
   - Where: "Run it, type one score, and watch. Then look at the last line inside your `while` loop."
   - What: the loop's condition must be able to change; the variable it checks is only updated by `input()`. See the sentinel-loop recap.
   - How: `word = input()`, `while word != "stop": print(word)` never ends. Adding `word = input()` as the last line of the body fixes it.

2. **`int(input(...))` before checking for `done`, so typing `done` crashes with `ValueError`** (py.while / py.io, major)
   - Where: "Read the last line of the error when you type `done`. Which line raised it?"
   - What: `input()` gives a `str`; you can only turn it into a number once you know it isn't the stop word.
   - How: `int("stop")` crashes. Keep `answer` as text, compare it to `"stop"`, and convert inside the loop.

3. **Grade boundaries off by one (`> 90` makes 90 a B, or `> 60` makes 60 fail)** (py.conditions / py.for, major)
   - Where: "Run it with 90, 80, 70, 60 and 59. Which ones get the wrong letter?"
   - What: `>=` includes the boundary number, `>` doesn't. The table says "90 to 100".
   - How: a lift for people "12 and older": `age > 12` turns away a 12-year-old, `age >= 12` doesn't.

4. **`elif` chain in the wrong order (checks `>= 60` first), so everything is D** (py.conditions, major)
   - Where: "What grade does 95 get? Which branch is the first one whose condition is true for 95?"
   - What: only the first true branch runs, so with `>=` the highest threshold goes first.
   - How: speed labels: if `speed >= 20` is checked before `speed >= 60`, a storm at 70 is called "breezy".

5. **Range check uses `and` for "outside" (`score < 0 and score > 100`), so 150 is accepted** (py.conditions, major)
   - Where: "Type 150. Is it rejected? Read your `if` aloud with 150 in it."
   - What: no number is both below 0 and above 100. Outside a range is `or`; inside is `and`.
   - How: month numbers: `month < 1 or month > 12` catches 13 and 0; `month < 1 and month > 12` catches nothing.

6. **Average computed with no empty check, so `done` straight away gives `ZeroDivisionError`** (py.lists-basic, major)
   - Where: "Type `done` first. Which line does the error point at?"
   - What: `len([])` is 0. Check the length before dividing and put the summary under `else`.
   - How: `minutes = []`, `print(0 / len(minutes))` crashes; `if len(minutes) == 0: print("No books")` / `else: ...` doesn't.

7. **Grading inside the while loop, or the `for` loop nested inside the `while`, so grades print as you type or repeat** (py.for / py.while, minor)
   - Where: "Look at the indentation of your `for` line. Is it inside the `while`?"
   - What: collect first, process after: the `for` loop starts after the `while` has finished (no indentation under it).
   - How: read three city names into a list, then, unindented, `for city in cities: print(city)`. Indent that `for` one level and see the list printed three times.

8. **Counting passes or total in the wrong place (counter reset inside the loop, or `passed = 1`)** (py.for, minor)
   - Where: "Print `passed` after each round of the loop. When does it go back to 0?"
   - What: accumulators start once, *before* the loop, and change inside it.
   - How: counting vowels in L0013: `count = 0` before `for ch in word:`, `count = count + 1` inside.

9. **Hard-coded count (`/ 3`, `of 3`) instead of `len(scores)`** (py.lists-basic, minor)
   - Where: "Try it with two scores. Is the average still right?"
   - What: the list knows its own size: `len(scores)`.
   - How: `prices = [2, 4]`, `sum_so_far / len(prices)` works for any number of prices.

## Do not nitpick
- Prompt wording, spacing, blank lines, a trailing full stop after the grade.
- `low <= x <= high` vs `x >= low and x <= high`, or checking "inside" with `and` + `else` vs "outside" with `or`: all fine.
- Storing the letter in a variable then printing once, or a `print` in every branch: both fine.
- Counting passes with a separate `if` vs inside the `elif` branches: fine as long as 60 counts.
- Not handling `Done`, `DONE`, ` done ` or non-numbers like `abc`. `.lower()`, `.strip()`, `try/except` and `isdigit()` aren't taught yet; don't suggest them.
- Not using `break`, `while True`, functions, `sum()`, `max()`, `min()`, `enumerate` or list comprehensions. Don't suggest them.

## Explain back
Ask him to walk through the `while` loop when the user types `85` then `done`: what `answer` holds on each check of the condition, where it changes, and what would happen if he deleted the last `input()` in the body. Then ask why 80 gets a B and not a C in his `elif` chain.
