# L0002 Moving around in the terminal

**What you get and what you write:** the starter gives you only an empty `commands.txt` with one comment line.
Everything else (every folder, every file) you make yourself by typing commands. No File Explorer, no VS Code
file tree.

Reading time: about 15–20 minutes, including trying things out. Open a Git Bash terminal (in VS Code:
Terminal → New Terminal) and try each example as you go. The examples use a made-up user called `ann`; your
paths will look different, and that's fine.

---

## Quick recap from L0001: command + argument

In L0001 you saw that `code.` fails but `code .` works. That's because a terminal line is split on spaces:

```
code   .
^^^^   ^
the    the argument (what the program
program   should work on)
```

The first word is the **command** (a program or a built-in instruction). Everything after it, separated by
spaces, are **arguments**. Keep this picture in mind: every command today works the same way. `cd Documents`
means "run `cd`, and give it `Documents`".

Also remember: the terminal is not the thing that runs Python code. It's the window where you *type commands*.
One of those commands can be `python`, which starts the Python interpreter. Today we don't use Python at all,
only the terminal's own commands.

---

## 1. The terminal always stands in some folder

At every moment, the terminal is "standing" in one folder. This is called the **working directory**
(directory = folder, same thing) or the **current folder**. Every command you type runs from there.

Two commands tell you where you are and what's around you:

- `pwd` = "print working directory". Prints the folder you are standing in.
- `ls` = "list". Shows what is inside the current folder.

```
$ pwd
/c/Users/ann
$ ls
Desktop  Documents  Downloads  Music  Pictures
```

