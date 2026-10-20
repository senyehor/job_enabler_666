# Week 01

## Calibration
This is the first week. Nothing is done yet, so there is no timing, mastery, review-round or issue data to calibrate against.
Sizes follow beginner norms instead:
- One new concept per lesson. No combining, even for small concepts, until real timing data shows he runs under estimate.
- Estimates are 60-70 min. Later lessons in the week get 70, because loops and conditions are where beginners usually slow down.
- Python, Git, VS Code and Claude Code are installed before lesson 1 (README setup). So `env.install` is about knowing what each tool does and checking it from the terminal, not about installing anything.
- Reviews are L0005, L0010 and L0015.
- No project this week. m00 ends this week (L0001-L0003). It has no project. m01 (10 concepts, about 12 regular lessons plus its project) carries on into week 02.
- Scaffold: everything is level 0. L0001-L0010 fall under the first-10-lessons rule. L0011-L0015 have no mastery data yet, so every concept counts as 0 mastery. None of their tasks needs a concept that hasn't been taught (no files, no functions), so no black-box helper is needed.
- Before `py.io` (L0009) there is no `input()`. Tasks up to L0008 are fixed programs whose output is checked. `print` itself is used from L0003 as part of running a script.
- Notes for week 02: `py.while` (L0012) and `py.lists-basic` (L0014) each get only one later practice this week. Week 02 must practise them early, for example in the `py.debugging` lesson and the number-guessing project.

## Lessons

### L0001 env-tools: Your tools: Python, Git, VS Code, Claude Code
- kind: regular / new: env.install / practiced: none / estimate: 60 / scaffold: level 0 (first 10 lessons)
- Brief: He opens a terminal (PowerShell on Windows) and runs version checks for each tool: `python --version`, `git --version`, `code --version`. He also opens the course folder in VS Code from the terminal with `code .`. For each tool he records in a short text file in `work/` (for example `tools.txt`) what the tool is for, in one sentence, plus the version his terminal printed. Theory explains what an interpreter, an editor, version control and an AI assistant each do, and how they fit together in this course. Tests check that the file exists and mentions Python 3 and git versions in the expected form. Nothing is provided except the empty file.

### L0002 terminal-basics: Moving around in the terminal
- kind: regular / new: env.terminal / practiced: env.install / estimate: 65 / scaffold: level 0 (first 10 lessons)
- Brief: Using only the terminal, he builds a small folder tree inside `work/` (for example `projects/notes/` and `projects/scratch/`, with a couple of text files). He moves files around and deletes one with `rm`. Then he writes `commands.txt`, listing the commands he ran and saying which paths he used were absolute and which relative. Skills: `pwd`, `ls`, `cd`, `mkdir`, `cat`, `rm`, and `..` / `.` in paths. Theory must cover the PowerShell equivalents and Windows path separators. Tests check the resulting tree and files, and that `commands.txt` mentions at least one absolute and one relative path. Nothing provided.

### L0003 first-script: Writing and running your first program
- kind: regular / new: env.run / practiced: env.terminal, env.install / estimate: 65 / scaffold: level 0 (first 10 lessons)
- Brief: He creates `hello.py` in VS Code and runs it with `python hello.py` from the terminal, after navigating to `work/` himself. The script prints a few fixed lines (a greeting, a short ASCII box or similar) using only `print` with string literals. Second part: the task text gives him a script with a typo (for example a missing quote or `prnt`) to type in as `broken.py`. He runs it, reads the error message, finds the line number, and fixes it. He writes the line number and error name in a comment. Theory covers what a program is, source file vs interpreter, and running top to bottom. Tests run both scripts and check their output.

