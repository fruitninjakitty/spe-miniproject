import unittest
import math
from calculator import (
    calculate_square_root,
    compute_factorial,
    approximate_natural_log,
    exponentiate
)

class TestScientificCalculator(unittest.TestCase):
    """Comprehensive unit tests for calculator functions"""
    
    # Square Root Tests
    def test_square_root_valid(self):
        self.assertAlmostEqual(calculate_square_root(25), 5.0)
        self.assertAlmostEqual(calculate_square_root(0), 0.0)
        self.assertAlmostEqual(calculate_square_root(2.25), 1.5)

    def test_square_root_errors(self):
        self.assertEqual(calculate_square_root(-4), 
                        "Error: Cannot calculate the square root of a negative number.")

    # Factorial Tests
    def test_factorial_valid(self):
        self.assertEqual(compute_factorial(0), 1)
        self.assertEqual(compute_factorial(5), 120)
        self.assertEqual(compute_factorial(7), 5040)

    def test_factorial_errors(self):
        self.assertEqual(compute_factorial(-2), 
                        "Error: Factorial is not defined for negative numbers or non-integers.")
        self.assertEqual(compute_factorial(3.5), 
                        "Error: Factorial is not defined for negative numbers or non-integers.")

    # Natural Log Tests
    def test_natural_log_valid(self):
        self.assertAlmostEqual(approximate_natural_log(math.e), 1.0, delta=0.1)
        self.assertAlmostEqual(approximate_natural_log(1), 0.0, delta=0.01)
        self.assertAlmostEqual(approximate_natural_log(10), math.log(10), delta=0.1)

    def test_natural_log_errors(self):
        self.assertEqual(approximate_natural_log(0), 
                        "Error: Natural logarithm requires positive numbers.")
        self.assertEqual(approximate_natural_log(-2.5), 
                        "Error: Natural logarithm requires positive numbers.")

    # Power Function Tests
    def test_exponentiate_normal_cases(self):
        self.assertAlmostEqual(exponentiate(2, 3), 8.0)
        self.assertAlmostEqual(exponentiate(3, -2), 1/9)
        self.assertAlmostEqual(exponentiate(5, 0), 1.0)
        self.assertAlmostEqual(exponentiate(2.5, 2), 6.25)

    def test_exponentiate_edge_cases(self):
        self.assertAlmostEqual(exponentiate(0, 5), 0.0)
        self.assertAlmostEqual(exponentiate(1, 100), 1.0)
        
    def test_exponentiate_errors(self):
        with self.assertRaises(ZeroDivisionError):
            exponentiate(0, -3)
        
        # Test very large exponent computation
        large_result = exponentiate(2, 100)
        self.assertEqual(large_result, 2**100)

if __name__ == "__main__":
    unittest.main()

#testing webhooks

