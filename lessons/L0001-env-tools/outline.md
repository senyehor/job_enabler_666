# L0001 outline: Your tools: Python, Git, VS Code, Claude Code

Terminal note: the course uses **Git Bash** (README sets it as VS Code's default terminal). Mention that
PowerShell also works for every command in this lesson, but stick to Git Bash in examples.

## Learning goals (env.install)
- He can say in one sentence what Python, Git, VS Code and Claude Code each do, and how they work together in this course.
- He checks each tool from the terminal (`python --version`, `git --version`, `code --version`, `claude --version`) and can read what it printed.
- He opens the course folder in VS Code from the terminal with `code .`.

## Key points, in teaching order

1. **What a terminal is.** A window where you type commands as text and a program answers with text.
   A command is a program name plus extra words (arguments). `--version` is an argument that asks a program
   "which version are you?" and then it exits.
   Example idea: `whoami` or `date` in Git Bash, which print something and finish. Not one of the four tools.

2. **Python is an interpreter.** It's a program that reads Python code and carries it out, line by line.
   Your code is just text until the interpreter runs it. Version numbers: `3.12.4` = major.minor.patch;
   this course needs Python **3** (3.12 or newer). Python 2 is old and different.
   Example idea: open the interactive interpreter by typing just `python`, type `2 + 3`, see `5`, then
   `exit()` to leave. Show the `>>>` prompt and explain it means "Python is waiting for Python code, not
   terminal commands". (He should not type `python --version` at `>>>`.)

3. **VS Code is an editor.** It edits text files (your code), shows the folder as a tree (Explorer), and has a
   built-in terminal (`` Ctrl+` ``). It does not run Python by itself; it asks the interpreter to.
   `code .` means "open VS Code on *this* folder"; the `.` is "the folder I'm in now" (details in L0002).
   Example idea: `code README.md` opens one file instead of a folder.

4. **Git is version control.** It saves snapshots (commits) of a folder's files, so you can see what changed and
   go back. In this course `learn.py` commits for him for now; later he'll do it himself.
   Example idea: `git log --oneline` in the course folder shows the snapshots so far (read only, harmless).

5. **Claude Code is an AI assistant in the terminal.** Here it acts as his tutor: explains, asks, reviews,
   but never writes his solutions. It reads the course files and runs `learn.py`.
   Example idea: `claude --version` prints something like `2.0.14 (Claude Code)`; contrast with the shape of
   `git version 2.47.0.windows.1`. Every tool prints its version slightly differently, so you read it, not guess.

6. **How they fit together.** He writes code in VS Code, runs it with Python from the terminal,
   Git keeps the history, Claude Code teaches and checks. One picture or a 4-line list is enough.

## Common misconceptions
- "VS Code is Python" / "VS Code runs my code." It's an editor; the interpreter runs code.
- "Git and GitHub are the same." Git is the tool on his computer; GitHub is a website that stores repos.
- Typing terminal commands at the Python `>>>` prompt (or Python code in the terminal). Teach how to tell which one you're in.
- "If `python` opens the Microsoft Store, Python is broken." It's the Windows app alias; README has the fix.
- `code .` without the space, or thinking `.` is a typo.
- Thinking `--version` changes or installs something. It only reports.

## Check-question ideas
1. Predict: what does `git --version` print, roughly? Which part is the version number?
2. Explain why: you see `>>>` and type `git --version`, and get `SyntaxError`. Why, and how do you get out?
3. Spot the bug: someone types `code.` and gets "command not found". What's wrong?
4. Explain: which of the four tools would you use to (a) edit a file, (b) run it, (c) save a snapshot, (d) ask why an error happened?

## Builds on
Nothing; this is the first lesson. Setup from README (all four tools already installed).
Leads into L0002 (terminal navigation: `pwd`, `cd`, `.` and `..`) and L0003 (running a script).
