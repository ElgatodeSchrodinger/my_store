

class AuthService:

    def __init__(self, hash):
        self.__hash = hash

    def bcrypt(self, password: str) -> str:
        return self.__hash.bcrypt(password)

    def verify(self, hashed_password: str, plain_password: str) -> str:
        return self.__hash.verify(plain_password, hashed_password)
