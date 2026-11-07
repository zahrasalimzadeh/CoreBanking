from Common.Entities.customer import Customer


class Account:
    def __init__(self, id, number, opening_date, customer: Customer):
        self.id = id
        self.account_number = number
        self.opening_date = opening_date
        self.owner_customer = customer

    @classmethod
    def from_model(cls, model, customer: Customer):
        return cls(model.id, model.account_number, model.opening_date, customer)