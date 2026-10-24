# L0006 Variables and assignment

**What you get and what you write.** The starter gives you two files in `work/`, each with only a one-line comment: `trace.txt` and `profile.py`. You write everything else yourself.

**Time:** about 15–20 minutes to read and try, then the task.

So far you've put every value straight into `print`. That's why you had to write the same expression twice in the quiz. Variables fix that: you give a value a name once, then use the name.

---

## 1. A variable is a name for a value

```python
city = "Lviv"
print(city)
print(type(city))
```

Output:

```
Lviv
<class 'str'>
```

`city = "Lviv"` creates a **variable**: a name (`city`) attached to a value (`"Lviv"`). After that line, wherever you write `city`, Python uses `"Lviv"`.

The `=` sign here is called **assignment**. It does **not** mean "equals" like in maths. It means "make this name point to this value". Python always:

1. works out the **right** side first,
2. then attaches the name on the **left** to the result.

So the name always goes on the left. `"Lviv" = city` is a SyntaxError.

**Quotes or no quotes?**

```python
print("city")   # city   (the text "city" itself)
print(city)     # Lviv   (look up the name city and print its value)
```

With quotes, it's text. Without quotes, Python treats it as a name and looks it up.

---

## 2. Reassignment replaces the value

Python runs your script from top to bottom. A variable holds whatever was assigned to it **last**:

```python
temperature = 12
print(temperature)       # 12
temperature = 18
print(temperature)       # 18
temperature = "warm"
print(temperature)       # warm
```

Giving a variable a new value is called **reassignment**. When `temperature = 18` runs, the old `12` is gone. The name now points at `18`.

The last line shows that a variable can even switch to a different type: it was an `int`, and now it holds a `str`.

---

## 3. Using a variable on both sides: `x = x + 1`

In maths, `x = x + 1` makes no sense. In Python it's very common. Remember the rule: **right side first**.

```python
lives = 3
lives = lives + 1
print(lives)    # 4
```

Line 2, step by step:
1. Right side: `lives` is currently `3`, so `lives + 1` is `3 + 1`, which is `4`.
2. Left side: the name `lives` now points to `4`.

The right side uses the **old** value, then the name gets the **new** value.

It works with strings too. From L0005 you know that `+` on two strings glues them:

```python
word = "sun"
word = word + "flower"
print(word)     # sunflower
```

---

## 4. Copying a variable copies the current value

```python
price = 10
old_price = price
price = 12
print(price, old_price)   # 12 10
```

Line 2, `old_price = price`, works out the right side, which is `10`, and attaches `old_price` to that `10`. It does **not** tie `old_price` to the name `price` forever.

So when `price` changes on line 3, `old_price` doesn't notice. It still holds `10`.

Think of it like copying a number off a whiteboard into your notebook. If someone rubs out the board and writes a new number, your notebook doesn't change.

---

## 5. Tracing by hand, and the swap

**Tracing** means playing the computer: going through the script line by line and writing down what every variable holds after each line. A **trace table** has one row per line and one column per variable:

```python
n = 1
m = n
n = 7
```

| after line | n | m |
|---|---|---|
| 1 | 1 | (doesn't exist yet) |
| 2 | 1 | 1 |
| 3 | 7 | 1 |

Each row is a snapshot of **all** the variables at that moment, not just the one that changed.

**The swap trap.** You want `left` and `right` to swap their values:

```python
left = "cat"
right = "dog"
left = right
right = left
print(left, right)
```

Trace it:

| after line | left | right |
|---|---|---|
| 1 | cat | |
| 2 | cat | dog |
| 3 | dog | dog |
| 4 | dog | dog |

Output: `dog dog`. On line 3, `left` gets `"dog"` and its old value `"cat"` is **gone**. By line 4, there's no `"cat"` left anywhere to copy.

**The fix:** keep the old value in a third variable before overwriting it. That extra variable is often called `tmp` (short for "temporary"):

```python
left = "cat"
right = "dog"
tmp = left       # save "cat"
left = right     # left is now "dog"
right = tmp      # right gets the saved "cat"
print(left, right)   # dog cat
```

(Python also has a one-line way to swap, `left, right = right, left`. For now we'll use the `tmp` version, because you can trace it step by step.)

---

## 6. Names and conversion

**Rules** (Python enforces these):
- Letters, digits and `_` only. No spaces, no `-`.
- Can't start with a digit: `2nd_place` is a SyntaxError, `place_2` is fine.
- Case-sensitive: `City` and `city` are two different names.

**Good habits** (Python doesn't check, but people reading your code will):
- Describe what the value is: `city`, not `c` or `x1`.
- Use `snake_case`: lowercase words joined with `_`, like `old_price`.
- True/False values often start with `is_`, like `is_open` or `is_member`.

**Converting a value stored in a variable** (from L0004):

```python
steps_text = "8000"
steps = int(steps_text)
print(steps, type(steps))   # 8000 <class 'int'>
```

`int(steps_text)` **gives back a new value**. It doesn't change `steps_text`, which is still the string `"8000"`. If you don't store the result with `=`, it's thrown away:

```python
steps_text = "8000"
int(steps_text)            # the result 8000 is thrown away
print(type(steps_text))    # <class 'str'>, still text
```

You can also store the result back under the same name: `steps = int(steps)`. Right side first, so it converts the old text and then the name points to the new int.

**NameError from a typo:**

```python
steps = 8000
print(stpes)
```

```
Traceback (most recent call last):
  File ".../scratch.py", line 2, in <module>
    print(stpes)
          ^^^^^
NameError: name 'stpes' is not defined. Did you mean: 'steps'?
```

Bottom line first: `NameError` means Python doesn't know the name `stpes`, because nothing was ever assigned to it. The line number is on the `File ... line 2` line. You also get a NameError if you use a variable **before** the line that assigns it.

---

## Common mistakes

- **"`=` checks whether two things are equal."** It assigns: right side first, then the name on the left.
- **"`b = a` ties b to a forever."** It copies a's current value. Changing a later doesn't affect b.
- **"`x = x + 1` is impossible."** The right side uses the old x, then x gets the new value.
- **Writing `5 = x`.** The name must be on the left.
- **"`print("age")` prints the variable."** Quotes make it text. Without quotes, it's the variable.
- **"`int(age_text)` changes `age_text`."** It returns a new value, which you have to store with `=`.
- **Using a variable before it's assigned, or misspelling it.** You'll get a `NameError`.

---

## Try it yourself (not graded)

1. Predict, then run:
   ```python
   points = 5
   bonus = points
   points = points + 10
   print(points, bonus)
   ```
2. Predict, then run:
   ```python
   greeting = "hi"
   greeting = greeting + "!"
   greeting = greeting + greeting
   print(greeting)
   ```
3. Make a trace table on paper for this, then run it to check:
   ```python
   first = "up"
   second = "down"
   first = first + second
   second = first
   print(first, second)
   ```

---

## Summary

- `name = value` attaches a name to a value. Right side first, then the name on the left.
- A variable holds whatever was assigned **last**. Reassignment throws away the old value.
- `x = x + 1` uses the old value to make the new one.
- `b = a` copies a's current value. It doesn't link the two names.
- Trace a script by writing every variable's value after each line. A swap needs a third variable.
- Names: letters, digits and `_`, no leading digit, case-sensitive. Make them descriptive.
- `int(...)` / `float(...)` return a new value. Store it with `=`.
- `NameError` means the name was never assigned, often because of a typo.

## Questions
