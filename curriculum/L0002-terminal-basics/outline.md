# L0002 Moving around in the terminal: outline for the tutor

## Learning goals (env.terminal)
- Uses `pwd`, `ls`, `cd`, `mkdir`, `cat`, `rm` (plus `mv` and `echo ... >`) without help.
- Understands absolute vs relative paths, including `.` and `..`, and can say which kind a given path is.
- Practised (env.install): opens a folder in VS Code from the terminal with `code <folder>`.

Note: the README sets **Git Bash** as his terminal (also the VS Code default profile). Teach the commands in Git Bash
first. Show the **PowerShell** equivalents in a small table, because he will meet PowerShell on Windows anyway.

## Key points, in teaching order

1. **The terminal always has a current folder ("working directory").** Every command runs "from" somewhere.
   `pwd` prints where you are, `ls` shows what is there.
   Example: open a terminal, run `pwd` (shows something like `/c/Users/yehor`), then `ls` to see Desktop, Documents...
   Explain the prompt: in Git Bash the `~` in the prompt means your home folder.

2. **Paths: absolute vs relative.** An absolute path starts from the top of the drive and means the same thing from
   anywhere. A relative path starts from the current folder.
   - Git Bash absolute: `/c/Users/yehor/Documents` (drive `C:` becomes `/c`).
   - PowerShell/Windows absolute: `C:\Users\yehor\Documents`. Windows uses `\` as separator; Git Bash uses `/`.
     (PowerShell accepts `/` too, Git Bash treats `\` as an escape character, so stick to `/` in Git Bash.)
   - Relative: `Documents`, `Documents/letters`, `./Documents`.
   - `.` is "this folder", `..` is "the folder above". `../..` goes up two.
   Example: from `/c/Users/yehor`, `Documents/letters` and `/c/Users/yehor/Documents/letters` name the same folder;
   from `/c/Users`, only the absolute one still works.

3. **Moving: `cd`.** `cd Documents`, `cd ..`, `cd` alone (or `cd ~`) goes home, `cd -` goes back to the previous folder.
   Tab completion: type the first letters and press Tab. Paths with spaces need quotes: `cd "My Music"`.
   Example: walk `~` -> `Documents` -> `..` -> `Desktop`, running `pwd` after each step.

4. **Making folders and files: `mkdir`, `echo ... >`, `echo ... >>`, `cat`.**
   `mkdir games` makes one folder; `mkdir -p games/chess/openings` makes the whole chain.
   `echo "hello" > greet.txt` creates (or **overwrites**) a file; `>>` appends a line. `cat greet.txt` prints it.
   Example: a `recipes/` folder with `pancakes.txt`, adding two ingredient lines with `>>`, then `cat`.

5. **Moving, renaming and deleting: `mv`, `rm`.** `mv a.txt folder/` moves, `mv a.txt b.txt` renames.
   `rm file.txt` deletes **for good** (no Recycle Bin). `rm -r folder` deletes a folder with everything in it.
   Use `ls` before and after to see the effect.
   Example: `mv pancakes.txt recipes/breakfast/`, then `rm recipes/old.txt`.

6. **PowerShell equivalents and opening VS Code.** Table:

   | Git Bash | PowerShell | Meaning |
   |---|---|---|
   | `pwd` | `pwd` (`Get-Location`) | where am I |
   | `ls` | `ls` / `dir` (`Get-ChildItem`) | list |
   | `cd` | `cd` (`Set-Location`) | change folder |
   | `mkdir -p a/b` | `mkdir a\b` (`New-Item -ItemType Directory`) | make folder(s) |
   | `cat f` | `cat f` (`Get-Content`) | show a file |
   | `mv a b` | `mv a b` (`Move-Item`) | move/rename |
   | `rm f` / `rm -r d` | `rm f` / `rm -Recurse d` (`Remove-Item`) | delete |
   | `echo hi > f` | `echo hi > f` (careful: older PowerShell writes UTF-16) | write to a file |

   `code .` opens the current folder in VS Code; `code recipes` opens a subfolder (callback to L0001).

## Common misconceptions
- "`cd` creates a folder" / "`mkdir` also moves me into it". They are separate steps.
- Thinking a relative path is relative to the course root or to where the file is, rather than to the current folder.
  Symptom: "No such file or directory" after a `cd` somewhere else.
- Mixing separators: typing `projects\notes` in Git Bash (the `\` gets swallowed, it becomes `projectsnotes`).
- `>` vs `>>`: using `>` twice and being surprised that the first line is gone.
- Expecting `rm` to send files to the Recycle Bin.
- Believing `~/something` or `./something` is absolute. (`~` is a shortcut to home, which expands to an absolute path,
  so it is fine to call `~/...` absolute-ish, but `./` is always relative.)
- Forgetting quotes around paths with spaces.

## Check-question ideas
1. Predict: you are in `/c/Users/ann/school`. You run `cd ../music` and then `pwd`. What prints?
   (`/c/Users/ann/music`)
2. Absolute or relative? `/c/Windows`, `notes/todo.txt`, `../photos`, `C:\Users\ann`, `./run.py`.
3. Spot the bug: `echo "milk" > list.txt` then `echo "eggs" > list.txt` then `cat list.txt` shows only `eggs`. Why,
   and what should the second command be?
4. Explain why: `cat report.txt` works in one terminal window but says "No such file or directory" in another.
   (Different current folders; a relative path depends on `pwd`.)

## Builds on
- L0001 env-tools: he opened PowerShell/Git Bash, ran `python --version` etc., and used `code .`. This lesson explains
  what "the folder the terminal is in" means and why `code .` opened that particular folder.
- Sets up L0003, where he must `cd` into `work/` himself and run `python hello.py`, and L0005, where he runs a script
  through a relative path from another folder.
