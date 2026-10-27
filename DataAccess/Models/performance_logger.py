from datetime import datetime
from decimal import Decimal
from DataAccess.Models.base import Base
from sqlalchemy import Integer, String, DateTime, Numeric
from sqlalchemy.orm import Mapped, mapped_column


class PerformanceLogger(Base):
    __tablename__ = "performance_logger"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    function_name: Mapped[str] = mapped_column(String(100), nullable=False)
    execution_time: Mapped[Decimal] = mapped_column(Numeric(18, 10), nullable=False)
    call_date_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)