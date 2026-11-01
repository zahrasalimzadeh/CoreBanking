from datetime import datetime
from Common.Entities.otp import Otp
from Common.Repositories.iotp_repository import IOtpRepository
from DataAccess.Config.database import create_session
from DataAccess.Models.otp import Otp as OtpModel


class SQLAlchemyOtpRepository(IOtpRepository):
    def insert(self, phone: str, code: str, expires_at: datetime) -> None:
        with create_session() as session:
            session.add(OtpModel(phone=phone, code=code, expires_at=expires_at))

    def get_valid_otp(self, phone: str, code: str) -> Otp | None:
        with create_session() as session:
            row = (
                session.query(OtpModel)
                .filter(OtpModel.phone == phone)
                .filter(OtpModel.code == code)
                .filter(OtpModel.is_used == False)
                .filter(OtpModel.expires_at > datetime.now())
                .order_by(OtpModel.created_at.desc())
                .first()
            )
            if row is None:
                return None
            return Otp(row.id, row.phone, row.code, row.created_at, row.expires_at, row.is_used)

    def mark_as_used(self, otp_id: int) -> None:
        with create_session() as session:
            row = session.get(OtpModel, otp_id)
            if row is not None:
                row.is_used = True