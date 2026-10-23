# Review round 1: changes requested

Tests: 5 passed, 3 failed

## What's good
- Every line of `quiz.py` lets Python do the work: the expression appears once inside the label and once without quotes, both as the value and inside `type()`. Nothing is hard-coded, and the script runs cleanly both from `work/` and from `work/elsewhere/` with `python ../review/quiz.py`.
- Your trap explanations are correct and in your own words. Trap 2 is especially good. You explain that `int()` turns the text into a number *before* the `+`, and you quote the exact `TypeError` you'd get without it. Your prediction for item 2 is `55`, with no quote marks, which is exactly how `print` shows a str.

## Issues
### 1. One quiz item is missing (major)
`work/review/quiz.py:6-7`: the task table has 8 items, but the script prints only 7 lines. Compare your lines with the table in `task.md` one by one, top to bottom. Which row has no line, and where in the order should it go? Remember to write its prediction comment *before* you run it.
Hint (level 1): after `int("7") + 1`, what is the next row in the table?

### 2. `Commands:` section is missing its label and the folders (major)
`work/answers.txt:5-6`: both commands are right, but the task asks for a line starting with `Commands:`. For each command it also asks *which folder you were in* when you typed it. Re-read step 10 of `task.md`, the last bullet. What two things does it ask for besides the commands themselves?
Hint (level 1): if a friend copied just these two lines, would they know where to `cd` before running each one?

## For next time
- `quiz.py:3-4`: the task writes trap 1 as `"5" + "5"` with double quotes; you used `'5' + '5'`. It means the same thing to Python, so it's fine, but the label your friend sees is slightly different from the task's (the tip in step 5 shows how to keep the double quotes).
- `answers.txt:4`: Trap 3 is right. Saying "only the empty string `""` gives `False`" would make it even sharper.
