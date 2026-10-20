# L0009 Outline: Talking to the user: print and input

## Learning goals (roadmap: py.io)
- **Builds a program that asks for input and responds**: reads text with `input("prompt")`, converts it with `int()` / `float()`, computes with it and answers with formatted `print` output.
- Knows that `input()` always returns a `str`, whatever the user typed.
- Controls `print` with `sep=` (what goes between values) and `end=` (what goes at the end, a newline by default).

## Key points (teaching order)

1. **Up to now every program did the same thing every run. `input()` lets the user decide.** `input("prompt")` shows the prompt, waits for the user to type and press Enter, and gives back what was typed. Store it in a variable. Point out that the prompt has no newline, so a trailing space (`"Name: "`) makes it look nicer.
   Example idea: `city = input("Where do you live? ")`, then `print(f"Hello from {city}!")`. Run it twice with different answers.

2. **`input()` always returns a `str`, even when the user types digits.** Link back to L0004 (`"10"` vs `10`) and the L0005 `"5" + "5"` trap. Show the bug first, then the fix.
   Example idea: `year = input("Birth year: ")`, `print(2026 - year)` gives `TypeError: unsupported operand type(s) for -: 'int' and 'str'`. And `n = input("Number: ")`, `print(n * 3)` with `4` prints `444`. Use `print(type(year))` to prove it's a `str`.

3. **Convert right away: `int(input(...))` and `float(input(...))`.** Pick the type by what the value means: counts are `int`, money and measurements are `float`. Wrapping is just L0004's conversion applied to `input()`'s result, read inside out. Typing `7.5` into `int(input())` gives a `ValueError` (L0004). No `if` yet, so for now we assume the user types sensible values.
   Example idea: a fuel-cost program: `litres = float(input("Litres: "))`, `trips = int(input("Trips: "))`. Show `int("7.5")` failing and why `float` is right for litres.

4. **Input, process, output.** Most small programs have three blocks: read everything, compute with arithmetic (L0007), print the results with f-strings and `:.2f` (L0008). Keep the computing separate from the printing so each value has a name.
   Example idea: rectangle area: read width and height as floats, compute `area` and `perimeter`, print `Area: 12.50 m2`.

5. **`print` options: `sep=` and `end=`.** `print("a", "b", "c")` puts a space between values because `sep=" "` by default. `sep="-"` or `sep=" | "` changes it, and `sep=""` glues the values together. Every `print` ends with a newline because `end="\n"`. With `end=" "` or `end=""`, the next `print` carries on on the same line. Also show `print()` with nothing, which prints an empty line.
   Example idea: `print(2026, 10, 20, sep="-")` gives `2026-10-20`. `print("Loading", end="")`, then `print("... done")` gives `Loading... done`.

## Common misconceptions
- "If I type `5`, `input()` gives me the number 5." It gives the string `"5"`.
- Converting in the wrong place: `int(input("Age: ")) + 1` is fine, but `age = input("Age: ")` followed later by `age + 1` without converting crashes. Also: converting once into a new variable but then using the old string variable.
- Using `int()` for money, so `47.60` crashes with `ValueError`.
- Thinking `sep` goes between *every character*, or that it also appears at the end. It only goes *between* the values.
- Writing `print("x", end)` or `print("x" end="")` (missing `=` or comma). Keyword arguments need `name=value` and come after the values.
- Expecting the tests or a program run to "type" the input for him; when he runs it himself, the program waits. A blinking cursor with no output means it's waiting for input.
- Thinking `:.2f` changes the stored number (from L0008). It only changes how it looks.

## Check-question ideas
1. **Predict the output** if the user types `3`: `x = input("x? ")`, then `print(x + x)` and `print(int(x) + int(x))`. (Answer: `33` and `6`.)
2. **Spot the bug:** `price = input("Price: ")`, `qty = int(input("Qty: "))`, `print(price * qty)` with `2.5` and `3`. What happens and how do you fix it? (Answer: prints `2.52.52.5`; convert price with `float`.)
3. **Predict the output:** `print("a", "b", "c", sep="")`, `print("x", end="!")`, `print("y")`. (Answer: `abc`, then `x!y`.)
4. **Explain why:** `int(input("Bill: "))` crashes when the user types `19.99`, but `float(input(...))` doesn't. Which one fits a count of people?

## Builds on
- L0004 values-and-types: `str` vs `int`/`float`, `int()`/`float()` conversions, `ValueError`.
- L0006 variables: storing each answer in a well-named variable.
- L0007 arithmetic: percentages and division.
- L0008 strings-fstrings: f-strings and `:.2f` for money.
- Leads into L0010 (review), which uses `input` again, and L0011, where `if` finally lets the program react to bad input.
