import unittest
from hashlib import md5
from BusinessLogic.auth_business_logic import AuthBusinessLogic
from Common.DTOs.response import Response
from Common.Entities.customer import Customer
from Common.Repositories.icustomer_repository import ICustomerRepository


class FakeCustomerRepository(ICustomerRepository):
    def get_by_mobile_password(self, mobile, password):
        if mobile == "09120000002" and password == md5("123456".encode()).hexdigest():
            return Customer(2, "Sara", "Ahmadi", mobile)

        return None


class FakeOtpBusinessLogic:
    def __init__(self, can_send=True):
        self.can_send = can_send
        self.sent_to = None

    def send_otp(self, phone):
        self.sent_to = phone
        return Response(self.can_send, "send result")

    def verify_otp(self, phone, code):
        return Response(code == "12345", "verify result")


class TestAuthBusinessLogic(unittest.TestCase):
    def setUp(self):
        self.otp_business_logic = FakeOtpBusinessLogic()
        self.business_logic = AuthBusinessLogic(FakeCustomerRepository(), self.otp_business_logic)

    def test_login_valid_customer(self):
        response = self.business_logic.login("09120000002", "123456")

        self.assertTrue(response.success)
        self.assertEqual(response.data["full_name"], "Sara Ahmadi")
        self.assertEqual(self.otp_business_logic.sent_to, "09120000002")

    def test_login_empty_mobile(self):
        response = self.business_logic.login("", "123456")

        self.assertFalse(response.success)
        self.assertEqual(response.message, "Invalid mobile number.")

    def test_login_short_mobile(self):
        response = self.business_logic.login("0912", "123456")

        self.assertFalse(response.success)
        self.assertEqual(response.message, "Invalid mobile number.")

    def test_login_mobile_with_letters(self):
        response = self.business_logic.login("0912abcdefg", "123456")

        self.assertFalse(response.success)
        self.assertEqual(response.message, "Invalid mobile number.")

    def test_login_short_password(self):
        response = self.business_logic.login("09120000002", "123")

        self.assertFalse(response.success)
        self.assertEqual(response.message, "Invalid structure password.")

    def test_login_wrong_password(self):
        response = self.business_logic.login("09120000002", "wrong123")

        self.assertFalse(response.success)
        self.assertEqual(response.message, "Invalid mobile or password.")
        self.assertIsNone(self.otp_business_logic.sent_to)

    def test_login_unknown_mobile(self):
        response = self.business_logic.login("09129999999", "123456")

        self.assertFalse(response.success)
        self.assertEqual(response.message, "Invalid mobile or password.")

    def test_login_when_otp_cannot_be_sent(self):
        business_logic = AuthBusinessLogic(FakeCustomerRepository(), FakeOtpBusinessLogic(can_send=False))

        response = business_logic.login("09120000002", "123456")

        self.assertFalse(response.success)

    def test_verify_otp_valid_code(self):
        response = self.business_logic.verify_otp("09120000002", "123456", "12345")

        self.assertTrue(response.success)
        self.assertEqual(response.data["customer_id"], 2)
        self.assertEqual(response.message, "Welcome Sara Ahmadi")

    def test_verify_otp_wrong_code(self):
        response = self.business_logic.verify_otp("09120000002", "123456", "00000")

        self.assertFalse(response.success)

    def test_verify_otp_wrong_password(self):
        response = self.business_logic.verify_otp("09120000002", "wrong123", "12345")

        self.assertFalse(response.success)
        self.assertEqual(response.message, "Invalid mobile or password.")
