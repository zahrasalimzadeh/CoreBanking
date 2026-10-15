from DataAccess.Models.base import Base
from sqlalchemy import String,SmallInteger
from sqlalchemy.orm import Mapped, mapped_column


class EmployeeStatus(Base):
    __tablename__ = "employee_status"


    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)