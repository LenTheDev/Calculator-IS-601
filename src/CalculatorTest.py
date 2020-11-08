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

    def test_instantiate_parser(self):
        self.assertIsInstance(self.datafile, CsvReader)

    # Test for the result property
    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    # Test for the result of addition
    def test_add_method_calculator(self):
        test_data = CsvReader('/Csv-Files/TestAddition.csv')
        csv_data = self.testData.csv(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.subtraction(row['Value 1'], row['Value 2']), int(row['Result']))
            csv_data.clear()

    # Test for the result of subtraction
    def test_subtract_method_calculator(self):
        test_data = CsvReader('/Csv-Files/TestSubtraction.csv')
        csv_data = self.testData.csv(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.subtraction(row['Value 1'], row['Value 2']), int(row['Result']))
            csv_data.clear()

    # Test for the result of multiplication
    def test_multiply_method_calculator(self):
        test_data = CsvReader('/Csv-Files/TestMultiplication.csv')
        csv_data = self.testData.csv(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.subtraction(row['Value 1'], row['Value 2']), int(row['Result']))
            csv_data.clear()

    # Test for the result of division
    def test_divide_method_calculator(self):
        test_data = CsvReader('/Csv-Files/TestDivision.csv')
        csv_data = self.testData.csv(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.subtraction(row['Value 1'], row['Value 2']),  int(row['Result']))
            csv_data.clear()

    # Test for the result of a squared number
    def test_squared_method_calculator(self):
        test_data = CsvReader('/Csv-Files/TestSquare.csv')
        csv_data = self.testData.csv(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.subtraction(row['Value 1'], row['Value 2']), int(row['Result']))
            csv_data.clear()

    # Test for the result of a square root
    def test_squareRoot_method_calculator(self):
        test_data = CsvReader('/Csv-Files/TestSquareRoot.csv')
        csv_data = self.testData.csv(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.subtraction(row['Value 1'], row['Value 2']),  int(row['Result']))
            csv_data.clear()

        if __name__ == '__main__':
            unittest.main()
