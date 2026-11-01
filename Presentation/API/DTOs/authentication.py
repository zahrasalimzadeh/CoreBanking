from pydantic import BaseModel


class LoginRequest(BaseModel):
    mobile: str
    password: str


class VerifyOtpRequest(BaseModel):
    mobile: str
    password: str
    code: str