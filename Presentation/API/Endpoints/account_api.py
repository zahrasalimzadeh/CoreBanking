from fastapi import APIRouter, Depends
from BusinessLogic.account_business_logic import AccountBusinessLogic
from Presentation.API.DI.account_dependency_injection import get_account_business_logic

router = APIRouter(prefix="/api/v1/accounts", tags=["Account"])

@router.get("")
def get_accounts(customer_id: int, business_logic: AccountBusinessLogic = Depends(get_account_business_logic)):
    return business_logic.get_accounts(customer_id)

@router.get("/{account_id}/balance")
def get_balance(account_id: int, business_logic: AccountBusinessLogic = Depends(get_account_business_logic)):
    return business_logic.get_balance(account_id)