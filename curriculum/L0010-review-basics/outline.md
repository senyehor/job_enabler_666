# L0010 Outline: Review of variables, arithmetic, strings and I/O

This is a review lesson, so there is nothing new. It consolidates L0006-L0009 before conditions start in L0011. Keep the theory short: recap each idea with one fresh example and one trap. He practises in the trace exercise and the converter.

## Learning goals (roadmap outcomes)
- py.variables: traces variable values through a script by hand, including a variable reassigned from its own old value.
- py.arithmetic: uses `//`, `%` and `**` correctly and knows operator precedence (`a + b // c`).
- py.strings-basic: formats output with f-strings (including `:.2f`), and indexes and slices strings.
- py.io: builds a program that asks for input and responds; knows `input()` always returns `str`; uses `print`'s `sep` and `end`.

## Key points (teaching order)

1. **A variable holds its latest value, and the right side is worked out first.** Recap tracing with a trace table (one row per line, one column per variable). `x = x + something` uses the old `x`.
   Example: `coins = 40`, `bags = coins // 15`, `coins = coins - bags * 15`, `bags = bags + coins` (trace: 40 / 2 / 10 / 12).

2. **`/`, `//` and `%`, and precedence.** `/` always gives a float (`8 / 2` is `4.0`), `//` the whole part, `%` the remainder. `*`, `/`, `//`, `%` go before `+` and `-`, and `**` before all of them. The "split a total into big units and leftovers" pattern: `big = total // size`, `rest = total % size`.
   Example: 200 days is `200 // 7` weeks and `200 % 7` days (28 weeks 4 days). Precedence: `10 + 7 // 2` is 13, `(10 + 7) // 2` is 8.

3. **Indexing and slicing.** Indexes start at 0, `[-1]` is the last character, `[a:b]` stops *before* `b`, `[:3]` is the first three, and a slice past the end doesn't crash (`"Al"[:3]` is `"Al"`). An index can be any int expression, like `len(s) // 2`.
   Example: `city = "Odesa"`: `city[0]`, `city[-1]`, `city[1:3]` is `"de"`, `city[:len(city) // 2]` is `"Od"`.

4. **`input()` always returns text, so convert it straight away.** `int(input("..."))` in one line. Without the conversion, `"5" * 2` is `"55"` and `"5" // 2` crashes with `TypeError`.
   Example: ask for a number of eggs and print how many full boxes of 6 that makes and how many eggs are left.

5. **f-strings and `print` options.** Expressions go inside `{}`, and `:.2f` rounds the *display* to 2 decimals. `print(a, b, sep="-")` changes what goes between items. `end=" "` changes what comes after the line, so the next `print` continues on the same line.
   Example: `print("Score", end=": ")` then `print(7, 10, sep="/")` prints `Score: 7/10`. And with `price = 19.999`, `f"{price:.2f}"` gives `20.00`.

6. **Magic numbers go in named variables.** A conversion factor like `0.4536` (kg per pound) is clearer as `kg_per_pound = 0.4536`. This recaps good variable names from L0006.

## Common misconceptions
- "`/` between two ints gives an int." It's always a float: `6 / 2` is `3.0`.
- Forgetting that after `n = n / 2`, `n` is a float in every later line.
- "A slice `[1:3]` includes index 3."
- "`input()` gives a number if the user types digits."
- "`:.2f` changes the stored value." It only changes how the value is shown.
- "`sep` adds a space as well." `sep="-"` replaces the space.
- "`end=" "` goes on the print that comes *after*." It belongs to the print whose line should not end.

## Check-question ideas
1. Predict the output: `t = 75`, `m = t // 60`, `s = t % 60`, `t = m + s`, `print(t, m, s)`. (16 1 15)
2. Spot the bug: `age = input("Age: ")`, `print(f"In 10 years: {age + 10}")`. What happens, and what one change fixes it?
3. Predict the output: `w = "river"`, `print(w[1:3], w[-2:], w[::-1][0])`. (iv er r)
4. Explain why: `print("a", "b", sep="")` then `print("c")` prints `ab` and `c` on two lines, but with `end=""` added to the first call they print on one line. Which option controls what?

## Builds on
- L0004 values-and-types: `int()`, `str()`, `type()`.
- L0006 variables: trace tables, `x = x + 1`, and the line-by-line trace layout he reuses here.
- L0007 arithmetic: `//`, `%`, `**`, precedence, `/` gives a float.
- L0008 strings-fstrings: f-strings, `:.2f`, indexing, slicing, `len()`.
- L0009 input-output: `input()`, converting with `int`/`float`, `sep` and `end`.
