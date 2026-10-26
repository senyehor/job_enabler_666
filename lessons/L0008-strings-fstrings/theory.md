# L0008 Theory: Strings, f-strings, indexing and slicing

**What you get and what you write.** The starter file `work/receipt.py` has only a one-line comment at the top. You write everything else yourself.

To try the examples, make a scratch file anywhere outside `work/` (for example `scratch.py` on your Desktop) and run it with `python scratch.py`. Or type them into the Python prompt: run `python` with no file name, type lines, and leave with `exit()`.

---

## 1. A string is a sequence of characters

You know from L0004 that quotes make a `str`. A **sequence** means the characters sit in a row, one after another, and each one has a position. Every character counts: letters, digits, spaces, dashes, dots.

`len()` is a built-in function that tells you how many characters a string has.

```python
city = "New York"
print(len(city))
```

Count by hand before you run it: `N e w (space) Y o r k`. That's **8**, not 7, because the space is a character too.

```python
print(len(""))        # 0: an empty string has no characters
print(len("2026"))    # 4: digits in quotes are characters, not a number
```

---

## 2. Indexing: positions start at 0

An **index** is the position number of a character. You write it in square brackets after the string: `word[0]`.

Python starts counting at **0**, not 1. So the first character is `[0]`, the second is `[1]`, and so on.

**Negative indexes** count from the end: `[-1]` is the last character, `[-2]` the one before it.

Here is `"Jupiter"` with both kinds of index:

```
 character:   J   u   p   i   t   e   r
 index:       0   1   2   3   4   5   6
 negative:   -7  -6  -5  -4  -3  -2  -1
```

```python
planet = "Jupiter"
print(planet[0])    # J
print(planet[3])    # i
print(planet[-1])   # r
print(planet[-2])   # e
print(planet[len(planet) - 1])   # r  (length is 7, last index is 6)
```

The last index is always `len - 1`. If you ask for a position that doesn't exist, Python crashes:

```python
print(planet[7])
```

```
IndexError: string index out of range
```

Read the bottom line: "index out of range" means "there's no character at that position".

---

## 3. Slicing: `[start:stop]`

A **slice** takes a piece of a string. `text[start:stop]` gives the characters from `start` up to, **but not including**, `stop`.

A handy rule: `stop - start` = how many characters you get. `[0:4]` gives 4 characters.

```python
date = "2026-10-20"
```

```
 character:   2   0   2   6   -   1   0   -   2   0
 index:       0   1   2   3   4   5   6   7   8   9
```

```python
year  = date[0:4]   # "2026"  positions 0,1,2,3 (stops before 4, the dash)
month = date[5:7]   # "10"    positions 5,6 (skips the dash at 4, stops before the dash at 7)
day   = date[8:10]  # "20"
print(year, month, day)
```

You can leave out `start` or `stop`:

- `[:3]` from the beginning up to 3 → the first 3 characters
- `[4:]` from position 4 to the end
- `[-3:]` from the third-from-last to the end → the last 3 characters

```python
print(date[:4])    # 2026
print(date[8:])    # 20
print(date[-2:])   # 20
```

Unlike an index, **a slice never crashes** when it goes past the end. It just gives you what's there:

```python
print(date[8:100])   # 20
```

---

## 4. The step: `[start:stop:step]`

A third number in a slice is the **step**: how far to jump each time. `[::2]` takes every second character (start and stop left out mean "the whole string").

```python
print("abcdefgh"[::2])   # aceg
```

The one you'll use most is a step of `-1`, which walks backwards. `[::-1]` reverses a string:

```python
print("stressed"[::-1])   # desserts
print("level"[::-1])      # level  (a palindrome: same both ways)
```

One more thing: you **can't change** a character inside a string. `word[0] = "X"` gives a `TypeError`. Strings are **immutable** (can't be changed in place). To get a different string, you build a new one.

---

## 5. f-strings: putting values into text

You already know two ways to print a label and a value:

```python
film = "Dune"
seats = 3
print("Seats:", seats)                 # L0006 way: commas, print adds spaces
print("Seats: " + str(seats))          # concatenation: + glues str + str
```

Concatenation needs `str()`. Without it you get the error you met in L0005:

```python
print("Seats: " + seats)
```

```
TypeError: can only concatenate str (not "int") to str
```

