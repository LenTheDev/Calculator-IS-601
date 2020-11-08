import unittest
from Calculator import Calculator

class MyTestCase(unittest.TestCase):
    # Test for the constructor
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    # Test for the result property
    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 4)

    # Test for the result of addition
    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 2), 4)
        self.assertEqual(calculator.result, 6)

        if __name__ == '__main__':
            unittest.main()
