import os
from dotenv import load_dotenv
from Presentation.main_view import MainView
from BusinessLogic.user_business_logic import UserBusinessLogic
from DataAccess.Config.database import create_session, engine
from DataAccess.Models.base import Base
from DataAccess.Models.employee import Employee
from DataAccess.Models.employee_status import EmployeeStatus
from DataAccess.Repositories.employee_repository import SQLAlchemyEmployeeRepository
from prometheus_client import start_http_server

load_dotenv()

sql_server_host = os.getenv("SQLSERVER_HOST", ".")
sql_server_database = os.getenv("SQLSERVER_DATABASE")


Base.metadata.create_all(engine)

with create_session() as session:
    status = session.query(EmployeeStatus).filter_by(title="Active").first()
    if not status:
        status = EmployeeStatus(title="Active")
        session.add(status)
        session.commit()

    employee_exists = session.query(Employee).filter_by(user_name="z.salimzadeh").first()
    if not employee_exists:
        employee = Employee(
            first_name="zahra",
            last_name="salimzadeh",
            mobile="09120000000",
            user_name="z.salimzadeh",
            password="e10adc3949ba59abbe56e057f20f883e",
            employee_status_id=status.id
        )
        session.add(employee)
        session.commit()

repository = SQLAlchemyEmployeeRepository()
user_business = UserBusinessLogic(repository)
start_http_server(8000)
MainView(user_business)
