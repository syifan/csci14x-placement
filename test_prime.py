import unittest
from prime import nth_prime


class TestNthPrime(unittest.TestCase):

  def test_basic_cases(self):
    # Test for the first few prime numbers
    self.assertEqual(nth_prime(1), 2)
    self.assertEqual(nth_prime(2), 3)
    self.assertEqual(nth_prime(3), 5)
    self.assertEqual(nth_prime(4), 7)
    self.assertEqual(nth_prime(5), 11)

  def test_larger_numbers(self):
    # Test larger numbers
    self.assertEqual(nth_prime(10), 29)
    self.assertEqual(nth_prime(25), 97)
    self.assertEqual(nth_prime(50), 229)

  def test_edge_cases(self):
    # Test edge cases
    with self.assertRaises(ValueError):
      nth_prime(0)  # Assuming you handle n=0 with an exception

    with self.assertRaises(ValueError):
      nth_prime(-5)  # Assuming you handle negative values with an exception


if __name__ == '__main__':
  unittest.main()
