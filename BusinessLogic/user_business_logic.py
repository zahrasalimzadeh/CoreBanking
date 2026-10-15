from hashlib import md5
from Common.Enums.employee_status import EmployeeStatus
from Common.DTOs.response import Response
from Common.Repositories.iemployee_repository import IEmployeeRepository


class UserBusinessLogic:
    def __init__(self, employee_repository: IEmployeeRepository):
        self.employee_repository = employee_repository

    def login(self, username: str, password: str, captcha_input: str, captcha_answer: str):
        missing = []

        if not username:
            missing.append("username")

        if not password:
            missing.append("password")

        if not captcha_input:
            missing.append("captcha")

        if missing:
            return Response(False, "Please enter " + ", ".join(missing) + ".")

        if captcha_input.upper() != captcha_answer.upper():
            return Response(False, "Captcha is incorrect.")

        if len(username) < 3 or len(password) < 6:
            return Response(False, "Invalid structure username or password.")

        password_hashed = md5(password.encode()).hexdigest()
        employee = self.employee_repository.get_by_username_password(username, password_hashed)

        if employee:
            match employee.status:
                case EmployeeStatus.Active:
                    return Response(True, f"Welcome {employee.get_fullname()}", employee)
                case EmployeeStatus.Pending:
                    return Response(False, "Your account is pending(call to administrator).", employee)
                case EmployeeStatus.Deactive:
                    return Response(False, "Your account was deactivated.", employee)
        else:
            return Response(False, "Invalid username or password")