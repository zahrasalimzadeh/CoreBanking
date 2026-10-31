from abc import ABC, abstractmethod
from Common.Entities.account import Account


class IAccountRepository(ABC):
    @abstractmethod
    def get_account_list(self, page_number=1, page_size=20):
        pass

    @abstractmethod
    def get_transaction_by_account_id(self, account_id):
        pass

    @abstractmethod
    def get_balance(self, account_id):
        pass

    @abstractmethod
    def insert(self, account: Account):
        pass

    @abstractmethod
    def update(self, account: Account):
        pass

    @abstractmethod
    def delete(self, account_id):
        pass

    @abstractmethod
    def insert_transaction(self, account_id, amount, transaction_type):
        pass