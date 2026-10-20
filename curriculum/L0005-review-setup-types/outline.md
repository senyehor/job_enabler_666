# L0005 outline: Review of terminal, scripts and types

This is a review lesson with no new concepts. It brings together L0001-L0004 before variables arrive in L0006.

## Learning goals (roadmap outcomes)
- `env.terminal`: uses `pwd`, `ls`, `cd`, `mkdir` without help, and can tell absolute paths from relative ones, including `..`.
- `env.run`: writes a `.py` file and runs it with `python`. Knows that the path after `python` is relative to the folder the terminal is **in**, not to the folder the script is in.
- `py.values`: predicts the type of an expression (int, float, str, bool) and converts between types with `int()`, `float()`, `str()`, `bool()`.

## Key points (in teaching order)

1. **The terminal always has a current folder.** `pwd` shows it, and every relative path starts from there. `..` means "one folder up".
   Example (not the task): from `C:\Users\Ann\course\notes\week1`, `cat ..\todo.txt` reads `notes\todo.txt`, and `cd ..\..` lands in `course`.
   On Windows PowerShell both `\` and `/` work as separators. Show `cd`, `mkdir`, `ls` in PowerShell form.

2. **`python <path>` takes a path, like any other command.** `python hello.py` only works if `hello.py` is in the current folder. Otherwise you give a relative path (`python scripts\hello.py`, `python ..\hello.py`) or an absolute one. The usual error when the path is wrong is `can't open file ... [Errno 2] No such file or directory`. That error is about the path, not about the code.
   Example: a script `tools\greet.py` run from its parent folder as `python tools\greet.py`, then from inside `tools` as `python greet.py`.

3. **`+` depends on the types.** Two numbers are added and two strings are glued together (concatenation). A string plus a number is a `TypeError`.
   Examples: `print(2 + 3)` prints `5`, `print("2" + "3")` prints `23`, `print("ab" + "cd")` prints `abcd`, and `print("2" + 3)` crashes. Read that error together: which line, what `TypeError` means.

4. **Convert first, then compute.** `int("12") + 3` is `15` because `int()` runs first and turns the text into a number. `str(12) + "3"` is `"123"`.
   Example: `float("1.5") + 1` gives `2.5`, and `int(4.7)` gives `4` because it cuts off the decimals and does not round.

5. **`bool()` of a string only checks whether it is empty.** It does not read the words. `bool("")` is `False`, and any other string, even `"False"`, `"0"` or `" "`, is `True`. For numbers, only `0` and `0.0` are `False`.
   Example: `bool("no")`, `bool("0")`, `bool(0)`, `bool(" ")`. Let him predict all four before showing the answers.

6. **`print` with commas** prints several values separated by spaces: `print("int('3') ->", int("3"), type(int("3")))` prints `int('3') -> 3 <class 'int'>`. The label in quotes is just text. The expression without quotes is what Python actually computes. Show the difference between `print("2 + 3")` and `print(2 + 3)`. Mixing quote kinds (`'...'` outside, `"..."` inside) lets a label contain quotes.

## Common misconceptions
- "`python quiz.py` finds the file wherever it is." It only looks in the current folder.
- "`..` means the folder where the script lives." It means the parent of the terminal's current folder.
- "`"5" + "5"` is 10." Quotes make it text, so the result is `55`.
- "`bool("False")` is False." `bool` doesn't read the word, it only checks whether the string is empty.
- "`int(9.99)` rounds to 10." It cuts off the decimals and gives 9.
- "The printed `55` and the number 55 look the same, so they are the same." `type()` tells them apart. That is why the quiz prints the type.
- "The label `"5" + "5"` in quotes gets computed." Anything inside quotes is printed as it is.

## Check-question ideas
1. Predict the output: `print("3" + "4", int("3") + 4, str(3) + "4")`. (`34 7 34`, so the first and last look the same but are both str.)
2. Predict: `print(bool("0"), bool(0), bool(""), bool("False"))`. (`True False False True`)
3. Spot the bug: he is in `notes` (a sibling of `review`) and types `python review\quiz.py`, and gets `[Errno 2] No such file or directory`. Why, and what are two ways to fix it? (Go up with `cd ..` first, or run `python ..\review\quiz.py`.)
4. Explain why: `print("7" + 1)` crashes but `print(int("7") + 1)` works.

## Builds on
- L0001 env-tools: terminal, `python --version`, VS Code.
- L0002 terminal-basics: `pwd`, `ls`, `cd`, `mkdir`, absolute vs relative paths, `..`.
- L0003 first-script: writing a `.py` file, running it, reading an error and its line number.
- L0004 values-and-types: `type()`, `int()`, `float()`, `str()`, `bool()`, and the `int("abc")` crash.
