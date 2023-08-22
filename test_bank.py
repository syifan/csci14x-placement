import unittest
from bank import BankAccount 

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # Set up method runs before each test case. 
        # We'll initialize a bank account here to be used in the tests.
        self.account = BankAccount(12345)

    def test_initial_balance(self):
        # Ensure the balance is initialized correctly
        self.assertEqual(self.account.display_balance(), 0.0)

    def test_deposit(self):
        # Test depositing money
        self.account.deposit(100.0)
        self.assertEqual(self.account.display_balance(), 100.0)

    def test_withdraw_success(self):
        # Test successful withdrawal
        self.account.deposit(150.0)
        self.account.withdraw(50.0)
        self.assertEqual(self.account.display_balance(), 100.0)

    def test_withdraw_insufficient_funds(self):
        # Test withdrawal with insufficient funds. 
        # Assuming your function prints an error message, this will capture that.
        with self.assertLogs() as cm:
            self.account.withdraw(200.0)
        self.assertIn("Insufficient funds", cm.output[0])
        self.assertEqual(self.account.display_balance(), 0.0)

    def test_multiple_operations(self):
        # Test combination of operations
        self.account.deposit(100.0)
        self.account.deposit(150.0)
        self.account.withdraw(50.0)
        self.assertEqual(self.account.display_balance(), 200.0)

if __name__ == '__main__':
    unittest.main()
