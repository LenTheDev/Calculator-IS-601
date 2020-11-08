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

        if __name__ == '__main__':
            unittest.main()
