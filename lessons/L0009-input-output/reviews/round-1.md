# Review round 1: changes requested

Tests: 6 passed, 1 failed

## What's good
- The input part is right. You wrapped each `input()` straight in its conversion (`float` for the bill, `int` for the percent and people), so `47.60` works and nothing crashes. The tip, total and share each get a clear name too.
- Every `:.2f` is inside the braces, with the `f` in front of the string, and that includes the four values on the recap line. That was the tricky part in the check questions, and here it's right every time.

## Issues
### 1. The word "Recap" isn't one of the values in the `sep` print (major)
`work/tip.py:15-16`: your recap line comes out as `Recap: 47.60 | 9.52 | 57.12 | 19.04`. Requirement 5 wants `Recap | 47.60 | 9.52 | 57.12 | 19.04`, made by **one** `print` call. Right now "Recap" is printed by a separate `print` on line 15, so the `sep=" | "` on line 16 never puts a bar after it. This is the test that fails.
Hint (level 1): `sep` only goes *between the values of the same `print` call*. On line 16, how many values does that `print` get, and is the word "Recap" one of them? What would change if it were?

### 2. "Each person pays:" uses one print instead of two with `end=` (major)
`work/tip.py:17`: this line prints the text and the share with one f-string. The output looks right, but requirement 6 asks for **two** `print` calls, with `end=` on the first one, so that both parts land on the same line. Using `end=` here is one of the two things this lesson is about. You did use `end=` on line 15, just on the wrong line: the Recap line should be a single print, and the share line should be split into two.
Hint (level 1): Look at lines 15 and 17 side by side. Which one does requirement 5 describe, and which one does requirement 6 describe? Do you have them the right way round?

## For next time
- `print('')` on line 11 works. A plain `print()` does the same thing and is a little shorter.
- Optional: the stretch goal (lining up the columns with widths like `:<8`) is still open if you'd like to try it.
