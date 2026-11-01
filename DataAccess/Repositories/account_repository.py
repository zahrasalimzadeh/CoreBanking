from Common.Entities.account import Account
from Common.Entities.customer import Customer
from Common.Entities.transaction import Transaction
from Common.Enums.transaction_type import TransactionType
from Common.Repositories.iaccount_repository import IAccountRepository
from Common.Decorators.performance_logger import performance_logger
from DataAccess.Config.database import create_session
from DataAccess.Models.account import Account as AccountModel
from DataAccess.Models.customer import Customer as CustomerModel
from DataAccess.Models.transaction import Transaction as TransactionModel
from sqlalchemy import func


class SQLAlchemyAccountRepository(IAccountRepository):
    @performance_logger
    def get_account_list(self, page_number=1, page_size=20):
        account_list = []

        with create_session() as session:
            rows = (
                session.query(AccountModel, CustomerModel)
                .join(CustomerModel, CustomerModel.id == AccountModel.customer_id)
                .order_by(AccountModel.id)
                .offset((page_number - 1) * page_size)
                .limit(page_size)
                .all()
            )

            for account_model, customer_model in rows:
                customer = Customer(customer_model.id, customer_model.first_name, customer_model.last_name)
                account = Account(account_model.id, account_model.account_number, account_model.opening_date, customer)
                account_list.append(account)

        return account_list

    @performance_logger
    def get_accounts_by_customer_id(self, customer_id):
        account_list = []

        with create_session() as session:
            rows = (
                session.query(AccountModel, CustomerModel)
                .join(CustomerModel, CustomerModel.id == AccountModel.customer_id)
                .filter(AccountModel.customer_id == customer_id)
                .order_by(AccountModel.id)
                .all()
            )

            for account_model, customer_model in rows:
                customer = Customer(customer_model.id, customer_model.first_name, customer_model.last_name)
                account = Account(account_model.id, account_model.account_number, account_model.opening_date, customer)
                account_list.append(account)

        return account_list

    def get_transaction_by_account_id(self, account_id):
        transaction_list = []

        with create_session() as session:
            rows = (
                session.query(TransactionModel, AccountModel, CustomerModel)
                .join(AccountModel, AccountModel.id == TransactionModel.account_id)
                .join(CustomerModel, CustomerModel.id == AccountModel.customer_id)
                .filter(TransactionModel.account_id == account_id)
                .order_by(TransactionModel.created_at.desc())
                .all()
            )

            for transaction_model, account_model, customer_model in rows:
                customer = Customer(customer_model.id, customer_model.first_name, customer_model.last_name)
                account = Account(account_model.id, account_model.account_number, account_model.opening_date, customer)
                transaction = Transaction(
                    transaction_model.id,
                    transaction_model.amount,
                    transaction_model.transaction_type_id,
                    transaction_model.created_at,
                    account
                )
                transaction_list.append(transaction)

        return transaction_list

    def get_balance(self, account_id):
        with create_session() as session:
            total_deposit = (
                session.query(func.coalesce(func.sum(TransactionModel.amount), 0))
                .filter(TransactionModel.account_id == account_id)
                .filter(TransactionModel.transaction_type_id == TransactionType.DEPOSIT.value)
                .scalar()
            )
            total_withdraw = (
                session.query(func.coalesce(func.sum(TransactionModel.amount), 0))
                .filter(TransactionModel.account_id == account_id)
                .filter(TransactionModel.transaction_type_id == TransactionType.WITHDRAW.value)
                .scalar()
            )

        return total_deposit - total_withdraw

    def insert_transaction(self, account_id, amount, transaction_type):
        with create_session() as session:
            session.add(TransactionModel(
                account_id=account_id,
                amount=amount,
                transaction_type_id=transaction_type.value
            ))

    def insert(self, account: Account):
        pass

    def update(self, account: Account):
        pass

    def delete(self, account_id):
        pass