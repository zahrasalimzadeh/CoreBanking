from Common.Enums.employee_status import EmployeeStatus
from Common.Enums.role import Roles


class Employee:
    def __init__(self, id, firstname, lastname, username, password, mobile, employee_status_id, role_id,
                 profile_image=None):
        self.id = id
        self.first_name = firstname
        self.last_name = lastname
        self.username = username
        self.password = password
        self.mobile = mobile
        self.status = EmployeeStatus(employee_status_id)
        self.role = Roles(role_id)
        self.profile_image = profile_image

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"