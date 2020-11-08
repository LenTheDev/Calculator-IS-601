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

        if __name__ == '__main__':
            unittest.main()
