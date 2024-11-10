import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, f"Value {rand_num} is out of range!")

    def test_function_B(self):
        # Test if the operator returned is one of the valid operators: '+', '-', or '*'
        for _ in range(1000):  # Test many times to ensure randomness
            operator = function_B()
            self.assertIn(operator, ['+', '-', '*'], f"Invalid operator returned: {operator}")

    def test_function_C(self):
        # Test for different operators to ensure correct calculation
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (3, 3, '+', '3 + 3', 6),
            (7, 4, '-', '7 - 4', 3),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = function_C(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
