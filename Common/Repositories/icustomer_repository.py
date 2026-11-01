from abc import ABC, abstractmethod
from Common.Entities.customer import Customer


class ICustomerRepository(ABC):
    @abstractmethod
    def get_by_mobile_password(self, mobile: str, password: str) -> Customer | None:
        pass