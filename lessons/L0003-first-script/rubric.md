# L0003 rubric: Writing and running your first program

## Must-have
- [env.run] `hello.py` runs with `python hello.py` from inside `work/` with no error.
- [env.run] `hello.py` prints, in order: `Hello, world!`, a `My name is ...` line, a three-line box (`+---+` border, `| Python rocks! |`, border), and `Goodbye!` as the last line, using only `print` with string literals.
- [env.run] `broken.py` keeps the original script's lines in the original order and is fixed: it prints all six lines and exits cleanly.
- [env.run] Comments at the bottom of `broken.py` name both errors with the right line numbers: **SyntaxError on line 7** (unclosed quote in `print("Done!)`), **NameError on line 5** (`prnt`). If he typed extra or missing lines, the numbers will differ. Accept numbers that match *his* file as it was before the fixes, and ask him to show where they came from.
- [env.terminal] He can show (or describe) running both scripts from the terminal after `cd`-ing into `work/` himself, not just with VS Code's Run button.

## Likely mistakes

1. **Line numbers from a different layout** (he added a blank line or removed the starter comment, so the numbers in his comments don't match the task's). [env.run], minor
   - Where: look at the comment lines at the bottom of `broken.py` and count from line 1 of the file.
   - Concept: the line number in the traceback counts every line of the file, including comments and blank lines.
   - Example: in a file with `# notes`, an empty line and then `prnt("hi")`, the traceback says line 3, not line 1.

2. **Fixed both bugs without running in between, so he never saw the second error message.** He may then guess the error names. [env.run], major
   - Where: ask what Python printed on his *second* run, and which lines appeared before the crash.
   - Concept: a SyntaxError stops the whole file before anything runs. A NameError only happens when Python reaches that line.
   - Example: `print("a")` then `print(b)` prints `a` and then NameError. `print("a")` then `print("b)` prints nothing at all.

3. **Swapped the error names or line numbers** (for example "NameError on line 7"). [env.run], major
   - Where: the two comments at the bottom of `broken.py`.
   - Concept: the last line of a traceback gives the error name, and the `File ..., line N` line gives where it was.
   - Example: in `File "x.py", line 3` followed by `NameError: name 'pirnt' is not defined`, the line is 3 and the name is NameError.

4. **Box borders don't line up** with the middle line (a different number of characters). [env.run], nit
   - Where: the three `print` lines that make the box in `hello.py`.
   - Concept: `print` shows the text between the quotes exactly, character for character, spaces included.
   - Example: `print("+---+")` and `print("| hi |")` are 5 and 6 characters wide, so the right edge is crooked. Count the characters.

5. **Fixed the error in a different way that changes the output** (for example deleting the `prnt` line instead of correcting it, or changing `Done!` text). [env.run], major
   - Where: compare the output of `broken.py` with the expected run in the task.
   - Concept: fixing a bug means making the line do what it was meant to do, not removing it.
   - Example: if `prnt("Step 2")` crashes, the fix is `print("Step 2")`. Deleting it loses step 2.

6. **Ran from the wrong folder** and got `can't open file ... No such file or directory`, then edited the code trying to "fix" it. [env.terminal], minor
   - Where: the terminal prompt or `pwd` output just before `python hello.py`.
   - Concept: `python hello.py` looks for `hello.py` relative to the current folder.
   - Example: from the repo root, either `cd work` and then `python hello.py`, or `python work\hello.py`.

7. **Deleted the starter comment on line 1.** [env.run], nit. It only matters because it shifts line numbers (see mistake 1).
   - Where: line 1 of `hello.py` / `broken.py`.
   - Concept: comments are ignored by Python but still count as lines.
   - Example: removing one line at the top turns a "line 5" error into "line 4".

## Don't nitpick
- Variables, f-strings, `sep`/`end` or any other way of building the output. He hasn't learned them. Plain `print("...")` repeated is exactly right here.
- `'` vs `"` quote style, or spacing inside `print( "x" )`.
- Whether he used `python` or `py` on Windows.
- How wide the box is, or minor extra spaces in it, as long as it reads as a box.
- Extra comments he wrote to himself.

## Explain back
Ask him: "On your first run of `broken.py` nothing printed at all, but on the second run three lines printed before it crashed. Why?" He should say that a SyntaxError means Python can't read the file, so nothing runs. A NameError happens while running, after the earlier lines already ran top to bottom.
