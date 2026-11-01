from fastapi import APIRouter, Depends
from BusinessLogic.account_business_logic import AccountBusinessLogic
from Presentation.API.DI.account_dependency_injection import get_account_business_logic

router = APIRouter(prefix="/api/v1/transactions", tags=["Transaction"])


@router.get("")
def get_transaction(account_id: int, business_logic: AccountBusinessLogic = Depends(get_account_business_logic)):
    return business_logic.get_transactions(account_id)