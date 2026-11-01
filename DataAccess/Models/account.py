from datetime import datetime
from DataAccess.Models.base import Base
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Account(Base):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    account_number: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    opening_date: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey("customer.id"), nullable=False)