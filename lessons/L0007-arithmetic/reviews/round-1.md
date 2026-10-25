# Review round 1: approved

Tests: 7 passed, 0 failed

## What's good
- `work/calculator.py:28`: `(total_seconds % 3600) // 60` is exactly right. You take the hours out first with `%` and then turn what's left into minutes. Lots of people use `total_seconds // 60` here and get 164. I also tried `total_seconds = 5000` in my head: your code gives `1 h 23 min 20 s`, which checks out (3600 + 1380 + 20 = 5000).
- `work/calculator.py:32` and `:37`: you put brackets around the sum for the average, and you left the brackets out of `start_points * 2 ** weeks` because `**` already goes before `*`. Both are correct uses of precedence. Every Part 2 number is computed from the variables.

## Issues
### 1. The points label won't follow `weeks` (minor)
`work/calculator.py:38`: the number 10 is typed into the label text. Requirement 8 says that changing one variable should be enough. If `weeks` became 12, what would this line say, and would it still be true?
Hint (level 1): you already know how to print several values separated by commas, as on line 30. Which of those values could stand in for the 10?

## For next time
- `work/calculator.py:35`: the task's format is `Whole km average: <whole average>` with no "km" after it. Harmless, but stick to the given format when you can.
- `work/calculator.py:18`: a short `# Part 2` comment above the variables would make the two halves easy to tell apart.
- All 8 predictions were right, so there was nothing to correct. That's fine. The stretch goal (`-2 ** 2` and `17 % 5 * 2`) would give you a real chance to catch yourself out.

## Explain back
Talk through line 28 in your own words. What does `9876 % 3600` mean in plain English? Why do you need `%` before the second `//`, and what number would you get without it? Then: why does `6 / 2` print `3.0` and not `3`? Getting time and money conversions right in a backend depends on exactly this.
