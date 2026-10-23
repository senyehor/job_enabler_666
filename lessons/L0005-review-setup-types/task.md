# L0005 task: The type quiz

A friend who is also learning Python keeps getting surprised by results like `"5" + "5"`, and asks you to make a quiz for them. Each line of the quiz shows a piece of Python, what it gives, and what type that result is, so they can check their guesses. To keep things tidy, the quiz gets its own folder, and you'll check that it runs no matter which folder your terminal is in. You use everything from this week: the terminal, scripts, and types.

## Part 1: Folders (terminal only)

1. Open a terminal and `cd` into `work/`. Check where you are with `pwd`.
2. Using **relative** paths only, create two folders inside `work/`: `review` and `elsewhere`.
   Use `mkdir`, not VS Code or File Explorer.

## Part 2: The quiz script

3. In VS Code, create `review/quiz.py`, so the file is `work/review/quiz.py`.
4. **Before running anything**, write your prediction as a comment above each line, for example `# predict: 10, int`.
5. The script prints one line per item below, in this order. Each line shows the expression as a text label, then its result, then its `type()`:

   | # | Expression |
   |---|---|
   | 1 | `5 + 5` |
   | 2 | `"5" + "5"` (trap 1) |
   | 3 | `int("7") + 1` (trap 2) |
   | 4 | `"7" + str(1)` |
   | 5 | `float("2.5")` |
   | 6 | `int(9.99)` |
   | 7 | `bool("False")` (trap 3) |
   | 8 | `bool("")` |

   Tip: to put double quotes inside a label, wrap the label in single quotes: `'"5" + "5" ->'`.
6. The script must run without crashing. No variables yet: put the expression straight into `print`, once inside the label and once without quotes, so Python works it out.
7. Run it, compare with your predictions, and fix any prediction comment that was wrong (leave a short note such as `# I was wrong: ...`).

## Part 3: Run it from two places

8. From `work/`, run `python review/quiz.py`.
9. Then `cd` into `elsewhere` and run the same script using a relative path that starts with `..`.

## Part 4: `answers.txt`

10. In `work/answers.txt` (already there, keep the first line), write these four lines, each followed by your explanation in your own words:
    - `Trap 1:` why `"5" + "5"` gives what it gives.
    - `Trap 2:` why `int("7") + 1` works and what it would do without `int(...)`.
    - `Trap 3:` why `bool("False")` gives what it gives.
    - `Commands:` the two commands you used in Part 3, exactly as you typed them, and which folder you were in for each.

## Example run

From `work/` (the first line is shown; the other seven are yours to discover):

```
> python review/quiz.py
5 + 5 -> 10 <class 'int'>
...
```

The `->` and spacing are up to you. What matters is that each line has the label, the result and the type.

## Files
- `work/review/quiz.py` (you create it, and its folder)
- `work/elsewhere/` (an empty folder is fine)
- `work/answers.txt`

## Run and test
- Run: `python review/quiz.py` from inside `work/` (on Windows `python review\quiz.py` works too).
- Test: `python tools/learn.py test` from the repo root.

## Stretch goal (optional)
Add a 9th line for `int(float("3.7"))` and predict it first. Then try `int("3.7")` on its own: it crashes. Read the error, comment that line out, and under a `Stretch:` line in `answers.txt` explain why going through `float` first works.
