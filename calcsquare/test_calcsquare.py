import unittest
from area.calcsquare.calcsquare import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_circle(self):
        self.assertEqual(self.calculator.circle(1), 3.141592653589793)

    def test_triangle(self):
        self.assertEqual(self.calculator.triangle(1, 2, 3), 0)


if __name__ == "__main__":
    unittest.main()
