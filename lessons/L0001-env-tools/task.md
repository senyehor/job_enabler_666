# Task: your tool check card

You're joining a team on your first day. Before anyone lets you touch code, they ask you to check that your
machine is ready and to show that you know what each tool is for. You'll do the same: check each of your four
tools from the terminal and write a small "tool card" for each one in a text file.

## Requirements

1. Open a terminal in VS Code (`` Ctrl+` ``, Git Bash) in the course folder. Run these four commands, one at a
   time, and read what each one prints:
   ```
   python --version
   git --version
   code --version
   claude --version
   ```
2. Open a separate Git Bash window from the Start menu (keep this Claude Code session open). Go to the course
   folder the same way you did during setup (`cd job_enabler_666`, or wherever you cloned it), and run `code .`
   to open the course folder in VS Code from the terminal. Check that the Explorer on the left shows the course
   files (`README.md`, `tools/`, `lessons/` ...). If VS Code was already open on that folder, it just switches to it.
3. In VS Code's Explorer, open `lessons/L0001-env-tools/work/tools.txt`. Write one block for each of the four tools
   (Python, Git, VS Code, Claude Code), in this exact shape:
   ```
   Tool: <tool name>
   Purpose: <one sentence, in your own words, about what this tool is for>
   Version: <what the version command printed>
   ```
   - The **Purpose** is a real sentence (at least 5 words), not one word.
   - The **Version** is copied from your terminal. For Python and Git, copy the whole line, for example
     `Python 3.12.4` and `git version 2.47.0.windows.1`. For VS Code, the first line it printed (the number) is enough.
4. At the end of the file add one line that starts with `Workflow:` and says, in one or two sentences of your own,
   how the four tools work together when you do a lesson in this course.
5. Save the file (`Ctrl+S`). You can delete the comment line at the top, or leave it.

## Example

This is the shape only. Your sentences and versions will be different, and the versions must be **yours**.

```
Tool: Git
Purpose: Git keeps snapshots of my files so I can see what changed.
Version: git version 2.45.1.windows.1

Tool: ...
```

Running a version command looks like this in the terminal (`$` is the prompt; you don't type it):

```
$ git --version
git version 2.45.1.windows.1
```

## Files
- `work/tools.txt` (already there, with one comment line).

## How to check it
There's no program to run in this lesson; the "program" is the terminal commands in step 1.
To test your file, run this from the course folder (the repo root):
```
python tools/learn.py test
```
The tests check that `tools.txt` has a block for each tool, a purpose sentence and a version for each one,
that the Python and Git versions look like what the terminal prints, and that your Python version matches the
Python on this computer.

## Stretch (optional)
Type `python` with nothing after it. You're now *inside* Python (the prompt changes to `>>>`). Type `7 * 6` and
press Enter, then leave with `exit()`. Add a line `Inside Python: ...` to the end of `tools.txt` saying what
the `>>>` prompt means and what happens if you type `git --version` there.
