class Response:
    def __init__(self, is_success: bool, message: str, data=None):
        self.success = is_success
        self.message = message
        self.data = data
