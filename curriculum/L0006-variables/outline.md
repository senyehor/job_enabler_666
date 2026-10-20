# L0006 Outline: Variables and assignment

## Learning goals (roadmap: py.variables)
- Traces variable values through a script by hand, line by line, including reassignments and a swap.
- Stores values in well-named variables and reassigns them (`age = age + 1`).
- Practises py.values: converts a text value stored in a variable with `int()` / `float()` and checks it with `type()`.

## Key points (teaching order)

1. **A variable is a name for a value.** `=` means "make this name point to this value". It is not "equals" from maths. Python works out the right side first, then attaches the name on the left.
   Example: `city = "Lviv"`, then `print(city)` and `print(type(city))`. Compare `print("city")` with `print(city)`: quotes mean the text itself, no quotes mean "look up this name".

2. **Reassignment replaces the value; the old one is gone.** Python runs top to bottom (links to L0003), so a name holds whatever was assigned to it last.
   Example: `temperature = 12`, `print(temperature)`, `temperature = 18`, `print(temperature)`. Then `temperature = "warm"`: a variable can even change type.

3. **Using a variable on both sides: `x = x + 1`.** The right side uses the *old* value, then the name gets the new value. This is the only arithmetic in this lesson (full arithmetic is L0007). `+` also joins strings, from L0005.
   Example: `lives = 3`, `lives = lives + 1` gives 4. `word = "sun"`, `word = word + "flower"`.

4. **Copying a variable copies the current value, not a link to the name.** After `b = a`, changing `a` later does not change `b` (for ints and strings, which is all he knows).
   Example: `price = 10`, `old_price = price`, `price = 12`: `old_price` is still 10.

5. **Tracing by hand, and the swap.** Show a trace table: one row per line, one column per variable. Then walk through the naive swap (`p = q`, `q = p`) on paper and show why both end up the same, then the fix with a third variable `tmp`. Use different names/values from the task (for example `left = "cat"`, `right = "dog"`).
   Mention `a, b = b, a` exists, but say the course uses the `tmp` version for now so he can trace it.

6. **Names and conversion.** Naming rules (letters, digits, `_`, can't start with a digit, case-sensitive, no spaces) and the habit of descriptive `snake_case` names (`is_student`, not `s`). Booleans often get an `is_` name. Show converting text stored in a variable: `steps_text = "8000"`, `steps = int(steps_text)`, `print(type(steps))` (links to L0004). Show `NameError` from a typo (`print(stpes)`) and how to read it.

## Common misconceptions
- "`=` checks if two things are equal." It assigns.
- "`b = a` ties `b` to `a` forever, so changing `a` changes `b`."
- "`x = x + 1` is impossible, because x can't equal x + 1."
- Writing `5 = x` (the name must be on the left).
- Thinking `print("age")` prints the variable's value.
- Thinking `int(age_text)` changes `age_text` itself. It returns a new value that you have to store.
- Using a variable before assigning it, or misspelling it (`NameError`).

## Check-question ideas
1. Predict the output: `n = 2`, `m = n`, `n = n + 1`, `print(n, m)`.
2. Spot the bug: `score = "7"`, `int(score)`, `score = score + 1` crashes. Why, and what one-line change fixes it?
3. Predict the output: `a = "x"`, `b = "y"`, `a = a + b`, `b = a + b`, `print(a, b)`.
4. Explain why: the swap `p = q` then `q = p` doesn't swap. What's lost, and on which line?

## Builds on
- L0003 first-script: top-to-bottom execution, reading an error and its line number.
- L0004 values-and-types: `type()`, `int()`, `float()`, `str()`.
- L0005 review: `+` joins strings, `int("7") + 1`.
