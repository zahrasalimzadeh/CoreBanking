from DataAccess.Models.base import Base
from sqlalchemy import Integer, String,SmallInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    mobile: Mapped[str] = mapped_column(String(11), nullable=False)
    user_name: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(50), nullable=False)
    employee_status_id: Mapped[int] = mapped_column(SmallInteger, ForeignKey("employee_status.id"))
    role_id: Mapped[int] = mapped_column(SmallInteger, nullable=False, default=1)