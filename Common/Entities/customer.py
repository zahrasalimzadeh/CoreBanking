class Customer:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"