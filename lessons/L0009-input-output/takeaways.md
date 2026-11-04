# L0009 Talking to the user: print and input

- `end=` switches how the line ends. `end="\n"` is a new line, so anything else in `end=` does not switch the line.
- `sep=` changes the default `" "` to anything that I want, so `print(a, b, c, sep="@")` will print `a@b@c`. If I'm not giving it `sep=`, it prints `a b c`.
- I tripped on using `sep=" | "` with an f-string: I wrote `print(f'Recap: {bill_amount:.2f, tip_amount:.2f, total_amount:.2f, share:.2f}', sep=" | ")`, which was totally wrong. `print` received only 1 value because my `{}` placement was wrong. The fix: `print(f"{x:.2f}", f"{y:.2f}", sep=" | ")`, separate values with commas between them.
- Next time I will follow the task more accurately.

## Tutor notes
- Check questions: thought `end="!"` carried over to the next print; fixed after re-explaining. Explain-back: said `int("47.60")` gives `TypeError`; corrected to `ValueError` (content wrong) vs `TypeError` (kind wrong), and he then got both quick checks right.
- Round 1 had `sep` and `end` on the wrong lines (req 5 vs 6); fixed in round 2. Last bullet stayed vague after two follow-ups. In L0010, prompt him to go through the numbered requirements one by one before `/review`.
- Watch: f-string formatting (one string = one value), and putting the `f` prefix on strings with no `{}`.
