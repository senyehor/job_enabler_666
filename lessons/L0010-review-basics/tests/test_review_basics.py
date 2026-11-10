"""Tests for L0010: trace.txt has hand-traced final values; unit_converter.py reads input and converts metres."""
import re
import unittest

from lessonkit import WORK, run_script

TRACE = "trace.txt"
SCRIPT = "unit_converter.py"


def normalise(line):
    """Lower-case and drop all spaces, so 'Miles:  7.67' and 'miles:7.67' match."""
    return "".join(line.split()).lower()


def final_values(script_letter):
    """Find the line 'A final: x = 1, y = 2' in trace.txt and return {'x': '1', 'y': '2'}."""
    path = WORK / TRACE
    if not path.is_file():
        return None
    prefix = f"{script_letter.lower()}final:"
    for line in path.read_text(encoding="utf-8").splitlines():
        clean = normalise(line).replace('"', "").replace("'", "")
        if clean.startswith(prefix):
            values = {}
            for part in clean[len(prefix):].split(","):
                if "=" in part:
                    name, value = part.split("=", 1)
                    values[name] = value
            return values
    return None


class TestTrace(unittest.TestCase):
    def check_final(self, letter, expected, why):
        found = final_values(letter)
        self.assertIsNotNone(
            found, f"Expected a line starting with `{letter} final:` in {TRACE}, like `{letter} final: x = 1, y = 2`.")
        for name, value in expected.items():
            self.assertEqual(
                found.get(name), value,
                f"In `{letter} final:` expected {name} = {value}, but found {found.get(name)}. {why}")

    def test_trace_a_integer_division_and_reassignment(self):
        self.check_final("A", {"total": "205", "minutes": "4", "seconds": "5", "text": "5s"},
                         "Line 4 changes total; line 5 uses that new total and the old minutes.")

    def test_trace_b_slicing_and_float_division(self):
        self.check_final("B", {"word": "lat", "n": "3.0", "part": "la"},
                         "A slice stops before the end index, and / always gives a float.")

    def test_trace_has_line_by_line_values(self):
        path = WORK / TRACE
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        lines = [l for l in text.splitlines() if normalise(l).startswith("line") and "=" in l]
        self.assertGreaterEqual(
            len(lines), 11,
            f"Expected a `line N: ...` entry for every assignment in scripts A and B "
            f"(11 in total), found {len(lines)}.")


class ConverterRun:
    """Runs the converter once with the given answers and finds labelled lines in the output."""

    def __init__(self, first, last, metres):
        self.stdin = f"{first}\n{last}\n{metres}\n"
        self.result = run_script(SCRIPT, stdin=self.stdin)
        self.lines = [normalise(l) for l in self.result.stdout.splitlines()]

    def line_with(self, label):
        label = normalise(label)
        found = None
        for line in self.lines:
            if line.startswith(label):
                found = line[len(label):]
        return found


class TestConverter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mara = ConverterRun("Mara", "Lind", 12345)
        cls.oskar = ConverterRun("Oskar", "Berg", 5007)

    def check_ran(self, run):
        self.assertEqual(run.result.returncode, 0,
                         f"{SCRIPT} crashed with input {run.stdin!r}. Error output:\n{run.result.stderr}")

    def check_label(self, run, label, pattern, expected):
        self.check_ran(run)
        rest = run.line_with(label)
        self.assertIsNotNone(rest, f"Expected a line starting with `{label}`.\nYour output was:\n{run.result.stdout}")
        self.assertRegex(rest, pattern,
                         f"Expected `{label} {expected}` for input {run.stdin!r}.\nYour output was:\n{run.result.stdout}")

    def test_greets_with_full_name(self):
        for run, name in [(self.mara, "Mara Lind"), (self.oskar, "Oskar Berg")]:
            self.check_ran(run)
            self.assertIn(name.lower(), run.result.stdout.lower(),
                          f"Expected a greeting like `Hello, {name}!`.\nYour output was:\n{run.result.stdout}")

    def test_prints_metres_and_kilometres(self):
        self.check_label(self.mara, "Metres:", r"^12345(m|metres)?$", "12345")
        self.check_label(self.mara, "Kilometres:", r"^12\.345(km|kilometres)?$", "12.345")
        self.check_label(self.oskar, "Kilometres:", r"^5\.007(km|kilometres)?$", "5.007")

    def test_miles_rounded_to_two_decimals(self):
        self.check_label(self.mara, "Miles:", r"^7\.67(mi|miles)?$", "7.67")
        self.check_label(self.oskar, "Miles:", r"^3\.11(mi|miles)?$", "3.11")

    def test_split_into_whole_km_and_leftover_metres(self):
        self.check_label(self.mara, "Split:", r"^12\D+345\D*$", "12 km 345 m")
        self.check_label(self.oskar, "Split:", r"^5\D+7\D*$", "5 km 7 m")

    def test_badge_has_initials_and_first_three_letters(self):
        self.check_label(self.mara, "Badge:", r"^ml-mar$", "ML-Mar")
        self.check_label(self.oskar, "Badge:", r"^ob-osk$", "OB-Osk")


if __name__ == "__main__":
    unittest.main()
