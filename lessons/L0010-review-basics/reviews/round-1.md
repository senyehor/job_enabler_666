# Review round 1: approved

Tests: 8 passed, 0 failed

## What's good
- Your traces are right on every line, including the two spots where most people slip. In Script A, line 5 uses the *new* `total` (205), so `minutes` becomes 4. In Script B, you wrote `n = 3.0` because `/` always gives a float, and `part = 'la'` because the slice stops before index 3.
- `unit_converter.py` is short and every value comes from the input. `int()` is wrapped around the `input()` for the metres, so `//` and `%` work on a whole number. `1609.344` has a clear name (`metres_per_mile`). And the badge uses the two-print trick correctly: `end=" "` on the first call and `sep="-"` on the second, so there is no stray dash after `Badge:`. I also tried it with a short name ("Al"), and it still worked fine.

## Issues
None that block approval.

## For next time
- `work/trace.txt:1`: the first line starts with `code#` instead of `#`. It looks like the word `code` got typed into the file by accident. Remove it so the comment reads cleanly.
- `work/unit_converter.py:3`: `name` sits next to `last_name`. Calling it `first_name` would make the pair easier to read.

## Explain back
Explain line 5 of Script A (`minutes = minutes + total // 100`) in your own words: which value of `total` does it use at that moment, and why does `minutes` end up as 4 and not 3? Then explain why the Split line in your program needs the metres as an `int`, and what would go wrong if you had used `float(input(...))` instead.
