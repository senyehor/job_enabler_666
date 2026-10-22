# L0001 theory: Your tools: Python, Git, VS Code, Claude Code

**What you get and what you do.** This lesson has no starter code. In `work/` there is one file,
`tools.txt`, with a single comment line. Everything you write in it is yours.

Reading and trying things out takes about 15–20 minutes.

A note on terminals: the course uses **Git Bash**. PowerShell also works for every command in this lesson,
but all examples here use Git Bash.

---

## 1. What a terminal is

A **terminal** is a window where you type commands as text, press Enter, and a program answers with text.
No buttons, no menus, just text in and text out.

The line where you type is the **prompt**. In Git Bash it ends with `$`. In the examples below, `$` is the
prompt. You don't type it.

A **command** is a program's name, sometimes followed by extra words called **arguments**. Arguments tell
the program what you want.

```
$ whoami
alex
```

`whoami` is a program. It prints your user name and finishes. Then you get a new `$` prompt.

```
$ date
Thu Oct 22 18:50:12 MSK 2026
```

`date` prints the current date and time, and finishes too.

Many programs understand the argument `--version` (two dashes). It asks the program "which version are you?"
The program prints an answer and exits. It does **not** install, update or change anything. It only reports.

---

## 2. Python is an interpreter

Python code is just text in a file. On its own, it does nothing. An **interpreter** is a program that reads
Python code and carries it out, line by line. When people say "install Python", they mean installing this
interpreter. Its command is `python`.

**Version numbers.** A version like `3.12.4` has three parts: **major.minor.patch**.
- major (`3`): big changes. Python 2 is old and works differently. This course needs Python **3**, version 3.12 or newer.
- minor (`12`): new features.
- patch (`4`): bug fixes.

**The interactive interpreter.** If you type just `python` with no arguments, you don't get a version.
You go *inside* Python:

```
$ python
Python 3.12.4 (tags/v3.12.4...) on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 3
5
>>> exit()
$
```

The `>>>` prompt means **"Python is waiting for Python code"**. It does not understand terminal commands.
`exit()` leaves Python and brings you back to the terminal's `$` prompt.

How to tell where you are, at a glance:

| You see | You're in | Type here |
|---|---|---|
| `$` | the terminal (Git Bash) | commands: `whoami`, `git --version` |
| `>>>` | the Python interpreter | Python: `2 + 3`, `exit()` |

---

## 3. VS Code is an editor

**VS Code** (Visual Studio Code) is an **editor**: a program for writing and changing text files, like your code.
It has:
- the **Explorer** on the left: your folder shown as a tree of files and subfolders;
- the editing area in the middle, where you type;
- a built-in terminal at the bottom. Open it with `` Ctrl+` `` (the key left of `1`).

VS Code does not run Python by itself. When code "runs in VS Code", VS Code is really asking the Python
interpreter to run it.

You can open VS Code from the terminal. Its command is `code`:

```
$ code README.md
```

This opens one file. To open a whole folder, you give it a folder instead. A single dot `.` means
"the folder I'm in right now". So `code .` (with a space before the dot) means "open VS Code on this folder".
You'll learn more about `.` and folders in L0002.

---

## 4. Git is version control

**Git** is a **version control** program. It saves **snapshots** of a folder's files. A snapshot is called a
**commit**. With commits you can see what changed, when, and go back to an older state if something breaks.

A folder that Git tracks is called a **repository** (repo). The course folder is one.

```
$ git log --oneline
523a675 Cut lesson generation cost: Sonnet builders, no solving
5c922a6 plan: week 01 (L0001-L0015)
...
```

`git log --oneline` lists the snapshots, newest first. It only reads; it changes nothing.
(Press `q` if the list doesn't end on its own.)

**Git is not GitHub.** Git is a program on your computer and works without the internet.
GitHub is a website where people can store a copy of a repo and share it.

For now, `learn.py` makes commits for you. Later in the course you'll make them yourself.

---

## 5. Claude Code is an AI assistant in the terminal

**Claude Code** is an AI assistant that runs in the terminal. In this course it's your tutor. It reads
the lesson files, explains, asks questions, gives hints and reviews your work. It runs `learn.py` to
track your lessons. It never writes your solutions.

Its command is `claude`. Different tools print their versions in different shapes:

```
$ git --version
git version 2.47.0.windows.1
$ claude --version
2.0.14 (Claude Code)
```

Git puts words first, then the number. Claude Code puts the number first, then its name. So you read what
was printed; you don't guess.

---

## 6. How they fit together

In each lesson:
1. You **write** code in VS Code.
2. You **run** it with Python, from the terminal.
3. **Git** keeps the history of your work.
4. **Claude Code** teaches you, answers questions and reviews.

---

## Common mistakes

- **"VS Code runs my code."** VS Code is an editor. The Python interpreter runs the code.
- **"Git and GitHub are the same."** Git is the program on your computer. GitHub is a website.
- **Typing in the wrong place.** Terminal commands at `>>>` give a `SyntaxError`, because Python
  doesn't understand them. Look at the prompt: `$` or `>>>`? Use `exit()` to leave Python.
- **`python` opens the Microsoft Store.** Python is not broken. That's a Windows "app alias".
  The README explains how to turn it off.
- **`code.` without a space.** The terminal looks for a program called `code.`, doesn't find it, and says
  "command not found". The space separates the program (`code`) from its argument (`.`).
- **Thinking `--version` changes something.** It only reports.

---

## Try it yourself (not graded)

1. In Git Bash, run `whoami` and then `date`. Notice how each one prints and gives you a new `$`.
2. Type `python`, then at `>>>` type `10 - 4`. Then type `whoami` at `>>>` and read the error. Leave with `exit()`.
3. In the course folder, run `git log --oneline`. How many snapshots are there so far?

---

## Summary

- A terminal takes text commands: a program name plus arguments. `--version` only reports.
- Python is an interpreter: it runs Python code. `$` = terminal, `>>>` = inside Python, `exit()` leaves.
- VS Code is an editor. `code .` opens the current folder.
- Git saves snapshots (commits) of your files. GitHub is a separate website.
- Claude Code is your AI tutor in the terminal.

## Questions

**Q: The prompt "ends with `$`", but in `$ whoami` the `$` is at the start. Why?**
A: The real Git Bash prompt is longer, something like `alex@PC MINGW64 ~/job_enabler_666` on one line
and `$` on the next. The prompt is everything up to and including the `$`; you type right after it.
In examples, people shorten the whole prompt to just `$`. So in `$ whoami`, the `$` is where the prompt
ends, and `whoami` is the part you type.

**Q: Typing `whoami` at `>>>` gave `NameError: name 'whoami' is not defined`. What does that mean?**
A: Read the last line of the error first. Python read `whoami` as a *name* (a word that should stand for
some value) and found nothing called that. It's a terminal program, not something Python knows.
At `>>>` you type Python; at `$` you type commands.

**Q: How does the dot work as an argument?**
A: The space splits a command into words: the first word is the program, the rest are arguments.
`.` is a short name for "the folder I'm in now". So `code README.md` opens a file, and `code .` opens the
current folder (the one shown above your `$`). Without the space, `code.` is one word, and the terminal
looks for a program called `code.`, which doesn't exist.
