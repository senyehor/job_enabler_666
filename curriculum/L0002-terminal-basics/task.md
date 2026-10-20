# Task: build a project folder using only the terminal

You're about to start writing lots of small programs, and a developer's day starts in the terminal: making folders,
peeking into files, tidying up. Today you set up a little `projects/` area the way a developer would, **without
touching File Explorer or the VS Code file tree**. Every folder and file below must be made, moved or deleted by
typing commands. At the end you write down what you typed, so you (and your reviewer) can see exactly how you got
there.

Use the terminal inside VS Code (Git Bash). All the work happens inside your lesson's `work/` folder.

## Requirements

1. Open the terminal and `cd` into this lesson's `work/` folder. Run `pwd` and keep what it prints; you'll need it in
   `commands.txt`.
2. Create this tree inside `work/` with `mkdir`:
   ```
   work/
     projects/
       notes/
       scratch/
   ```
3. Create `projects/notes/todo.txt` with **at least two lines** of your own to-do items. Write the first line with
   `echo "..." > file` and add the second with `echo "..." >> file`. Check it with `cat`.
4. Create `projects/scratch/ideas.txt` (any one line of text), then **move** it into `projects/notes/` with `mv`.
5. Create `projects/scratch/draft.txt` (any text). It stays in `scratch/`.
6. Create `projects/scratch/junk.txt`, look at it with `ls`, then **delete** it with `rm`.
7. At least once, use `cd ..` to go up a folder, and at least once use a full absolute path (for example
   `ls /c/Users/<you>/...` or `cd` to an absolute path and back).
8. Open the `notes` folder in VS Code from the terminal with `code projects/notes` (or `code .` from inside it).
9. Write `work/commands.txt`. You may write this one in VS Code. It must contain:
   - the absolute path `pwd` printed in step 1;
   - every command you ran, in order, one per line (it's fine to copy them from the terminal; the Up arrow and the
     `history` command help);
   - a short section that names **at least one absolute path and at least one relative path** you used, each labelled
     with the word `absolute` or `relative`. Include one path with `..` in the relative ones.

## What the result looks like

After you finish, running these from `work/` should show (your text will differ):

```
$ ls projects
notes  scratch

$ ls projects/notes
ideas.txt  todo.txt

$ ls projects/scratch
draft.txt

$ cat projects/notes/todo.txt
finish lesson 2
buy coffee
```

A `commands.txt` could start like this (yours will have your own paths and more lines):

```
pwd: /c/Users/yehor/job_enabler_666/lessons/L0002-terminal-basics/work

pwd
mkdir projects
cd projects
...

absolute: /c/Users/yehor/job_enabler_666/lessons/L0002-terminal-basics/work
relative: projects/notes
relative: ..
```

## Files in `work/`
- `projects/` with everything above (made by you in the terminal)
- `commands.txt`

## How to test
There's no program to run with `python` today; the "program" is the commands you type. To check your result, go to
the course folder (the repo root) and run:

```
python tools/learn.py test
```

The tests look at the folders and files you made and at `commands.txt`.

## Stretch goal (optional)
While standing inside `projects/scratch/`, make `projects/archive/2026/october/` in **one** command (look up
`mkdir -p`) using a relative path that starts with `..`. Then, still without leaving `scratch/`, create
`old.txt` inside `october/` with `echo` and print it with `cat`. Add these commands to `commands.txt` too.
