from datetime import timedelta
from typing import Optional


class AuthService:
    def __init__(self, hash):
        self.__hash = hash

    def bcrypt(self, password: str) -> str:
        return self.__hash.bcrypt(password)

    def decode(self, token: str) -> str:
        return self.__hash.decode(token)

    def verify(self, hashed_password: str, plain_password: str) -> str:
        return self.__hash.verify(plain_password, hashed_password)

    def create_access_token(
        self, data: dict, expires_delta: Optional[timedelta] = None
    ):
        return self.__hash.create_access_token(
            data, expires_delta=expires_delta
        )
