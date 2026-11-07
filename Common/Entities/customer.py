class Customer:
    def __init__(self, id, first_name, last_name, mobile=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile

    @classmethod
    def from_model(cls, model):
        return cls(model.id, model.first_name, model.last_name, model.mobile)

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"