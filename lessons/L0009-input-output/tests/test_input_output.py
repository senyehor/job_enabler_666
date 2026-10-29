"""Tests for L0009: tip.py asks for a bill, tip percent and people, then prints the tip, total and share."""
import unittest

from lessonkit import run_script

SCRIPT = "tip.py"


def normalise(text):
    """Lower-case and drop all spaces, so 'Recap |  9.52' and 'recap | 9.52' match."""
    return "".join(text.split()).lower()


class TestTipCalculator(unittest.TestCase):
    runs = {}

    def run_tip(self, bill, percent, people):
        key = (bill, percent, people)
        if key not in self.runs:
            self.runs[key] = run_script(SCRIPT, stdin=f"{bill}\n{percent}\n{people}\n")
        result = self.runs[key]
        self.assertEqual(
            result.returncode, 0,
            f"{SCRIPT} crashed when the user typed {bill}, {percent} and {people}. "
            f"Did you convert each input() answer (float for the bill, int for the others)?\n"
            f"Error output:\n{result.stderr}")
        return result.stdout

    def assert_amount(self, output, amount, what, typed):
        self.assertIn(
            amount, output,
            f"Expected the {what} {amount} in the output when the user types {typed}. "
            f"Remember :.2f for money.\nYour output was:\n{output}")

    def find_line(self, output, start):
        for line in output.splitlines():
            if start in line.lower():
                return line
        self.fail(f"Expected a line containing '{start}'.\nYour output was:\n{output}")

    def test_accepts_a_bill_with_cents(self):
        output = self.run_tip("47.60", "20", "3")
        self.assert_amount(output, "57.12", "total", "47.60, 20, 3")

    def test_prints_the_header(self):
        output = self.run_tip("47.60", "20", "3")
        self.assertIn("tip calculator", output.lower(),
                      f"Expected the title line '=== Tip calculator ==='.\nYour output was:\n{output}")

    def test_shows_tip_and_total_with_two_decimals(self):
        output = self.run_tip("47.60", "20", "3")
        typed = "47.60, 20, 3"
        self.assert_amount(output, "47.60", "bill", typed)
        self.assert_amount(output, "9.52", "tip", typed)
        self.assert_amount(output, "57.12", "total", typed)

    def test_whole_number_bill_still_shows_cents(self):
        output = self.run_tip("80", "15", "4")
        typed = "80, 15, 4"
        self.assert_amount(output, "80.00", "bill", typed)
        self.assert_amount(output, "12.00", "tip", typed)
        self.assert_amount(output, "92.00", "total", typed)
        self.assert_amount(output, "23.00", "share per person", typed)

    def test_share_is_rounded_to_cents(self):
        output = self.run_tip("100", "10", "3")
        self.assert_amount(output, "36.67", "share per person (110 / 3)", "100, 10, 3")
        self.assertNotIn("36.666", output,
                         f"The share should show only 2 decimals (36.67), not 36.666...\nYour output was:\n{output}")

    def test_recap_line_lists_all_amounts_separated_by_bars(self):
        output = self.run_tip("47.60", "20", "3")
        line = self.find_line(output, "recap")
        self.assertIn(
            "recap|47.60|9.52|57.12|19.04", normalise(line),
            f"Expected the recap line to look like 'Recap | 47.60 | 9.52 | 57.12 | 19.04' "
            f"(one print with sep=\" | \").\nYour recap line was:\n{line}")

    def test_each_person_pays_is_on_one_line(self):
        output = self.run_tip("47.60", "20", "3")
        line = self.find_line(output, "each person pays")
        self.assertIn(
            "19.04", line,
            f"Expected 'Each person pays: 19.04' on one line. Use end=\" \" on the first print "
            f"so the amount stays on the same line.\nYour line was:\n{line}")


if __name__ == "__main__":
    unittest.main()
