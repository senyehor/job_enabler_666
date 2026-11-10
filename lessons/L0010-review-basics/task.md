# L0010 Task: The trail-walk badge

A local walking club logs every member's walk in metres, because that is what their step counters show. Members keep asking "so how far is that in kilometres? in miles?" The club wants a small terminal program: a member types in their name and how many metres they walked, and the program greets them, converts the distance, and prints a short badge code for the club notice board. Before you write it, you'll warm up by tracing two short scripts by hand, the way you did in L0006, but this time with `//`, `%` and slicing mixed in.

## What to write

Two files in `work/`. Both already exist with a one-line comment at the top:
- `work/trace.txt`: your hand-traces (Part 1)
- `work/unit_converter.py`: the program (Part 2)

## Part 1: Trace by hand (`trace.txt`)

**Don't run these yet.**

Script A:
```python
total = 125
minutes = total // 60
seconds = total % 60
total = minutes * 100 + seconds
minutes = minutes + total // 100
text = str(seconds) + "s"
```

Script B:
```python
word = "planet"
n = len(word)
part = word[1:n // 2]
n = n / 2
word = part + word[-1]
```

1. For each script, write one line per assignment showing the value of **every** variable that exists after that line, then a `final:` line. Use the same layout as in L0006:
   ```
   A
   line 1: total = 125
   line 2: total = 125, minutes = 2
   ...
   A final: total = ..., minutes = ..., seconds = ..., text = ...
   ```
   Do the same for `B`, ending with `B final: ...`. Quotes around text values are optional.
2. When both traces are written, add `print(...)` lines to a scratch copy (for example `work/check.py`), run it and compare. If a prediction was wrong, **don't delete it**: fix the line and add a note below, like `# I was wrong: I thought ... because ...`.

## Part 2: The converter (`unit_converter.py`)

3. Ask for three things with `input()`, in this order: the first name, the last name, and the distance walked in whole metres. Convert the distance to an `int`.
4. Print a greeting with the full name, built with an f-string: `Hello, Mara Lind!`
5. Print `Metres:` with the distance as typed.
6. Print `Kilometres:` with the distance divided by 1000.
7. Print `Miles:` with the distance in miles, **rounded to 2 decimals** with f-string formatting. One mile is `1609.344` metres; store that number in a variable.
8. Print `Split:` with the whole kilometres and the leftover metres, worked out with `//` and `%`, like `Split: 12 km 345 m`.
9. Print `Badge:` followed by the initials (first letter of each name) and the first 3 letters of the first name, joined by a dash: `Badge: ML-Mar`. Get the letters with indexing and slicing. Print it with **two** `print` calls: the first prints `Badge:` and uses `end=" "` so the line doesn't end; the second prints the two parts using `sep="-"`.

Every value must come from what the user typed: if you type `12` or `"Mar"` into your code, the program only works for one walker.

## Example runs

From inside `work/` (what the user types is after each prompt):

```
$ python unit_converter.py
First name: Mara
Last name: Lind
Metres walked: 12345
Hello, Mara Lind!
Metres: 12345
Kilometres: 12.345
Miles: 7.67
Split: 12 km 345 m
Badge: ML-Mar
```

```
$ python unit_converter.py
First name: Oskar
Last name: Berg
Metres walked: 5007
Hello, Oskar Berg!
Metres: 5007
Kilometres: 5.007
Miles: 3.11
Split: 5 km 7 m
Badge: OB-Osk
```

The prompts can be worded differently, and spacing doesn't matter, but keep the labels (`Metres:`, `Kilometres:`, `Miles:`, `Split:`, `Badge:`) as shown. The tests check them.

## Run and test

- Run it: in the terminal, `cd` into `work/`, then `python unit_converter.py`.
- Test it: from the repo root, run `python tools/learn.py test`.

## Stretch goal (optional)

Walkers also want to know how long that took. Ask one more question, the walk time in whole minutes, and print `Time: 2 h 5 min` (for 125 minutes) and the average speed as `Speed: 5.93 km/h`, rounded to 2 decimals. Look at Script A for a hint.
