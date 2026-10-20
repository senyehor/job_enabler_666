import re
import unittest

from lessonkit import WORK, run_script

ROW = re.compile(r"(-?\d+)[x*×](\d+)=(-?\d+)")


def run(script, stdin):
    return run_script(script, stdin=stdin)


def check_ran(test, result, script, stdin):
    test.assertEqual(result.returncode, 0,
                     f"{script} crashed when the input was {stdin.strip()!r}. The error was:\n{result.stderr}")
    test.assertTrue(result.stdout.strip(), f"{script} printed nothing when the input was {stdin.strip()!r}")


def table_rows(output):
    """(number, multiplier, result) for each line that looks like '7 x 3 = 21', ignoring spaces and case."""
    rows = []
    for line in output.splitlines():
        match = ROW.search(line.replace(" ", "").lower())
        if match:
            rows.append(tuple(int(part) for part in match.groups()))
    return rows


class TimesTableTest(unittest.TestCase):
    def table_for(self, number):
        stdin = f"{number}\n"
        result = run("times_table.py", stdin)
        check_ran(self, result, "times_table.py", stdin)
        rows = table_rows(result.stdout)
        self.assertTrue(rows, f"expected rows like '{number} x 1 = {number}' but found none.\n"
                              f"Output was:\n{result.stdout}")
        return rows, result.stdout

    def test_table_has_first_row_1_and_last_row_10(self):
        rows, output = self.table_for(7)
        self.assertEqual(rows[0], (7, 1, 7), f"the first row should be '7 x 1 = 7'.\nOutput was:\n{output}")
        self.assertEqual(rows[-1], (7, 10, 70), f"the last row should be '7 x 10 = 70'. If it stops at 9, "
                                                f"remember range stops before its stop value.\nOutput was:\n{output}")

    def test_table_has_exactly_ten_rows_from_1_to_10(self):
        rows, output = self.table_for(7)
        multipliers = [row[1] for row in rows]
        self.assertEqual(multipliers, list(range(1, 11)),
                         f"expected exactly 10 rows, x 1 to x 10 in order (no x 0, no x 11).\nOutput was:\n{output}")

    def test_table_results_are_correct_for_another_number(self):
        rows, output = self.table_for(12)
        expected = [(12, m, 12 * m) for m in range(1, 11)]
        self.assertEqual(rows, expected,
                         f"for 12 the rows should go from '12 x 1 = 12' to '12 x 10 = 120', each result being "
                         f"the number times the multiplier.\nOutput was:\n{output}")


class VowelsTest(unittest.TestCase):
    def vowel_count(self, word):
        stdin = f"{word}\n"
        result = run("vowels.py", stdin)
        check_ran(self, result, "vowels.py", stdin)
        match = re.search(r"vowels\s*:\s*(\d+)", result.stdout.lower())
        self.assertIsNotNone(match, f"expected a line like 'Vowels: 3' for the word {word!r}.\n"
                                    f"Output was:\n{result.stdout}")
        return int(match.group(1))

    def test_counts_every_vowel_in_a_word(self):
        self.assertEqual(self.vowel_count("banana"), 3, "banana has 3 vowels (a, a, a), so expected 'Vowels: 3'")
        self.assertEqual(self.vowel_count("education"), 5, "education has 5 vowels (e, u, a, i, o)")
        self.assertEqual(self.vowel_count("queue"), 4, "queue has 4 vowels (u, e, u, e), so expected 'Vowels: 4'")

    def test_word_without_vowels_gives_zero(self):
        self.assertEqual(self.vowel_count("rhythm"), 0,
                         "rhythm has no a, e, i, o or u, so expected 'Vowels: 0' (set the count before the loop)")


class CountdownForTest(unittest.TestCase):
    def countdown(self, start):
        stdin = f"{start}\n"
        result = run("countdown_for.py", stdin)
        check_ran(self, result, "countdown_for.py", stdin)
        numbers = []
        liftoff_after = None
        for line in result.stdout.splitlines():
            if "liftoff" in line.lower():
                liftoff_after = len(numbers)
            match = re.search(r"(-?\d+)\s*$", line)
            if match:
                numbers.append(int(match.group(1)))
        return numbers, liftoff_after, result.stdout

    def test_counts_down_to_1_then_liftoff(self):
        numbers, liftoff_after, output = self.countdown(5)
        self.assertEqual(numbers, [5, 4, 3, 2, 1],
                         f"starting from 5, expected 5, 4, 3, 2, 1 on separate lines (no 0).\nOutput was:\n{output}")
        self.assertIsNotNone(liftoff_after, f"expected 'Liftoff!' after the countdown.\nOutput was:\n{output}")
        self.assertEqual(liftoff_after, len(numbers), f"'Liftoff!' should come after the last number, 1.\n"
                                                      f"Output was:\n{output}")

    def test_countdown_from_1_prints_just_1(self):
        numbers, liftoff_after, output = self.countdown(1)
        self.assertEqual(numbers, [1], f"starting from 1, expected just 1 and then Liftoff!.\nOutput was:\n{output}")
        self.assertIsNotNone(liftoff_after, f"expected 'Liftoff!' after the countdown.\nOutput was:\n{output}")

    def test_has_comment_about_when_while_fits_better(self):
        source = (WORK / "countdown_for.py").read_text(encoding="utf-8")
        comments = [line for line in source.splitlines() if line.strip().startswith("#")]
        self.assertTrue(any("while" in line.lower() for line in comments),
                        "countdown_for.py needs a comment (a line starting with #) saying when a while loop "
                        "fits better than a for loop")


if __name__ == "__main__":
    unittest.main()
