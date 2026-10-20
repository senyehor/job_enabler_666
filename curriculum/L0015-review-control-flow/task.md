# L0015 Task: The quiz grade book

Your friend teaches an evening coding class. After every weekly quiz she has a stack of scores out of 100 and has to work out each student's letter grade, the class average and how many students passed. She does it by hand and always gets one wrong. You'll write her a small terminal program: she types the scores one at a time, types `done` when she runs out, and the program does the rest. You don't know in advance how many scores there will be, so think about which loop fits the reading part and which loop fits the grading part.

## What to write

One file in `work/`: `grades.py`. The starter has a one-line comment at the top.

Use only what you've learned so far: `if/elif/else`, `and`/`or`, `while`, `for`, lists with `.append()` and `len()`. Don't use `break`, functions, `sum()`, `max()` or string methods like `.lower()`.

## Requirements

**Reading the scores (a `while` loop)**

1. Start with an empty list. Ask for a score with `input("Score (or done): ")`.
2. Keep asking, with a `while` loop, until the user types exactly `done`. Every other answer is a whole number: turn it into an `int`.
3. If the number is between 0 and 100 (both included), add it to the list. Otherwise print `Scores must be from 0 to 100.` and don't add it. Write this check as **one** `if` that uses `and` or `or`.

**Grading (a `for` loop, after reading has finished)**

4. If the list is empty (the user typed `done` straight away), print `No scores entered.` and nothing else. The program must not crash.
5. Otherwise, loop over the list with `for` and print one line per score, in the order typed, like `85: B`. Use `if/elif/else` with these grades:

   | Score     | Grade |
   |-----------|-------|
   | 90 to 100 | A     |
   | 80 to 89  | B     |
   | 70 to 79  | C     |
   | 60 to 69  | D     |
   | below 60  | F     |

6. In the same loop, add up the total and count how many scores **passed** (60 or more).
7. After the loop, print the average with one decimal, `Average: 77.0`, and the pass count out of the total, `Passed: 2 of 3`.

The boundaries matter: 90 is an A, 89 is a B, 60 passes, 59 doesn't. Check them yourself before you run the tests.

## Example runs

From inside `work/` (what the user types is after each prompt):

```
$ python grades.py
Score (or done): 95
Score (or done): 59
Score (or done): 77
Score (or done): done
95: A
59: F
77: C
Average: 77.0
Passed: 2 of 3
```

```
$ python grades.py
Score (or done): 80
Score (or done): 150
Scores must be from 0 to 100.
Score (or done): 69
Score (or done): done
80: B
69: D
Average: 74.5
Passed: 2 of 2
```

```
$ python grades.py
Score (or done): done
No scores entered.
```

Spacing doesn't matter, but keep the score-colon-letter form (`85: B`) and the labels `Average:` and `Passed:` as shown. The tests look for them. You only need to handle whole numbers and the exact word `done`; typing `abc` may crash, and that's fine for now.

## Run and test

- Run it: in the terminal, `cd work`, then `python grades.py`.
- Test it: from the repo root, run `python tools/learn.py test`.

## Stretch goal (optional)

After `Passed:`, also print the highest and lowest score, `Highest: 95` and `Lowest: 59`, found by hand inside your `for` loop (no `max()` or `min()`). Hint from L0014: what should the "best so far" start as?
