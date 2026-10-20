# L0011 Outline: Making decisions with if/elif/else

## Learning goals (roadmap: py.conditions)
- Writes comparisons (`==`, `!=`, `<`, `<=`, `>`, `>=`) and knows each one produces a `bool` (`True`/`False`).
- Writes chained conditions with `if`/`elif`/`else`, and knows only the first true branch runs.
- Writes nested conditions: an `if` inside another `if` branch, with indentation showing what belongs where.
- Combines conditions with `and`, `or` and `not`, and writes each side of `or` as a full comparison.
- Guards against an obviously invalid input with an `if` before the main logic.

## Key points (teaching order)

1. **Comparisons give booleans.** Links back to `bool` from L0004. A comparison is just an expression with a `True`/`False` value, so it can be printed or stored in a variable.
   Example: `print(3 < 5, 10 == 10.0, "a" == "A")` prints `True True False`. Store one: `is_hot = temperature > 30`. Stress `=` (assign) vs `==` (compare), and that `input()` gives a `str`, so `"7" == 7` is `False` (links to L0009).

2. **`if` and `else`, and indentation as structure.** The colon, the 4-space indent, and the fact that the indented block is "inside" the `if`. Code after the dedent always runs.
   Example: a parking meter: `minutes = int(input("Minutes parked? "))`, `if minutes > 60: print("Pay 2 EUR")`, `else: print("Free")`, then an unindented `print("Goodbye")` that runs either way. Show the `IndentationError` you get from a missing indent.

3. **Chains with `elif`: the first true branch wins.** Python checks top to bottom and stops at the first true condition, so order matters. With ranges, test from one end and use `<=`/`<` so each branch only needs one bound.
   Example: a thermometer label: `if temp < 0: "freezing"`, `elif temp < 15: "cold"`, `elif temp < 25: "mild"`, `else: "hot"`. Then reverse the order (`if temp < 25` first) and show that `-5` now prints "mild". Boundary checks: what does `15` print? `0`?

4. **`and`, `or`, `not`.** Truth tables in plain words. `and` needs both, `or` needs at least one, `not` flips. The `or` trap: `answer == "y" or "Y"` is always truthy; each side must be a full comparison. Python also allows `0 <= x < 10` (worth showing as an aside).
   Example: a bike-hire rule: `if has_helmet and age >= 12:`. Weekend check: `day == "sat" or day == "sun"`. `if not is_raining: print("Go outside")`.

5. **Nested conditions.** An `if` inside a branch, for a decision that only makes sense once the first one is settled. Indentation shows the levels. Mention that an `and` can sometimes replace nesting, and that both are fine.
   Example: a lift: `if floor >= 0:` then inside it `if floor == 0: "Ground floor"` / `else: "Going up"`, and the outer `else: "Basement"`.

6. **Guarding against bad input.** Check the nonsense case first with `if`, and put the normal logic under `else`. Then a variable set only in the normal branch is never printed when it doesn't exist. Only `if` here; `try`/`except` comes much later.
   Example: `count = int(input("How many tickets? "))`, `if count <= 0: print("Must be at least 1")`, `else:` compute and print the total.

## Common misconceptions
- "`=` and `==` are the same." `if x = 5:` is a `SyntaxError`.
- "`answer == "y" or "Y"` checks both letters." It is always true, because `"Y"` on its own is truthy.
- "All matching `elif`s run." Only the first true branch runs, then Python skips the rest of the chain.
- "The order of `elif`s doesn't matter." It does with overlapping ranges: `if age < 65` before `if age < 18` swallows the children.
- "`input()` gives a number, so `age > 17` works." `input()` gives a `str`, and comparing `"20" > 17` raises a `TypeError`. Convert first.
- Off by one at the boundaries: `age < 17` vs `age <= 17`.
- "`else` needs a condition." `else:` takes none; `else age > 65:` is a `SyntaxError`.

## Check-question ideas
1. Predict the output for `score = 75`: `if score >= 50: print("pass")` / `elif score >= 70: print("good")` / `else: print("fail")`. Why is "good" never printed?
2. Spot the bug: `day = input("Day? ")`, `if day == "sat" or "sun": print("Weekend!")`. It prints "Weekend!" for `mon`. Why, and how do you fix it?
3. Predict the output: `print(not (3 > 2 and 2 > 5))` and `print(3 > 2 or 1 / 0 > 1)`. (The second one is a hint about short-circuiting; it doesn't crash.)
4. Explain why: `x = 10`, `if x > 5:` / `    print("big")` / `print("done")`. What changes if `print("done")` is indented too, and `x` is 3?

## Builds on
- L0004 values-and-types: `bool`, `True`/`False`, `int()` conversion.
- L0006 variables: storing a boolean such as `is_member = answer == "y"`.
- L0008 strings-fstrings: f-strings for the result lines.
- L0009 input-output: `input()` returns a `str`, so convert before comparing numbers.
