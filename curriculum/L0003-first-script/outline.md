# L0003 outline: Writing and running your first program

## Learning goals (env.run)
- Writes a `.py` file in VS Code and runs it with `python <file>` from the terminal, from the right folder.
- Reads a basic error message: finds the file and line number, names the error (`SyntaxError`, `NameError`), and fixes the line.

## Key points, in teaching order

1. **A program is a text file of instructions; the interpreter carries them out.**
   `hello.py` is plain text. VS Code only edits it. `python` (the interpreter from L0001) reads it and does what it says. Saving is not running, and running is not saving.
   Example: open a `.py` file in Notepad to show it's just text, then run the same file with `python`.

2. **Running a script from the terminal: `python file.py`, from the folder that holds it.**
   The path is resolved relative to the current folder (L0002's relative paths). Show `pwd` / `ls` first, then the run. Show the failure from the wrong folder: `can't open file '...\notes.py': [Errno 2] No such file or directory`. That error comes from the terminal side, not from your code. Mention `py` as the Windows fallback launcher. Also the difference between the PowerShell prompt `PS C:\...>` and the Python REPL `>>>`: typing `python hello.py` inside `>>>` gives a SyntaxError. Show `exit()` to get out.
   Example: a `notes.py` in `work/projects/` run as `python projects\notes.py` from `work/`, and as `python notes.py` after `cd projects`.

3. **`print` and string literals.**
   `print("text")` puts one line on screen. Quotes mark where text starts and ends, and they aren't printed. Either `'` or `"` works, as long as both ends match. Each `print` makes a new line. `print()` with nothing inside gives an empty line.
   Example: printing a three-line poem, with a blank line in between using `print()`.

4. **Top to bottom, one line at a time.**
   Lines run in order. Output order = line order. Swapping two lines swaps the output.
   Example: a "recipe steps" script. Swap steps 2 and 3, then predict and run.

5. **Reading an error: where, what kind, what message.**
   Anatomy of a traceback: `File "...", line N`, the line of code shown, the `^` marker, and the last line `ErrorName: message`. Read the last line first, then go to the line number.
   - `SyntaxError`: Python can't even understand the file, so **nothing** runs, not even the lines before the mistake. Examples: an unclosed quote, a missing `)`.
   - `NameError`: the file is valid, it runs, and it crashes when it reaches an unknown name. The lines **before** it already printed.
   - The line number is where Python *noticed* the problem. That's usually the line itself. With a missing `)` it can be the next line.
   Example (not the task's): `print("Weather report")` then `Print("Sunny")`. Capital P gives NameError on line 2, after line 1 already printed. Then `print('Rain")` with mismatched quotes gives a SyntaxError and nothing prints.

6. **Comments.**
   `#` to the end of the line is for humans. Python skips it. Adding lines at the top shifts every line number below, which is why the task puts comments at the bottom.

## Common misconceptions
- "Saving the file runs it" or "running it in VS Code's Run button is the same thing". Insist on the terminal this time.
- Typing `python hello.py` inside the `>>>` REPL.
- Running from the repo root and getting "No such file", then thinking the code is wrong.
- Thinking Python runs every line it can and skips the bad one. In fact a SyntaxError stops everything, and a runtime error stops at that line.
- Thinking the quotes are printed, or that `print(Hello)` without quotes prints `Hello` (it's a NameError).
- `Print` / `PRINT` work like `print`. Python is case-sensitive.
- The error is always on exactly the line reported (missing `)` counter-example).

## Check-question ideas
1. **Predict:** a 4-line script whose 3rd line is `prnt("c")`. What is printed before the crash, and what is the error name and line?
2. **Predict:** the same script, but line 3 is `print("c)`. What is printed now? Why is it different from question 1?
3. **Spot the bug:** `print('It's sunny')`. What error happens, and how would you fix it (use `"` outside)?
4. **Explain why:** he's in the repo root and runs `python hello.py`, and gets `No such file or directory`. Is the code broken? What two ways can fix it?

## Builds on
- L0001 env-tools (env.install): what the interpreter and the editor are, `code .`, and `python --version`.
- L0002 terminal-basics (env.terminal): `cd`, `pwd`, `ls`, and relative paths, needed to get into `work/` and to run files by path.
