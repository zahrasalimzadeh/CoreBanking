from Common.Decorators.performance_logger import performance_logger
from Common.Entities.customer import Customer
from Common.Repositories.icustomer_repository import ICustomerRepository
from DataAccess.Config.database import create_session
from DataAccess.Models.customer import Customer as CustomerModel


class SQLAlchemyCustomerRepository(ICustomerRepository):
    @performance_logger
    def get_by_mobile_password(self, mobile: str, password: str) -> Customer | None:
        with create_session() as session:
            row = session.query(CustomerModel).filter_by(mobile=mobile, password=password).first()

            if row is None:
                return None

            return Customer(row.id, row.first_name, row.last_name, row.mobile)