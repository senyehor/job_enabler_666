# L0012 Repeating with while loops (outline)

## Learning goals (py.while)
- Writes `while` loops with a clear exit condition: a variable that the condition checks, and a line inside the loop that moves it toward making the condition false.
- Spots infinite loops: reads a loop and says which variable never changes, stops a runaway program with Ctrl+C, and fixes it.

## Key points, in teaching order

1. **`while` is an `if` that repeats.** Python checks the condition. If it is True, the indented body runs, then Python jumps back up and checks again. When it is False, Python carries on with the first line after the body.
   Example: print "Hello" 3 times with `n = 0` / `while n < 3:` / `print("Hello")` / `n = n + 1`. Trace it in a table (n, condition, output), one row per round.

2. **The three parts of a counter loop: start, condition, step.** Before the loop, give the variable its start value. The condition decides when to stop. Inside the body, the step changes the variable. If any one of them is missing, the loop breaks.
   Example: print the even numbers 2, 4, 6, 8, 10 (`x = 2`, `while x <= 10`, `x = x + 2`). Then show that `<` vs `<=` decides whether 10 is printed (off-by-one).

3. **Looping "until something happens" (no fixed count).** The number of rounds isn't known in advance. The loop keeps going until a value crosses a threshold, and a separate counter variable records how many rounds it took.
   Example: a snail climbs 3 m per day up a 20 m well. `height = 0`, `days = 0`, `while height < 20:` add 3 to height and 1 to days, then print days after the loop (7). Same shape as the task, different story.

4. **Infinite loops: why they happen and how to stop them.** If nothing in the body changes what the condition checks, or it changes in the wrong direction, the condition stays True forever. In the terminal (Git Bash or PowerShell), Ctrl+C stops the program and Python prints `KeyboardInterrupt`. Show the two classic causes: the step is missing (or not indented into the body), and the step goes the wrong way (`while n > 0:` with `n = n + 1`).
   Example: `lives = 3` / `while lives > 0:` / `print("Still playing")` with no `lives = lives - 1`.

5. **Guard the loop with an `if` when input could make it endless.** Some inputs mean the exit condition can never be reached (a step of 0, for example). Check for those with `if/else` before the loop. Also, if the condition is False at the start, the body runs zero times, and that is often the correct answer.
   Example: "how many steps of size s does it take to walk d metres": if `s <= 0`, print a message instead of looping.

6. **Aside: `break`.** Mention that `break` leaves a loop immediately and that `while True:` + `break` exists. Keep it an aside: the task doesn't need it, and a clear condition is preferred for now.

## Common misconceptions
- Thinking the condition is watched all the time, so the loop stops the moment the variable changes mid-body. (It is only checked at the top of each round.)
- Putting the step (`n = n - 1`) after the loop because of wrong indentation, so the loop never ends.
- Expecting the body to run at least once. If the condition is False at the start, it never runs.
- Writing `n - 1` on its own line (it calculates a value and throws it away) instead of `n = n - 1`.
- Believing an infinite loop "broke" the computer. It's a program that never ends, and Ctrl+C stops it.
- Printing inside the loop when the result should be printed once after it, or the other way round.

## Check-question ideas
1. Predict the output:
   ```python
   n = 10
   while n > 0:
       print(n)
       n = n - 3
   print("end", n)
   ```
   (10, 7, 4, 1, then `end -2`.)
2. Spot the bug. Why does this never stop?
   ```python
   i = 0
   while i < 5:
       print(i)
   i = i + 1
   ```
   (The step is outside the body because of its indentation.)
3. How many times does the body run if `x = 5` and the loop is `while x < 5:`? (Zero. Explain why that isn't an error.)
4. Explain why `while total != 10: total = total + 3`, starting at 0, never ends, but `while total < 10:` would. (`!=` can jump past the target: 9, 12, ...)

## Builds on
- L0011 conditions: the `while` condition is the same kind of boolean expression as in `if`, and the guard before the loop is an `if/else`.
- L0009 input-output: `input()` with `int()`/`float()` gives the start values.
- L0007 arithmetic: the step (`n - 1`, adding a percentage) is plain arithmetic. L0008 `:.2f` formats money.
- L0006 variables: reassignment (`n = n - 1`) is what moves the loop forward. The tracing tables from L0006 work for loops too.
