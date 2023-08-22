
import unittest
from string_multiplication import string_multiply  

class TestStringMultiply(unittest.TestCase):

    def test_basic_cases(self):
        # Basic cases
        self.assertEqual(string_multiply("2", "3"), "6")
        self.assertEqual(string_multiply("123", "456"), "56088")
    
    def test_with_zeros(self):
        # Cases involving zeros
        self.assertEqual(string_multiply("123", "0"), "0")
        self.assertEqual(string_multiply("0", "456"), "0")
        self.assertEqual(string_multiply("0", "0"), "0")

    def test_large_numbers(self):
        # Test with long strings
        long_num1 = "1234567890123456789012345678901234567890"
        long_num2 = "9876543210987654321098765432109876543210"
        expected_result = "12193263113702179522618503273386678859448712086533622923332237463801111263526900"
        self.assertEqual(string_multiply(long_num1, long_num2), expected_result)

if __name__ == '__main__':
    unittest.main()