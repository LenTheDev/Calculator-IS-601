import unittest
from Calculator import Calculator

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    # Test for the constructor
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    # Test for the result property
    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    # Test for the result of addition
    def test_add_method_calculator(self):
        self.assertEqual(calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 6)

    # Test for the result of subtraction
    def test_subtract_method_calculator(self):
        self.assertEqual(calculator.subtract(10, 7), 3)
        self.assertEqual(self.calculator.result, 3)

    # Test for the result of multiplication
    def test_multiply_method_calculator(self):
        self.assertEqual(calculator.multiplication(10, 5), 50)
        self.assertEqual(self.calculator.result, 50)

    # Test for the result of division
    def test_divide_method_calculator(self):
        self.assertEqual(calculator.division(100, 10), 10)
        self.assertEqual(self.calculator.result, 10)

    # Test for the result of a squared number
    def test_squared_method_calculator(self):
        self.assertEqual(calculator.squared(2, 3), 9)
        self.assertEqual(self.calculator.result, 9)

    # Test for the result of a square root
    def test_squareRoot_method_calculator(self):
        self.assertEqual(calculator.square_root(144), 12)
        self.assertEqual(self.calculator.result, 12)

        if __name__ == '__main__':
            unittest.main()
