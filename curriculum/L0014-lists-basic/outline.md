# L0014 Outline: Lists basics

## Learning goals (roadmap: py.lists-basic)
- **Creates, indexes, appends to and loops over lists**: writes a list literal (`[...]`) and an empty list (`[]`), reads items with positive and negative indexes, grows a list with `.append()`, gets its length with `len()`, and visits every item with `for item in my_list`.
- Practises `py.for` (a loop that fills a list, a loop that reads one) and `py.io` (reading a number of answers from the user).

## Key points, in teaching order

1. **A list is one value that holds many values, in order.**
   Square brackets, items separated by commas. Items can be any type from L0004, and a list can be empty: `[]`. `print(my_list)` shows the brackets and quotes, which is fine for checking but not for a user. `type([1, 2])` is `list`.
   Example idea: `scores = [7, 9, 4]`, `names = ["Ana", "Bo"]`, `nothing = []`. Print each one and its `type()`.

2. **Indexing works like strings (L0008): from 0, and negative indexes count from the end.**
   `my_list[0]` is the first item, `my_list[-1]` the last, `my_list[len(my_list) - 1]` is also the last. An index that is too big gives `IndexError: list index out of range`. Indexing an empty list always crashes, so check `len(...) == 0` first (L0011 `if`). Unlike strings, you can also *change* an item: `scores[1] = 10`. Slicing exists too but mention it only briefly.
   Example idea: `planets = ["Mercury", "Venus", "Earth", "Mars"]`. Ask for `planets[1]`, `planets[-1]`, `planets[-2]`, then `planets[4]` (crash, read the error).

3. **`len()` and `.append()`: building a list up step by step.**
   Start with `items = []` *before* the loop, then `items.append(x)` inside it. `append` changes the list in place and returns nothing, so `items = items.append(x)` is a bug (the variable becomes `None`). The dot syntax is new: "ask this list to append". Other list methods come later (`ds.lists`); only `append` is needed now.
   Example idea: collect three favourite songs with `input()` in a `for _ in range(3)` loop, then print `len(songs)` and the list.

4. **Looping over a list: `for item in my_list` and numbering with a counter or `range(len(...))`.**
   `for item in my_list` gives the items themselves, the same way `for ch in word` gave characters in L0013. When you also need a position, either keep a counter (`number = 1` before, `number = number + 1` inside) or loop `for i in range(len(my_list))` and use `my_list[i]`, printing `i + 1` for humans. Show both; both are fine at this stage.
   Example idea: a podium: `runners = ["Kim", "Lea", "Max"]` printed as `1. Kim`, `2. Lea`, `3. Max`.

5. **Accumulating over a list by hand: total and largest.**
   Same pattern as the L0013 accumulator: set up before, update inside, print after. For a total, start at `0`. For the largest, start with the *first item* (`biggest = values[0]`), not `0`, because if every value is negative, `0` would "win" even though it isn't in the list. The average is `total / len(values)`, formatted with `:.1f` (L0008).
   Example idea: lengths of rivers or prices in a basket: `prices = [3.5, 1.2, 8.0, 2.3]`, total and most expensive. Then show the trap with `losses = [-5, -2, -9]` and `biggest = 0`.

## Common misconceptions
- The first item is at index 1. (It's 0; the last is `len - 1` or `-1`.)
- `items = items.append(x)` "saves" the result. (`append` returns `None`.)
- Creating `items = []` *inside* the loop, so the list is reset every pass and ends with only the last item.
- `for i in my_list` gives positions. (It gives the items; `range(len(my_list))` gives positions.)
- Starting the maximum at `0` always works. (It fails when all values are negative.)
- `print(my_list)` is the same as printing the items one per line.

## Check-question ideas
1. Predict: `colors = ["red", "green", "blue"]`, then `print(colors[1], colors[-1], len(colors))`. (green blue 3)
2. Spot the bug: a loop that does `names = []` and `names.append(name)` both inside `for _ in range(3):`. What does `print(names)` show after typing a, b, c, and why?
3. Predict: `nums = []`, then `nums.append(4)`, `nums.append(1)`, `nums[0] = 9`, `print(nums, len(nums))`. ([9, 1] 2)
4. Explain why: `top = 0`, then `for t in [-3, -8, -1]:` with `if t > top: top = t` prints `0`. How do you fix it?

## Builds on
- L0008 (strings): indexing from 0, negative indexes, `len()`, `IndexError` style crashes, `:.1f` formatting.
- L0009 (input/output): `input()` returns `str`, converting the count with `int()`.
- L0011 (conditions): `if` for the empty-list case and for "is this bigger than the best so far?".
- L0013 (for loops): `range`, looping over a sequence, the accumulator pattern (set up before, update inside, print after).