An **f-string** is easier. Put the letter `f` right before the opening quote, then write any value inside `{}`:

```python
print(f"{seats} tickets for {film}")   # 3 tickets for Dune
```

Inside `{}` you can put any **expression** (anything that gives a value): arithmetic, an index, a slice, `len()`.

```python
ticket_price = 9.5
print(f"Total: {seats * ticket_price}")      # Total: 28.5
print(f"Film starts with {film[0]}")         # Film starts with D
print(f"Title has {len(film)} letters")      # Title has 4 letters
```

Two more string operators:

- `+` joins strings: `"Dune" + " 2"` → `"Dune 2"`
- `*` with a whole number repeats a string: `"=" * 10` → `==========`

```python
print("=" * 10)
```

---

## 6. Format specs: `{value:.2f}`

Floats sometimes print in surprising ways:

```python
print(0.1 + 0.2)   # 0.30000000000000004
print(2.5 * 2)     # 5.0
```

Computers store most decimals as very close approximations, and a float always shows at least one decimal. For money you want **exactly two decimals**.

A **format spec** goes after a colon inside the braces and controls how the value is *shown*. `:.2f` means "a float with 2 digits after the point":

```python
litres = 32.5
price = 1.879
print(f"Fuel: {litres * price:.2f} EUR")   # Fuel: 61.07 EUR
print(f"{2.5 * 2:.2f}")                    # 5.00
print(f"{0.1 + 0.2:.2f}")                  # 0.30
```

`:.2f` rounds **only the text** it prints. The number in the variable stays the same:

```python
cost = litres * price
print(f"{cost:.2f}")   # 61.07
print(cost)            # 61.0675  (unchanged)
```

**Optional (for the stretch goal): width and alignment.** A number before the dot sets a minimum width, `<` aligns left, `>` aligns right:

```python
print(f"[{'tea':<8}]")       # [tea     ]
print(f"[{3.5:>8.2f}]")      # [    3.50]
```

---

## Recap: don't type what the program can compute

In L0007 your review flagged a "10" typed into a label instead of using `weeks`. The same idea matters a lot today. `print("Year: 2026")` prints the right thing, but only for one code. `print(f"Year: {code[4:8]}")` is right for every code in that format. If a value is in a variable, take it from the variable.

---

## Common mistakes

- **Starting at 1.** The first character is `[0]`. The last is `[-1]` or `[len - 1]`.
- **Thinking `stop` is included.** `"Jupiter"[0:3]` is `"Jup"` (3 characters), not `"Jupi"`.
- **Forgetting that spaces and dashes count.** Write the string out with indexes under it before you slice.
- **Forgetting the `f`.** `print("{seats} seats")` prints `{seats} seats` exactly as written. There's no error, so check your output.
- **Thinking `:.2f` changes the variable.** It only changes what's displayed.
- **`"Total: " + 9.5`.** A `TypeError`: `+` only joins str with str. Use an f-string.

---

## Try it yourself (not graded)

1. With `word = "Python"`, predict `word[2]`, `word[-3]`, `word[1:4]` and `word[::-1]`, then check.
2. With `phone = "+380-67-1234567"`, slice out the country code `380`, the operator code `67` and the last 7 digits. Draw the index table first.
3. Print `f"{10 / 3:.2f}"`, `f"{10 / 3:.4f}"` and `f"{7:.2f}"`. What does the last one tell you about ints?

---

## Summary

- A string is a row of characters. `len()` counts them, spaces included.
- `s[i]` gets one character. Indexes start at 0; `-1` is the last one. A bad index is an `IndexError`.
- `s[start:stop]` gets a piece, stopping *before* `stop`. Leaving out a side means "from the start" / "to the end". Slices never crash.
- `s[::-1]` reverses a string.
- `f"...{expr}..."` puts any value or expression into text. `"-" * 24` repeats a string.
- `{value:.2f}` shows exactly 2 decimals without changing the value.

## Questions

**Q: How does `print(planet[len(planet) - 1])` work?**
A: Python works from the inside out. `len(planet)` → `7`, then `7 - 1` → `6`, then `planet[6]` → `"r"`, and `print` shows it. Counting starts at 0, so the length is always one past the last position, and the last index is `len - 1`. `planet[-1]` is the short way to write the same thing.
