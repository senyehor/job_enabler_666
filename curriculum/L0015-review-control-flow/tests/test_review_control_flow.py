"""Tests for L0015: grades.py reads scores until 'done', grades each one and prints a summary."""
import re
import unittest

from lessonkit import run_script

SCRIPT = "grades.py"


def feed(*answers):
    """Turn the answers into stdin, one per line, always ending with 'done'."""
    return "\n".join([str(a) for a in answers] + ["done"]) + "\n"


class GradeRun:
    """Runs grades.py once with the given scores and reads the grades and summary out of its output."""

    def __init__(self, *answers):
        self.stdin = feed(*answers)
        self.result = run_script(SCRIPT, stdin=self.stdin)
        # Remove spaces and lower-case everything, so '85 : B' and '85:b' both read as '85:b'.
        self.clean = "".join(self.result.stdout.split()).lower()

    def grades(self):
        """Return [(score, letter), ...] in the order they were printed, e.g. [('95', 'a'), ('59', 'f')]."""
        found = []
        for line in self.result.stdout.splitlines():
            match = re.search(r"(?<![\d.\-])(\d+):([a-f])\.?$", "".join(line.split()).lower())
            if match:
                found.append((match.group(1), match.group(2)))
        return found

    def number_after(self, label):
        match = re.search(re.escape(label.lower()) + r"(-?\d+(?:\.\d+)?)", self.clean)
        return match.group(1) if match else None

    def passed(self):
        match = re.search(r"passed:(\d+)(?:of|/|outof)(\d+)", self.clean)
        return (match.group(1), match.group(2)) if match else None

    def describe(self):
        return f"Input typed: {self.stdin!r}\nYour output was:\n{self.result.stdout}"


class TestGrades(unittest.TestCase):
    def check_ran(self, run):
        self.assertEqual(run.result.returncode, 0,
                         f"{SCRIPT} crashed.\n{run.describe()}\nError output:\n{run.result.stderr}")

    def check_grades(self, run, expected):
        self.check_ran(run)
        found = run.grades()
        self.assertEqual(
            found, expected,
            f"Expected one `score: letter` line per score, in the order typed: "
            f"{', '.join(s + ': ' + g.upper() for s, g in expected)}.\n{run.describe()}")

    def test_gives_a_letter_grade_for_each_score_in_order(self):
        run = GradeRun(95, 59, 77)
        self.check_grades(run, [("95", "a"), ("59", "f"), ("77", "c")])

    def test_boundary_scores_get_the_right_grade(self):
        run = GradeRun(100, 90, 89, 80, 79, 70, 69, 60, 59, 0)
        self.check_grades(run, [("100", "a"), ("90", "a"), ("89", "b"), ("80", "b"), ("79", "c"),
                                ("70", "c"), ("69", "d"), ("60", "d"), ("59", "f"), ("0", "f")])

    def test_prints_the_average_with_one_decimal(self):
        for scores, expected in [((95, 59, 77), "77.0"), ((80, 69), "74.5"), ((90, 85, 88), "87.7")]:
            run = GradeRun(*scores)
            self.check_ran(run)
            found = run.number_after("Average:")
            self.assertEqual(found, expected,
                             f"Expected `Average: {expected}` (one decimal).\n{run.describe()}")

    def test_counts_how_many_passed_out_of_the_total(self):
        for scores, expected in [((95, 59, 77), ("2", "3")), ((60, 59, 40, 61), ("2", "4")), ((10,), ("0", "1"))]:
            run = GradeRun(*scores)
            self.check_ran(run)
            self.assertEqual(run.passed(), expected,
                             f"Expected `Passed: {expected[0]} of {expected[1]}` (60 or more passes).\n"
                             f"{run.describe()}")

    def test_done_straight_away_prints_a_friendly_message(self):
        run = GradeRun()
        self.check_ran(run)
        self.assertIn("noscoresentered", run.clean,
                      f"Expected `No scores entered.` when the first answer is `done`.\n{run.describe()}")
        self.assertNotIn("average:", run.clean,
                         f"With no scores there is nothing to average, so don't print `Average:`.\n{run.describe()}")

    def test_rejects_scores_outside_0_to_100(self):
        run = GradeRun(80, 150, -5, 101, 69)
        self.check_ran(run)
        self.assertEqual(run.clean.count("0to100"), 3,
                         f"Expected `Scores must be from 0 to 100.` once for each of 150, -5 and 101.\n"
                         f"{run.describe()}")
        self.check_grades(run, [("80", "b"), ("69", "d")])
        self.assertEqual(run.passed(), ("2", "2"),
                         f"Rejected scores must not be counted: expected `Passed: 2 of 2`.\n{run.describe()}")


if __name__ == "__main__":
    unittest.main()
