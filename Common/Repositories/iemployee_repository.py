from abc import ABC, abstractmethod
from Common.Entities.employee import Employee


class IEmployeeRepository(ABC):
    @abstractmethod
    def get_by_username_password(self, username: str, password: str) -> Employee:
        pass

    @abstractmethod
    def insert(self, employee: Employee):
        pass
