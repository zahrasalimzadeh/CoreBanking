from hashlib import md5
from Common.DTOs.response import Response
from Common.Repositories.icustomer_repository import ICustomerRepository


class AuthBusinessLogic:
    def __init__(self, customer_repository: ICustomerRepository, otp_business_logic):
        self.customer_repository = customer_repository
        self.otp_business_logic = otp_business_logic

    def login(self, mobile: str, password: str):
        customer, error = self.authenticate(mobile, password)

        if error:
            return error

        response = self.otp_business_logic.send_otp(customer.mobile)

        if not response.success:
            return response

        return Response(True, "Code was sent.", {"full_name": customer.get_fullname()})

    def verify_otp(self, mobile: str, password: str, code: str):
        customer, error = self.authenticate(mobile, password)

        if error:
            return error

        response = self.otp_business_logic.verify_otp(customer.mobile, code)

        if not response.success:
            return response

        return Response(True, f"Welcome {customer.get_fullname()}", {
            "customer_id": customer.id,
            "full_name": customer.get_fullname()
        })

    def authenticate(self, mobile: str, password: str):
        if not mobile or not mobile.isdigit() or len(mobile) != 11:
            return None, Response(False, "Invalid mobile number.")

        if not password or len(password) < 6:
            return None, Response(False, "Invalid structure password.")

        password_hashed = md5(password.encode()).hexdigest()
        customer = self.customer_repository.get_by_mobile_password(mobile, password_hashed)

        if customer is None:
            return None, Response(False, "Invalid mobile or password.")

        return customer, None