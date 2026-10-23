# L0004 Outline: Values and types

## Learning goals (roadmap: py.values)
- Predicts the type of a value or expression: `int`, `float`, `str`, `bool`.
- Converts between types with `int()`, `float()`, `str()`, `bool()`, and knows when a conversion fails (`ValueError`).

## Key points (teaching order)

1. **Every value has a type.** A value is a piece of data. Its type says what kind of data it is and what you can do with it. Use `type()` to ask Python.
   Example: `print(type(2026))`, `print(type("Kyiv"))`. Show that `print(type(...))` prints `<class '...'>` and briefly explain that "class" here just means "type".

2. **The four basic types and how to recognise them as you read.**
   - `int`: whole numbers, no dot (`0`, `-15`, `1000000`)
   - `float`: has a dot (`0.25`, `-1.0`, `100.0`). `100.0` is a float even though it is a whole number.
   - `str`: anything in quotes, single or double (`'cat'`, `"99"`, `""`). The quotes make it text, even if it looks like a number.
   - `bool`: only `True` and `False`, capitalised, no quotes.
   Example: a "sort these" list such as `55`, `55.5`, `"55"`, `False`, `"False"`, `-0.0`.

3. **print shows values, not types.** `print("5")` and `print(5)` look the same on screen. That's why `type()` matters. Also show that `print(a, b)` puts a space between the two things.
   Example: `print("8", 8)` prints `8 8`, then `print(type("8"), type(8))`.

4. **Converting with int(), float(), str().** The type name works as a converter.
   Examples (different from the task): `int("100")`, `float("0.75")`, `float(3)` gives `3.0`, `str(2.5)` gives `'2.5'`, `int(7.99)` gives `7`. It truncates (cuts off the decimal part). It does not round, and `int(-2.7)` gives `-2`.

5. **bool() and "truthiness".** `bool()` of zero or of an empty string is `False`. Almost everything else is `True`.
   Examples: `bool(0.0)`, `bool(42)`, `bool("")`, `bool(" ")` (a space is not empty). Save the `bool("False")` trap for the stretch goal or check questions.

6. **When conversion fails: ValueError.** `int("twelve")` and `int("3.5")` crash with `ValueError: invalid literal for int() with base 10: ...`. Read the traceback bottom-up: the last line gives the error name and message, and the line above shows the file and line number (links to L0003). Commenting out a line with `#` stops it from running.
   Example: `float("ten")` crashes too.

## Common misconceptions
- "`"42"` is a number because it looks like one." The quotes make it a `str`.
- "`int(3.9)` rounds to 4." It truncates to 3.
- "`2.0` is an int because it's whole." The dot makes it a float.
- "`bool("False")` is False." Any non-empty string is True.
- Writing `true`/`false` in lower case, which gives a `NameError`.
- "`int("3.5")` gives 3." It crashes; you'd need `int(float("3.5"))`.
- Thinking `type()` changes the value, or that `str(7)` and `7` would print differently.

## Check-question ideas
1. Predict the output: `print(type(7.0))`, `print(type("7.0"))`, `print(int(7.0))`.
2. Predict the output: `print(bool(""), bool(" "), bool(0), bool(-1))`.
3. Spot the bug: `print(int("4.5"))` crashes. Why, and what would you change so it prints `4`?
4. Explain why: `print("3")` and `print(3)` show the same thing, so how can you find out which one a script used?

## Builds on
- L0003 first-script: running `python file.py`, `print` with string literals, reading an error message and line number, comments with `#`.
- L0002 terminal-basics: `cd` into `work/` to run the script.
