# L0004 Rubric: Values and types

## Must-have
- [py.values] Part 1 prints all 7 values with their `type()`, in the order given: `10`, `-7`, `3.14`, `2.0`, `"hello"`, `"10"`, `True`.
- [py.values] Part 2 prints all 7 conversions with the type of the result: `int("42")`, `float("3.5")`, `str(7)`, `int(3.9)`, `float(5)`, `bool(0)`, `bool("hi")`.
- [py.values] There is a prediction comment above each print, and wrong predictions are corrected but not deleted. This is the main learning evidence, so look for the corrections.
- [py.values] `int("abc")` is still in the file, commented out, with a comment naming `ValueError` and a reason in his own words.
- [env.run] The script runs from `work/` with `python values.py` and doesn't crash.

## Likely mistakes

1. **Predicts `"10"` as int** (py.values, minor)
   - Where: "Look at your Part 1 prediction for the sixth value. What's around it that isn't around the first one?"
   - What: quotes make a `str`. See "The four basic types" in theory.md.
   - How: `print(type("2026"))` and `print(type(2026))`: run both and compare.

2. **Predicts `int(3.9)` gives 4** (py.values, minor)
   - Where: "Check your prediction for `int(3.9)` against what the terminal printed."
   - What: `int()` truncates, it doesn't round. See "Converting" in theory.md.
   - How: try `int(8.99)` and `int(-1.5)` in a scratch file.

3. **Predicts `bool("hi")` or `bool(0)` wrongly** (py.values, minor)
   - Where: "Which of your bool predictions did the run disagree with?"
   - What: zero and empty are False, everything else is True.
   - How: compare `bool(0.0)`, `bool("")`, `bool("0")`.

4. **Deleted wrong predictions instead of correcting them, or wrote predictions after running** (py.values, major if all predictions match perfectly with no corrections and it seems unlikely, otherwise minor)
   - Where: "Show me a prediction that turned out wrong. Where's the correction?"
   - What: the point of the task is to compare what you expected with what happened. See task requirement 4.
   - How: an example pattern on different data: `# predict: 1 <class 'int'>  WRONG: actually 1.0 <class 'float'>, the dot makes it float`.

5. **Deleted the `int("abc")` line, or the script still crashes** (env.run, major if it crashes, minor if deleted)
   - Where: "Run `python values.py`. What's the last line it prints?"
   - What: `#` turns a line into a comment that Python skips (from L0003).
   - How: `# print("this won't run")` vs `print("this will")`.

6. **Error comment names the wrong error, or just copies the message** (py.values, minor)
   - Where: "Read the last line of the traceback again. What's the word before the colon?"
   - What: the error name is the first word on the last line, and the rest explains it.
   - How: `float("ten")` gives the same error name. What do the two cases have in common?

7. **Writes `print(10, type("10"))` or similar mismatches** (py.values, minor)
   - Where: point to the line whose value and type don't describe the same thing.
   - What: the value and the `type(...)` should use exactly the same literal.
   - How: `print(5.5, type(5.5))` is correct, `print(5.5, type("5.5"))` is not.

## Do not nitpick
- Using variables instead of literals is against the task wording, but don't fail him for it. At most, mention it.
- Comment style, wording or capitalisation of predictions. Anything readable is fine.
- Spacing in output, single vs double quotes.
- Anything not taught yet: f-strings, `input()`, functions, `isinstance`, `if`, `try/except`. Don't suggest them.
- Python style rules (PEP 8) beyond basic readability.

## Explain back
Ask him to explain, in his own words, why `print("10")` and `print(10)` look identical but `type()` gives different answers. Then ask what `int("10")` changes.
