# L0001 rubric: tool check card

## Must-have
- [env.install] `work/tools.txt` has one `Tool:` / `Purpose:` / `Version:` block each for Python, Git, VS Code and Claude Code.
- [env.install] Each purpose is a correct sentence in his own words: Python runs (interprets) code, VS Code edits code,
  Git tracks versions/snapshots, Claude Code is the AI assistant/tutor. Not copied word for word from theory.
- [env.install] Versions are real output from his machine: `Python 3.x.y`, `git version 2.x...`, a VS Code number like `1.9x.y`,
  a Claude Code number. The Python test checks it against the interpreter running the tests.
- [env.install] A `Workflow:` line that correctly puts the tools in order (edit in VS Code, run with Python, Git saves history, Claude teaches/reviews).
- [env.install] He opened the course folder with `code .` (ask him; this can't be tested).

## Likely mistakes

### Mixes up editor and interpreter ("VS Code runs my Python code")
- concept: env.install / severity: major
- Hints:
  1. Where: read your VS Code `Purpose:` line and your Python `Purpose:` line side by side. Which one actually carries out the code?
  2. What: the difference between an editor and an interpreter (theory: "Python is an interpreter", "VS Code is an editor").
  3. Example: Notepad can open a recipe, but it can't cook it. Which tool is the notepad and which is the cook, for a `.py` file?

### Version invented or copied from the example instead of from his terminal
- concept: env.install / severity: major
- Hints:
  1. Where: your Git `Version:` line. Run `git --version` again and compare character by character.
  2. What: `--version` asks the program on *this* computer; the example in task.md is someone else's computer.
  3. Example: `whoami` prints a different name on every computer; you'd copy yours, not your neighbour's.

### Version line shortened (`3.12` instead of `Python 3.12.4`, or just `2.47` for Git)
- concept: env.install / severity: minor
- Hints:
  1. Where: compare your Python/Git `Version:` lines with what the terminal printed.
  2. What: task.md asks for the whole line the command prints; the parts are major.minor.patch.
  3. Example: `date` prints a full line like `Tue Oct 20 ...`; "copy the line" means all of it.

### Typed the command at the `>>>` prompt and recorded the error, or says it "didn't work"
- concept: env.install / severity: minor
- Hints:
  1. Where: what did the line before your cursor look like when you typed it: `$` or `>>>`?
  2. What: the terminal prompt vs the Python interactive prompt (theory: "Python is an interpreter").
  3. Example: at `>>>`, `5 + 5` works but `whoami` doesn't; at `$` it's the other way round. `exit()` gets you out.

### Confuses Git with GitHub ("Git is a website where code is stored")
- concept: env.install / severity: minor
- Hints:
  1. Where: your Git `Purpose:` line. Does `git --version` need the internet to answer?
  2. What: Git is a program on your computer that keeps snapshots; GitHub is a website that can store a copy.
  3. Example: a camera vs a photo-sharing website. Which one takes the photos?

### Purpose is one word or a fragment ("editor", "AI")
- concept: env.install / severity: nit (the test also flags under 5 words)
- Hints:
  1. Where: the short `Purpose:` line.
  2. What: a purpose says what you *use* it for, as a full sentence.
  3. Example: not "kettle" but "A kettle boils water for tea."

## Don't nitpick
- Spelling, grammar, capitalisation, blank lines between blocks, extra notes he adds.
- The order of the blocks, or extra lines from `code --version` (commit hash, `x64`).
- Exact tool names ("VSCode", "Visual Studio Code" and "VS Code" are all fine).
- Anything about Python code, files, `cd`/paths (L0002) or running scripts (L0003). There is no Python code in this lesson.
- Git commands; `learn.py` commits for him at this stage.

## Explain back
Ask him: "What's the difference between typing `python --version` and typing just `python`?"
He should say the first asks for the version and returns to the terminal, the second starts the interpreter
(`>>>` prompt) where he types Python, and `exit()` leaves it. Also ask what the `.` in `code .` means
("the folder I'm in now").
