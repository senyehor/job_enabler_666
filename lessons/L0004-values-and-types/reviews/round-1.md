# Review round 1: approved

Tests: 8 passed, 0 failed

## What's good
- Your Part 2 predictions are all right, including `int(3.9)` giving `3`. In the check questions you mixed up `int()` on a float with `int()` on text. Here you clearly had "int cuts off the decimal part" sorted out.
- Part 3 is done properly. The `int("abc")` line is still there, commented out, and the comment above it names `ValueError` and says why it happened (the text isn't a number). Your stretch goal also shows the habit the task is after: you predicted `ValueError` for `float("1e3")`, saw `1000.0`, and wrote `WRONG` instead of quietly changing the prediction.

## Issues
### 1. Two predictions don't match what was printed, and have no correction (minor)
`work/values.py:11` and `work/values.py:13`: you predicted `"hello" <class 'str'>` and `"10" <class 'str'>`. Run the script and look at lines 5 and 6 of the output. Are the quote marks there? Requirement 4 says every wrong prediction gets a `WRONG, actually ...` note, and these two don't have one yet. This one matters because it's the reason the bug in the task story is hard to spot: what does `print` show for `"10"`, and what does it show for `10`?
Hint (level 1): put your line 13 prediction next to the 6th line of the terminal output, character by character. What's different, and what does that tell you about what `print` does with the quotes?

## For next time
- `float("1e3")` printing `1000.0`: `e3` is a short way of writing "times 10 to the power 3", so `1e3` means 1 × 1000. You'll see it in numbers like `2.5e6` (2.5 million). Your "I don't know why" note was the honest thing to write.
- Part 3 comment: you can drop the copied part of the error message. Your own sentence after it already explains it well.

## Explain back
`print("10")` and `print(10)` look exactly the same in the terminal, but `type()` gives a different answer for each. In your own words, why? Then: what does `int("10")` change, and how does that connect to the "age saved as `"10"`" bug from the task?
