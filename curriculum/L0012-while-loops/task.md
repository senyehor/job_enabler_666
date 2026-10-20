# L0012 Repeating with while loops

You're helping a small space club with two tiny tools. The launch crew wants a countdown they can start from any number. The club treasurer wants to know how many years the club's savings need to sit in the bank, earning interest, before they can afford a new telescope. Then you'll meet every programmer's first runaway program: a loop that never ends. You'll stop it, work out why it never ends, and fix it.

Write three files in `work/`: `countdown.py`, `savings.py` and `fix_loop.py`. Use `while` loops for all three (no `for` yet, and no `break`).

## Part 1: `countdown.py`

1. Ask for the start number with `input("Start from: ")` and turn it into an `int`.
2. If the number is less than 1, print `Please enter a number of 1 or more.` and nothing else.
3. Otherwise use a `while` loop to print the numbers from that number down to 1, one per line. Do not print 0.
4. After the loop, print `Liftoff!`.

```
$ python countdown.py
Start from: 5
5
4
3
2
1
Liftoff!
```

```
$ python countdown.py
Start from: 0
Please enter a number of 1 or more.
```

## Part 2: `savings.py`

5. Ask for three numbers, each turned into a `float`, using these prompts:
   - `Starting balance: `
   - `Yearly interest rate (%): `
   - `Goal: `
6. If the rate is 0 or less and the balance is below the goal, the money will never grow enough, so a loop would never end. In that case print `You will never reach your goal with that rate.` and don't loop.
7. Otherwise, use a `while` loop that runs as long as the balance is below the goal. Each round is one year: add that year's interest (`balance * rate / 100`) to the balance and add 1 to a year counter.
8. After the loop, print the number of years and the final balance with 2 decimals, like below. If the balance already reaches the goal at the start, the answer is 0 years.

```
$ python savings.py
Starting balance: 1000
Yearly interest rate (%): 5
Goal: 1500
Years needed: 9
Final balance: 1551.33
```

```
$ python savings.py
Starting balance: 800
Yearly interest rate (%): 0
Goal: 1000
You will never reach your goal with that rate.
```

## Part 3: `fix_loop.py`

This program should add up the numbers 1 to 5 and print `Total: 15`. Type it into `fix_loop.py` exactly as shown:

```python
count = 1
total = 0
while count <= 5:
    total = total + count
print("Total:", total)
```

9. Run it with `python fix_loop.py`. It never prints anything and never ends. Stop it with **Ctrl+C** and look at the last line of the error (`KeyboardInterrupt`).
10. Fix the program by changing as little as possible, so it prints `Total: 15` and ends.
11. Above the loop, add a comment (a line starting with `#`) explaining in your own words why the original loop never ended.

## Running and testing

Run each program from inside `work/`, for example:

```
cd work
python countdown.py
```

Test everything from the repo root:

```
python tools/learn.py test
```

## Stretch goal (optional)

In `savings.py`, also print the balance at the end of every year inside the loop, e.g. `Year 1: 1050.00`, `Year 2: 1102.50`, ... before the final summary.
