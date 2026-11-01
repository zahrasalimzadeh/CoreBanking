import unittest
from datetime import datetime, timedelta
from BusinessLogic.otp_business_logic import OtpBusinessLogic
from Common.Entities.otp import Otp
from Common.Repositories.iotp_repository import IOtpRepository


class FakeOtpRepository(IOtpRepository):
    def __init__(self):
        self.items = []

    def insert(self, phone, code, expires_at):
        self.items.append(Otp(len(self.items) + 1, phone, code, datetime.now(), expires_at, False))

    def get_valid_otp(self, phone, code):
        for item in self.items:
            if item.phone == phone and item.code == code and not item.is_used and item.expires_at > datetime.now():
                return item

        return None

    def mark_as_used(self, otp_id):
        for item in self.items:
            if item.id == otp_id:
                item.is_used = True


class FakeSmsService:
    def generate_code(self):
        return "12345"


class FakePublisher:
    def __init__(self, is_down=False):
        self.is_down = is_down
        self.messages = []

    def publish(self, phone, content):
        if self.is_down:
            raise Exception("broker is down")

        self.messages.append((phone, content))


class TestOtpBusinessLogic(unittest.TestCase):
    def setUp(self):
        self.repository = FakeOtpRepository()
        self.publisher = FakePublisher()
        self.business_logic = OtpBusinessLogic(self.repository, FakeSmsService(), self.publisher)

    def test_send_otp_valid_phone(self):
        response = self.business_logic.send_otp("09120000002")

        self.assertTrue(response.success)
        self.assertEqual(len(self.repository.items), 1)
        self.assertEqual(self.publisher.messages, [("09120000002", "12345")])

    def test_send_otp_empty_phone(self):
        response = self.business_logic.send_otp("")

        self.assertFalse(response.success)
        self.assertEqual(len(self.repository.items), 0)
        self.assertEqual(len(self.publisher.messages), 0)

    def test_send_otp_when_broker_is_down(self):
        business_logic = OtpBusinessLogic(self.repository, FakeSmsService(), FakePublisher(is_down=True))

        response = business_logic.send_otp("09120000002")

        self.assertFalse(response.success)
        self.assertEqual(response.message, "Notification service is not available.")

    def test_verify_otp_valid_code(self):
        self.business_logic.send_otp("09120000002")

        response = self.business_logic.verify_otp("09120000002", "12345")

        self.assertTrue(response.success)

    def test_verify_otp_wrong_code(self):
        self.business_logic.send_otp("09120000002")

        response = self.business_logic.verify_otp("09120000002", "00000")

        self.assertFalse(response.success)

    def test_verify_otp_wrong_phone(self):
        self.business_logic.send_otp("09120000002")

        response = self.business_logic.verify_otp("09120000003", "12345")

        self.assertFalse(response.success)

    def test_verify_otp_used_code(self):
        self.business_logic.send_otp("09120000002")
        self.business_logic.verify_otp("09120000002", "12345")

        response = self.business_logic.verify_otp("09120000002", "12345")

        self.assertFalse(response.success)

    def test_verify_otp_expired_code(self):
        self.repository.insert("09120000002", "99999", datetime.now() - timedelta(minutes=1))

        response = self.business_logic.verify_otp("09120000002", "99999")

        self.assertFalse(response.success)

    def test_verify_otp_empty_code(self):
        response = self.business_logic.verify_otp("09120000002", "")

        self.assertFalse(response.success)
