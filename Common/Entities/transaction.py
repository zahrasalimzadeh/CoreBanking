from Common.Entities.account import Account
from Common.Enums.transaction_type import TransactionType


class Transaction:
    def __init__(self, id, amount, transaction_type_id, created_at, account: Account):
        self.id = id
        self.amount = amount
        self.transaction_type = TransactionType(transaction_type_id)
        self.created_at = created_at
        self.account = account