from Common.Entities.customer import Customer


class Account:
    def __init__(self, id, number, opening_date, customer: Customer):
        self.id = id
        self.account_number = number
        self.opening_date = opening_date
        self.owner_customer = customer