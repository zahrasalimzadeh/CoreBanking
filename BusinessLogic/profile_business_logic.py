from hashlib import md5
from Common.DTOs.response import Response
from Common.Repositories.iemployee_repository import IEmployeeRepository


class ProfileBusinessLogic:
    def __init__(self, employee_repository: IEmployeeRepository):
        self.employee_repository = employee_repository

    def get_profile(self, employee_id: int):
        employee = self.employee_repository.get_by_id(employee_id)

        if employee is None:
            return Response(False, "Employee not found.")

        return Response(True, "Profile loaded.", employee)

    def update_profile(self, employee_id: int, first_name: str, last_name: str, mobile: str):
        first_name = first_name.strip()
        last_name = last_name.strip()
        mobile = mobile.strip()

        missing = []

        if not first_name:
            missing.append("first name")

        if not last_name:
            missing.append("last name")

        if not mobile:
            missing.append("mobile")

        if missing:
            return Response(False, "Please enter " + ", ".join(missing) + ".")

        if len(mobile) != 11 or not mobile.isdigit():
            return Response(False, "Mobile must be 11 digits.")

        self.employee_repository.update_profile(employee_id, first_name, last_name, mobile)
        return Response(True, "Profile updated.")

    def change_password(self, employee_id: int, current_password: str, new_password: str, confirm_password: str):
        if not current_password or not new_password or not confirm_password:
            return Response(False, "Please fill all password fields.")

        employee = self.employee_repository.get_by_id(employee_id)

        if employee.password != md5(current_password.encode()).hexdigest():
            return Response(False, "Current password is incorrect.")

        if len(new_password) < 6:
            return Response(False, "New password must be at least 6 characters.")

        if new_password != confirm_password:
            return Response(False, "New passwords do not match.")

        self.employee_repository.update_password(employee_id, md5(new_password.encode()).hexdigest())
        return Response(True, "Password changed.")

    def change_image(self, employee_id: int, image_bytes: bytes):
        if not image_bytes:
            return Response(False, "Please choose a picture.")

        if len(image_bytes) > 2 * 1024 * 1024:
            return Response(False, "Picture must be smaller than 2 MB.")

        self.employee_repository.update_image(employee_id, image_bytes)
        return Response(True, "Picture saved.")