from BusinessLogic.account_business_logic import AccountBusinessLogic
from DataAccess.Repositories.account_repository import SQLAlchemyAccountRepository


def get_account_business_logic():
    repository = SQLAlchemyAccountRepository()
    return AccountBusinessLogic(repository)