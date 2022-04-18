from typing import Optional, List
from pydantic import BaseModel

from infrastructure.auth.jwt import oauth2_scheme

AuthSchema = oauth2_scheme

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []
