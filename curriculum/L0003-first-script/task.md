# L0003: Writing and running your first program

Until now you have used tools other people wrote. Today you write your own program: a small text file of instructions that Python reads and carries out, one line at a time, from top to bottom. Every developer also spends a lot of time with programs that *don't* work, so in part 2 you get a script that someone typed in a hurry. It crashes. Your job is to read Python's error message the way a professional does: which line, what kind of error, and then fix it.

You write two files in `work/`: `hello.py` and `broken.py`. Both already exist with a one-line comment at the top. Keep the comment, write below it.

## Part 1: `hello.py`

1. Open `hello.py` in VS Code. Write it using only `print(...)` with text in quotes.
2. The first line it prints must be exactly `Hello, world!`
3. Next it prints a line that introduces you: `My name is <your name>.`
4. Then it prints a box made of three lines: a border made of `+` and `-`, a middle line `| Python rocks! |`, and the same border again. Make the borders as wide as the middle line, so the box looks straight.
5. The last line it prints must be `Goodbye!`
6. Run it from the terminal. Open a terminal (PowerShell), go into the `work/` folder with `cd` yourself, then run:

   ```
   python hello.py
   ```

   (If `python` isn't found on Windows, try `py hello.py`.)

Example run (your name will differ):

```
PS C:\...\work> python hello.py
Hello, world!
My name is Yehor.
+---------------+
| Python rocks! |
+---------------+
Goodbye!
```

## Part 2: `broken.py`

7. Type this script into `broken.py` **exactly as shown**: same lines, same order, and no blank lines. Line 1 is the starter comment, so `print("Shopping list")` is line 2. Don't copy-paste it. Typing it is part of the exercise.

   ```python
   # L0003 task, part 2: type in the broken shopping-list script from task.md, then fix it
   print("Shopping list")
   print("-------------")
   print("1. bread")
   prnt("2. milk")
   print("3. apples")
   print("Done!)
   ```

8. Before you run it, guess: which lines will print? Then run `python broken.py` from inside `work/`.
9. Read the error. Look for three things: the **file name and line number** (`File "...broken.py", line N`), the **error name** (the word ending in `Error` on the last line) and the message after it. Fix **only** that one mistake, then run it again.
10. There's a second mistake. Run it, read the new error, and fix it the same way. Notice which lines printed this time before the crash, and think about why that differs from the first run.
11. At the **bottom** of the file (so the line numbers above don't move), add one comment per error with its name and line number, for example:

    ```python
    # Error 1: XxxError on line N
    # Error 2: YyyError on line M
    ```

    Use the real names and numbers that Python printed.

Once it's fixed, a run looks like this:

```
PS C:\...\work> python broken.py
Shopping list
-------------
1. bread
2. milk
3. apples
Done!
```

## Testing

From the **repo root** (not `work/`), run:

```
python tools/learn.py test
```

The tests run both scripts and check what they print, and they check that `broken.py` has comments naming both errors with their line numbers.

## Stretch (optional)

Make a third file, `oops.py`, and break it on purpose in a *new* way, for example a missing `)` or a space at the start of a line. Run it and add a comment saying which error name Python gave you. It isn't tested, but bring it to the review.
