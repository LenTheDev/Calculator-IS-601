import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()
        self.testData = CsvReader()

    # Test for the constructor
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    # Test for the Csv Reader
    def test_instantiate_parser(self):
        self.assertIsInstance(self.testData, CsvReader)

    # Test for the result property
    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    # Test for the result of addition
    def test_add_method_calculator(self):
        data_path = 'Addition.csv'
        csv_data = self.testData.csv(data_path)
        for row in csv_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
        csv_data.clear()

    # Test for the result of subtraction
    def test_subtract_method_calculator(self):
        data_path = 'Subtraction.csv'
        csv_data = self.testData.csv(data_path)
        for row in csv_data:
            self.assertEqual(self.calculator.subtraction(row['Value 1'], row['Value 2']), int(row['Result']))
        csv_data.clear()

    # Test for the result of multiplication
    def test_multiply_method_calculator(self):
        data_path = 'Multiplication.csv'
        csv_data = self.testData.csv(data_path)
        for row in csv_data:
            self.assertEqual(self.calculator.multiplication(row['Value 1'], row['Value 2']), float(row['Result']))
        csv_data.clear()

    # Test for the result of division
    def test_divide_method_calculator(self):
        data_path = 'Division.csv'
        csv_data = self.testData.csv(data_path)
        for row in csv_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
        csv_data.clear()

    # Test for the result of a squared number
    def test_squared_method_calculator(self):
        data_path = 'Square.csv'
        csv_data = self.testData.csv(data_path)
        for row in csv_data:
            self.assertEqual(self.calculator.squared(row['Value 1']), int(row['Result']))
            csv_data.clear()

    # Test for the result of a square root
    def test_squareRoot_method_calculator(self):
        data_path = 'SquareRoot.csv'
        csv_data = self.testData.csv(data_path)
        for row in csv_data:
            self.assertEqual(self.calculator.square_root(row['Value 1']), float(row['Result']))
            csv_data.clear()


if __name__ == '__main__':
    unittest.main()
