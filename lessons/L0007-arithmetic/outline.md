# L0007 Outline: Arithmetic and operators

## Learning goals (roadmap: py.arithmetic)
- Uses `+ - * /`, `//`, `%` and `**` correctly, and knows which ones give an `int` and which give a `float`.
- Knows operator precedence (`**` first, then `* / // %`, then `+ -`, left to right within a level), and uses brackets to change it.
- Stores inputs in variables and computes results from them instead of working them out by hand.

## Key points (teaching order)

1. **The basic four and the "/ always gives float" rule.** `+ - *` on two ints give an int. `/` always gives a float, even when it divides evenly.
   Example: `print(9 - 4, 3 * 5, 12 / 4, 10 / 4)` prints `5 15 3.0 2.5`. Mixing an int and a float gives a float: `2 + 0.5`, `3 * 1.0` (links to L0004 types).

2. **Floor division `//` and remainder `%`, as a pair.** `a // b` is "how many whole times b fits in a", `a % b` is "what is left over". Use a real picture: sharing sweets.
   Example: 17 sweets for 5 children: `17 // 5` is `3` each, `17 % 5` is `2` left over. Check: `3 * 5 + 2 == 17`. Also `% 2` tells even/odd (`10 % 2` is `0`, `11 % 2` is `1`). Mention that `//` with a float gives a float (`7.0 // 2` is `3.0`), and only briefly that negative numbers round *down* (`-7 // 2` is `-4`), without dwelling on it.

3. **Unit conversion with `//` and `%`.** Turning one big number into bigger units step by step: divide off the biggest unit, keep the remainder, repeat.
   Example (different from the task): 200 minutes into hours and minutes: `200 // 60` is `3`, `200 % 60` is `20`. Or 1000 days into weeks and days: `142` weeks and `6` days. Show it with variables: `total = 200`, `hours = total // 60`, `minutes = total % 60` (links to L0006).

4. **Powers with `**`.** `2 ** 5` is `32`. Growth and doubling are the classic use: something that triples every day for 4 days is `start * 3 ** 4`. Note that `^` is not power in Python (it's something else; don't explain it, just warn).
   Example: `print(3 ** 4)`, `print(10 ** 6)`, `print(2 ** 0.5)` (a float result).

5. **Operator precedence and brackets.** Order: brackets, then `**`, then `* / // %`, then `+ -`. Operators at the same level go left to right, except `**`, which goes right to left.
   Examples: `1 + 2 * 3` is `7`, `(1 + 2) * 3` is `9`, `100 / 10 / 2` is `5.0`, `2 ** 2 ** 3` is `256`. The average trap: `a + b + c / 3` only divides `c`. Write `(a + b + c) / 3`. When unsure, add brackets: they are never wrong.

6. **Printing results with commas.** No f-strings yet, so labels and values are printed with `print("Hours:", hours)`. Commas add a space between items. Variables are computed once and printed later.
   Example: `print("Total:", 3 + 4, "items")` prints `Total: 7 items`.

## Common misconceptions
- "`6 / 2` gives `3`." It gives `3.0`. `/` always returns a float.
- "`//` rounds to the nearest whole number." It rounds down (floor): `7 // 2` is `3`, not `4`.
- "`%` means percent." It is the remainder.
- "`2 ^ 3` is 8." Power is `**`.
- "Python works left to right, so `2 + 3 * 4` is 20." Multiplication binds tighter.
- "`a + b + c / 3` is the average." Only `c` gets divided.
- Typing the answer into `print` (like `print("Hours:", 2)`) instead of computing it from the variable.

## Check-question ideas
1. Predict the output: `print(14 // 4, 14 % 4, 14 / 4)`.
2. Predict the output: `print(2 + 2 * 2 ** 2)` and `print((2 + 2) * 2 ** 2)`.
3. Spot the bug: `average = 6 + 8 + 10 / 3` prints `17.333333333333332`, not `8.0`. Why, and how do you fix it?
4. Explain why: `print(10 / 5)` shows `2.0` but `print(10 // 5)` shows `2`.

## Builds on
- L0004 values-and-types: `int` vs `float`, `type()`.
- L0006 variables: storing values in well-named variables, computing a new value from old ones.
- L0003 first-script: running `python file.py`, comments with `#`.
