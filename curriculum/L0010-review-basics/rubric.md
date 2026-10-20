# L0010 Rubric: Review of variables, arithmetic, strings and I/O

## Must-have
- [py.variables] `trace.txt` has a line-by-line trace for both scripts and `final:` lines that match: A `total = 205, minutes = 4, seconds = 5, text = 5s`; B `word = lat, n = 3.0, part = la`. Wrong predictions are corrected with a note, not silently replaced.
- [py.io] The program asks for first name, last name and metres with `input()`, and converts the metres with `int()`.
- [py.strings-basic] The greeting and the labelled lines use f-strings. Miles uses `:.2f` (`7.67` for 12345 m).
- [py.arithmetic] Kilometres uses `/ 1000`. The split uses `// 1000` and `% 1000` on the metres (`12 km 345 m`).
- [py.variables] The mile factor `1609.344` is stored in a named variable, and every printed value comes from the inputs (nothing typed in for one walker).
- [py.strings-basic] The badge uses `first[0]`, `last[0]` and `first[:3]`.
- [py.io] The badge is printed with two `print` calls: `end=" "` on the first, `sep="-"` on the second.

## Likely mistakes

1. **Trace A, line 5 uses the old `total` (writes `minutes = 3`)** (py.variables, major)
   - Where: "Look at line 5 of Script A. Which value does `total` hold at that moment?"
   - What: each line uses the values as they are *right then*, and line 4 already changed `total`. See the trace-table recap.
   - How: `p = 3`, `p = 10`, `q = p + 1`: is `q` 4 or 11?

2. **Trace B writes `n = 3` instead of `3.0`, or `part = "lan"`** (py.arithmetic / py.strings-basic, major)
   - Where: "Check lines 3 and 4 of Script B separately."
   - What: `/` always gives a float, and a slice stops *before* the end index.
   - How: `print(9 / 3)` gives `3.0`, and `"garden"[1:3]` is `"ar"`, not `"ard"`.

3. **Forgets `int()` on the metres, so `//` crashes with `TypeError`** (py.io, major)
   - Where: "Read the last line of the error. Which types does it say it can't combine?"
   - What: `input()` always returns a `str`, even when he types digits.
   - How: `eggs = input("Eggs: ")` then `eggs // 6` crashes; `eggs = int(input("Eggs: "))` works.

4. **Split computed from the kilometres or with `/` (`12.345 km 345 m`, or `12.0`)** (py.arithmetic, major)
   - Where: "Look at your Split line. Is the first number a whole number?"
   - What: whole units come from `//` on the int metres, leftovers from `%`.
   - How: 200 days: `200 // 7` is 28 weeks, `200 % 7` is 4 days.

5. **Miles not rounded, or rounded by hand (`7.67` typed in)** (py.strings-basic, major if typed in, minor if just unrounded)
   - Where: "Run it with 5007 metres. Does the Miles line still look right?"
   - What: `:.2f` inside the braces rounds the display. See the f-string recap.
   - How: `f"{10 / 3:.2f}"` gives `3.33`.

6. **Badge printed in one call, so `sep="-"` also lands after `Badge:` (`Badge:-ML-Mar`)** (py.io, minor)
   - Where: "Look at what is between `Badge:` and the initials."
   - What: `sep` goes between *every* item of that one call. That's why the task splits it into two prints with `end=" "`.
   - How: `print("Score:", 7, 10, sep="/")` prints `Score:/7/10`. Compare it with `print("Score:", end=" ")` then `print(7, 10, sep="/")`.

7. **`1609.344` written directly in the expression** (py.variables, nit)
   - Where: "Which number in your Miles line would a reader not recognise?"
   - What: a named variable makes a magic number readable (requirement 7).
   - How: `kg_per_pound = 0.4536`, then `pounds * kg_per_pound`.

## Do not nitpick
- Prompt wording, spacing, blank lines, or `km`/`m` written differently.
- Computing a value inside the f-string vs into a variable first: both are fine.
- Initials built with `+` or with an f-string: either is fine as long as they come from indexing.
- Names shorter than 3 letters: `"Al"[:3]` just gives `"Al"`, so no handling is needed.
- Invalid input (letters for metres, empty names). There are no conditions yet. Don't suggest `if`, `try`, loops, functions, `.upper()`, `.split()`, `round()` or `divmod`.

## Explain back
Ask him to explain line 5 of Script A out loud: which value of `total` it uses, and why `minutes` ends up as 4. Then ask why the Split line needs the metres as an `int` from `int(input(...))`, and what would go wrong if he used `float` instead.
