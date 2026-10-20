# L0006 Task: Keeping track of values

You're helping build the profile page of a small sign-up app. Before you touch the real code, a teammate warns you: "most bugs here come from someone thinking a variable holds one value when it actually holds another." So you'll practise two things. First you play the computer: you follow short scripts line by line on paper and write down what every variable holds. Then you write a tiny profile script that keeps a user's details in variables and updates them when something changes, like a birthday.

## What to write

Two files in `work/`. Both already exist with a one-line comment at the top:
- `work/trace.txt`: your hand-traces (Part 1)
- `work/profile.py`: the profile script (Part 2)

## Part 1: Trace by hand (`trace.txt`)

Here are three short scripts. **Don't run them yet.**

Script A:
```python
x = 5
y = x
x = 10
print(x, y)
```

Script B:
```python
a = "red"
b = "blue"
a = b
b = a
print(a, b)
```

Script C:
```python
count = "3"
count = int(count)
count = count + 1
label = "level"
label = label + str(count)
print(count, label)
```

1. For each script, write in `trace.txt` one line per assignment, showing the value of **every** variable that exists after that line. Then write a `final:` line with the values at the end. Use exactly this layout (here for a different script, `n = 1` / `m = n` / `n = 7`):
   ```
   Example
   line 1: n = 1
   line 2: n = 1, m = 1
   line 3: n = 7, m = 1
   Example final: n = 7, m = 1
   ```
   So your file has a block for `A`, `B` and `C`, each ending with `A final: ...`, `B final: ...` and `C final: ...`. Quotes around text values are optional.
2. Only when all three traces are written: type each script into a scratch file (for example `work/check.py`), run it, and compare the printed values with your `final:` lines. If you were wrong, **don't delete your answer**. Fix the line and add a note below it, for example `# I was wrong: I thought ... because ...`.
3. Under Script B's block, write one sentence explaining why it doesn't swap the two colours.

## Part 2: The profile script (`profile.py`)

The sign-up form sends everything as text. Your user is:

| fact | value from the form |
|---|---|
| name | `"Mara Lind"` |
| age | `"29"` (text!) |
| height in metres | `"1.68"` (text!) |
| is a student | `True` |

4. Store each fact in its own well-named variable (for example `name`, `age`, `height`, `is_student`).
5. Convert the age to an `int` and the height to a `float`, and store the results back in variables. Write the value `"29"` only once in your file, and the same for `"1.68"`.
6. Print the profile, then print the type of `age` and of `height` so you can see the conversion worked.
7. It's Mara's birthday and she has just graduated. Update the variables: age goes up by 1 using `age = age + 1` (don't type `30`), and `is_student` becomes `False`.
8. Print the profile again.

Use `print` with commas, like `print("Age:", age)`. The output must look like this (spacing doesn't matter):

```
$ python profile.py
Name: Mara Lind
Age: 29
Height: 1.68
Student: True
age is <class 'int'>
height is <class 'float'>
--- after the birthday ---
Name: Mara Lind
Age: 30
Height: 1.68
Student: False
```

## Run and test

- Run it: in the terminal, `cd` into `work/`, then `python profile.py`.
- Test it: from the repo root, run `python tools/learn.py test`.

## Stretch goal (optional)

Script B was meant to swap the colours. In `work/swap.py`, write a version that really swaps them, so it prints `blue red`, using a third variable. Add a trace of it at the bottom of `trace.txt`.
