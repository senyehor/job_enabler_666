# L0013 Task: Three small loop tools

Your little cousin is learning her times tables and keeps asking you to write them out. Typing "7 x 1 = 7, 7 x 2 = 14 ..." by hand is boring and easy to get wrong, and a computer is very good at boring. While you're at it, she has a word game (who can find a word with the most vowels?) that needs a referee, and the rocket countdown you wrote in L0012 could be shorter now that you know `for`. You'll write three short programs, each built around a `for` loop.

## What to write

Three files in `work/`: `times_table.py`, `vowels.py` and `countdown_for.py`. Each starter has a one-line comment at the top.

Use a `for` loop in each one. Don't use lists, functions or string methods like `.lower()` or `.count()`; they come in later lessons.

## Requirements

**Part 1: `times_table.py`**

1. Ask for a number with `input()` (prompt: `Number: `) and convert it with `int()`.
2. Use a `for` loop with `range` to print the multiplication table from **1 to 10**, one row per line, in the form `7 x 3 = 21`.
3. It must print exactly 10 rows: the first row is `x 1`, the last row is `x 10`. No `x 0` row and no `x 11` row. Check both ends before you test.

**Part 2: `vowels.py`**

4. Ask for a word (prompt: `Word: `).
5. Loop over the word's characters with `for ch in word:` and count how many are vowels (`a`, `e`, `i`, `o`, `u`) with an `if`. You only need to handle lowercase words.
6. After the loop, print `Vowels: ` followed by the count, for example `Vowels: 3`.

**Part 3: `countdown_for.py`**

7. Ask for a number (prompt: `Start from: `) and count down from it to 1 with `for` and `range(n, 0, -1)`, one number per line.
8. After the last number, print `Liftoff!`. No `0` should be printed.
9. At the top of the file, under the starter comment, write a comment of one or two lines saying **when a `while` loop fits better than a `for` loop**. Think about the savings program from L0012: could you have written that one with `range`?

## Example runs

From inside `work/`:

```
$ python times_table.py
Number: 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

```
$ python vowels.py
Word: banana
Vowels: 3
```

```
$ python vowels.py
Word: rhythm
Vowels: 0
```

```
$ python countdown_for.py
Start from: 5
5
4
3
2
1
Liftoff!
```

Spaces don't matter to the tests (`7 x 3 = 21` and `7 x 3 =21` both pass), but the `x` and `=` in the table rows, and the labels `Vowels:` and `Liftoff!`, must be there.

**Tip:** if your table stops at `x 9`, look at the second number you gave `range`. `range(a, b)` goes from `a` up to `b - 1`.

## Run and test

- Run each one: in the terminal, `cd` into `work/`, then run `python times_table.py`, `python vowels.py` or `python countdown_for.py`.
- Test them: from the repo root, run `python tools/learn.py test`.

## Stretch goal (optional)

Make `vowels.py` also count capital vowels, so `Education` gives `Vowels: 5`. Then add a second line `Consonants: ` with the count of the other letters (you can assume the word has only letters).
