# L0009 Task: Split the bill

You're out for dinner with friends, the bill arrives, and everyone pulls out their phone to work out the tip and who owes what. Someone always gets it wrong. Your programs so far printed the same thing every time you ran them. This one is different: it **asks** the person at the table for the numbers and answers with *their* tip, total and share. That's your first interactive program.

## What to write

Write one file: `work/tip.py`. The starter has a one-line comment at the top.

## Requirements

1. **Header.** First print a title line: `=== Tip calculator ===`.
2. **Ask three questions with `input()`**, in this order:
   - the bill amount, e.g. `Bill amount: ` (it can have cents, like `47.60`)
   - the tip percent, e.g. `Tip percent: ` (a whole number, like `15`)
   - the number of people, e.g. `Number of people: ` (a whole number)

   `input()` always gives you text. Convert each answer to the right type: `float` for the bill, `int` for the percent and the number of people. You can assume the user types sensible numbers (no checking needed yet).
3. **Compute** three values, each in its own variable:
   - the tip: the bill times the percent, divided by 100
   - the total: the bill plus the tip
   - each person's share: the total divided by the number of people
4. **Print a summary** with f-strings. Every money amount shows exactly 2 decimals (`:.2f`). Print an empty line first, then one line each for the bill, the tip and the total (see the example).
5. **Recap line with `sep`.** Print one line that starts with `Recap` and lists the bill, tip, total and share, separated by ` | `. Do it with **one** `print` call that has several values and `sep=" | "`. Don't type the `|` characters into a string yourself.
6. **Share line with `end`.** Print `Each person pays:` and the share amount using **two** `print` calls. Use `end=` on the first one so both parts end up on the same line.

## Example runs

What you type is shown after each prompt.

```
$ python tip.py
=== Tip calculator ===
Bill amount: 47.60
Tip percent: 20
Number of people: 3

Bill:  47.60
Tip:   9.52
Total: 57.12
Recap | 47.60 | 9.52 | 57.12 | 19.04
Each person pays: 19.04
```

```
$ python tip.py
=== Tip calculator ===
Bill amount: 100
Tip percent: 10
Number of people: 3

Bill:  100.00
Tip:   10.00
Total: 110.00
Recap | 100.00 | 10.00 | 110.00 | 36.67
Each person pays: 36.67
```

Notice in the second run: `110 / 3` is `36.666...`, and `:.2f` shows it as `36.67`.

The exact wording of the prompts and labels and the spacing don't need to match. The numbers do, and so do the `Recap` line with its ` | ` separators and the `Each person pays:` line.

## Run and test

- Run it: open the terminal, `cd` into `work/`, then run `python tip.py`. The program waits for you to type each answer and press Enter. If nothing seems to happen, it's waiting for you.
- Test it: from the repo root, run `python tools/learn.py test`. The tests type the answers for you and check the numbers in your output.

## Stretch goal (optional)

Line up the summary like a real receipt: make the labels and amounts form two neat columns with width specs, for example `{"Total:":<8}{total:>8.2f}`. Then try a bill of `1234.5` to check the columns still line up.
