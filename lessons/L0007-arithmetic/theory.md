# L0007 Arithmetic and operators

**What you get and what you write.** The starter gives you `work/calculator.py` with just one comment line at the top. You write everything else yourself.

An **operator** is a symbol that tells Python to do something with values, like `+` (add) or `*` (multiply). Today you learn all the maths operators, the order Python runs them in, and how to use them with variables.

Run the examples yourself: make a scratch file (for example `play.py`, anywhere outside `work/`) and paste them in.

---

## Quick recap: the right side runs first

From L0006: in `total = total + 5`, Python first works out the right side (`total + 5`) using the *current* value of `total`. Then it stores the result in `total`, and the old value is gone.

```python
total = 10
total = total + 5   # right side: 10 + 5 = 15, then total becomes 15
print(total)        # 15
```

You'll use this a lot today: compute new values from old ones, one line at a time.

---

## 1. The basic four, and "/ always gives a float"

```python
print(9 - 4, 3 * 5, 12 / 4, 10 / 4)
```
prints
```
5 15 3.0 2.5
```

- `+`, `-`, `*` on two ints give an int: `9 - 4` is `5`.
- `/` (division) **always** gives a float, even when it divides evenly: `12 / 4` is `3.0`, not `3`.

Mixing an int and a float gives a float (remember `float` from L0004):

```python
print(2 + 0.5)    # 2.5
print(3 * 1.0)    # 3.0
print(type(8 / 2))  # <class 'float'>
```

---

## 2. Floor division `//` and remainder `%`

These two work as a pair. Picture 17 sweets shared between 5 children:

- `17 // 5` is **floor division**: how many whole times 5 fits into 17. Each child gets `3`.
- `17 % 5` is the **remainder** (also called "modulo"): what's left over. `2` sweets are left.

```python
sweets = 17
children = 5
print(sweets // children)   # 3
print(sweets % children)    # 2
print(3 * 5 + 2)            # 17, the check: whole parts times 5, plus leftover
```

`%` has nothing to do with percent. It's the leftover.

A handy use: `% 2` tells you even or odd.

```python
print(10 % 2)   # 0, even (nothing left over)
print(11 % 2)   # 1, odd
```

Two small details:
- `//` **rounds down**, it doesn't round to the nearest: `7 // 2` is `3`, not `4`.
- `//` with a float gives a float: `7.0 // 2` is `3.0`.
- (Just so you know: with negative numbers "down" means more negative, so `-7 // 2` is `-4`. You won't need this today.)

**Try it yourself:** predict, then run: `print(23 // 4, 23 % 4)`.

---

## 3. Converting units with `//` and `%`

A big number of small units can be turned into bigger units. `//` gives the whole big units, `%` gives what's left over in small units.

200 minutes into hours and minutes:

```python
total_minutes = 200
hours = total_minutes // 60     # 3, three whole hours fit in
minutes = total_minutes % 60    # 20, minutes left over
print(hours, "h", minutes, "min")   # 3 h 20 min
```

Check: `3 * 60 + 20` is `200`. Good.

Same idea, 1000 days into weeks and days:

```python
total_days = 1000
weeks = total_days // 7    # 142
days = total_days % 7      # 6
print(weeks, "weeks", days, "days")
```

If there are more than two units, the rule is: divide off the **biggest** unit first, keep the **leftover** (`%`), and then repeat the same step on that leftover with the next unit. Never go back to the original total for the smaller units, or you count the big part twice.

---

## 4. Powers with `**`

`**` means "to the power of": `2 ** 5` is `2 * 2 * 2 * 2 * 2`, which is `32`.

```python
print(3 ** 4)     # 81
print(10 ** 6)    # 1000000
print(2 ** 0.5)   # 1.4142135623730951 (a float, the square root of 2)
```

The classic use is growth. Something that triples every day: after 4 days you have `start * 3 ** 4`.

```python
bacteria = 5
print(bacteria * 3 ** 4)   # 405
```

**Warning:** `^` is **not** power in Python. It does something else entirely. `2 ^ 3` gives `1`, not `8`. Always use `**`.

---

## 5. Order of operations and brackets

Python doesn't just go left to right. Like in school maths, some operators go first. **Precedence** means "which operator goes first". From first to last:

1. `( )` brackets
2. `**`
3. `*`, `/`, `//`, `%`
4. `+`, `-`

Operators on the same level go left to right. The one exception: `**` goes **right to left**.

```python
print(1 + 2 * 3)      # 7, because * goes first: 1 + 6
print((1 + 2) * 3)    # 9, brackets first: 3 * 3
print(100 / 10 / 2)   # 5.0, left to right: 10.0 / 2
print(2 ** 2 ** 3)    # 256, right to left: 2 ** 8
```

**The average trap.** The average of three numbers:

```python
a = 4
b = 5
c = 9
wrong = a + b + c / 3      # only c is divided: 4 + 5 + 3.0 = 12.0
right = (a + b + c) / 3    # the sum is divided: 18 / 3 = 6.0
print(wrong, right)
```

When you're not sure, add brackets. Extra brackets are never wrong.

**Try it yourself:** predict, then run: `print(10 - 2 * 3)` and `print(2 * 3 ** 2)`.

---

## 6. Printing results with commas

No f-strings yet (that's a later lesson), so you print labels and values with commas. `print` puts one space between the items.

```python
print("Total:", 3 + 4, "items")   # Total: 7 items
```

Normally you compute into variables first, and print later:

```python
price = 3
count = 4
total = price * count
print("Total price:", total)   # Total price: 12
```

Notice that `total` is computed from `price` and `count`. If the price changes to 5, you change one line and the total updates by itself. Writing `print("Total price:", 12)` would give the right answer today and the wrong one tomorrow.

**Try it yourself:** set `length = 7` and `width = 3`, compute the area and print `Area: 21` with a label.

---

## Common mistakes

- **"`6 / 2` gives `3`."** It gives `3.0`. `/` always returns a float.
- **"`//` rounds to the nearest."** It rounds down: `7 // 2` is `3`.
- **"`%` means percent."** It's the remainder.
- **"`2 ^ 3` is 8."** Power is `**`.
- **"Python goes left to right, so `2 + 3 * 4` is 20."** `*` goes first.
- **"`a + b + c / 3` is the average."** Only `c` gets divided. Use brackets.
- **Typing the answer yourself**, like `print("Hours:", 2)`, instead of computing it from a variable.

---

## Summary

- `+ - *` on ints give ints. `/` always gives a float. Mixing int and float gives a float.
- `//` is "how many whole times", `%` is "what's left over". Together they convert units.
- `**` is power. `^` is not.
- Order: brackets, `**`, then `* / // %`, then `+ -`. Same level: left to right, except `**`.
- Store inputs in variables and compute results from them.

## Questions
