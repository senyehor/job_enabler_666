# L0010 Review: variables, arithmetic, strings, I/O

This is a **review lesson**: nothing new today. We go back over L0006–L0009 with fresh examples, one trap per idea, before conditions (`if`) start in L0011.

**What you get and what you write:** the starter gives you two files with only a one-line comment at the top (`work/trace.txt` and `work/unit_converter.py`). You write everything else by hand.

Reading and trying the examples should take about 15–20 minutes.

---

## 1. A variable holds its latest value

When Python runs `x = something`, it works out the **right side first**, using the values the variables have *at that moment*. Then it stores the result in the name on the left. The old value is gone.

That's why `x = x + 1` makes sense: "take the current `x`, add 1, store it back in `x`".

A **trace table** helps you follow this by hand: one row per line, one column per variable.

```python
coins = 40
bags = coins // 15
coins = coins - bags * 15
bags = bags + coins
print(coins, bags)
```

| line | coins | bags |
|---|---|---|
| 1 | 40 | – |
| 2 | 40 | 2 |
| 3 | 10 | 2 |
| 4 | 10 | 12 |

Output: `10 12`

**The trap:** on line 4, `coins` is already 10, not 40. Line 3 changed it. Always use the value from the row just above.

---

## 2. `/`, `//`, `%` and precedence

- `/` is normal division and **always gives a float**: `8 / 2` is `4.0`, not `4`.
- `//` gives the whole part: `17 // 5` is `3`.
- `%` gives the remainder: `17 % 5` is `2`.

The "split a total into big units and leftovers" pattern:

```python
total_days = 200
weeks = total_days // 7
days = total_days % 7
print(weeks, "weeks", days, "days")   # 28 weeks 4 days
```

**Precedence** (which operator goes first), from first to last:

1. `( )`
2. `**`
3. `*`, `/`, `//`, `%` (all on the **same** level, left to right)
4. `+`, `-`

Your L0007 list had levels 1, 2 and 4 right. The thing to remember is that `//` and `%` sit on level 3, together with `*` and `/`.

```python
print(10 + 7 // 2)     # 13: 7 // 2 is 3 first, then 10 + 3
print((10 + 7) // 2)   # 8:  17 // 2
```

**The trap:** after `n = n / 2`, `n` is a float in every later line, even if the result looks whole (`6 / 2` is `3.0`).

---

## 3. Indexing and slicing

- Indexes start at **0**. `[-1]` is the last character.
- `[a:b]` starts at `a` and stops **before** `b`. It gives `b - a` characters.
- `[:3]` is the first three characters.
- A slice past the end doesn't crash: `"Al"[:3]` is just `"Al"`.
- An index can be any int expression, like `len(s) // 2`.

```python
city = "Odesa"
print(city[0])                  # O
print(city[-1])                 # a
print(city[1:3])                # de   (indexes 1 and 2, not 3)
print(city[:len(city) // 2])    # Od   (5 // 2 is 2, so [:2])
```

Write the indexes under the letters when you're unsure:

```
O d e s a
0 1 2 3 4
```

**The trap:** thinking `[1:3]` includes index 3. Think of `b` as a fence: you stop in front of it.

---

## 4. `input()` always returns text

Whatever the user types, `input()` gives you a `str`, even if they typed only digits. So convert it **straight away**, in the same line:

```python
eggs = int(input("How many eggs? "))
boxes = eggs // 6
left = eggs % 6
print(f"{boxes} full boxes, {left} eggs left")
```

With `20` typed in, this prints `3 full boxes, 2 eggs left`.

Without `int(...)`:
- `"5" * 2` is `"55"` (the text repeated, no error, just a wrong answer)
- `"5" // 2` crashes with `TypeError` (you can't do whole-division on text)

Reminder from L0009: `TypeError` means the **kind** of value is wrong (text where a number is needed). `ValueError` means the kind is fine but the **content** can't be converted, like `int("4.5")` or `int("abc")`.

---

## 5. f-strings and `print` options

**f-strings:** put `f` before the quotes, and any expression inside `{}`. The format spec goes **inside** the braces, after a colon:

```python
price = 19.999
print(f"Price: {price:.2f}")   # Price: 20.00
print(price)                   # 19.999  (the variable didn't change)
```

`:.2f` only changes how the value is **shown**. One pair of braces holds one value.

**`sep` and `end`** (this was the tricky part in L0009):

- `sep` goes **between the items of one `print` call**. By default it's a space. `sep="-"` *replaces* the space; it doesn't add to it.
- `end` goes **after the last item of that same call**. By default it's a new line (`"\n"`). If you change it, the line doesn't end, so the **next** `print` continues on the same line.

```python
print("Score", end=": ")
print(7, 10, sep="/")
```

Output: `Score: 7/10`

Read it like this: the first call prints `Score`, then `: ` instead of a new line. The second call prints `7`, then `/` (its `sep`), then `10`, then a normal new line.

Both options belong to the call they're written in. `end` doesn't "carry over" to the next print, and `sep` doesn't affect any other print.

---

## 6. Magic numbers go in named variables

A **magic number** is a number in your code whose meaning a reader has to guess. Compare:

```python
print(pounds * 0.4536)
```

```python
kg_per_pound = 0.4536
print(pounds * kg_per_pound)
```

The second one says what the number *is*. It's the same idea as good variable names from L0006.

---

## Try it yourself (not graded)

1. Predict, then run:
   ```python
   a = 9
   b = a % 4
   a = a // 4 + b
   print(a, b)
   ```
2. With `s = "keyboard"`, predict `s[3:6]`, `s[-3:]` and `s[:len(s) // 4]`.
3. Predict exactly what this prints, including where the lines break:
   ```python
   print("x", "y", sep="", end="|")
   print("z")
   ```

---

## Common mistakes

- **"`/` between two ints gives an int."** It always gives a float: `6 / 2` is `3.0`.
- **Forgetting a reassigned variable changed.** After `n = n / 2`, `n` is a float from then on.
- **"`[1:3]` includes index 3."** It stops before 3.
- **"`input()` gives a number if I type digits."** It's always `str`. Wrap it in `int(...)` or `float(...)`.
- **"`:.2f` changes the stored value."** It only changes the display.
- **"`sep` adds a space as well."** `sep="-"` replaces the space.
- **"`end=` goes on the print that comes after."** It goes on the print whose line should *not* end.
- **Putting everything in one f-string and expecting `sep` to split it.** One string is one value for `print`, so there is nothing to separate.

---

## Summary

- The right side is worked out first, with the values as they are right now.
- `/` gives a float; `//` whole part; `%` remainder. `*`, `/`, `//`, `%` share a level, above `+` and `-`.
- Indexes start at 0; `[a:b]` stops before `b`; slices past the end are safe.
- `input()` is always text: convert it in the same line.
- f-strings: `{value:.2f}` shows 2 decimals without changing the value. `sep` goes between items of one call, `end` goes after that call.
- Give magic numbers a name.

## Questions
