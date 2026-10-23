import re
import unittest

from lessonkit import WORK, run_script

QUIZ = "review/quiz.py"


def quiz_lines(test):
    path = WORK / "review" / "quiz.py"
    test.assertTrue(path.is_file(), "Expected the script at work/review/quiz.py (folder 'review', file 'quiz.py').")
    result = run_script(QUIZ)
    test.assertEqual(result.returncode, 0,
                     "review/quiz.py crashed. It must run without errors. Python said:\n" + result.stderr)
    return [line.strip().lower() for line in result.stdout.splitlines() if line.strip()]


def find_line(lines, value_pattern, type_name):
    """A line that shows the result (as a whole value) and the type, e.g. "... 10 <class 'int'>"."""
    for line in lines:
        if f"<class '{type_name}'>" in line and re.search(value_pattern, line):
            return line
    return None


def answers_text(test):
    path = WORK / "answers.txt"
    test.assertTrue(path.is_file(), "Expected work/answers.txt to exist.")
    return path.read_text(encoding="utf-8")


def section(text, label):
    """The text after e.g. 'Trap 1:' up to the next 'Trap N:' / 'Commands:' / 'Stretch:' label."""
    match = re.search(label + r"\s*:(.*?)(?=(?:trap\s*\d|commands|stretch)\s*:|\Z)", text, re.I | re.S)
    return match.group(1).strip() if match else None


class TestFolders(unittest.TestCase):
    def test_review_and_elsewhere_folders_exist(self):
        self.assertTrue((WORK / "review").is_dir(), "Expected a folder work/review (create it with mkdir).")
        self.assertTrue((WORK / "elsewhere").is_dir(), "Expected a folder work/elsewhere (create it with mkdir).")


class TestQuizOutput(unittest.TestCase):
    def test_prints_one_line_per_quiz_item(self):
        lines = [line for line in quiz_lines(self) if "<class '" in line]
        self.assertGreaterEqual(len(lines), 8,
                                f"Expected at least 8 lines that show a type like <class 'int'>, found {len(lines)}.")

    def test_trap1_text_plus_text_is_glued_str(self):
        lines = quiz_lines(self)
        self.assertIsNotNone(find_line(lines, r"(?<![\d.])55(?![\d.])", "str"),
                             "Expected a line for \"5\" + \"5\" showing 55 and <class 'str'>.")

    def test_trap2_converted_then_added_is_int(self):
        lines = quiz_lines(self)
        self.assertIsNotNone(find_line(lines, r"(?<![\d.])8(?![\d.])", "int"),
                             "Expected a line for int(\"7\") + 1 showing 8 and <class 'int'>.")

    def test_other_items_show_correct_result_and_type(self):
        lines = quiz_lines(self)
        self.assertIsNotNone(find_line(lines, r"(?<![\d.])10(?![\d.])", "int"),
                             "Expected a line for 5 + 5 showing 10 and <class 'int'>.")
        self.assertIsNotNone(find_line(lines, r"(?<![\d.])71(?![\d.])", "str"),
                             "Expected a line for \"7\" + str(1) showing 71 and <class 'str'>.")
        self.assertIsNotNone(find_line(lines, r"(?<![\d.])2\.5(?![\d.])", "float"),
                             "Expected a line for float(\"2.5\") showing 2.5 and <class 'float'>.")
        self.assertIsNotNone(find_line(lines, r"(?<![\d.])9(?![\d.])", "int"),
                             "Expected a line for int(9.99) showing 9 and <class 'int'>.")

    def test_trap3_bool_of_text_false_is_true(self):
        lines = quiz_lines(self)
        bool_lines = [line for line in lines if "<class 'bool'>" in line]
        self.assertTrue(any(re.search(r"\btrue\b", line) for line in bool_lines),
                        "Expected a line for bool(\"False\") showing True and <class 'bool'>.")
        self.assertTrue(any("false" in line and "true" not in line for line in bool_lines),
                        "Expected a line for bool(\"\") showing False and <class 'bool'>.")


class TestAnswers(unittest.TestCase):
    def test_answers_explain_all_three_traps(self):
        text = answers_text(self)
        for n in (1, 2, 3):
            body = section(text, rf"trap\s*{n}")
            self.assertIsNotNone(body, f"Expected a line starting with 'Trap {n}:' in answers.txt.")
            self.assertGreaterEqual(len(body.split()), 5,
                                    f"The explanation after 'Trap {n}:' should be at least a short sentence.")

    def test_answers_list_both_run_commands(self):
        body = section(answers_text(self), "commands")
        self.assertIsNotNone(body, "Expected a line starting with 'Commands:' in answers.txt.")
        body = body.replace("\\", "/").lower()
        self.assertRegex(body, r"\b(python3?|py)\s+(\./)?review/quiz\.py",
                         "Under 'Commands:' expected the command you ran from work/: python review/quiz.py")
        self.assertRegex(body, r"\b(python3?|py)\s+\.\./review/quiz\.py",
                         "Under 'Commands:' expected the command you ran from elsewhere, "
                         "with a path starting with ../ (for example python ../review/quiz.py)")


if __name__ == "__main__":
    unittest.main()
