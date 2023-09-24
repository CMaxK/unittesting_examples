import unittest
from math_functions import add_numbers, factorial

class TestFunctions(unittest.TestCase):
    #Below functions test the add_numbers function
    def test_addition_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_addition_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)

    #Below functions test the factorial function
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive_number(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-2)



if __name__ == '__main__':
    unittest.main()
