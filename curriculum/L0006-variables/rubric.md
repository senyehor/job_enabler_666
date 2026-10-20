# L0006 Rubric: Variables and assignment

## Must-have
- [py.variables] `trace.txt` has a line-by-line trace for scripts A, B and C, showing every existing variable after each assignment, plus correct `final:` lines (A: x=10, y=5; B: a=blue, b=blue; C: count=4, label=level4).
- [py.variables] Wrong traces are corrected with a note, not silently replaced. This is the main learning evidence.
- [py.variables] Under Script B there's a sentence saying that line 3 overwrites `a`'s old value ("red") before `b` can copy it.
- [py.variables] `profile.py` stores each fact in its own descriptive variable and reassigns `age` with `age = age + 1` and `is_student = False`. The second profile is printed from the same variables, not from new literals.
- [py.values] Age and height are converted with `int()` / `float()`, the results are stored, and `type()` shows `int` and `float`.
- [env.run] `profile.py` runs from `work/` without crashing and prints both profiles in the order shown.

## Likely mistakes

1. **Thinks `y = x` links y to x, so traces A as y = 10** (py.variables, major)
   - Where: "Look at line 2 of Script A. What value does y get at that moment?"
   - What: assignment copies the current value. Changing x later doesn't reach back. See "Copying a variable" in theory.md.
   - How: `price = 10`, `old_price = price`, `price = 12`, `print(old_price)`: predict, then run.

2. **Traces B as a real swap (blue red)** (py.variables, major)
   - Where: "In your trace of B, what does `a` hold right after line 3? Where did 'red' go?"
   - What: a reassigned variable loses its old value. A swap needs a third variable to keep it. See "The swap" in theory.md.
   - How: trace `left = "cat"`, `right = "dog"`, `left = right`, `right = left` on paper, row by row.

3. **Converts without storing: writes `int(age)` on its own line** (py.variables / py.values, major if the type line shows `str` or the script crashes on `age + 1`, otherwise n/a)
   - Where: "Run it. What does the `age is` line print, and which line crashed?"
   - What: `int(...)` gives back a new value. It doesn't change the variable unless you assign it.
   - How: `steps = "8000"`, `int(steps)`, `print(type(steps))`, then try `steps = int(steps)`.

4. **Types the new values as literals (`print("Age:", 30)` or `age = 30`)** (py.variables, major)
   - Where: "Where in your code does 30 come from?"
   - What: reassignment using the old value, `x = x + 1`. See "Using a variable on both sides".
   - How: `lives = 3`, `lives = lives + 1`, `print(lives)`.

5. **Trace lists only the changed variable, not all of them** (py.variables, minor)
   - Where: "In line 3 of your trace of Script A, what's y?"
   - What: a trace row is a snapshot of every variable that exists at that point.
   - How: show a two-column table for `n = 1`, `m = n`, `n = 7`.

6. **Script C traced as count = "31" or label = "level 4"** (py.values, minor)
   - Where: "What type is `count` after line 2? And what does `str(count)` give?"
   - What: after `int()` it's a number, so `+ 1` is arithmetic. `+` on strings joins without adding a space.
   - How: `int("5") + 1` vs `"5" + "1"`, and `"go" + "al"`.

7. **Vague names (`a`, `x1`, `s`) or names with typos causing NameError** (py.variables, minor / nit for style)
   - Where: "If someone else read only the variable names, could they tell what each holds?"
   - What: names should describe the value; booleans often start with `is_`. A NameError means the name was never assigned (often a typo).
   - How: compare `s = True` with `is_member = True`.

## Do not nitpick
- Spacing, capitalisation or quotes in `trace.txt`, or extra comments and blank lines in it.
- `print` with commas vs string joining with `+`, as long as the output matches.
- Not using f-strings, `input()`, `if`, or tuple swap `a, b = b, a`. Don't suggest f-strings yet (L0008).
- Keeping the text value in a separate variable (`age_text`) vs converting in place (`age = int(age)`). Both are fine.
- PEP 8 details beyond readable names.
- Skipping the stretch goal.

## Explain back
Point at `age = age + 1` and ask him to explain, step by step, what Python does on that line: which side runs first, and what `age` is before and after. Then ask why the same idea makes Script B fail to swap.
