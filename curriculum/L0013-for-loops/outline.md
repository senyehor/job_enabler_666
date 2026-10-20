# L0013 Outline: for loops and range

## Learning goals (roadmap: py.for)
- **Iterates over ranges and strings**: writes `for i in range(...)` with one, two and three arguments, and `for ch in word` to visit each character of a string.
- **Avoids off-by-one errors**: knows that `range` stops *before* its stop value, so he can pick the right start and stop for "1 to 10" or "n down to 1" and check the first and last value on purpose.

## Key points, in teaching order

1. **A `for` loop runs its body once for each item, and the loop variable holds the current item.**
   Compare with L0012: a `while` loop needs a counter you set up, test and update yourself. A `for` loop does all three for you, so it can't forget the update and loop forever. The loop variable is a normal variable that gets a new value on each pass. Indentation marks the body, the same as `if` and `while`.
   Example idea: `for ch in "hey": print(ch)`. Then trace it in a table (pass 1: ch = "h", pass 2: ...) before running it.

2. **`range(stop)` and `range(start, stop)`: the stop value is never included.**
   `range(5)` gives 0, 1, 2, 3, 4 (five numbers, no 5). `range(1, 6)` gives 1 to 5. Rule of thumb: `range(a, b)` gives `b - a` numbers, from `a` up to `b - 1`. To get "1 to N" you write `range(1, N + 1)`.
   Example idea: print the seat numbers of a row with 8 seats (`range(1, 9)`), and ask him first how many lines it prints. Show `range(1, 8)` missing seat 8, which is the classic off-by-one.

3. **`range(start, stop, step)`: counting by twos, and counting down.**
   A step of 2 skips numbers. A negative step counts down, and the stop is still excluded, so `range(5, 0, -1)` gives 5, 4, 3, 2, 1 and `range(5, 1, -1)` misses the 1. A count-down `range` with a start smaller than its stop is just empty (no error, no output).
   Example idea: even years `range(2020, 2031, 2)`, then "stairs" going down: `for step in range(10, 0, -2)`. Show `range(0, 5, -1)` printing nothing.

4. **Using the loop variable in calculations and output.**
   The loop variable is an `int` (from `range`) or a one-character `str` (from a string), so it can go into arithmetic and f-strings from L0008. An accumulator is created *before* the loop and updated *inside* it; the result is printed *after* it.
   Example idea: sum of 1 to 100 with `total = 0` before the loop and `total = total + n` inside it (Gauss's answer, 5050). Then a "squares" table: `print(f"{n} squared is {n * n}")` for `n` in 1 to 5.

5. **Looping over a string with an `if` inside: counting matches.**
   `for ch in text:` plus an `if` from L0011 picks out the characters you care about. Combine comparisons with `or` (L0011). Comparisons are case-sensitive: `"A" == "a"` is `False`.
   Example idea: count the spaces in a sentence (`if ch == " "`), which tells you the number of words minus one. Or count the letter `s` in `"mississippi"` (4).

6. **When to use `for` and when to use `while`.**
   `for`: you know in advance what to go through (a fixed number of times, or each character of a string). `while`: you repeat *until something happens* and you can't know how many passes it takes (the savings goal in L0012, asking again until the input is valid). Anything a `for` over `range` does, a `while` can do too, but with more places to make a mistake.
   Example idea: show the same "print 1 to 5" written both ways side by side, and point at the three lines the `while` version needs that the `for` version doesn't.

## Common misconceptions
- **"`range(1, 10)` includes 10."** It stops before the stop value. This is the main off-by-one of the lesson.
- **"`range(10)` starts at 1."** It starts at 0.
- **"`range(5, 0)` counts down."** Without a negative step it's empty, so nothing prints and there's no error message, which makes it confusing.
- **Changing the loop variable inside the body changes the next pass.** `for i in range(5): i = i + 10` doesn't skip anything; `i` gets the next value from `range` anyway.
- **Putting the accumulator (`count = 0`) inside the loop**, so it resets on every pass and ends up 0 or 1.
- **Printing the result inside the loop** (indented), so it prints once per pass instead of once at the end.
- **Forgetting `int()` on the input**, so `range("7")` or `"7" * i` gives a TypeError or a strange repeated string.

## Check-question ideas
1. **Predict the output:** `for i in range(2, 6): print(i)`. How many lines, and what are the first and last? (2 to 5, four lines.)
2. **Spot the bug:** a loop meant to print 1 to 10 uses `range(1, 10)`. What's printed, and what's the one-character fix? (Stops at 9; `range(1, 11)`.)
3. **Predict the output:** `count = 0` / `for ch in "Banana": if ch == "a": count = count + 1` / `print(count)`. (3. Follow up: what would `"Anna"` give? 1, because the capital `A` is not equal to `"a"`.)
4. **Explain why:** `for n in range(10, 0): print(n)` prints nothing and doesn't crash. Why, and how do you make it count down? (Default step is +1, so it's empty; add `-1`.)

## Builds on
- **L0012 (py.while)**: counter loops, exit conditions and infinite loops. The countdown is rewritten here, and the `for` vs `while` comparison is a key point.
- **L0011 (py.conditions)**: `if` and `or` inside the loop body for counting vowels.
- **L0008 (py.strings-basic)**: strings are sequences of characters, and f-strings for the table rows.
- **L0009 (py.io)** and **L0004 (py.values)**: `input()` with `int()` to get the number.
- **L0007 (py.arithmetic)**: multiplication in the table and `+ 1` in the range stop.
