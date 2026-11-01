from fastapi import APIRouter, Depends
from BusinessLogic.auth_business_logic import AuthBusinessLogic
from Presentation.API.DI.authentication_dependency_injection import get_authentication_business_logic
from Presentation.API.DTOs.authentication import LoginRequest, VerifyOtpRequest

router = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])


@router.post("/login")
def login(request: LoginRequest, business_logic: AuthBusinessLogic = Depends(get_authentication_business_logic)):
    return business_logic.login(request.mobile, request.password)


@router.post("/verify-otp")
def verify_otp(request: VerifyOtpRequest,
               business_logic: AuthBusinessLogic = Depends(get_authentication_business_logic)):
    return business_logic.verify_otp(request.mobile, request.password, request.code)