"""Tests for L0007: calculator.py predicts operator results and computes workout stats."""
import unittest

from lessonkit import WORK, run_script

SCRIPT = "calculator.py"


def normalise(text):
    """Lower-case and drop all spaces, so '7 / 2 =  3.5' and '7/2=3.5' match."""
    return "".join(text.split()).lower()


class TestArithmetic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_script(SCRIPT)
        cls.lines = [normalise(line) for line in cls.result.stdout.splitlines()]
        source = (WORK / SCRIPT).read_text(encoding="utf-8")
        cls.source = source
        cls.code = "\n".join(line.split("#")[0] for line in source.splitlines())

    def find_line(self, *pieces):
        for line in self.lines:
            if all(normalise(p) in line for p in pieces):
                return line
        return None

    def assert_line(self, *pieces, why=""):
        self.assertIsNotNone(
            self.find_line(*pieces),
            f"Expected a line in the output of {SCRIPT} containing: {'  and  '.join(pieces)}. {why}\n"
            f"Your output was:\n{self.result.stdout}")

    def test_script_runs_without_crashing(self):
        self.assertEqual(self.result.returncode, 0,
                         f"{SCRIPT} crashed. Error output:\n{self.result.stderr}")

    def test_prints_precedence_expressions_with_results(self):
        self.assert_line("2 + 3 * 4 = 14", why="Print it like print(\"2 + 3 * 4 =\", 2 + 3 * 4).")
        self.assert_line("(2 + 3) * 4 = 20")
        self.assert_line("20 - 10 - 5 = 5")
        self.assert_line("2 ** 3 ** 2 = 512")

    def test_prints_division_results_with_right_types(self):
        self.assert_line("7 / 2 = 3.5")
        self.assert_line("7 // 2 = 3")
        self.assert_line("7 % 2 = 1")
        self.assert_line("6 / 2 = 3.0", why="Let Python compute 6 / 2; don't type the answer.")

    def test_workout_time_in_hours_minutes_seconds(self):
        line = self.find_line("workout time")
        self.assertIsNotNone(line, f"Expected a line starting with 'Workout time:'.\n"
                                   f"Your output was:\n{self.result.stdout}")
        self.assertIn("2h44min36s", line,
                      "Expected 'Workout time: 2 h 44 min 36 s'. Check: hours * 3600 + minutes * 60 "
                      "+ seconds should give back 9876, and minutes and seconds must be under 60.")

    def test_average_distance_with_slash_and_floor_division(self):
        self.assert_line("average distance", "6.5",
                         why="The average of 7, 4, 9 and 6 is 6.5. Did you put brackets around the sum?")
        line = self.find_line("whole km average")
        self.assertIsNotNone(line, f"Expected a line starting with 'Whole km average:'.\n"
                                   f"Your output was:\n{self.result.stdout}")
        value = line.split(":")[-1].replace("km", "")
        self.assertIn(value, ("6", "6.0"),
                      f"Expected 'Whole km average: 6' (the same sum, but with //). Got: {line}")

    def test_points_double_every_week(self):
        self.assert_line("points after 10 weeks", "51200",
                         why="50 points doubling for 10 weeks is 50 * 2 ** 10.")

    def test_results_are_computed_not_typed_in(self):
        self.assertIn("9876", self.code, "Expected total_seconds = 9876 in calculator.py.")
        for op in ("//", "%", "**"):
            self.assertIn(op, self.code, f"Expected calculator.py to use the {op} operator.")
        for answer in ("51200", "6.5", "44"):
            self.assertNotIn(answer, self.code,
                             f"{answer} appears in your code (outside comments). Compute it from "
                             f"the variables instead of typing the answer in.")
        self.assertGreaterEqual(self.source.lower().count("predict"), 8,
                                "Expected a '# predict:' comment above each of the 8 Part 1 prints.")


if __name__ == "__main__":
    unittest.main()
