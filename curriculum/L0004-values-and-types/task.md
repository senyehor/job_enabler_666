# L0004 Task: What type is it?

You've just joined a team, and on your first day a bug report lands: a form saved someone's age as `"10"` instead of `10`, and now the total comes out wrong. Before you can fix bugs like that, you need to know what kind of value Python thinks it's holding. In this task you build a small "type detective" script. For each value you write down what you *think* Python will say first, then you run the script and see whether you were right.

## What to write

Write one file: `work/values.py`. The starter already has a one-line comment at the top.

Don't use variables. Put the values straight into `print`, like `print(10, type(10))`.

## Requirements

1. **Predict first.** Above each `print` line, write a comment with what you expect it to print, for example:
   ```python
   # predict: 10 <class 'int'>
   print(10, type(10))
   ```
   Write all your predictions **before** you run the script for the first time.

2. **Part 1: values and their types.** Print each of these values followed by its type, one per line, in this order:
   `10`, `-7`, `3.14`, `2.0`, `"hello"`, `"10"`, `True`

3. **Part 2: conversions.** Print each of these conversions followed by the type of the result, one per line. For example, `print(int("42"), type(int("42")))`.
   `int("42")`, `float("3.5")`, `str(7)`, `int(3.9)`, `float(5)`, `bool(0)`, `bool("hi")`

4. **Check your predictions.** Run the script. For every prediction that was wrong, don't delete it. Add a correction on the same line or the next one, for example `# predict: ... WRONG, actually ... because ...`.

5. **Part 3: a conversion that crashes.** Add this line at the end and run the script again:
   ```python
   print(int("abc"))
   ```
   It will crash. Read the error message in the terminal, starting with the last line. Then:
   - put `#` in front of that line so it no longer runs (keep the line in the file), and
   - above it, add a comment with the **name of the error** and, in your own words, why it happened.

## Example run

From inside `work/`, once everything is done, the output starts like this:

```
$ python values.py
10 <class 'int'>
-7 <class 'int'>
3.14 <class 'float'>
...
```

and Part 2 starts like this:

```
42 <class 'int'>
3.5 <class 'float'>
...
```

Some lines are left out on purpose, because those are the ones you're predicting. The script must finish without an error once Part 3's line is commented out.

## Run and test

- Run it: open the terminal, `cd` into `work/`, then run `python values.py`.
- Test it: from the repo root, run `python tools/learn.py test`.

## Stretch goal (optional)

Add a Part 4 with three more conversions you're unsure about, such as `bool("False")`, `int("  8  ")` and `float("1e3")`. Predict each one first, then run it. Write in a comment which one surprised you most.
