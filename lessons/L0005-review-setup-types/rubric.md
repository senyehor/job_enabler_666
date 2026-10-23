# L0005 rubric: The type quiz (review)

## Must-have
- [env.terminal] `work/review/` and `work/elsewhere/` exist, made with `mkdir` and relative paths (ask him which command he used, if it isn't clear).
- [env.run] `review/quiz.py` runs without errors from `work/` and from `work/elsewhere/` (as `python ../review/quiz.py`).
- [env.run] `answers.txt` under `Commands:` lists both commands, and says which folder he was in for each.
- [py.values] The quiz prints 8 lines in the given order. Each one has a text label, the computed result and its `type()`, and the results are correct (10 int, 55 str, 8 int, 71 str, 2.5 float, 9 int, True bool, False bool).
- [py.values] Each expression is actually computed by Python (written without quotes once), not typed in by hand as text such as `print("55 <class 'str'>")`.
- [py.values] There is a prediction comment above each line, and the wrong ones are marked as corrected.
- [py.values] `Trap 1-3` explanations are in his own words and correct: str + str joins the text; `int()` turns the text into a number before `+`, and without it you get a `TypeError`; `bool()` of a non-empty string is `True` no matter what it says.

## Likely mistakes

1. **Result hard-coded as text** (`print('"5" + "5" -> 55', "<class 'str'>")`). [py.values] major
   - Where: look at line 2 of `quiz.py`. Which part is Python working out, and which part did you type yourself?
   - Concept: text inside quotes is printed as it is. Only an expression without quotes gets computed, and `type()` has to be given that expression.
   - Example: `print("2 + 3")` prints `2 + 3`, while `print(2 + 3, type(2 + 3))` prints `5 <class 'int'>`.

2. **Ran from the wrong folder, so the command in `answers.txt` is wrong** (e.g. `python review/quiz.py` written as the command from `elsewhere`). [env.terminal] major
   - Where: the second command under `Commands:`. Run `pwd` in `elsewhere`, then `ls review`. What happens?
   - Concept: a relative path starts at the terminal's current folder, and `..` steps up one level.
   - Example: from `C:\course\notes`, the file `C:\course\todo.txt` is `..\todo.txt`.

3. **Label quotes break the line** (`print(""5" + "5" ->", ...)` gives a `SyntaxError`). [env.run] minor
   - Where: the line number in the error message. Look at where each string starts and ends.
   - Concept: a string ends at the next matching quote. Using the other kind of quote outside lets you put quotes inside.
   - Example: `print('She said "hi"')` works, and `print("She said "hi"")` doesn't.

4. **Trap 2 explanation says `int("7") + 1` is `71` or "glues"**, or doesn't say what happens without `int`. [py.values] major
   - Where: your `Trap 2:` line, compared with the output of line 3.
   - Concept: `int()` runs first and gives a number, so `+` then adds. `"7" + 1` mixes str and int, which is a `TypeError`.
   - Example: `float("1.5") + 1` is `2.5`, but `"1.5" + 1` crashes. Try both.

5. **Trap 3 explanation claims Python "reads the word"**, or calls it a Python bug. [py.values] major
   - Where: your `Trap 3:` line. What's the only string that `bool` turns into `False`?
   - Concept: `bool(text)` only asks whether the string is empty.
   - Example: predict `bool("no")`, `bool("0")` and `bool("")`, then run them.

6. **Predictions missing, or wrong predictions left uncorrected.** [py.values] minor
   - Where: the comment above each `print`.
   - Concept: predicting before running is the point of the exercise. That's how he finds out which types surprise him.
   - Example: `# predict: 2.5, float`, and after running, `# I was wrong: ...` if needed.

7. **Folders created in VS Code or File Explorer instead of with `mkdir`**, or with an absolute path. [env.terminal] minor
   - Where: ask him how he made `review` and `elsewhere`.
   - Concept: the terminal part of this review is practice with relative paths.
   - Example: from `work`, `mkdir notes` and then `mkdir notes\week1`, with no `C:\...` needed.

8. **Line order differs from the table, or there are extra spaces.** [py.values] nit
   - Mention it only if it makes the output hard to compare.

## Do not nitpick
- Variables: he hasn't learned them yet (L0006). Repeating the expression in the label, the value and `type()` is expected here.
- f-strings, `sep=`, or formatting tricks (L0008). Commas in `print` are fine.
- The separator style (`->`, `=`, `:`), and capital letters in labels.
- `/` vs `\` in paths. Both work on Windows.
- Arithmetic beyond `+` (L0007). He doesn't need it, so don't suggest it.
- File or comment style beyond the prediction comments.

## Explain back
Ask him to point at line 3 of `quiz.py` and explain, step by step, what Python does with `int("7") + 1`: what runs first, what type it has at each step, and what would change if `int(...)` were removed. Then ask why `python ../review/quiz.py` works from `elsewhere` but `python review/quiz.py` doesn't.
