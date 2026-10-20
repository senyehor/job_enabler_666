"""Tests for L0011: ticket_price.py picks a ticket category and price from age and student answer."""
import unittest

from lessonkit import run_script

SCRIPT = "ticket_price.py"


def run(age, student):
    """Run the script with the two answers. Returns (result, category, price) from the output."""
    result = run_script(SCRIPT, stdin=f"{age}\n{student}\n")
    category = price = None
    # Prompts and answers can share a line with the output, so look for the labels anywhere.
    text = result.stdout.lower()
    for line in text.splitlines():
        if "category:" in line:
            category = line.split("category:")[-1].strip()
        if "price:" in line:
            price = line.split("price:")[-1].strip().replace("eur", "").replace("€", "").strip()
    return result, category, price


class TestTicketPrice(unittest.TestCase):
    def check(self, age, student, want_category, want_price):
        result, category, price = run(age, student)
        case = f"age {age}, student answer '{student}'"
        self.assertEqual(result.returncode, 0,
                         f"{SCRIPT} crashed for {case}. Error output:\n{result.stderr}")
        self.assertIsNotNone(category, f"For {case}: expected a line 'Category: {want_category}'.\n"
                                       f"Your output was:\n{result.stdout}")
        self.assertIsNotNone(price, f"For {case}: expected a line 'Price: {want_price}'.\n"
                                    f"Your output was:\n{result.stdout}")
        self.assertIn(want_category, category,
                      f"For {case}: expected 'Category: {want_category}', got 'Category: {category}'.")
        self.assertIn(price, (str(want_price), f"{want_price}.0"),
                      f"For {case}: expected 'Price: {want_price}', got 'Price: {price}'.")

    def test_children_under_six_go_free(self):
        self.check(0, "n", "free", 0)
        self.check(5, "y", "free", 0)

    def test_ages_six_to_seventeen_pay_child_price(self):
        self.check(6, "n", "child", 5)
        self.check(17, "y", "child", 5)

    def test_students_aged_18_to_25_get_student_price(self):
        self.check(18, "y", "student", 8)
        self.check(25, "y", "student", 8)

    def test_capital_y_also_counts_as_student(self):
        self.check(21, "Y", "student", 8)

    def test_non_students_and_older_students_pay_adult_price(self):
        self.check(18, "n", "adult", 12)
        self.check(26, "y", "adult", 12)
        self.check(64, "n", "adult", 12)

    def test_age_65_and_over_pays_senior_price(self):
        self.check(65, "n", "senior", 6)
        self.check(80, "y", "senior", 6)

    def test_negative_age_says_invalid_and_prints_no_price(self):
        result, category, price = run(-4, "n")
        self.assertEqual(result.returncode, 0,
                         f"{SCRIPT} crashed for age -4. Error output:\n{result.stderr}")
        self.assertIn("invalid age", result.stdout.lower(),
                      f"For age -4: expected a line containing 'Invalid age'.\n"
                      f"Your output was:\n{result.stdout}")
        self.assertIsNone(price, f"For age -4: expected no 'Price:' line, because the age makes no sense.\n"
                                 f"Your output was:\n{result.stdout}")
        self.assertIsNone(category, f"For age -4: expected no 'Category:' line.\n"
                                    f"Your output was:\n{result.stdout}")


if __name__ == "__main__":
    unittest.main()
