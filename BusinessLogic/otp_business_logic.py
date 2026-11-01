from datetime import datetime, timedelta
from Common.DTOs.response import Response
from Common.Repositories.iotp_repository import IOtpRepository


class OtpBusinessLogic:
    def __init__(self, otp_repository: IOtpRepository, sms_service, notification_publisher):
        self.otp_repository = otp_repository
        self.sms_service = sms_service
        self.notification_publisher = notification_publisher

    def send_otp(self, phone: str):
        if not phone:
            return Response(False, "Please enter phone number.")

        code = self.sms_service.generate_code()
        expires_at = datetime.now() + timedelta(minutes=2)
        self.otp_repository.insert(phone, code, expires_at)

        try:
            self.notification_publisher.publish(phone, code)
        except Exception:
            return Response(False, "Notification service is not available.")

        return Response(True, "Code was sent.")

    def verify_otp(self, phone: str, code: str):
        if not phone or not code:
            return Response(False, "Please enter phone number and code.")

        otp = self.otp_repository.get_valid_otp(phone, code)

        if otp is None:
            return Response(False, "The code is invalid or expired.")

        self.otp_repository.mark_as_used(otp.id)
        return Response(True, "Code is verified.")