(The `$` is the **prompt**: the terminal saying "I'm ready, type something". You don't type the `$`.)

Look at the line above the `$` in Git Bash. It often ends with `~`. The `~` (tilde) is a shortcut for your
**home folder**, which is `/c/Users/<your name>`. So `~` in the prompt means "you are at home right now".

**This explains the L0001 surprise.** When you ran `code README.md` and got an empty file, the terminal was
standing in `~`, your home folder. There was no `README.md` there, so VS Code opened a new, empty one with
that name. The command was fine; it just ran from the wrong place.

### Try it yourself (1)

Open a new Git Bash terminal and run `pwd`, then `ls`. Is the folder you see the course folder or your home
folder? What does the prompt show?

---

## 2. Paths: absolute and relative

A **path** is the "address" of a file or folder. There are two kinds.

**Absolute path:** starts from the very top of the drive. It means the same thing no matter where you are
standing.

- In Git Bash: `/c/Users/ann/Documents`. The drive `C:` is written as `/c`, and folders are separated by `/`.
- In Windows/PowerShell: `C:\Users\ann\Documents`. Same place, but Windows uses `\` as the separator.

**Relative path:** starts from the current folder. Its meaning depends on where you are standing.

- `Documents`, `Documents/letters`, `./Documents`

Two special names help with relative paths:

- `.` (one dot) means "this folder, where I am now".
- `..` (two dots) means "the folder one level up" (the **parent** folder).
- `../..` means "two levels up".

Example. Say this folder tree exists:

```
/c/Users/ann/
  Documents/
    letters/
  Music/
```

If you are standing in `/c/Users/ann`:

- `Documents/letters` (relative) and `/c/Users/ann/Documents/letters` (absolute) name the **same** folder.

If you are standing in `/c/Users` instead:

- `Documents/letters` now means `/c/Users/Documents/letters`, which doesn't exist.
- The absolute path `/c/Users/ann/Documents/letters` still works, because it doesn't care where you are.

And from `/c/Users/ann/Documents`, the path `../Music` means "go up to `ann`, then into `Music`", which is
`/c/Users/ann/Music`.

**How to tell them apart:** in Git Bash, an absolute path starts with `/` (or `~`, which expands to your home
folder's absolute path). In Windows, it starts with a drive letter like `C:\`. Anything else is relative.

**Slashes:** in Git Bash, always use `/`. The `\` means something special there (it "escapes" the next
character), so `Documents\letters` turns into `Documentsletters`. PowerShell accepts both `/` and `\`.

### Try it yourself (2)

Absolute or relative? Decide first, then read the answer below.
`/c/Program Files`, `Music/rock`, `../Desktop`, `D:\games`, `./notes.txt`

<details><summary>Answer</summary>
Absolute: `/c/Program Files`, `D:\games`. Relative: `Music/rock`, `../Desktop`, `./notes.txt`.
</details>

---

## 3. Moving around: `cd`

`cd` = "change directory". It moves the terminal to another folder. It does **not** create anything.

| What you type | Where you end up |
|---|---|
| `cd Documents` | into `Documents` (relative to where you are) |
| `cd ..` | one folder up |
| `cd` or `cd ~` | your home folder |
| `cd -` | back to the folder you were in before |
| `cd /c/Users/ann/Music` | that exact folder (absolute) |

A walk, running `pwd` after each step:

```
$ cd ~
$ pwd
/c/Users/ann
$ cd Documents
$ pwd
/c/Users/ann/Documents
$ cd ..
$ pwd
/c/Users/ann
$ cd Desktop
$ pwd
/c/Users/ann/Desktop
```

Two habits that save a lot of typing and errors:

- **Tab completion.** Type the first few letters of a folder name and press **Tab**. The terminal finishes
  the name for you. If nothing happens, press Tab twice to see the options. If still nothing, the folder
  isn't where you think it is: run `ls`.
- **Quotes for spaces.** `cd My Music` gives `cd` two arguments (`My` and `Music`), which fails. Write
  `cd "My Music"` so it's one argument.

---

## 4. Making folders and files: `mkdir`, `echo >`, `echo >>`, `cat`

`mkdir` = "make directory".

```
$ mkdir games
$ mkdir -p games/chess/openings
```

The first makes one folder. The second makes the whole chain at once; `-p` means "also make the parent folders
if they're missing". Without `-p`, `mkdir games/chess/openings` fails if `games/chess` doesn't exist yet.

Note: `mkdir` does **not** move you into the new folder. You're still where you were. Use `cd` for that.

`echo` prints text. With `>` you send that text into a file instead of the screen:

- `echo "text" > file.txt` creates the file with that one line. **If the file already exists, its old
  content is erased** and replaced.
- `echo "text" >> file.txt` adds the line to the **end** of the file and keeps what was there.

`cat file.txt` prints a file's content to the screen.

Example:

```
$ mkdir recipes
$ cd recipes
$ echo "Pancakes" > pancakes.txt
$ echo "- 2 eggs" >> pancakes.txt
$ echo "- 1 cup flour" >> pancakes.txt
$ cat pancakes.txt
Pancakes
- 2 eggs
- 1 cup flour
$ ls
pancakes.txt
```

Memory trick: one arrow `>` = "start over"; two arrows `>>` = "add more".

### Try it yourself (3)

In your home folder (not in the course folder), make a folder `sandbox`, go into it, create `colors.txt`
with three lines (one `>` and two `>>`), and `cat` it. Then run `echo "oops" > colors.txt` and `cat` it again.
What happened to your three lines?

---

## 5. Moving, renaming, deleting: `mv` and `rm`

`mv` = "move". It does two jobs:

- `mv pancakes.txt breakfast/` moves the file into the `breakfast` folder (which must exist).
- `mv pancakes.txt crepes.txt` renames it (moving it to a new name in the same place).

After a move, the file is **gone** from where it was. It isn't copied.

`rm` = "remove":

- `rm old.txt` deletes a file.
- `rm -r oldfolder` deletes a folder and **everything inside it** (`-r` = "recursive", go inside).

**`rm` does not use the Recycle Bin.** The file is gone for good. Before an `rm`, run `ls` and read the name
twice.

Use `ls` before and after, so you see what each command did:

```
$ ls
breakfast  old.txt  pancakes.txt
$ mv pancakes.txt breakfast/
$ rm old.txt
$ ls
breakfast
$ ls breakfast
pancakes.txt
```

Notice `ls breakfast`: you can give `ls` (and `cat`, `rm`, ...) a path, so you don't have to `cd` everywhere.

---

## 6. PowerShell equivalents, and opening VS Code

You'll use Git Bash in this course, but Windows also has **PowerShell**, and you'll meet it. Most short
names work there too:

| Git Bash | PowerShell | Meaning |
|---|---|---|
| `pwd` | `pwd` (`Get-Location`) | where am I |
| `ls` | `ls` / `dir` (`Get-ChildItem`) | list |
| `cd` | `cd` (`Set-Location`) | change folder |
| `mkdir -p a/b` | `mkdir a\b` (`New-Item -ItemType Directory`) | make folder(s) |
| `cat f` | `cat f` (`Get-Content`) | show a file |
| `mv a b` | `mv a b` (`Move-Item`) | move/rename |
| `rm f` / `rm -r d` | `rm f` / `rm -Recurse d` (`Remove-Item`) | delete |
| `echo hi > f` | `echo hi > f` (older PowerShell saves it in a different encoding, UTF-16) | write to a file |

**Opening VS Code from the terminal.** `code` takes a path as its argument:

- `code .` opens the current folder (remember, `.` = "this folder").
- `code recipes` opens the `recipes` folder, relative to where you stand.

So in L0001, `code .` opened whatever folder the terminal happened to be in. Now you know why.

---

## Common mistakes

- **Thinking `mkdir` moves you in, or `cd` creates a folder.** They're separate steps: `mkdir x`, then `cd x`.
- **Relative path from the wrong place.** "No such file or directory" usually means you're standing somewhere
  else. First move: run `pwd`, then `ls`.
- **Backslashes in Git Bash.** `mkdir music\rock` makes a folder called `musicrock`. Use `/`.
- **`>` twice.** The second `>` erased the first line. Use `>>` to add.
- **Expecting a Recycle Bin.** `rm` is permanent.
- **Calling `./something` absolute.** It starts with `.`, "this folder", so it's relative.
- **Forgetting quotes around names with spaces.** `cd "My Music"`, not `cd My Music`.
- **Typing the `$`.** That's the prompt, not part of the command.

---

## Summary

- The terminal always stands in a folder. `pwd` shows which, `ls` shows what's in it, `~` is home.
- Absolute paths start at the top (`/c/...` in Git Bash, `C:\...` in Windows) and work from anywhere.
  Relative paths start where you stand. `.` = here, `..` = one up.
- `cd` moves you; `mkdir` (with `-p` for a chain) makes folders.
- `echo "..." > f` creates or overwrites a file; `>>` appends; `cat` shows it.
- `mv` moves or renames; `rm` (and `rm -r` for folders) deletes for good.
- `code <folder>` opens a folder in VS Code; `code .` opens the current one.
- When something says "No such file or directory": `pwd`, then `ls`.

---

## Questions
