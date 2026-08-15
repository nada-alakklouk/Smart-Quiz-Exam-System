"""
Unit tests module for Smart Quiz & Exam System.
Uses Python standard unittest library to test core business logic.
"""
import unittest


from Authentication import validate
from quiz import check_answer, calculate_score


class TestSmartQuizSystem(unittest.TestCase):

    # -------------------------------------------------------------
    # 1. Login Validation Tests
    # -------------------------------------------------------------
    def test_login_validation_success(self):
        """Test valid credentials pass authentication."""
        users = {"admin": "admin123", "student": "pass123"}
        self.assertTrue(validate("admin", "admin123", users))
        self.assertTrue(validate("ADMIN", "admin123", users))  # Case-insensitive username
        self.assertTrue(validate(" student ", "pass123", users))  # Space trim

    def test_login_validation_failure(self):
        """Test invalid credentials fail authentication."""
        users = {"admin": "admin123"}
        self.assertFalse(validate("admin", "wrongpass", users))
        self.assertFalse(validate("nonexistent", "admin123", users))

    # -------------------------------------------------------------
    # 2. Answer Validation Tests (Challenge 2 & 3)
    # -------------------------------------------------------------
    def test_check_answer_exact_match(self):
        """Test exact uppercase answer match."""
        self.assertTrue(check_answer("A", "A"))
        self.assertTrue(check_answer("B", "B"))

    def test_check_answer_case_insensitive(self):
        """Test lowercase input matches uppercase answer (Challenge 2)."""
        self.assertTrue(check_answer("a", "A"))
        self.assertTrue(check_answer("b", "B"))

    def test_check_answer_space_tolerant(self):
        """Test answer checking ignores leading/trailing spaces (Challenge 3)."""
        self.assertTrue(check_answer(" A ", "A"))
        self.assertTrue(check_answer("  b  ", "B"))

    def test_check_answer_incorrect(self):
        """Test wrong answer identification."""
        self.assertFalse(check_answer("A", "B"))
        self.assertFalse(check_answer("C", "A"))

    # -------------------------------------------------------------
    # 3. Score & Percentage Calculation Tests
    # -------------------------------------------------------------
    def test_calculate_score_full_marks(self):
        """Test 100% score calculation."""
        res = calculate_score(5, 5)
        self.assertEqual(res["score"], 5.0)
        self.assertEqual(res["percentage"], 100.0)
        self.assertEqual(res["status"], "PASSED")
        self.assertEqual(res["wrong"], 0)

    def test_calculate_score_partial_pass(self):
        """Test passing score calculation (>=50%)."""
        res = calculate_score(3, 5)
        self.assertEqual(res["score"], 3.0)
        self.assertEqual(res["percentage"], 60.0)
        self.assertEqual(res["status"], "PASSED")
        self.assertEqual(res["wrong"], 2)

    def test_calculate_score_fail(self):
        """Test failing score calculation (<50%)."""
        res = calculate_score(1, 5)
        self.assertEqual(res["score"], 1.0)
        self.assertEqual(res["percentage"], 20.0)
        self.assertEqual(res["status"], "FAILED")
        self.assertEqual(res["wrong"], 4)

    def test_calculate_score_zero_total(self):
        """Test zero total questions edge case."""
        res = calculate_score(0, 0)
        self.assertEqual(res["percentage"], 0.0)
        self.assertEqual(res["status"], "N/A")

    # -------------------------------------------------------------
    # 4. Search Functionality Logic Tests
    # -------------------------------------------------------------
    def test_search_by_id(self):
        """Test searching questions by unique ID."""
        sample_questions = [
            {"id": 1, "question": "What is Python?", "difficulty": "Easy"},
            {"id": 2, "question": "What is Django?", "difficulty": "Medium"},
        ]
        found = [q for q in sample_questions if q["id"] == 1]
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]["question"], "What is Python?")

    def test_search_by_keyword(self):
        """Test keyword searching in question text."""
        sample_questions = [
            {"id": 1, "question": "What is Python?", "difficulty": "Easy"},
            {"id": 2, "question": "What is Django?", "difficulty": "Medium"},
        ]
        found = [q for q in sample_questions if "python" in q["question"].lower()]
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]["id"], 1)

if __name__ == "__main__":
    unittest.main()
