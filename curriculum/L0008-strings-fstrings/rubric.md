# L0008 Rubric: Strings, f-strings, indexing and slicing

## Must-have
- [py.variables] All the given data (shop, three items with price and quantity, order code) is stored in variables with the given values. Nothing printed is typed in by hand.
- [py.arithmetic] Line totals are `price * qty` and the total is the sum of the line totals, computed by the program rather than typed in.
- [py.strings-basic] Every receipt line is built with an f-string, and every money amount uses `:.2f` (`5.00`, not `5.0`; `13.45`, not `13.450000000000001`).
- [py.strings-basic] The dividers use string repetition (`"-" * 24`).
- [py.strings-basic] First letter by index (`shop[0]`), last 3 by a negative slice (`shop[-3:]`), reversed with `[::-1]`, length with `len()`.
- [py.strings-basic] Prefix, year and number come from slices of `order_code` with correct positions (`[0:3]` or `[:3]`, `[4:8]`, `[9:]` or `[-4:]`).
- [env.run] `python receipt.py` runs without errors, and all tests pass.

## Likely mistakes

1. **Hard-codes values instead of slicing or computing** (py.strings-basic, major), e.g. `print("Year: 2026")` or `print("Total: 13.45")`.
   - Where: "If the order code changed to `ORD-2027-0100`, which lines would still be right?"
   - What: each value has to come out of the variable through an index, slice or arithmetic. See "Slicing" in theory.md.
   - How: with `date = "2026-10-20"`, `date[5:7]` gives the month for *any* date in that format.

2. **Off-by-one slice positions on the order code** (py.strings-basic, major if the output is wrong, minor if he fixed it by trial and error and can't explain it), e.g. `order_code[3:7]` giving `-202`.
   - Where: "Print `order_code[3]`. What character is that?"
   - What: indexes start at 0, the dashes count, and `stop` is not included. See "Indexing" and "Slicing".
   - How: write `"AB-12"` with indexes under it (`A`=0 ... `2`=4), then work out the slice for `12`.

3. **Missing `f` before the quote** (py.strings-basic, major, since the output shows the braces literally)
   - Where: "Look at the line your output shows `{total1:.2f}` on, and the first character before its quote."
   - What: only `f"..."` fills in the `{}`. A normal string keeps them as text.
   - How: compare `print("{2 + 2}")` with `print(f"{2 + 2}")`.

4. **No `:.2f`, or only on some amounts** (py.strings-basic, minor), e.g. `Coffee 2.5 x 2 = 5.0`.
   - Where: "Compare your Coffee line with a real receipt. How many decimals does each amount have?"
   - What: a format spec after `:` inside the braces controls how a value is shown. See "Format specs".
   - How: `x = 7 / 3`, then `print(f"{x}")` vs `print(f"{x:.2f}")`.

5. **Concatenation with a number causes a TypeError** (py.strings-basic, minor), e.g. `"Code length: " + len(order_code)`.
   - Where: "Read the last line of the traceback. Which two types does it say can't be added?"
   - What: `+` only joins str with str. Use an f-string (or `str()` from L0004).
   - How: `"Seats: " + 4` crashes, but `f"Seats: {4}"` works.

6. **Rounds the total with `round()` but prints without `:.2f`** (py.strings-basic, minor). `round(5.0, 2)` still prints `5.0`.
   - Where: "What does your program print for the Coffee line total?"
   - What: `round` changes the number, `:.2f` controls how it's shown. For receipts you want the display fixed.
   - How: `print(round(3.0, 2))` vs `print(f"{3.0:.2f}")`.

7. **Types 24 dashes instead of using `*`** (py.strings-basic, nit)
   - Where: "How would you make the divider 40 wide?"
   - What: `*` with a string and an int repeats the string.
   - How: `print("=" * 10)`.

8. **Last 3 done with a positive slice like `shop[8:11]`** (py.strings-basic, minor: the output is right, but the requirement asked for a negative slice)
   - Where: "If the shop were called `Bean Bar`, would `[8:11]` still give the last 3?"
   - What: negative indexes count from the end, so `[-3:]` works for any length.
   - How: `"Jupiter"[-3:]` and `"Mars"[-3:]`.

## Do not nitpick
- The exact item-line layout (`Coffee 2.50 x 2 = 5.00` vs `Coffee x2: 2.50 each, 5.00`), spacing, or a missing currency sign.
- `[0:3]` vs `[:3]`, `[9:]` vs `[-4:]` vs `[9:13]`. All are correct.
- Computing totals in variables vs inside the braces.
- Using string methods (`.split()`, `.upper()`) is against the task wording, so point it out, but it isn't a failure. Don't suggest methods, loops, lists, functions or `input()`; none have been taught yet.
- Variable naming beyond the given names, or PEP 8 details.

## Explain back
Ask him to explain `order_code[4:8]`: which characters positions 4 and 8 point at, why the slice gives `2026` and not `2026-`, and how many characters any `[a:b]` slice returns.
