from Common.Entities.employee import Employee
from Common.Repositories.iemployee_repository import IEmployeeRepository
from DataAccess.Config.database import create_session
from DataAccess.Models.employee import Employee as EmployeeModel
from Common.Decorators.performance_logger import performance_logger


class SQLAlchemyEmployeeRepository(IEmployeeRepository):
    @performance_logger
    def get_by_username_password(self, username: str, password: str) -> Employee:
        with create_session() as session:
            employee_model = session.query(EmployeeModel).filter_by(
                user_name=username, password=password
            ).first()

            if employee_model:
                return Employee(
                    employee_model.id,
                    employee_model.first_name,
                    employee_model.last_name,
                    employee_model.user_name,
                    employee_model.password,
                    employee_model.mobile,
                    employee_model.employee_status_id,
                    employee_model.role_id
                )

    def insert(self, employee: Employee):
        pass