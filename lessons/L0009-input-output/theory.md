# L0009 Talking to the user: print and input

**What you get and what you write.** The starter `work/tip.py` has only a one-line comment. You write every line of the program yourself (scaffold level 0).

Until now every program printed the same thing on every run. In this lesson your program starts asking the user questions and answering with *their* numbers.

---

## 1. `input()`: let the user decide

`input("prompt")` does three things:

1. shows the prompt text,
2. waits until the user types something and presses Enter,
3. gives back what was typed, so you can store it in a variable.

```python
city = input("Where do you live? ")
print(f"Hello from {city}!")
```

Run it twice and type a different city each time:

```
$ python hello.py
Where do you live? Kyiv
Hello from Kyiv!
$ python hello.py
Where do you live? Lisbon
Hello from Lisbon!
```

Two details:

- The prompt has **no newline** at the end. The cursor stays right after the text. That's why the prompt ends with a space (`"... live? "`): without it the answer would be glued on, like `live?Kyiv`.
- While the program waits, nothing happens. A blinking cursor and no new output means **it's waiting for you to type**. It hasn't frozen.

---

## 2. `input()` always gives you text

Whatever the user types, even `1999` or `4`, `input()` returns a `str`. Python does not guess that you meant a number.

You've seen this trap before: in L0004, `"10"` and `10` were different things, and in L0005 `"5" + "5"` gave `"55"`.

Here's the bug in action:

```python
year = input("Birth year: ")
print(type(year))
print(2026 - year)
```

```
Birth year: 1999
<class 'str'>
Traceback (most recent call last):
  File "age.py", line 3, in <module>
    print(2026 - year)
TypeError: unsupported operand type(s) for -: 'int' and 'str'
```

Read the traceback from the bottom: `TypeError` means "wrong type for this operation". You can't subtract a `str` from an `int`. The line above tells you where: line 3.

Sometimes there's no crash at all, which is worse:

```python
n = input("Number: ")
print(n * 3)
```

```
Number: 4
444
```

`"4" * 3` repeats the text three times. No error, just a wrong answer.

---

## 3. Convert right away: `int(input(...))` and `float(input(...))`

The fix is L0004's conversions, applied to what `input()` gives back:

```python
litres = float(input("Litres of fuel: "))
trips = int(input("Number of trips: "))
price_per_litre = 1.85

cost_per_trip = litres * price_per_litre / trips
print(f"Each trip costs {cost_per_trip:.2f}")
```

Read `float(input("Litres of fuel: "))` **inside out**: first `input(...)` runs and returns text like `"12.5"`, then `float(...)` turns that text into the number `12.5`, then `=` stores it in `litres`.

You can also do it in two steps, which is just as good:

```python
litres_text = input("Litres of fuel: ")
litres = float(litres_text)
```

**Pick the type by what the value means:**

- things you count (people, trips, apples): `int`
- money, measurements, anything that can have a fraction: `float`

Why it matters: `int()` only accepts whole-number text.

```python
print(float("7.5"))   # 7.5
print(int("7"))       # 7
print(int("7.5"))     # ValueError: invalid literal for int() with base 10: '7.5'
```

So if the user types `7.5` into `int(input(...))`, the program crashes. We don't have a way to check the user's answer yet (that comes with `if` in L0011), so for now we assume they type sensible values.

---

## 4. Input, process, output

Most small programs have three blocks, in this order:

1. **Input**: read everything you need, converted to the right type.
2. **Process**: compute the results with arithmetic. Give each result its own name.
3. **Output**: print the results.

```python
# input
width = float(input("Width (m): "))
height = float(input("Height (m): "))

# process
area = width * height
perimeter = 2 * (width + height)

# output
print(f"Area: {area:.2f} m2")
print(f"Perimeter: {perimeter:.2f} m")
```

```
Width (m): 2.5
Height (m): 5
Area: 12.50 m2
Perimeter: 15.00 m
```

Why keep computing and printing apart? Each value gets a clear name (`area`), you can print it several times without repeating the formula, and when a number is wrong you know exactly which line to look at.

### Quick recap: `:.2f` (from L0008)

`:.2f` inside an f-string's braces shows a float with **exactly** 2 decimals. It pads if needed (`5.0` shows as `5.00`) and rounds if needed (`36.666...` shows as `36.67`). It only changes how the number **looks** in that one print. The variable still holds the full number.

```python
share = 10 / 3
print(f"{share:.2f}")   # 3.33
print(share)            # 3.3333333333333335  (unchanged)
```

Use it for money. Don't use it for counts: nobody buys "2.00 coffees".

---

## 5. `print` options: `sep=` and `end=`

When you give `print` several values separated by commas, it puts a space between them:

```python
print("Mon", "Tue", "Wed")    # Mon Tue Wed
```

That space comes from an option called `sep` (separator), which is `" "` unless you change it:

```python
print(2026, 10, 29, sep="-")          # 2026-10-29
print("Mon", "Tue", "Wed", sep=" / ") # Mon / Tue / Wed
print("snow", "ball", sep="")         # snowball
```

`sep` goes only **between** values. Not between characters, and not at the start or the end. Each value can be anything: text, a number, a variable, a calculation, even an f-string.

The second option is `end`: what `print` adds **after** everything. By default that's `"\n"`, a newline, which is why each `print` starts a new line. Change it and the next `print` carries on on the same line:

```python
print("Loading", end="")
print("... done")
```

```
Loading... done
```

`end` replaces the newline with exactly what you give it, nothing more. `end=""` adds nothing; `end=" "` adds one space.

And `print()` with nothing inside prints an empty line.

**How to write options:** they go after the values, with a comma before them, in `name=value` form:

```python
print("a", "b", sep="+")    # right
print("a", "b" sep="+")     # SyntaxError: missing comma
print("a", end)             # NameError: end isn't a variable
```

---

## Common mistakes

- **"I typed 5, so I got the number 5."** You got the string `"5"`. Convert it.
- **Converting but not storing it.** `int(age)` on its own line makes a number and throws it away. You need `age = int(age)` (you wrote this in your L0006 takeaways).
- **Converting into a new variable, then using the old one.** After `price = float(price_text)`, calculate with `price`, not `price_text`.
- **`int()` for money.** `int("47.60")` crashes with `ValueError`. Money is `float`.
- **Thinking `sep` also goes at the end.** It only goes between values.
- **Missing comma or `=` with `sep`/`end`.**
- **"My program froze."** It's probably waiting for input. Type something and press Enter.
- **Thinking `:.2f` changes the stored number.** It only changes how it looks.

---

## Try it yourself (not graded)

Make a scratch file anywhere outside `work/`, e.g. `scratch.py`, and run these.

1. Ask for a number with `input`, then print the number times 2. First without converting, then with `int(...)`. Type `21` both times. What's the difference?
2. Ask for a temperature in Celsius (it can have decimals) and print it in Fahrenheit with 1 decimal. Formula: `c * 9 / 5 + 32`. Try `36.6`.
3. Predict, then run:
   ```python
   print("x", "y", "z", sep="")
   print("one", end="|")
   print("two")
   print()
   print(1, 2, 3, sep=", ", end=".\n")
   ```

---

## Summary

- `input("prompt ")` shows the prompt, waits, and returns what was typed, **always as a `str`**.
- Convert right away: `int(input(...))` for counts, `float(input(...))` for money and measurements. Read it inside out.
- Programs are input → process → output. Give each computed value its own name.
- `print(a, b, c, sep="X")` puts `X` between the values. `print(a, end="X")` puts `X` after them instead of a newline.
- `:.2f` changes how a number looks, not the number itself.

---

## Questions