### L0004 values-and-types: Values and types
- kind: regular / new: py.values / practiced: env.run, env.terminal / estimate: 65 / scaffold: level 0 (first 10 lessons)
- Brief: A script `types.py` prints a series of values and their `type()`: int, float, str, bool. It also converts between them: `int("42")`, `float("3.5")`, `str(7)`, `bool(0)`, `int(3.9)`. He first writes his predictions as comments, then runs the script and corrects any prediction that was wrong. The task includes one conversion that crashes (`int("abc")`), which he runs, reads the error for, and then comments out. No variables yet (use literals directly in `print`). He may use them only if theory needs a single example, but the task shouldn't require them. Tests check the printed types and converted values.

### L0005 review-setup-types: Review: terminal, scripts and types
- kind: review / new: none / practiced: env.terminal, env.run, py.values / estimate: 60 / scaffold: level 0 (first 10 lessons)
- Brief: No weak-concept data exists yet, so this review consolidates L0001-L0004. Terminal part: create a subfolder in `work/` using relative paths and run a script from a different directory using a relative path to it. Script part: a "type quiz" script `quiz.py` that prints expressions alongside their type and converted forms. It includes two or three traps (`"5" + "5"`, `int("7") + 1`, `bool("False")`). A short `answers.txt` explains each trap in his own words. Tests check the folder layout and the quiz output.

### L0006 variables: Variables and assignment
- kind: regular / new: py.variables / practiced: py.values, env.run / estimate: 65 / scaffold: level 0 (first 10 lessons)
- Brief: A trace-the-values exercise plus a small script. Part 1 (`trace.txt`): the task gives 2-3 short scripts with reassignments and swaps. He writes the value of each variable after each line by hand, then checks by running them. Part 2 (`profile.py`): store a few facts about a fictional user (name, age, height, is_student) in well-named variables, reassign some (birthday: age goes up by 1), and print them. Uses type conversions from L0004. No arithmetic beyond `+ 1`, and no f-strings yet (`print` with commas). Tests check the printed output and that `trace.txt` has the right final values.

### L0007 arithmetic: Arithmetic and operators
- kind: regular / new: py.arithmetic / practiced: py.variables, py.values / estimate: 65 / scaffold: level 0 (first 10 lessons)
- Brief: A `calculator.py` with fixed inputs in variables, computing a small real-world set of numbers. For example: total seconds turned into hours/minutes/seconds with `//` and `%`, a compound value with `**`, and an average with `/`. He predicts the results of a few precedence expressions in comments first. Exercises int vs float results (`/` vs `//`) and operator precedence. Output uses `print` with commas (no f-strings yet). Tests check the computed values in the output.

### L0008 strings-fstrings: Strings, f-strings, indexing and slicing
- kind: regular / new: py.strings-basic / practiced: py.variables, py.arithmetic / estimate: 70 / scaffold: level 0 (first 10 lessons)
- Brief: A `receipt.py` that formats a small fixed receipt with f-strings (item names, prices, total computed with arithmetic, rounding with `:.2f`). It also pulls parts out of fixed strings with indexing and slicing: first letter, last 3 characters, a reversed word with `[::-1]`, an order code like `"ORD-2026-0042"` split into parts by slicing. String methods are not in scope (those are `ds.strings` later), apart from `len()`. Tests check the formatted lines and the sliced values. This is the heaviest lesson so far, so keep the receipt to 3 items.

### L0009 input-output: Talking to the user: print and input
- kind: regular / new: py.io / practiced: py.values, py.strings-basic, py.arithmetic / estimate: 65 / scaffold: level 0 (first 10 lessons)
- Brief: An interactive `tip.py`. It asks for the bill amount, the tip percent and the number of people with `input()`, converts them with `float`/`int`, computes the tip, the total and the per-person share, and prints a formatted summary with f-strings. Exercises: `input` always returns str, converting it, and `print` options (`sep`, `end`). No conditions yet, so the inputs are assumed valid. Tests use `run_script` with stdin and check the computed amounts in the output.

