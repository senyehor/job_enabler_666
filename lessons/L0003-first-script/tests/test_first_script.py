import re
import unittest

from lessonkit import WORK, run_script


def output_lines(result):
    """Non-empty output lines, stripped and lower-cased."""
    return [line.strip().lower() for line in result.stdout.splitlines() if line.strip()]


def comment_lines(name):
    path = WORK / name
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    return [line.strip().lower() for line in text.splitlines() if line.strip().startswith("#")]


class TestHello(unittest.TestCase):
    def setUp(self):
        self.assertTrue((WORK / "hello.py").exists(), "Expected a file work/hello.py")
        self.result = run_script("hello.py")
        self.lines = output_lines(self.result)

    def test_hello_runs_without_errors(self):
        self.assertEqual(self.result.returncode, 0,
                         f"hello.py crashed. Python said:\n{self.result.stderr}")

    def test_hello_first_line_is_hello_world(self):
        self.assertTrue(self.lines, "hello.py printed nothing. Did you use print(...)?")
        self.assertIn("hello, world", self.lines[0],
                      f"Expected the first line to be 'Hello, world!', got: {self.lines[0]!r}")

    def test_hello_says_your_name(self):
        self.assertTrue(any("my name is" in line for line in self.lines),
                        "Expected a line like 'My name is Yehor.'")

    def test_hello_prints_a_box_around_python_rocks(self):
        borders = [line for line in self.lines
                   if line.startswith("+") and line.endswith("+") and "-" in line]
        self.assertGreaterEqual(len(borders), 2,
                                "Expected a top and bottom border line like +---------------+")
        middle = [line for line in self.lines
                  if line.startswith("|") and line.endswith("|") and "python rocks" in line]
        self.assertTrue(middle, "Expected a middle line like | Python rocks! |")

    def test_hello_last_line_is_goodbye(self):
        self.assertTrue(self.lines, "hello.py printed nothing.")
        self.assertIn("goodbye", self.lines[-1],
                      f"Expected the last line to be 'Goodbye!', got: {self.lines[-1]!r}")


class TestBroken(unittest.TestCase):
    EXPECTED = ["shopping list", "-------------", "1. bread", "2. milk", "3. apples", "done!"]

    def setUp(self):
        self.assertTrue((WORK / "broken.py").exists(), "Expected a file work/broken.py")
        self.result = run_script("broken.py")

    def test_broken_runs_without_errors_after_fixing(self):
        self.assertEqual(self.result.returncode, 0,
                         f"broken.py still crashes. Python said:\n{self.result.stderr}")

    def test_broken_prints_the_whole_list_in_order(self):
        lines = output_lines(self.result)
        self.assertEqual(lines, self.EXPECTED,
                         "Expected these 6 lines, in this order:\n" + "\n".join(self.EXPECTED))

    def test_broken_has_comments_naming_both_errors_and_their_lines(self):
        comments = comment_lines("broken.py")
        for error in ("syntaxerror", "nameerror"):
            matching = [c for c in comments if error in c]
            self.assertTrue(matching,
                            f"Expected a comment (a line starting with #) that names the {error}")
            self.assertTrue(any(re.search(r"\d", c) for c in matching),
                            f"Expected the comment about the {error} to include its line number")


if __name__ == "__main__":
    unittest.main()
