# L0011 Rubric: Making decisions with if/elif/else

## Must-have
- [py.io] Reads the age with `input()` and converts it with `int()`, then reads the student answer with a second `input()`. Both questions are always asked, age first.
- [py.conditions] `y` and `Y` both count as a student, using `or` with a full comparison on each side (`answer == "y" or answer == "Y"`).
- [py.conditions] A negative age prints `Invalid age` and nothing about category or price. Done with `if`/`else` before the main chain (or as the first branch, as long as no `Category:`/`Price:` line is printed).
- [py.conditions] One `if`/`elif`/`else` chain covers free (0-5), child (6-17), the 18-64 group and senior (65+), with correct boundaries: 5 free, 6 child, 17 child, 18 adult or student, 64 adult, 65 senior.
- [py.conditions] Inside the 18-64 branch, a **nested** `if`/`else` picks student vs adult, and the student test uses `and` to combine the age limit (`<= 25`) with the student answer.
- [py.values] Prints `Category: <category>` and `Price: <price>` with a whole-number price.

## Likely mistakes

1. **`if answer == "y" or "Y":`** (py.conditions, major)
   - Where: "Run it with age 30 and answer `n`. Which category do you get? Now look at the line where you check the student answer."
   - What: each side of `or` is its own condition. `"Y"` on its own counts as true, so the whole line is always true. See "`and`, `or`, `not`" in theory.
   - How: `day = "mon"`, then compare `print(day == "sat" or "sun")` with `print(day == "sat" or day == "sun")`.

2. **Boundaries off by one, e.g. `age < 17` for child or `age < 25` for student** (py.conditions, major)
   - Where: "Try exactly 17 and exactly 25 (with `y`). What does the table say, and what does your program say?"
   - What: `<` leaves the number itself out, `<=` includes it. Check every edge of each range.
   - How: for a "10 items or fewer" checkout lane, which is right: `items < 10` or `items <= 10`? Test it with `items = 10`.

3. **Branches in the wrong order, e.g. `elif age <= 64` before `elif age <= 17`** (py.conditions, major)
   - Where: "Try age 10. Which branch runs first?"
   - What: only the first true branch in a chain runs, so a wider range written first swallows the narrower ones.
   - How: thermometer: `if temp < 25: "mild"` before `elif temp < 0: "freezing"`. What does `-5` print?

4. **Student check not nested, e.g. a separate `elif age <= 25 and is_student` branch in the main chain** (py.conditions, minor)
   - Where: "Requirement 5: where does the student decision live in your code?"
   - What: the task asks for a nested `if`/`else` inside the 18-64 branch, to practise nesting. Behaviour may be correct, so this is minor.
   - How: lift example: `if floor >= 0:` then inside it `if floor == 0:` / `else:`. Indentation shows the inner decision.

5. **Invalid age still prints a price, or crashes with `NameError`** (py.conditions, major)
   - Where: "Run it with `-4`. What gets printed after `Invalid age`?"
   - What: put the normal logic, including the final two `print`s, under the `else` of the invalid-age check so it doesn't run for bad input.
   - How: tickets: `if count <= 0: print("Must be at least 1")` / `else:` with the total computed **and printed** inside the `else`.

6. **Comparing the raw `input()` string with a number (`TypeError`), or `=` instead of `==`** (py.values / py.conditions, major)
   - Where: "Read the last line of the error message. Which line does it point to?"
   - What: `input()` returns a `str`. Convert with `int()` before comparing. `=` assigns, `==` compares.
   - How: `"20" > 17` crashes, `int("20") > 17` is `True`. `x = 5` stores, `x == 5` asks.

7. **Redundant double bounds like `elif age >= 6 and age <= 17`** (py.conditions, nit)
   - Where: "In your child branch, can `age` ever be below 6 when Python gets there?"
   - What: earlier branches already ruled the lower ages out, so one bound is enough. It isn't wrong, just longer.
   - How: thermometer chain: after `if temp < 0`, the next one only needs `elif temp < 15`.

8. **Category or price printed with different labels (`Ticket type: child`, `5 EUR`)** (py.values, minor)
   - Where: "Compare your last two output lines with the example runs."
   - What: the machine's screen has a fixed format (requirement 6).
   - How: `print(f"Total: {total}")` prints `Total: 7`, with the exact label.

## Do not nitpick
- Prompt wording, extra blank lines, or an extra friendly line like `Enjoy the film!`.
- Printing `Category:`/`Price:` inside each branch instead of once at the end, as long as the output is right.
- Storing the answer as `is_student` vs comparing `answer` directly in the nested `if`.
- Not using `not`: the main task doesn't need it (the stretch does).
- Non-numeric age input (`abc`) crashing: `try`/`except` isn't taught. Only the negative case is required.
- Anything not taught yet: `.lower()` and other string methods, `in ("y", "Y")`, loops, functions, `exit()`/`sys.exit()`. Don't suggest them.

## Explain back
Ask him to walk through what happens for `age = 25` and answer `y`, branch by branch: which conditions Python checks, which one is the first true one, and why the `child` branch doesn't need `age >= 6`. Then ask what would change if the answer were `n`.
