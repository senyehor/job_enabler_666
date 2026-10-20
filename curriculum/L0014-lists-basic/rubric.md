# L0014 Rubric: Lists basics

## Must-have
- [py.lists-basic] `shopping.py` creates an empty list (`[]`) **before** the input loop and fills it with `.append()`.
- [py.for] [py.io] The input loop uses `for ... in range(count)`, where `count` is the `int` of the first answer, and asks exactly that many times.
- [py.lists-basic] The numbered output loops over the list (`for item in items` with a counter, or `range(len(items))` with `items[i]`), not over a second copy of the input.
- [py.lists-basic] The first item uses `[0]`, the last uses `[-1]`, and the count uses `len()`.
- [py.lists-basic] The empty case is checked with `len(...) == 0` (or equivalent) *before* any indexing, so `0` doesn't crash.
- [py.lists-basic] [py.for] `temperatures.py` uses the given list and loops over it for the total and the warmest, without `sum()` or `max()`.
- [py.lists-basic] The warmest starts from an item of the list (usually `temps[0]`), not from `0`.
- [py.lists-basic] The average divides by `len(temps)`, not a hard-coded `7`.

## Likely mistakes

**1. `items = []` inside the loop** (py.lists-basic, major)
- Where: look at the line where your list is created, and which lines are indented under the `for`.
- Concept: everything inside the loop runs again on each pass, so the list is made new (empty) every time and only the last item survives.
- Example: `for n in range(3): box = []; box.append(n)` leaves `box` as `[2]`. Move `box = []` above the loop and it becomes `[0, 1, 2]`.

**2. `items = items.append(item)`** (py.lists-basic, major)
- Where: the line that adds an item to the list.
- Concept: `append` changes the list itself and gives back `None`; assigning that result throws the list away.
- Example: `x = [1]; y = x.append(2); print(x, y)` prints `[1, 2] None`.

**3. Warmest starts at `0`** (py.lists-basic, major)
- Where: the line before the loop that sets up your "highest so far" variable.
- Concept: the starting value has to be a real candidate from the list, otherwise a starting value higher than every item wins.
- Example: for `[-9, -3, -5]`, starting at `0` reports `0`; starting at `[-9, -3, -5][0]` (which is `-9`) correctly ends at `-3`.

**4. Indexing before checking for an empty list** (py.lists-basic, major)
- Where: run it with `0` items and read which line the `IndexError` points to.
- Concept: an empty list has no index 0 or -1; check `len(...) == 0` first and put the indexing in the `else`.
- Example: `print([][0])` crashes with `IndexError: list index out of range`.

**5. Numbering off by one** (py.for, minor)
- Where: the loop that prints `1. ...`, `2. ...`.
- Concept: positions start at 0, people count from 1; print `i + 1` (or start a counter at 1).
- Example: for `["a", "b"]`, `for i in range(len(...)): print(i, ...)` prints `0 a`, `1 b`; using `i + 1` gives `1 a`, `2 b`.

**6. Last item as `items[len(items)]`** (py.lists-basic, minor)
- Where: the `Last item:` line.
- Concept: the last index is `len - 1`; the task asks for the negative index `[-1]`.
- Example: `nums = [5, 6, 7]`: `nums[3]` crashes, `nums[2]` and `nums[-1]` are both `7`.

**7. Average divided by a hard-coded 7** (py.lists-basic, nit)
- Where: the average line.
- Concept: `len()` keeps the code correct if the list changes.
- Example: add an eighth temperature and see which version still gives the right average.

**8. Using `sum()` / `max()`** (py.for, minor)
- Where: the total and warmest lines.
- Concept: the task is to practise the accumulator loop; the built-ins come later.
- Example: write the loop for `[2, 9, 4]` by hand and check it gives 15 and 9.

## Do not nitpick
- Other list methods (`insert`, `remove`, `sort`, `pop`), slicing of lists, `enumerate`, `in` for membership: these belong to `ds.lists` later.
- Functions, `sum()`/`max()`/`min()` in places the task doesn't cover, list comprehensions.
- Validating the count (negative numbers or non-numbers). `int()` crashing on `abc` is fine at this stage.
- Counter vs `range(len(...))` for numbering: both are fine. One combined loop vs two separate loops for total and warmest: both fine.
- Exact prompt wording, blank lines, whether the total prints as `-28` or `-28.0`.
- Variable names like `i` or `t` for loop variables.

## Explain back
Ask him to explain the warmest-day loop in `temperatures.py`: why the "highest so far" variable starts at `temps[0]`, what happens on each pass, and what the program would print if it started at `0` instead.
