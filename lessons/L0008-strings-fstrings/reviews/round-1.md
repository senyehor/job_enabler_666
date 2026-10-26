# Review round 1: approved

Tests: 8 passed, 0 failed

## What's good
- Your `order_code` slices are all right: `[:3]`, `[4:8]` and `[-4:]`. You skipped both dashes and didn't include the stop position. In the check questions that was the tricky part, and here you got it right.
- Nothing is typed in by hand. Every total is worked out inside the f-string, and `Last 3` uses a negative slice, so it would still work for a shop with a different name. You also went for the stretch goal and lined up the item columns with `:<14` and `:>6.2f`.

## Issues
### 1. Quantities are shown as money (minor)
`work/receipt.py:16-18`: the receipt prints `2.50 * 2.00`. Do you ever order "2.00 coffees"? Which of the values on this line are amounts of money, and which are counts of things? The task asks for two decimals on the **money** amounts only.
Hint (level 1): look at the format spec after `qty1` inside the braces. What does `.2f` do to a whole number like `2`?

### 2. One item name doesn't match the given value (minor)
`work/receipt.py:9`: compare `item3` with the table in `task.md`, letter by letter. One letter's case is different. The tests ignore upper/lower case, so they didn't notice, but the task says "using exactly these values".
Hint (level 1): is `"Orange Juice" == "Orange juice"` True or False in Python?

## For next time
- `work/receipt.py:15,19`: `f'-' * 24` has an `f` but no `{}` inside. What does the `f` add here?
- Stretch goal: the `Total:` amount doesn't end in the same column as the item totals. It's optional, so only fix it if you want to.

## Explain back
Explain `order_code[4:8]` in your own words: which characters are at positions 4 and 8, why the slice gives `2026` and not `2026-`, and how many characters any `[a:b]` slice returns. Slices come up all the time when reading data apart, like dates, codes and IDs, so this needs to be automatic.
