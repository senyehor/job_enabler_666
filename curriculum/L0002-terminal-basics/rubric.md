# L0002 rubric: Moving around in the terminal

The "code" here is the folder tree in `work/projects/` plus `work/commands.txt`. Check the tree with `ls -R` (or the
tests), and read `commands.txt` to see that the work was really done in the terminal.

## Must-have
- [env.terminal] `projects/notes/` and `projects/scratch/` exist, made with `mkdir` (visible in `commands.txt`).
- [env.terminal] `projects/notes/todo.txt` has at least two lines, written with `echo ... >` and then `echo ... >>`.
- [env.terminal] `ideas.txt` was created in `scratch/` and moved with `mv`; it is now only in `notes/`.
- [env.terminal] `projects/scratch/draft.txt` exists; `junk.txt` was created and removed with `rm`.
- [env.terminal] `commands.txt` lists the commands in a believable order, including `pwd`, `ls`, `cd`, `cd ..`,
  `mkdir`, `cat`, `mv`, `rm`.
- [env.terminal] `commands.txt` contains the absolute path of `work/` from `pwd`, and labels at least one absolute and
  one relative path correctly (a relative one uses `..`).
- [env.install] `code projects/notes` (or `code .`) appears in the commands.

## Likely mistakes

### Files made in VS Code or File Explorer instead of the terminal
- concept: env.terminal / severity: major (the whole point of the lesson)
- Hints:
  1. Look at `commands.txt`: which command created `todo.txt`?
  2. Files can be created from the terminal with `echo "text" > file`; `>>` adds a line.
  3. Example: `echo "flour" > shopping.txt` then `echo "eggs" >> shopping.txt`, then `cat shopping.txt`.

### Second `>` overwrote the first line
- concept: env.terminal / severity: minor (the test catches it as "only one line")
- Hints:
  1. Run `cat projects/notes/todo.txt`. How many lines are there compared with how many `echo` commands you ran?
  2. `>` replaces the whole file; `>>` appends to the end.
  3. Example: `echo a > x.txt; echo b > x.txt` leaves only `b`; `echo a > x.txt; echo b >> x.txt` leaves both.

### `ideas.txt` copied (or re-created) instead of moved; it's still in `scratch/`
- concept: env.terminal / severity: minor
- Hints:
  1. Run `ls projects/scratch`. What's still in there that shouldn't be?
  2. `mv source destination-folder/` moves; the file disappears from the source.
  3. Example: `mv photo.jpg pictures/` then `ls` shows `photo.jpg` is gone from here and is in `pictures/`.

### Backslashes in Git Bash paths (`projects\notes` became `projectsnotes`)
- concept: env.terminal / severity: minor
- Hints:
  1. Run `ls` in `work/`. Is there a strangely named folder like `projectsnotes`?
  2. Git Bash uses `/` as the separator; `\` is an escape character there. PowerShell accepts both.
  3. Example: `mkdir music/rock` makes `rock` inside `music`; `mkdir music\rock` in Git Bash makes `musicrock`.

### Absolute and relative mislabelled
- concept: env.terminal / severity: minor
- Hints:
  1. Look at the path you labelled `absolute`. Where does it start?
  2. Absolute starts at the top of the drive (`/c/...` in Git Bash, `C:\...` in Windows); relative starts from the
     current folder (`notes`, `./notes`, `../x`).
  3. Example: `/c/Users/ann/music` is absolute; `music` and `../ann/music` are relative and depend on `pwd`.

### `commands.txt` doesn't match what was actually done (missing `cd ..`, `rm`, wrong order)
- concept: env.terminal / severity: minor
- Hints:
  1. Compare your list with the tree: which step has no command behind it?
  2. The terminal remembers your commands; Up arrow and `history` show them.
  3. Example: `history | tail -20` prints the last 20 commands you typed.

### Folder tree created in the wrong place (repo root, or `work/work/`)
- concept: env.terminal / severity: major (tests fail)
- Hints:
  1. Run `pwd` before your first `mkdir`. Is it the lesson's `work/` folder?
  2. Relative paths are relative to the current folder, so `mkdir projects` lands wherever you are standing.
  3. Example: in `/c/Users/ann`, `mkdir games` makes `/c/Users/ann/games`; after `cd Desktop` it makes
     `/c/Users/ann/Desktop/games`.

## Do not nitpick
- Python code: there is none in this lesson; no `print`, no scripts.
- Exact wording or formatting of `commands.txt`; extra blank lines, comments, prompt characters (`$`) copied along.
- Using PowerShell instead of Git Bash, or PowerShell spellings (`dir`, `Remove-Item`). Both are fine.
- Extra experiment files or folders, unless they replace required ones.
- Typos he made and corrected along the way that appear in the history.
- Not using flags like `-p`, `-r`, `-la`.
- Whether `~/...` counts as absolute: accept it either way if he explains it.

## Explain back
Ask him to pick one relative path from his `commands.txt` (ideally the `..` one) and explain what folder it pointed
to, why it only worked from where he was standing, and what the absolute version of the same path would be.
