"""Tests for L0004: values.py prints values with their type() and converts between types."""
import unittest
from collections import Counter

from lessonkit import WORK, run_script

SCRIPT = "values.py"


def normalise(line):
    """Lower-case and drop all spaces, so '3.5  <class 'float'>' and '3.5 <class 'float'>' match."""
    return "".join(line.split()).lower()


class TestValuesAndTypes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_script(SCRIPT)
        cls.lines = Counter(normalise(line) for line in cls.result.stdout.splitlines())

    def assert_line(self, expected, times=1, why=""):
        found = self.lines[normalise(expected)]
        self.assertGreaterEqual(
            found, times,
            f"Expected the line `{expected}` in the output of {SCRIPT}"
            + (f" at least {times} times" if times > 1 else "")
            + f". {why}\nYour output was:\n{self.result.stdout}")

    def test_script_runs_without_crashing(self):
        self.assertEqual(
            self.result.returncode, 0,
            f"{SCRIPT} crashed. Did you comment out the int(\"abc\") line after running it?\n"
            f"Error output:\n{self.result.stderr}")

    def test_prints_int_values_with_their_type(self):
        self.assert_line("10 <class 'int'>", why="Use print(10, type(10)).")
        self.assert_line("-7 <class 'int'>")

    def test_prints_float_values_with_their_type(self):
        self.assert_line("3.14 <class 'float'>")
        self.assert_line("2.0 <class 'float'>", why="2.0 has a dot, so it is not an int.")

    def test_prints_str_values_with_their_type(self):
        self.assert_line("hello <class 'str'>")
        self.assert_line("10 <class 'str'>", why="\"10\" in quotes is text, not a number.")

    def test_prints_bool_value_with_its_type(self):
        self.assert_line("True <class 'bool'>")

    def test_converts_text_to_numbers(self):
        self.assert_line("42 <class 'int'>", why="This is int(\"42\").")
        self.assert_line("3.5 <class 'float'>", why="This is float(\"3.5\").")

    def test_converts_numbers_to_text_bool_and_float(self):
        self.assert_line("7 <class 'str'>", why="This is str(7).")
        self.assert_line("3 <class 'int'>", why="This is int(3.9): int() cuts off the decimal part.")
        self.assert_line("5.0 <class 'float'>", why="This is float(5).")
        self.assert_line("False <class 'bool'>", why="This is bool(0).")
        self.assert_line("True <class 'bool'>", times=2,
                         why="One True comes from the literal True, one from bool(\"hi\").")

    def test_crashing_line_is_commented_out_with_error_name(self):
        source = (WORK / SCRIPT).read_text(encoding="utf-8")
        commented = [line for line in source.splitlines()
                     if line.strip().startswith("#") and 'int("abc")' in line.replace("'", '"')]
        self.assertTrue(commented,
                        'Expected the line with int("abc") to still be in values.py, commented out with #.')
        self.assertIn("valueerror", source.lower(),
                      "Expected a comment naming the error that int(\"abc\") raised.")


if __name__ == "__main__":
    unittest.main()
