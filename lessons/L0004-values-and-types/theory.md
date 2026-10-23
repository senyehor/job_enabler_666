# L0004 Values and types

**What you get and what you write.** The starter `work/values.py` has only a one-line comment at the top. You write everything else yourself.

**Time:** about 15–20 minutes to read and try the examples, then the task.

To try an example, make a scratch file (for example `code scratch.py` somewhere outside `work/`), paste the example in, save, and run it with `python scratch.py`.

---

## 1. Every value has a type

A **value** is one piece of data: a number, a word, a yes/no answer.
A value's **type** says what kind of data it is, and so what you can do with it. You can add two numbers, but "adding" two pieces of text glues them together instead.

You can ask Python for the type of any value with `type()`:

```python
print(type(2026))
print(type("Kyiv"))
```

Output:

```
<class 'int'>
<class 'str'>
```

`<class 'int'>` is Python's way of saying "the type is `int`". For now, **class** just means **type**. You'll meet the word properly much later.

Note that `type()` only *asks*. It never changes the value.

---

## 2. The four basic types

Here's how to recognise each type just by reading the code:

| Type | What it is | How to spot it | Examples |
|---|---|---|---|
| `int` | whole number ("integer") | digits, **no dot** | `0`, `-15`, `1000000` |
| `float` | number with a decimal part ("floating point") | **has a dot** | `0.25`, `-1.0`, `100.0` |
| `str` | text ("string" of characters) | **in quotes**, `'...'` or `"..."` | `'cat'`, `"99"`, `""` |
| `bool` | yes/no ("boolean") | only `True` or `False`, capital first letter, **no quotes** | `True`, `False` |

Two rules beat "what it looks like":

- **The dot wins.** `100.0` is a whole number in maths, but in Python it's a `float` because of the dot.
- **The quotes win.** `"99"` looks like a number, but the quotes make it a `str`. The same goes for `"False"`: that's text, not a bool.

`""` (two quotes with nothing between) is the **empty string**: text with zero characters. It's still a `str`.

Sort these in your head before running them:

```python
print(type(55))
print(type(55.5))
print(type("55"))
print(type(False))
print(type("False"))
print(type(-0.0))
```

(Answers: int, float, str, bool, str, float.)

---

## 3. print shows values, not types

`print` shows the value on the screen *without* quotes. So text and numbers can look identical:

```python
print("8", 8)
print(type("8"), type(8))
```

Output:

```
8 8
<class 'str'> <class 'int'>
```

The first line looks like two eights. Only `type()` shows they're different kinds of data.

Also notice: when you give `print` two things separated by a comma, it prints them on one line with **one space** between them. That's how `print(55, type(55))` puts the value and its type side by side.

**Recap from L0003:** `print` shows text *exactly* as written inside the quotes, every character and every space. Nothing is added except that one space between comma-separated items.

---

## 4. Converting with int(), float(), str()

Each type name also works as a **converter**: give it a value, and it gives back a new value of that type. This is called **converting** (or "casting").

```python
print(int("100"))      # text "100"  -> number 100
print(float("0.75"))   # text "0.75" -> number 0.75
print(float(3))        # int 3       -> 3.0
print(str(2.5))        # float 2.5   -> text "2.5" (prints as 2.5)
print(int(7.99))       # float 7.99  -> 7
print(int(-2.7))       # float -2.7  -> -2
```

The last two are the surprising ones. `int()` on a float **truncates**: it simply cuts off everything after the dot. It does **not** round. So `7.99` becomes `7`, not `8`, and `-2.7` becomes `-2`, not `-3`.

And remember section 3: `str(2.5)` prints as `2.5`, just like the number. To see that it really became text, wrap it: `print(type(str(2.5)))`.

---

## 5. bool() and "truthiness"

`bool()` turns a value into `True` or `False`. The rule is short:

- **Zero** (`0`, `0.0`) and **empty** (`""`) become `False`.
- Almost everything else becomes `True`.

```python
print(bool(0.0))   # False: zero
print(bool(42))    # True: not zero
print(bool(""))    # False: empty text
print(bool(" "))   # True: a space is a character, so not empty
```

Whether a value counts as `True` or `False` like this is called its **truthiness**. You'll use it a lot later, when programs start making decisions.

---

## 6. When conversion fails: ValueError

Some conversions are impossible. Python can't turn the word `"twelve"` into a number, so it stops with an error:

```python
print("before")
print(float("ten"))
print("after")
```

Output:

```
before
Traceback (most recent call last):
  File "C:\Users\...\scratch.py", line 2, in <module>
    print(float("ten"))
          ~~~~~^^^^^^^
ValueError: could not convert string to float: 'ten'
```

Read it **bottom line first**, like in L0003:

1. **Last line**: the error name is the word before the colon, `ValueError`. A **ValueError** means "the type is right, but this particular value doesn't make sense for the job". The rest of the line explains it.
2. **Line above that**: the code that failed.
3. **The `File "...", line N` line**: this is where the line number lives for errors that happen while the script runs. Here it's line 2. (In L0003 you saw "detected at line N" too, but that only appears for a SyntaxError.)

Also notice: `before` was printed, but `after` never was. The script ran line by line and stopped at the crash.

`int()` is pickier than you might expect: `int("3.5")` also crashes with a ValueError, because `"3.5"` isn't text of a *whole* number. To get `3` from it you'd convert in two steps, text to float, then float to int.

To keep a broken line in your file but stop it from running, put `#` in front of it. It becomes a comment, and Python skips it.

---

## Common mistakes

- **"`"42"` is a number."** The quotes make it a `str`, whatever is inside.
- **"`int(3.9)` rounds to 4."** It truncates. Everything after the dot is cut off.
- **"`2.0` is an int because it's whole."** The dot makes it a `float`.
- **"`bool("False")` is False."** It's a non-empty string, so it's `True`.
- **Writing `true` or `false` in lower case.** Python doesn't know those names, so you get a `NameError`. It must be `True` / `False`.
- **"`int("3.5")` gives 3."** It crashes with a ValueError.
- **"`type()` changes the value."** It only reports the type.
- **"`str(7)` prints differently from `7`."** They print the same. Only `type()` tells them apart.

---

## Try it yourself (not graded)

1. Predict, then run:
   ```python
   print(type(0), type(0.0), type("0"))
   ```
2. Predict, then run:
   ```python
   print(int(9.999), int(-0.5), float(12))
   ```
3. Predict which lines print before the crash, and which line number the traceback shows:
   ```python
   print(bool("no"))
   print(int("seven"))
   print(bool(""))
   ```

---

## Summary

- Every value has a type. `type()` tells you which.
- `int` = no dot, `float` = has a dot, `str` = in quotes, `bool` = `True`/`False`.
- `print` hides the difference between `"5"` and `5`. `type()` doesn't.
- `int()`, `float()`, `str()`, `bool()` convert. `int()` on a float cuts off the decimal part.
- `bool()`: zero and empty are `False`, almost everything else is `True`.
- An impossible conversion gives a `ValueError`. Read the traceback bottom-up. The line number is on the `File "...", line N` line.

## Questions
