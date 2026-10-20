# L0014 Task: The shopping list and the cold week

Your flatmate keeps forgetting half the shopping, so you're writing a tiny program that asks what to buy and then reads the list back neatly, numbered, so nothing gets lost on the way to the shop. While you're at it, your friend at the mountain hut sent you last week's midday temperatures and wants to know how cold it really was in total, what the warmest day was, and the average. Both jobs need the same new tool: a list, which keeps many values together in one variable, in order.

## What to write

Two files in `work/`: `shopping.py` and `temperatures.py`. Each starter file has a one-line comment at the top.

## Part 1: `shopping.py`

1. Ask `How many items? ` with `input()` and convert the answer to an `int`.
2. Create an empty list **before** the loop. Then use a `for` loop with `range` to ask for that many item names (`Item 1: `, `Item 2: `, ...) and `.append()` each name to the list.
3. If the list is empty (he answered `0`), print `Your list is empty.` and nothing else. Use `len()` to check this.
4. Otherwise, print `Your shopping list:` and then every item on its own line, numbered from 1, like `1. milk`. Use a `for` loop over the list (or over `range(len(...))`) to do this.
5. Then print these three lines:
   ```
   First item: <first item>
   Last item: <last item>
   Total items: <how many>
   ```
   Get the last item with a negative index (`[-1]`), and the count with `len()`.

## Part 2: `temperatures.py`

This program has no input. Start it with exactly this list:

```python
temps = [-4, -2, -7, -1, -5, -3, -6]
```

6. With **one or more `for` loops over `temps`**, work out the total of all the temperatures and the highest temperature. Don't use the built-in `sum()` or `max()`; the point is to do it by hand.
7. Work out the average as the total divided by `len(temps)`.
8. Print these three lines:
   ```
   Total: <total>
   Warmest: <highest>
   Average: <average with 1 decimal>
   ```

Careful with the warmest day: every temperature in this list is below zero. Think about what value your "highest so far" variable should start with.

## Example runs

From inside `work/`:

```
$ python shopping.py
How many items? 3
Item 1: milk
Item 2: eggs
Item 3: bread
Your shopping list:
1. milk
2. eggs
3. bread
First item: milk
Last item: bread
Total items: 3
```

```
$ python shopping.py
How many items? 1
Item 1: coffee
Your shopping list:
1. coffee
First item: coffee
Last item: coffee
Total items: 1
```

```
$ python shopping.py
How many items? 0
Your list is empty.
```

For `temperatures.py`, the output has this shape (work out the numbers yourself before you run it):

```
$ python temperatures.py
Total: ...
Warmest: ...
Average: ...
```

Your prompt text can be a little different, but the numbered lines and the `First item:`, `Last item:`, `Total items:`, `Total:`, `Warmest:` and `Average:` lines must look like the ones above.

## Run and test

- Run it: open the terminal, `cd` into `work/`, then run `python shopping.py` or `python temperatures.py`.
- Test it: from the repo root, run `python tools/learn.py test`.

## Stretch goal (optional)

In `temperatures.py`, also find the coldest day and *which day it was*. Print `Coldest: <value> on day <number>`, where day 1 is the first item in the list. Hint: loop over `range(len(temps))` so you have the position as well as the value.
