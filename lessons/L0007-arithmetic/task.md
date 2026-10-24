# L0007 Task: The workout stats calculator

A friend is building a fitness app and asks you to work out the numbers for its weekly "stats" screen. The watch only stores raw data: the total workout time as one big number of seconds, the distance of each run, and a points streak that doubles every week. Nobody wants to read "9876 seconds", so your script has to turn that into hours, minutes and seconds, find the average run, and work out the points. Before that, you warm up by predicting what Python does with a few tricky expressions, because getting the order of operations wrong is how apps end up showing the wrong numbers.

## What to write

Write one file: `work/calculator.py`. The starter already has a one-line comment at the top.

Print with commas, like `print("Hours:", hours)`. No f-strings yet.

## Requirements

### Part 1: predict, then check

1. Print each of these 8 expressions, one per line, **with the expression as a label**, in this order:

   | Expression     |
   |----------------|
   | `2 + 3 * 4`    |
   | `(2 + 3) * 4`  |
   | `20 - 10 - 5`  |
   | `2 ** 3 ** 2`  |
   | `7 / 2`        |
   | `7 // 2`       |
   | `7 % 2`        |
   | `6 / 2`        |

   Put the label in quotes and the real expression after the comma, for example:
   ```python
   # predict: 11
   print("1 + 5 * 2 =", 1 + 5 * 2)
   ```
2. Above each `print`, write a `# predict:` comment with the result you expect. Write all 8 **before** you run the script for the first time.
3. Run it. For each wrong prediction, don't delete it. Add a correction, for example `# predict: 12  WRONG, actually 11 because * goes first`.

### Part 2: the stats screen

4. Store the raw data in variables at the top of Part 2. Use these exact values:
   - `total_seconds = 9876`
   - four run distances in km: `7`, `4`, `9` and `6` (one variable each, for example `run1`, `run2`, ...)
   - `start_points = 50` and `weeks = 10`
5. **Workout time.** Turn `total_seconds` into whole hours, leftover minutes and leftover seconds using `//` and `%`. Print one line:
   `Workout time: <hours> h <minutes> min <seconds> s`
6. **Average distance.** Compute the average of the four runs with `/` and print:
   `Average distance: <average> km`
   Then compute it again with `//` and print:
   `Whole km average: <whole average>`
7. **Points.** The points double every week, so after `weeks` weeks they are `start_points` times 2 to the power of `weeks`. Compute this with `**` and print:
   `Points after 10 weeks: <points>`
8. Every number in Part 2 must be **computed from the variables**. Don't work it out on paper and type the answer into `print`. If the watch sent `total_seconds = 5000` tomorrow, changing that one line should be enough.

## Example run

From inside `work/`, Part 1 starts like this (the rest is what you're predicting):

```
$ python calculator.py
2 + 3 * 4 = 14
...
```

Part 2 has this shape. The real numbers are left out on purpose:

```
Workout time: ? h ? min ? s
Average distance: ? km
Whole km average: ?
Points after 10 weeks: ?
```

Check your Part 2 numbers yourself: `hours * 3600 + minutes * 60 + seconds` should give back `9876`.

## Run and test

- Run it: open the terminal, `cd` into `work/`, then run `python calculator.py`.
- Test it: from the repo root, run `python tools/learn.py test`.

## Stretch goal (optional)

Add a Part 3 with two more predictions you're unsure about: `-2 ** 2` and `17 % 5 * 2`. Predict, run, and write in a comment which rule explains each result. Then change `total_seconds` to `100000` and check that your workout time still makes sense (more than 24 hours is fine).
