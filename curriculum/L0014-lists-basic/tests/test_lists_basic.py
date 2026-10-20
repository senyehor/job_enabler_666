"""Tests for L0014: shopping.py builds a list from input; temperatures.py totals a fixed list by hand."""
import re
import unittest

from lessonkit import run_script


def value_after(label, text):
    """Return what follows 'label:' on the first line that has it (lowercased, stripped), or None."""
    for line in text.lower().splitlines():
        if label + ":" in line:
            return line.split(label + ":")[-1].strip()
    return None


def numbered_index(number, item, text):
    """Index of the first line that looks like '<number>. <item>' (also '1)' or '1 -'), or -1."""
    pattern = rf"(^|\s){number}\s*[.):\-]?\s+{re.escape(item)}\s*$"
    for index, line in enumerate(text.lower().splitlines()):
        if re.search(pattern, line.strip()):
            return index
    return -1


def numbered_line(number, item, text):
    """True if some line looks like '<number>. <item>'."""
    return numbered_index(number, item, text) != -1


class TestShopping(unittest.TestCase):
    SCRIPT = "shopping.py"

    def run_with(self, items):
        stdin = f"{len(items)}\n" + "".join(f"{item}\n" for item in items)
        result = run_script(self.SCRIPT, stdin=stdin)
        self.assertEqual(result.returncode, 0,
                         f"{self.SCRIPT} crashed for the items {items}. Error output:\n{result.stderr}")
        return result.stdout

    def test_prints_every_item_numbered_from_1(self):
        out = self.run_with(["milk", "eggs", "bread"])
        for number, item in [(1, "milk"), (2, "eggs"), (3, "bread")]:
            self.assertTrue(numbered_line(number, item, out),
                            f"Expected a line '{number}. {item}' after typing 3 items milk, eggs, bread.\n"
                            f"Your output was:\n{out}")

    def test_numbered_list_keeps_the_order_items_were_typed(self):
        out = self.run_with(["tea", "apples", "rice", "soap"])
        positions = [numbered_index(n, item, out) for n, item in [(1, "tea"), (2, "apples"), (3, "rice"), (4, "soap")]]
        self.assertNotIn(-1, positions,
                         f"Expected the lines '1. tea', '2. apples', '3. rice', '4. soap'.\nYour output was:\n{out}")
        self.assertEqual(positions, sorted(positions),
                         f"Expected the items in the order they were typed: tea, apples, rice, soap.\n"
                         f"Your output was:\n{out}")

    def test_shows_first_and_last_item_and_count(self):
        out = self.run_with(["milk", "eggs", "bread"])
        self.assertEqual(value_after("first item", out), "milk",
                         f"Expected 'First item: milk'.\nYour output was:\n{out}")
        self.assertEqual(value_after("last item", out), "bread",
                         f"Expected 'Last item: bread'.\nYour output was:\n{out}")
        self.assertEqual(value_after("total items", out), "3",
                         f"Expected 'Total items: 3'.\nYour output was:\n{out}")

    def test_one_item_is_both_first_and_last(self):
        out = self.run_with(["coffee"])
        self.assertTrue(numbered_line(1, "coffee", out),
                        f"Expected a line '1. coffee'.\nYour output was:\n{out}")
        self.assertEqual(value_after("first item", out), "coffee",
                         f"Expected 'First item: coffee'.\nYour output was:\n{out}")
        self.assertEqual(value_after("last item", out), "coffee",
                         f"Expected 'Last item: coffee'.\nYour output was:\n{out}")
        self.assertEqual(value_after("total items", out), "1",
                         f"Expected 'Total items: 1'.\nYour output was:\n{out}")

    def test_zero_items_says_the_list_is_empty_without_crashing(self):
        out = self.run_with([])
        self.assertIn("empty", out.lower(),
                      f"With 0 items, expected 'Your list is empty.'.\nYour output was:\n{out}")
        self.assertIsNone(value_after("first item", out),
                          f"With 0 items there is no first item, so don't print 'First item:'.\n"
                          f"Your output was:\n{out}")


class TestTemperatures(unittest.TestCase):
    SCRIPT = "temperatures.py"

    def output(self):
        result = run_script(self.SCRIPT)
        self.assertEqual(result.returncode, 0, f"{self.SCRIPT} crashed. Error output:\n{result.stderr}")
        return result.stdout

    def test_total_of_all_temperatures(self):
        out = self.output()
        self.assertIn(value_after("total", out), ("-28", "-28.0"),
                      f"Expected 'Total: -28' for the list [-4, -2, -7, -1, -5, -3, -6].\nYour output was:\n{out}")

    def test_warmest_is_the_highest_value_even_when_all_are_below_zero(self):
        out = self.output()
        self.assertEqual(value_after("warmest", out), "-1",
                         f"Expected 'Warmest: -1'. Every temperature is below zero, so the warmest can't be 0.\n"
                         f"Your output was:\n{out}")

    def test_average_with_one_decimal(self):
        out = self.output()
        self.assertEqual(value_after("average", out), "-4.0",
                         f"Expected 'Average: -4.0' (total -28 divided by 7 days, 1 decimal).\nYour output was:\n{out}")


if __name__ == "__main__":
    unittest.main()
