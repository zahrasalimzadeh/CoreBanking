from BusinessLogic.auth_business_logic import AuthBusinessLogic
from BusinessLogic.otp_business_logic import OtpBusinessLogic
from Common.Services.notification_publisher import NotificationPublisher
from Common.Services.sms_service import SmsService
from DataAccess.Repositories.customer_repository import SQLAlchemyCustomerRepository
from DataAccess.Repositories.otp_repository import SQLAlchemyOtpRepository


def get_authentication_business_logic():
    otp_business_logic = OtpBusinessLogic(SQLAlchemyOtpRepository(), SmsService(), NotificationPublisher())
    return AuthBusinessLogic(SQLAlchemyCustomerRepository(), otp_business_logic)