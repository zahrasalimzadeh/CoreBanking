from Common.Entities.employee import Employee
from Common.Repositories.iemployee_repository import IEmployeeRepository
from DataAccess.Config.database import create_session
from DataAccess.Models.employee import Employee as EmployeeModel
from Common.Decorators.performance_logger import performance_logger


class SQLAlchemyEmployeeRepository(IEmployeeRepository):
    def to_entity(self, employee_model: EmployeeModel) -> Employee:
        return Employee(
            employee_model.id,
            employee_model.first_name,
            employee_model.last_name,
            employee_model.user_name,
            employee_model.password,
            employee_model.mobile,
            employee_model.employee_status_id,
            employee_model.role_id,
            employee_model.profile_image
        )

    @performance_logger
    def get_by_username_password(self, username: str, password: str) -> Employee:
        with create_session() as session:
            employee_model = session.query(EmployeeModel).filter_by(
                user_name=username, password=password
            ).first()

            if employee_model:
                return self.to_entity(employee_model)

    @performance_logger
    def get_by_id(self, employee_id: int) -> Employee:
        with create_session() as session:
            employee_model = session.get(EmployeeModel, employee_id)

            if employee_model:
                return self.to_entity(employee_model)

    @performance_logger
    def update_profile(self, employee_id: int, first_name: str, last_name: str, mobile: str):
        with create_session() as session:
            employee_model = session.get(EmployeeModel, employee_id)
            employee_model.first_name = first_name
            employee_model.last_name = last_name
            employee_model.mobile = mobile
            session.commit()

    @performance_logger
    def update_password(self, employee_id: int, password_hash: str):
        with create_session() as session:
            employee_model = session.get(EmployeeModel, employee_id)
            employee_model.password = password_hash
            session.commit()

    @performance_logger
    def update_image(self, employee_id: int, image_bytes: bytes):
        with create_session() as session:
            employee_model = session.get(EmployeeModel, employee_id)
            employee_model.profile_image = image_bytes
            session.commit()

    def insert(self, employee: Employee):
        pass