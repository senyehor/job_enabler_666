# Review round 3: approved

Tests: 8 passed, 0 failed

## What's good
- `answers.txt:5` now starts with `Commands:` and says which folder you were in for each command. Both commands are correct. The second one uses `..` to step up from `elsewhere` to `work/` and then goes into `review/`. I ran the quiz from both places, and it prints the same 8 lines each time.
- `quiz.py` is solid from top to bottom. All 8 items are in the table's order. Python works out every result, both the value and the `type()`, so nothing is typed in by hand. Every prediction comment matches the real output. Your Trap 2 explanation gets the order right: `int()` turns the text into a number *before* the `+` runs, and you quoted the exact `TypeError` you'd get without it.

## Issues
### 1. The `Commands:` line is hard to read (minor)
`work/answers.txt:5`: both commands and both folders are on one line, with nothing between them. A reader has to work out where the folder name ends and the command begins, and where the first command ends and the second starts. This doesn't block approval, because everything the task asks for is there.
Hint (level 1): imagine your friend copying the first command straight from this line into the terminal. Where would they stop selecting? Could you set it out so the answer is obvious?

## For next time
- `quiz.py:4` and `quiz.py:8`: the labels use `'5'` and `'7'` where the task has `"5"` and `"7"`. Python treats both the same, so this is only about matching the task's wording.
- `answers.txt:4`: Trap 3 is right. "Only the empty string `""` gives False" would be more exact than "anything present inside quotes".

## Explain back
Point at line 6 of `quiz.py` and explain, step by step, what Python does with `int("7") + 1`. What runs first? What type is the value at each step? What would change if you removed `int(...)`? Then explain why `python ../review/quiz.py` works from `elsewhere` but `python review/quiz.py` doesn't. This matters because "what runs first, and what type does it give" is how you'll read every expression from now on. Knowing where a relative path starts is how you'll avoid most "file not found" errors.
