from abc import ABC, abstractmethod
from Common.Entities.employee import Employee


class IEmployeeRepository(ABC):
    @abstractmethod
    def get_by_username_password(self, username: str, password: str) -> Employee:
        pass

    @abstractmethod
    def insert(self, employee: Employee):
        pass

    @abstractmethod
    def get_by_id(self, employee_id: int) -> Employee:
        pass

    @abstractmethod
    def update_profile(self, employee_id: int, first_name: str, last_name: str, mobile: str):
        pass

    @abstractmethod
    def update_password(self, employee_id: int, password_hash: str):
        pass

    @abstractmethod
    def update_image(self, employee_id: int, image_bytes: bytes):
        pass