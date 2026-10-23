# L0003 Writing and running your first program

**What you get and what you write:** the starter gives you two files in `work/`, `hello.py` and `broken.py`, each
with only a one-line comment at the top. Every line of code below that comment you type yourself.

Reading time: about 15–20 minutes, including trying things out. Keep a Git Bash terminal open in VS Code. For the
experiments, make a scratch folder in your home folder (for example `mkdir ~/pytry` and `cd ~/pytry`), not in
`work/`.

---

## Recap: who does what (from L0001 and L0002)

- **VS Code** is the editor. It only lets you type and save text.
- **The terminal** is the window where you type commands. It doesn't understand Python.
- **`python`** is a program (the interpreter). You start it from the terminal, like `cd` or `ls`.

So in `python weather.py`, `python` is the **command** (the program), and `weather.py` is its **argument** (the file
it should read). And `weather.py` is a relative path, so it's looked up in the folder `pwd` shows.

---

## 1. A program is a text file; the interpreter carries it out

A Python program (also called a **script**) is a plain text file whose name ends in `.py`. There's nothing magic
inside, only lines of text. You could open it in Notepad and see the same thing.

Two separate steps:

1. **Write and save** the file in VS Code. Saving doesn't run anything.
2. **Run** it: the terminal starts `python`, `python` reads the file and does what each line says.

If you change the file and forget to save (VS Code shows a dot `●` on the tab), `python` runs the *old* saved
version. Save with **Ctrl+S** before every run.

---

## 2. Running a script: `python file.py`, from the right folder

Say you have a file `weather.py` in `~/pytry`:

```
$ cd ~/pytry
$ ls
weather.py
$ python weather.py
Weather report
```

`python weather.py` looks for `weather.py` **in the current folder**. If you're somewhere else, you get:

```
$ cd ~
$ python weather.py
C:\...\python.exe: can't open file 'C:\\Users\\ann\\weather.py': [Errno 2] No such file or directory
```

Read it: "can't open file". Python never even started reading your code. **Your code is not broken.** You're
standing in the wrong folder. Two fixes, both from L0002:

- `cd` to the folder with the file, then `python weather.py`, or
- give the path from where you are: `python pytry/weather.py`.

Habit: `pwd` and `ls` before running. If you can see the file in `ls`, `python <that name>` will find it.

If `python` itself isn't found on Windows, `py weather.py` does the same thing.

**Two different prompts.** If you type just `python` (no file) you start Python's interactive mode, and the prompt
changes to `>>>`. That's Python waiting for Python code, not for terminal commands. Typing `python weather.py` there
gives a `SyntaxError`. Type `exit()` and press Enter to get back to the terminal (`$`, or `PS C:\...>` in
PowerShell).

### Try it yourself (1)

In `~/pytry`, run `code weather.py`, type `print("Weather report")`, save, and run `python weather.py`. Then
`cd ~` and run the same command again. Read the error. Then run it with the path instead.

---

## 3. `print` and text in quotes

`print(...)` shows one line on the screen.

```python
print("Roses are red")
print('Violets are blue')
print()
print("Python is fun")
```

Output:

```
Roses are red
Violets are blue

Python is fun
```

- Text in quotes is called a **string** (a string of characters).
- The quotes mark where the text starts and ends. They are **not** printed.
- `"` or `'` both work, as long as both ends match.
- Each `print` makes its own line. `print()` with nothing inside prints an empty line.
- What's between the quotes is printed **exactly**, character for character, spaces included.

Python is **case-sensitive**: `print` works, `Print` and `PRINT` don't.

---

## 4. Top to bottom, one line at a time

Python runs the lines in order: line 1, then line 2, and so on. The output appears in the same order.

```python
print("Step 1: boil water")
print("Step 2: add pasta")
print("Step 3: wait 10 minutes")
```

Swap the last two lines and the output swaps too: Python doesn't know what makes sense, it just goes in order.

### Try it yourself (2)

Make `pasta.py` with the three steps above. Before running, swap steps 2 and 3 and write down what you expect to
see. Then run it.

---

## 5. Reading an error

When something goes wrong, Python prints an error report called a **traceback**. Here's a file `report.py`:

```python
print("Weather report")
Print("Sunny")
```

Running it:

```
Weather report
Traceback (most recent call last):
  File "C:\Users\ann\pytry\report.py", line 2, in <module>
    Print("Sunny")
    ^^^^^
NameError: name 'Print' is not defined. Did you mean: 'print'?
```

