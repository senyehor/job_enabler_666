# L0006 Variables and assignment

- I learned how to work with assigned values: `name = value` assigns a value to its name with the `=` symbol.
- I can convert a value with `name = int(name)`, `float(name)` etc. Then it's converted (just `int(name)` on its own doesn't store it).
- I can copy a value with `name = value`, `name2 = name`, and swap values with `tmp` in between the steps.
- I tripped on the type lines (`age is` / `height is`) in profile.py: I forgot to add them, but I read the task one more time, then read my code line by line, and found they were missing.
- Next time I will proceed with the same attention to details.

## Tutor notes
- All 3 check questions right first try; traces fully correct before running; approved round 1. His "check every step" rule caught the missing type prints himself.
- Weak spot: explaining *why* the naive swap fails. Twice (review and explain-back) he described the result ("both blue") rather than "line 3 overwrites the only copy of red". Revisit "reassignment loses the old value" when tracing comes up again.
- Ran ~125 min vs 65 estimated, finishing around 4:30 a.m. after a long session. Lessons run consistently long (~1.5–2x), so the planner may want bigger estimates or smaller tasks.
