import unittest

from lessonkit import run_script

SCRIPT = "receipt.py"


class ReceiptTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_script(SCRIPT)
        cls.lines = [line.strip() for line in cls.result.stdout.splitlines() if line.strip()]

    def line_with(self, text):
        """The first output line that contains text (case-insensitive), or fail with a clear message."""
        for line in self.lines:
            if text.lower() in line.lower():
                return line
        self.fail(f"expected a line containing '{text}' in the output of {SCRIPT}, but there is none.\n"
                  f"Output was:\n{self.result.stdout}")

    def value_after(self, label):
        """What comes after the label's colon on its line, e.g. 'C' for 'First letter: C'."""
        line = self.line_with(label)
        start = line.lower().index(label.lower()) + len(label)
        return line[start:].lstrip(":").strip()

    def test_script_runs_without_errors(self):
        self.assertEqual(self.result.returncode, 0,
                         f"{SCRIPT} crashed. The error was:\n{self.result.stderr}")
        self.assertTrue(self.lines, f"{SCRIPT} printed nothing")

    def test_receipt_starts_with_shop_name_and_dash_divider(self):
        self.assertTrue(self.lines, f"{SCRIPT} printed nothing")
        self.assertIn("corner cafe", self.lines[0].lower(), "the first line should be the shop name, Corner Cafe")
        dividers = [line for line in self.lines if line == "-" * len(line) and len(line) >= 10]
        self.assertGreaterEqual(len(dividers), 2,
                                "expected two divider lines made of dashes (\"-\" * 24), one under the shop name "
                                "and one before the total")

    def test_each_item_line_shows_unit_price_and_line_total_with_two_decimals(self):
        expected = {"Coffee": ("2.50", "5.00"), "Croissant": ("1.75", "5.25"), "Orange juice": ("3.20", "3.20")}
        for name, (unit, total) in expected.items():
            with self.subTest(item=name):
                line = self.line_with(name)
                self.assertIn(unit, line, f"the {name} line should show the unit price as {unit} (use :.2f)")
                if unit != total:
                    self.assertIn(total, line, f"the {name} line should show the line total {total} (price * qty, :.2f)")

    def test_total_is_sum_of_line_totals_with_two_decimals(self):
        self.assertEqual(self.value_after("Total:"), "13.45",
                         "the Total: line should show 13.45 (5.00 + 5.25 + 3.20, formatted with :.2f)")

    def test_first_letter_and_last_three_of_shop_name(self):
        self.assertEqual(self.value_after("First letter:"), "C",
                         "First letter: should show C, the character at index 0 of shop")
        self.assertEqual(self.value_after("Last 3:"), "afe",
                         "Last 3: should show afe, the last three characters of shop")

    def test_reversed_item_name(self):
        self.assertEqual(self.value_after("Reversed:").lower(), "eeffoc",
                         "Reversed: should show eeffoC, which is Coffee backwards")

    def test_order_code_length(self):
        self.assertEqual(self.value_after("Code length:"), "13",
                         "Code length: should show 13, the len() of ORD-2026-0042 (dashes count too)")

    def test_order_code_split_into_prefix_year_and_number(self):
        expected = {"Prefix:": "ORD", "Year:": "2026", "Number:": "0042"}
        for label, value in expected.items():
            with self.subTest(label=label):
                self.assertEqual(self.value_after(label).upper(), value,
                                 f"{label} should show {value}, sliced out of ORD-2026-0042 (no dashes)")


if __name__ == "__main__":
    unittest.main()