Read it like a detective, **last line first**:

1. **Last line: error name and message.** `NameError: name 'Print' is not defined`. Python doesn't know the word
   `Print`.
2. **The `File ..., line N` line: where.** Line 2 of `report.py`.
3. **The code line and the `^^^` marker:** the exact spot.

Then go to that line in VS Code (the line numbers are on the left) and fix it.

There are two kinds of errors you'll meet today, and they behave differently:

**`NameError`: crash while running.** The file is valid Python, so Python starts running it top to bottom. Line 1
runs and prints `Weather report`. At line 2 it meets an unknown name and stops. Lines **before** the error already
ran; lines after it don't.

**`SyntaxError`: Python can't read the file at all.** "Syntax" means the grammar of the language. Python first reads
the whole file to check it's grammatical, and only then runs it. If the grammar is broken anywhere, **nothing runs,
not even line 1**.

```python
print("Weather report")
print('Rain")
```

```
  File "C:\Users\ann\pytry\report.py", line 2
    print('Rain")
          ^
SyntaxError: unterminated string literal (detected at line 2)
```

Notice: no `Weather report` this time, even though line 1 is fine. ("Unterminated string literal" means: a string
was opened with a quote and never closed with a matching one. The `'` opens it, the `"` doesn't count as the end.)

**The line number is where Python *noticed* the problem.** Usually that's the broken line. But with a missing `)`,
Python may only notice on the next line, so if the reported line looks fine, check the line above it.

**Fix one error, run again.** A file can have several mistakes, and Python reports one at a time. Fixing the one it
showed and running again is how you find the next.

### Try it yourself (3)

Make `days.py`:

```python
print("Monday")
print("Tuesday")
pirnt("Wednesday")
```

Predict: what prints before the crash, which error, which line? Run it and compare. Then change line 3 to
`print("Wednesday)` and predict again: what changes, and why?

---

## 6. Comments

A `#` starts a **comment**: everything from `#` to the end of the line is for humans, and Python skips it.

```python
# This script prints a weather report
print("Weather report")  # the title
```

Comments are ignored when running, but they are still **lines of the file**. Line numbers in a traceback count every
line, including comments and blank lines. If you add a comment at the top, every line below moves down by one, and
an error that was "line 5" becomes "line 6".

---

## Common mistakes

- **Forgetting to save** before running, then wondering why nothing changed.
- **Running from the wrong folder.** "can't open file ... No such file or directory" is about *where you are*, not
  your code. `pwd`, `ls`, then run.
- **Typing `python file.py` inside `>>>`.** Leave with `exit()` first.
- **Thinking Python skips the bad line and runs the rest.** A `SyntaxError` stops everything before it starts; a
  `NameError` stops at that line.
- **`print(Hello)` without quotes.** Without quotes Python thinks `Hello` is a name, so it's a `NameError`.
- **`Print` or `PRINT`.** Python is case-sensitive.
- **Mixing quotes:** `print('Hi")`. Both ends must match.
- **A quote inside the text:** `print('It's late')`. The `'` in `It's` closes the string early. Use the other quote
  type outside: `print("It's late")`.
- **Using the VS Code Run button instead of the terminal.** Today, run everything with `python ...` in the terminal,
  so you see exactly which folder it runs from.

---

## Summary

- A `.py` file is plain text. VS Code edits it; `python file.py` runs it. Save first.
- `python file.py` looks for the file relative to the current folder. "can't open file" means wrong folder.
- `print("...")` prints the text between the quotes exactly, one line per `print`; `print()` is an empty line.
- Lines run top to bottom, in order.
- Read a traceback from the bottom: error name and message, then `line N`, then the code and `^`.
- `SyntaxError`: file can't be read, nothing runs. `NameError`: runs until that line, then stops.
- `#` comments are skipped by Python but still count as lines.

---

## Questions

**Q: Why `code weather.py` and not `echo "Weather report" > weather.py`?**
A: The terminal strips the quotes, so the file would contain just `Weather report`: English, not Python code, and
running it gives a SyntaxError. The file needs `print("Weather report")`. Also, programs are many lines that you keep
editing, and the editor shows line numbers you need for reading errors. The terminal makes folders and runs things;
VS Code writes the code. `code weather.py` creates the file and opens it.
