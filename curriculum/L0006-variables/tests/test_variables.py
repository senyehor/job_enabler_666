"""Tests for L0006: trace.txt holds hand-traced final values; profile.py stores, converts and reassigns variables."""
import re
import unittest

from lessonkit import WORK, run_script

TRACE = "trace.txt"
SCRIPT = "profile.py"


def normalise(line):
    """Lower-case and drop all spaces, so 'Age:  29' and 'age:29' match."""
    return "".join(line.split()).lower()


def final_values(script_letter):
    """Find the line 'A final: x = 10, y = 5' in trace.txt and return {'x': '10', 'y': '5'}."""
    path = WORK / TRACE
    if not path.is_file():
        return None
    for line in path.read_text(encoding="utf-8").splitlines():
        clean = normalise(line).replace('"', "").replace("'", "")
        prefix = f"{script_letter.lower()}final:"
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

    def test_trace_a_copy_keeps_old_value(self):
        self.check_final("A", {"x": "10", "y": "5"},
                         "y = x copies the value x had at that moment.")

    def test_trace_b_naive_swap_loses_a_value(self):
        self.check_final("B", {"a": "blue", "b": "blue"},
                         "Trace line 3 carefully: what does `a` hold when line 4 runs?")

    def test_trace_c_conversion_and_reassignment(self):
        self.check_final("C", {"count": "4", "label": "level4"},
                         "int(\"3\") is 3, plus 1; str(count) turns it back into text to join.")

    def test_trace_has_line_by_line_values(self):
        path = WORK / TRACE
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        lines = [l for l in text.splitlines() if normalise(l).startswith("line") and "=" in l]
        self.assertGreaterEqual(
            len(lines), 12,
            f"Expected a `line N: ...` entry for every assignment in scripts A, B and C "
            f"(12 in total), found {len(lines)}.")


class TestProfile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_script(SCRIPT)
        cls.lines = [normalise(l) for l in cls.result.stdout.splitlines()]

    def index_of(self, expected, start=0):
        target = normalise(expected)
        for i in range(start, len(self.lines)):
            if self.lines[i] == target:
                return i
        return -1

    def test_prints_profile_before_birthday(self):
        self.assertEqual(self.result.returncode, 0,
                         f"{SCRIPT} crashed. Error output:\n{self.result.stderr}")
        for expected in ["Name: Mara Lind", "Age: 29", "Height: 1.68", "Student: True"]:
            self.assertNotEqual(self.index_of(expected), -1,
                                f"Expected the line `{expected}`.\nYour output was:\n{self.result.stdout}")

    def test_age_and_height_are_converted(self):
        self.assertNotEqual(self.index_of("age is <class 'int'>"), -1,
                            "Expected `age is <class 'int'>`. Did you convert age with int()?"
                            f"\nYour output was:\n{self.result.stdout}")
        self.assertNotEqual(self.index_of("height is <class 'float'>"), -1,
                            "Expected `height is <class 'float'>`. Did you convert height with float()?"
                            f"\nYour output was:\n{self.result.stdout}")

    def test_prints_updated_profile_after_birthday(self):
        first = self.index_of("Age: 29")
        self.assertNotEqual(first, -1, "Expected `Age: 29` first, before the birthday.")
        for expected in ["Name: Mara Lind", "Age: 30", "Height: 1.68", "Student: False"]:
            self.assertNotEqual(self.index_of(expected, first + 1), -1,
                                f"Expected `{expected}` after the birthday, below `Age: 29`."
                                f"\nYour output was:\n{self.result.stdout}")

    def test_new_age_is_computed_not_typed(self):
        source = (WORK / SCRIPT).read_text(encoding="utf-8")
        code = "\n".join(l.split("#")[0] for l in source.splitlines())
        self.assertIsNone(re.search(r"\b30\b", code),
                          "Don't type 30 in your code: compute it with age = age + 1.")


if __name__ == "__main__":
    unittest.main()
