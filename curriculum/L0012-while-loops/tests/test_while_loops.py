import re
import subprocess
import unittest

from lessonkit import WORK, run_script


def run(name, stdin=""):
    """Run a script; a loop that never ends becomes a clear test failure instead of a hang."""
    try:
        return run_script(name, stdin=stdin, timeout=5)
    except subprocess.TimeoutExpired:
        raise AssertionError(f"{name} was still running after 5 seconds. Is there a loop that never ends?") from None


def numbers_in(text):
    return [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", text)]


class TestCountdown(unittest.TestCase):
    def test_counts_down_from_the_start_number_to_1(self):
        result = run("countdown.py", "5\n")
        found = [int(n) for n in numbers_in(result.stdout)]
        self.assertEqual(found, [5, 4, 3, 2, 1],
                         f"Starting from 5, expected the numbers 5 4 3 2 1 in that order (and no 0).\n"
                         f"Your output was:\n{result.stdout}{result.stderr}")

    def test_prints_liftoff_after_the_countdown(self):
        result = run("countdown.py", "3\n")
        out = result.stdout.lower()
        self.assertIn("liftoff", out, f"Expected 'Liftoff!' at the end. Your output was:\n{result.stdout}{result.stderr}")
        self.assertGreater(out.rfind("liftoff"), out.rfind("1"),
                           "'Liftoff!' should come after the last number, not before it.")

    def test_rejects_a_start_number_below_1(self):
        result = run("countdown.py", "0\n")
        out = result.stdout.lower()
        self.assertIn("1 or more", out,
                      f"For 0, expected the message 'Please enter a number of 1 or more.'. Your output was:\n{result.stdout}{result.stderr}")
        self.assertNotIn("liftoff", out, "For 0, the program should not print 'Liftoff!'.")


class TestSavings(unittest.TestCase):
    def check_years(self, stdin, years, balance):
        result = run("savings.py", stdin)
        out = result.stdout + result.stderr
        found = numbers_in(result.stdout)
        self.assertIn(years, found, f"Expected {years} years for input {stdin.split()}. Your output was:\n{out}")
        self.assertIn(balance, result.stdout, f"Expected the final balance {balance}. Your output was:\n{out}")

    def test_counts_the_years_until_the_goal_is_reached(self):
        self.check_years("200\n10\n300\n", 5, "322.10")

    def test_goal_already_reached_takes_0_years(self):
        self.check_years("1000\n4\n600\n", 0, "1000.00")

    def test_zero_rate_says_never_instead_of_looping_forever(self):
        result = run("savings.py", "800\n0\n1000\n")
        self.assertIn("never", result.stdout.lower(),
                      f"With a 0% rate the goal can't be reached; expected "
                      f"'You will never reach your goal with that rate.'. Your output was:\n{result.stdout}{result.stderr}")


class TestFixLoop(unittest.TestCase):
    def test_fixed_loop_ends_and_prints_total_15(self):
        result = run("fix_loop.py")
        self.assertIn("total: 15", result.stdout.lower().replace("  ", " "),
                      f"Expected 'Total: 15'. Your output was:\n{result.stdout}{result.stderr}")

    def test_has_a_comment_explaining_the_bug(self):
        lines = (WORK / "fix_loop.py").read_text(encoding="utf-8").splitlines()
        comments = [line for line in lines if line.strip().startswith("#") and "L0012 part 3" not in line]
        self.assertTrue(comments, "Add a comment (a line starting with #) explaining why the original loop never ended.")
        self.assertIn("while", "\n".join(lines), "fix_loop.py should still use the while loop.")


if __name__ == "__main__":
    unittest.main()
