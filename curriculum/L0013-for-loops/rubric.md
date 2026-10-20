# L0013 Rubric: for loops and range

## Must-have
- [py.for] `times_table.py` uses one `for` loop over `range(1, 11)` (or an equivalent that gives exactly 1 to 10) and prints 10 rows, `x 1` to `x 10`, with correct results.
- [py.io] Each script reads its input with `input()`, and the two number scripts convert it with `int()`.
- [py.for] `vowels.py` loops over the word itself (`for ch in word:`), not over indexes the task didn't ask for.
- [py.conditions] The vowel check is an `if` inside the loop (with `or`, or another correct comparison), and the counter is set to 0 *before* the loop and printed *after* it.
- [py.for] `countdown_for.py` uses `range(n, 0, -1)` (no `while`), prints n down to 1 and then `Liftoff!`, with no 0.
- [py.while] The comment in `countdown_for.py` gives a sensible reason for `while`: you repeat until a condition changes and don't know the number of passes in advance (savings goal, waiting for valid input).
- [env.run] All three scripts run without errors and all tests pass.

## Likely mistakes

1. **Off-by-one in the table range** (py.for, major), e.g. `range(1, 10)` stopping at `x 9`, or `range(10)` starting at `x 0`.
   - Where: "Look at the first and last row your table prints. Which one is missing or extra?"
   - What: `range(start, stop)` includes start but stops *before* stop. See "range" in theory.md.
   - How: to get the seats 1 to 8 of a row you need `range(1, 9)`. Ask him how many numbers `range(3, 7)` gives before running it.

2. **Counter reset inside the loop** (py.for, major), e.g. `count = 0` indented under `for`, so the result is 0 or 1.
   - Where: "Trace `banana` by hand: what is `count` just after the second `a`?"
   - What: the accumulator must be created once, before the loop. Everything indented runs on every pass.
   - How: summing 1 to 5 with `total = 0` inside vs outside the loop; print `total` inside the loop to watch it reset.

3. **Result printed inside the loop** (py.for, minor), so `Vowels: ...` appears once per character.
   - Where: "How many times does your `Vowels:` line appear for `queue`? Why that many?"
   - What: indentation decides what belongs to the loop body. The final result goes after the loop, back at the outer level.
   - How: `for n in range(3): print("inside")` followed by an unindented `print("after")`.

4. **Vowel condition written as `if ch == "a" or "e" or "i" ...`** (py.conditions, major): every character counts as a vowel, because `"e"` on its own is truthy.
   - Where: "What does `rhythm` give? Is that right?"
   - What: each side of `or` must be a full comparison. See the `or` section from L0011.
   - How: `x = "z"` then `print(x == "a" or "b")` prints `b`, while `print(x == "a" or x == "b")` prints `False`.

5. **Countdown with `range(n, 0)` or `range(n, 1, -1)`** (py.for, major): the first prints nothing, the second misses the 1.
   - Where: "Run it from 3. What's the last number before Liftoff, or does anything print at all?"
   - What: counting down needs a negative step, and the stop is still excluded, so to reach 1 the stop is 0.
   - How: `range(6, 2, -1)` gives 6, 5, 4, 3. Ask him which stop gives 6 down to 2.

6. **Forgets `int()` on the input** (py.values, major): `range("7")` gives a TypeError.
   - Where: "Read the last line of the traceback. Which type does it say it got?"
   - What: `input()` always returns a `str`. Convert it with `int()` (L0004, L0009).
   - How: `type(input("n: "))` with `5` typed in.

7. **Loop variable not used, the multiplier hard-coded or computed with a separate counter** (py.for, minor), e.g. `i = 1` before the loop and `i = i + 1` inside a `for`.
   - Where: "Which variable already holds 1, 2, 3 ... on each pass?"
   - What: the `for` loop updates the loop variable for you. A manual counter is the `while` habit from L0012.
   - How: `for day in range(1, 8): print(f"Day {day}")` needs no counter.

8. **Comment says something vague like "while is for loops"** (py.while, nit, unless it's wrong rather than vague)
   - Where: "Could you write the savings program from L0012 with `range`? What number would you put in it?"
   - What: `for` needs to know what it goes through; `while` repeats until a condition changes.
   - How: "keep asking for a password until it's correct": how many passes is that?

## Do not nitpick
- Spacing and the exact row layout (`7 x 3 = 21` vs `7 x 3 = 21.` or `7 * 3 = 21`), or prompt wording.
- The name of the loop variable (`i`, `n`, `m`, `ch`, `letter`) as long as it reads sensibly.
- `count = count + 1` vs `count += 1`.
- A long `or` chain for vowels. `if ch in "aeiou":` is fine if he found it, but don't push it. Don't suggest `.count()`, `.lower()`, lists, `sum()` or functions; none have been taught.
- Uppercase vowels not being counted (that's the stretch goal).
- No handling of non-number or negative input. A negative start just prints `Liftoff!`, which is fine.
- PEP 8 details.

## Explain back
Ask him to explain `range(n, 0, -1)` in `countdown_for.py`: what each of the three numbers does, why the stop is 0 and not 1, and what changes if he removes the `-1`.
