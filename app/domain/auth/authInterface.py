
from abc import abstractmethod
from datetime import datetime
from typing import Optional

class IJWT():
    @abstractmethod
    async def bcrypt(password: str) -> str:
        raise NotImplementedError
    
    @abstractmethod
    async def verify(hashed_password: str, plain_password: str) -> bool:
        raise NotImplementedError
    
    @abstractmethod
    async def create_access_token(data: dict, expires_delta: Optional[datetime] = None):
        raise NotImplementedError