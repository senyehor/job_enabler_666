# L0005 Review: terminal, scripts and types

**What you get and what you write.** The starter gives you only `work/answers.txt` with one comment line in it. You make the folders, the script and the answers yourself.

**Time:** about 15 minutes to read and try, then the task. This is a review lesson. There's nothing new here, just this week's pieces put together.

The terminal is Git Bash, so paths here use `/`.

---

## 1. The terminal always has a current folder

Your terminal is always "standing" in one folder, called the **current folder**. `pwd` shows which folder that is.

Every **relative path** (a path that doesn't start with `/c/...`) starts from the current folder. `..` means "one folder up".

Imagine this layout:

```
course/
  todo.txt
  notes/
    week1/
```

If you're in `course/notes/week1`:

```bash
pwd                 # /c/Users/Ann/course/notes/week1
cat ../todo.txt     # one up is notes/ ... but todo.txt isn't in notes/, so this fails
cat ../../todo.txt  # two up is course/, and todo.txt is there, so this works
cd ../..            # now you're in course/
```

Read a path one step at a time: each `..` is one step up, and each name is one step down.

The commands you know:

| Command | Does |
|---|---|
| `pwd` | show the current folder |
| `ls` | list what's in the current folder |
| `cd name` / `cd ..` | step down into `name` / step up |
| `mkdir name` | make a new folder `name` inside the current folder |

---

## 2. `python <path>` takes a path, like any other command

`python` is the program. The thing after it is the **path to your script**, and that path starts from the terminal's current folder, just like `cat` or `cd`.

```
project/
  tools/
    greet.py
```

```bash
# standing in project/
python tools/greet.py    # works: step down into tools, then greet.py

# standing in project/tools/
python greet.py          # works: greet.py is right here
python tools/greet.py    # fails: there's no tools/ inside tools/
```

When the path is wrong, you get this error:

```
python: can't open file '.../tools/tools/greet.py': [Errno 2] No such file or directory
```

This error is about the **path**, not your code. Python never even opened the file. Fix it with `pwd` and `ls`: where am I, and where is the file from here?

---

## 3. `+` depends on the types

The same `+` sign does different jobs depending on the types around it:

```python
print(2 + 3)        # 5:    int + int is adding
print("2" + "3")    # 23:   str + str is gluing text together
print("ab" + "cd")  # abcd
```

Gluing strings together is called **concatenation**.

What about a string plus a number?

```python
print("2" + 3)
```

```
Traceback (most recent call last):
  File ".../scratch.py", line 1, in <module>
    print("2" + 3)
          ~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

Bottom line first: a **TypeError** means "these types can't do this together". Python won't guess whether you meant adding or gluing, so it stops. The line number is on the `File ... line 1` line.

---

## 4. Convert first, then compute

Python works out the innermost brackets first. So you can convert a value, and *then* use `+`:

```python
print(int("12") + 3)     # int("12") becomes 12, then 12 + 3 = 15
print(str(12) + "3")     # str(12) becomes "12", then "12" + "3" = "123"
print(float("1.5") + 1)  # 1.5 + 1 = 2.5
print(int(4.7))          # 4: cuts off the decimals, doesn't round
```

Read each one in two steps: what does the conversion give, and what type is that? Then what does `+` do with those types?

---

## 5. `bool()` of a string only checks whether it's empty

`bool()` doesn't read words. For a string it asks one question: **is there at least one character?**

- `""` (nothing between the quotes) → `False`
- any other string → `True`, whatever it says

For numbers, only `0` and `0.0` are `False`.

**Predict these four before you run them:**

```python
print(bool("no"))
print(bool("0"))
print(bool(0))
print(bool(" "))
```

(Answers: `True`, `True`, `False`, `True`. `"no"` and `"0"` are both non-empty strings. Only the number `0` is `False`.)

---

## 6. print with commas, and labels

**Recap from L0004:** `print` doesn't show a string's quotes. `print("10")` and `print(10)` both show `10`. Only `type()` tells them apart.

`print` with commas prints several things on one line, with a space between each:

```python
print("int('3') ->", int("3"), type(int("3")))
```

```
int('3') -> 3 <class 'int'>
```

There are three parts here:
1. `"int('3') ->"` is a **label**. It's in quotes, so it's just text and is printed exactly as written. Nothing gets computed.
2. `int("3")` has no quotes around it, so Python **computes** it and prints `3`.
3. `type(int("3"))` computes the type.

Compare:

```python
print("2 + 3")   # 2 + 3   (text, printed as written)
print(2 + 3)     # 5       (computed)
```

**Quotes inside a label:** a string ends at the next matching quote. If you need `"` inside the label, wrap the label in `'...'` instead:

```python
print('She said "hi"')    # She said "hi"
print("She said "hi"")    # SyntaxError: the string ends after "She said "
```

---

## Common mistakes

- **"`python quiz.py` finds the file wherever it is."** It only looks from the current folder.
- **"`..` means the folder the script is in."** It means one up from the *terminal's* current folder.
- **"`"5" + "5"` is 10."** Quotes make them text, so `+` glues them.
- **"`bool()` understands the word."** It only checks whether the string is empty.
- **"`int(9.99)` rounds to 10."** It cuts off the decimals and gives 9.
- **"The label in quotes gets computed."** Anything in quotes is printed exactly as written.

---

## Try it yourself (not graded)

1. Predict, then run:
   ```python
   print("1" + "2" + "3", 1 + 2 + 3)
   ```
2. Predict, then run:
   ```python
   print(int("20") + 5, str(20) + "5")
   ```
3. Make a folder `a` with a folder `b` inside it, and put a script `hi.py` in `b` that prints something. Run it once from the folder that contains `a`, and once from inside `b`. What path do you type each time?

---

## Summary

- The terminal has a current folder (`pwd`). Relative paths, including the one after `python`, start from there. `..` is one up.
- `[Errno 2] No such file or directory` means a wrong path, not wrong code.
- `+`: int + int adds, str + str glues, str + int is a `TypeError`.
- Convert first (`int(...)`, `str(...)`), then `+` works on the new type.
- `bool(string)` is `False` only for `""`.
- In `print`, a label in quotes is shown exactly as written, and an expression without quotes gets computed.

## Questions
