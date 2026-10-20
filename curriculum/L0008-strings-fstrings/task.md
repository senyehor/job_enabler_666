# L0008 Task: The Corner Cafe receipt

A small cafe called Corner Cafe has asked you for help. Their till prints receipts like `Coffee 2.5 2 5.0`, and customers keep asking what the numbers mean. Worse, the order codes are long strings like `ORD-2026-0042`, and staff have to read the year and the order number out of them by eye. You'll write a script that prints a tidy receipt with prices that always show two decimals, and then takes the order code (and a few other strings) apart with indexing and slicing.

## What to write

Write one file: `work/receipt.py`. The starter has a one-line comment at the top.

Store every piece of data in a variable first, and build each printed line with an **f-string**. Don't use string methods like `.upper()` or `.split()`; they come in a later lesson. `len()` is fine.

## Requirements

**Part 1: the receipt**

1. Create these variables, using exactly these values:

   | variable | value |
   |---|---|
   | `shop` | `"Corner Cafe"` |
   | `item1`, `price1`, `qty1` | `"Coffee"`, `2.5`, `2` |
   | `item2`, `price2`, `qty2` | `"Croissant"`, `1.75`, `3` |
   | `item3`, `price3`, `qty3` | `"Orange juice"`, `3.2`, `1` |
   | `order_code` | `"ORD-2026-0042"` |

2. Print the shop name on the first line, then a divider line of dashes. Make the divider with `"-" * 24`, not by typing 24 dashes.
3. Print one line per item: the name, the unit price, the quantity and the line total (price times quantity). Both money amounts must show **exactly two decimals** (`:.2f`). Compute the line total inside the f-string or in a variable. Don't type the result by hand.
4. Print another divider, then a `Total:` line with the sum of the three line totals, also with two decimals.

**Part 2: taking strings apart**

5. Print `First letter:` followed by the first character of `shop`, using an index.
6. Print `Last 3:` followed by the last three characters of `shop`, using a slice with a negative number.
7. Print `Reversed:` followed by `item1` written backwards, using `[::-1]`.
8. Print `Code length:` followed by the length of `order_code`, using `len()`.
9. Using slices of `order_code`, print three lines: `Prefix:` (the letters before the first dash), `Year:` (the 4 digits after it) and `Number:` (the last 4 digits).

Get every value in Part 2 from the variables. If you type `"afe"` or `"2026"` yourself, the program still "works" but you haven't solved the task.

## Example run

From inside `work/`:

```
$ python receipt.py
Corner Cafe
------------------------
Coffee 2.50 x 2 = 5.00
Croissant 1.75 x 3 = 5.25
Orange juice 3.20 x 1 = 3.20
------------------------
Total: 13.45
First letter: C
Last 3: afe
Reversed: eeffoC
Code length: 13
Prefix: ORD
Year: 2026
Number: 0042
```

Your item lines don't have to look exactly like this: `Coffee x2: 2.50 each, 5.00` is fine too. But each item must be on one line with its name and both amounts, and the labels in Part 2 (`Total:`, `First letter:`, ...) must be spelled as shown.

**Tip:** before slicing `order_code`, write its characters on paper with their index under each one (`O`=0, `R`=1, `D`=2, `-`=3, ...). The dashes count too.

## Run and test

- Run it: in the terminal, `cd` into `work/`, then run `python receipt.py`.
- Test it: from the repo root, run `python tools/learn.py test`.

## Stretch goal (optional)

Make the receipt line up in columns, like a real till. Inside the braces, `{item1:<14}` pads the name to 14 characters, and `{price1 * qty1:>6.2f}` right-aligns the amount in 6 characters. Make all the totals end in the same column, including the `Total:` line.
