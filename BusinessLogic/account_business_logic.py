from Common.DTOs.response import Response
from Common.Repositories.iaccount_repository import IAccountRepository


class AccountBusinessLogic:
    def __init__(self, account_repository: IAccountRepository):
        self.account_repository = account_repository

    def get_balance(self, account_id: int):
        if account_id is None or account_id <= 0:
            return Response(False, "Invalid account.")

        balance = self.account_repository.get_balance(account_id)
        return Response(True, "Balance was loaded.", balance)

    def get_transactions(self, account_id: int):
        if account_id is None or account_id <= 0:
            return Response(False, "Invalid account.")

        transactions = self.account_repository.get_transaction_by_account_id(account_id)
        return Response(True, "Transactions were loaded.", transactions)