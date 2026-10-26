# L0008 Outline: Strings, f-strings, indexing and slicing

## Learning goals (roadmap: py.strings-basic)
- **Formats output with f-strings**: puts variables and expressions inside `f"..."`, and shows money with exactly two decimals using `:.2f`.
- **Slices strings**: gets single characters with `[i]` and `[-i]`, pieces with `[start:stop]`, and reverses with `[::-1]`. Uses `len()` to measure a string.

## Key points, in teaching order

1. **A string is a sequence of characters, and `len()` counts them.**
   Recap from L0004: quotes make a `str`. New: every character has a position, spaces and dashes included. `len("New York")` is 8, not 7.
   Example idea: `city = "New York"`, then `print(len(city))`. Ask him to count by hand first.

2. **Indexing: positions start at 0, and negative indexes count from the end.**
   `word[0]` is the first character, `word[len(word) - 1]` and `word[-1]` are both the last one. An index that's too big gives `IndexError`.
   Example idea: `planet = "Jupiter"`: show `planet[0]`, `planet[3]`, `planet[-1]`, `planet[-2]`, then `planet[7]` crashing. Draw the index table under the letters (0..6 on top, -7..-1 below).

3. **Slicing: `[start:stop]` takes from start up to *but not including* stop.**
   You can leave out start or stop: `[:3]` is the first 3, `[-3:]` the last 3, `[4:]` everything from position 4. A slice never crashes when it goes past the end. `stop - start` is how many characters you get.
   Example idea: a phone number `"+380-67-1234567"` or a date `"2026-10-20"`: year `[0:4]`, month `[5:7]`, day `[8:]`. Point out that the dashes sit at positions 4 and 7, which is why the slices skip them.

4. **The step: `[start:stop:step]`, and `[::-1]` reverses.**
   Mention `[::2]` (every second character) briefly, then focus on `[::-1]`.
   Example idea: `"stressed"[::-1]` gives `"desserts"`. Also `"level"[::-1]` gives the same word back (palindrome).

5. **f-strings: `f"..."` with `{}` puts values into text.**
   Compare with what he knows: `print("Age:", age)` (L0006) and `"Age: " + str(age)` (concatenation needs `str()`, a TypeError otherwise). In an f-string, `{}` can hold any expression, including arithmetic and slices: `f"{price * 2}"`, `f"{name[0]}"`. Strings are also joined with `+` and repeated with `*` (`"-" * 20` makes a divider line).
   Example idea: a movie ticket: `film = "Dune"`, `seats = 3`, `print(f"{seats} tickets for {film}")`. Then show `"Dune" + 3` failing and the fix.

6. **Format specs: `{value:.2f}` shows exactly 2 decimals.**
   Floats print surprisingly: `0.1 + 0.2` shows `0.30000000000000004`, and `2.5 * 2` shows `5.0`, not `5.00`. `:.2f` fixes how it *looks* without changing the value. Optional at the end: width and alignment `{name:<12}` / `{amount:>8.2f}` (this is the stretch goal).
   Example idea: fuel cost: `litres = 32.5`, `price = 1.879`, `print(f"Fuel: {litres * price:.2f} EUR")`, which shows `61.07`.

## Common misconceptions
- Thinks the first character is at index 1.
- Thinks `[0:3]` includes position 3 (gives 4 characters).
- Forgets that spaces and dashes count as characters, so his slice positions for `"ORD-2026-0042"` are off by one.
- Forgets the `f` before the quote: `"{total}"` prints the braces literally, and there's no error to warn him.
- Thinks `:.2f` changes the number stored in the variable. It only changes the displayed text.
- Tries `"Total: " + total` with a float and gets a TypeError. Use an f-string or `str()`.
- Thinks a string can be changed in place (`word[0] = "X"`). That's a TypeError: strings are immutable. Only mention it briefly.

## Check-question ideas
1. **Predict the output:** `s = "Python"`, then `print(s[1], s[-2], s[1:4], s[::-1])`. (Answer: `y o yth nohtyP`.)
2. **Spot the bug:** `price = 4.5`, then `print("Total: {price * 2:.2f}")` prints `Total: {price * 2:.2f}`. Why? (Answer: the `f` is missing.)
3. **Explain why:** `code = "AB-12"`. Why does `code[3:5]` give `"12"`, but `code[5]` crashes? (Answer: a slice stops before 5 and may go past the end. An index must point at a real character.)
4. **Predict the output:** `print(f"{7 / 2:.2f}")` and `print(f"{2.999:.2f}")`. (Answer: `3.50` and `3.00`. Rounding happens only in the display.)

## Builds on
- L0004 (values and types): `str` vs numbers, `str()` / `float()` conversions.
- L0006 (variables): every receipt value lives in a named variable, and the slices are stored in variables too.
- L0007 (arithmetic): line totals with `*`, sum with `+`, and `/` results that need formatting.
- Leads into L0009 (input/output), where f-strings format answers to the user's input. Later, `ds.strings` adds string methods (`.upper()`, `.split()`, ...). Those are deliberately left out here.
