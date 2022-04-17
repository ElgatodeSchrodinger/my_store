
from abc import abstractmethod

class IHash():
    @abstractmethod
    async def bcrypt(password: str) -> str:
        raise NotImplementedError
    
    @abstractmethod
    async def verify(hashed_password: str, plain_password: str) -> bool:
        raise NotImplementedError