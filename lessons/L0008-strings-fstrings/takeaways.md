# L0008 Strings, f-strings, indexing and slicing

- I learned that adding `f` before the string turns a regular string into an f-string, which lets me mix str, int, float and bool into the same str with `{}`.
- I learned that a str has indexes, written like `[a]`. Now I know how to slice it with `[a:b]`, reverse it with `[::-1]`, and position values with `:>x` or `:<x`.
- `:.2f` shows a float with exactly 2 decimals: `5.0` prints as `5.00`, not shorter. The variable keeps the original number.
- I tripped because it was hard getting used to counting from 0 instead of 1, but I will get used to it eventually.
- Next time I will not forget about that, and I will have more than 3 hours of sleep before the lesson.

## Tutor notes
- Check Q1: included the stop index (`[1:4]` → `ytho`); got the variant right after the "stop is a fence, b − a" explanation. Also counted indexes from 1 once while teaching (`"cafe"`). He fixed both himself, and the task slices were all correct. Explain-back gave b − a only when prompted; keep checking that it's automatic.
- Takeaway said `:.2f` "shortens" the float; corrected through questions (pads 5.0 → 5.00, value unchanged). Approved round 1 with 2 minors left unfixed (`:.2f` on quantities, `"Orange Juice"` case). Watch format specs on ints and copying given values exactly.
- Ran ~172 min vs 70 estimated, on about 3 hours of sleep. Lessons keep running 2x+ long; the planner should consider that.
