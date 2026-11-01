from datetime import datetime


class Otp:
    def __init__(self, id: int, phone: str, code: str, created_at: datetime, expires_at: datetime, is_used: bool):
        self.id = id
        self.phone = phone
        self.code = code
        self.created_at = created_at
        self.expires_at = expires_at
        self.is_used = is_used