### L0010 review-basics: Review: variables, arithmetic, strings, I/O
- kind: review / new: none / practiced: py.variables, py.arithmetic, py.strings-basic, py.io / estimate: 65 / scaffold: level 0 (first 10 lessons)
- Brief: Still no issue data, so this consolidates L0006-L0009. A `unit_converter.py` asks for a name and a distance in km. It prints a personalised greeting, the distance in metres, miles (rounded with f-string formatting) and whole km plus leftover metres (`//`, `%`), and the initials or first 3 letters of the name via slicing. Plus a short trace exercise (`trace.txt`) mixing reassignment and integer division, to check his hand-tracing again. Tests use stdin and check the values.

### L0011 conditions: Making decisions with if/elif/else
- kind: regular / new: py.conditions / practiced: py.io, py.values / estimate: 70 / scaffold: level 0 (no mastery data yet, every concept counts as 0, and nothing needs a black-box helper)
- Brief: A `ticket_price.py` that asks for age and whether the user is a student (y/n). It works out a ticket price from chained rules (child, student, adult, senior, with a combined rule using `and`/`or`) and prints the result. Covers comparisons, booleans, `if/elif/else`, one nested condition and `and/or/not`. He should also handle one obviously invalid input (negative age) with a message, using only `if`. Tests run the script with several stdin cases, one per rule plus the boundaries.

### L0012 while-loops: Repeating with while loops
- kind: regular / new: py.while / practiced: py.conditions, py.io, py.arithmetic / estimate: 70 / scaffold: level 0 (no mastery data yet, so no pre-written code)
- Brief: Two small programs. `countdown.py` asks for a number and counts down to liftoff (a simple counter loop with a clear exit condition). `savings.py` asks for a starting balance, a yearly interest rate and a goal. It loops year by year until the goal is reached and prints the number of years. Part 3: the task shows an infinite loop to type in as `fix_loop.py`. He runs it, stops it with Ctrl+C, explains why it never ends, and fixes it. Mention `break` only as an aside; the task doesn't need it. Tests use stdin and check the counts and years.

### L0013 for-loops: for loops and range
- kind: regular / new: py.for / practiced: py.while, py.strings-basic, py.conditions / estimate: 70 / scaffold: level 0 (no mastery data yet, so no pre-written code)
- Brief: `times_table.py` asks for a number and prints its multiplication table 1-10 with `range` (watch the off-by-one). `vowels.py` asks for a word, loops over its characters, counts the vowels with an `if`, and prints the count. Part 3: rewrite the countdown from L0012 with `for` and `range(n, 0, -1)` (`countdown_for.py`). In a comment, say when `while` fits better than `for`. Tests use stdin for each script and check the table rows and counts, including the boundary rows 1 and 10.

### L0014 lists-basic: Lists basics
- kind: regular / new: py.lists-basic / practiced: py.for, py.io / estimate: 70 / scaffold: level 0 (no mastery data yet, so no pre-written code)
- Brief: A `shopping.py` that asks how many items there will be, reads that many item names with a `for` loop, and appends each one to a list. It then prints the list numbered from 1, the first and last items (including `[-1]`), and the item count with `len`. Second part: a fixed list of temperatures. Loop to compute the sum and the max by hand (no `sum()`/`max()` yet, so he practises the loop). Methods beyond `append` are out of scope (they belong to `ds.lists`). Tests use stdin and check the numbered output and the computed values.

### L0015 review-control-flow: Review: conditions and loops
- kind: review / new: none / practiced: py.conditions, py.while, py.for, py.lists-basic / estimate: 70 / scaffold: level 0 (no mastery data yet, so no pre-written code)
- Brief: Consolidates L0011-L0014 ahead of debugging and the number-guessing project in week 02. A `grades.py` reads scores with a `while` loop until the user types `done`. It stores them in a list, then uses a `for` loop to classify each score into a letter grade with `if/elif`. It prints each one and also prints the average and how many passed. The empty input case (immediately `done`) must print a friendly message rather than crash. Tests use several stdin cases, including the empty case and the boundary scores.
