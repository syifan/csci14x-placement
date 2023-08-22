import unittest
from two_sum import two_sum 

class TestTwoSum(unittest.TestCase):

    def test_basic_cases(self):
        # Basic cases
        self.assertEqual(set(two_sum([2, 7, 11, 15], 9)), {0, 1})
        self.assertEqual(set(two_sum([3, 2, 4], 6)), {1, 2})
        self.assertEqual(set(two_sum([3, 3], 6)), {0, 1})

    def test_negative_numbers(self):
        # Case with negative numbers
        self.assertEqual(set(two_sum([-1, -2, -3, -4, -5], -8)), {2, 4})

    def test_no_solution(self):
        # No solution available
        with self.assertRaises(ValueError):
            two_sum([1, 2, 3, 4], 10)

    def test_duplicate_numbers(self):
        # Case with duplicate numbers that can be part of the solution
        self.assertEqual(set(two_sum([4, 4], 8)), {0, 1})
        self.assertEqual(set(two_sum([1, 3, 3, 5], 6)), {1, 2})

if __name__ == '__main__':
    unittest.main()
