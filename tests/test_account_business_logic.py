import unittest
from BusinessLogic.account_business_logic import AccountBusinessLogic
from Common.Repositories.iaccount_repository import IAccountRepository


class FakeAccountRepository(IAccountRepository):
    def get_account_list(self, page_number=1, page_size=20):
        return []

    def get_accounts_by_customer_id(self, customer_id):
        return ["account-1", "account-2"]

    def get_transaction_by_account_id(self, account_id):
        return ["transaction-1", "transaction-2", "transaction-3"]

    def get_balance(self, account_id):
        return 5500000

    def insert(self, account):
        pass

    def update(self, account):
        pass

    def delete(self, account_id):
        pass

    def insert_transaction(self, account_id, amount, transaction_type):
        pass


class TestAccountBusinessLogic(unittest.TestCase):
    def setUp(self):
        self.business_logic = AccountBusinessLogic(FakeAccountRepository())

    def test_get_balance_valid_account(self):
        response = self.business_logic.get_balance(32)

        self.assertTrue(response.success)
        self.assertEqual(response.data, 5500000)

    def test_get_balance_zero_account_id(self):
        response = self.business_logic.get_balance(0)

        self.assertFalse(response.success)

    def test_get_balance_none_account_id(self):
        response = self.business_logic.get_balance(None)

        self.assertFalse(response.success)

    def test_get_transactions_valid_account(self):
        response = self.business_logic.get_transactions(32)

        self.assertTrue(response.success)
        self.assertEqual(len(response.data), 3)

    def test_get_transactions_negative_account_id(self):
        response = self.business_logic.get_transactions(-5)

        self.assertFalse(response.success)

    def test_get_accounts_valid_customer(self):
        response = self.business_logic.get_accounts(2)

        self.assertTrue(response.success)
        self.assertEqual(len(response.data), 2)

    def test_get_accounts_zero_customer_id(self):
        response = self.business_logic.get_accounts(0)

        self.assertFalse(response.success)

    def test_get_accounts_none_customer_id(self):
        response = self.business_logic.get_accounts(None)

        self.assertFalse(response.success)
