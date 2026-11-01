from abc import ABC, abstractmethod
from datetime import datetime
from Common.Entities.otp import Otp


class IOtpRepository(ABC):
    @abstractmethod
    def insert(self, phone: str, code: str, expires_at: datetime) -> None:
        pass

    @abstractmethod
    def get_valid_otp(self, phone: str, code: str) -> Otp | None:
        pass

    @abstractmethod
    def mark_as_used(self, otp_id: int) -> None:
        pass