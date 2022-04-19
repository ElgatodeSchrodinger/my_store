from domain.auth.authInterface import IJWT
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from core.config import settings

# from domain.auth.authInterface import IHash
from passlib.context import CryptContext
from domain.userManagment.userConstants import UserRoles

pwd_cxt = CryptContext(schemes="bcrypt", deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={
        profile.value: f"Permission for {profile} profile"
        for profile in UserRoles
    },
)


class JWT(IJWT):
    def bcrypt(self, password: str) -> str:
        return pwd_cxt.hash(password)

    def verify(self, hashed_password: str, plain_password: str) -> str:
        return pwd_cxt.verify(plain_password, hashed_password)

    def decode(self, token: str) -> str:
        return jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=settings.ALGORITHM
        )

    def create_access_token(
        self, data: dict, expires_delta: Optional[timedelta] = None
    ):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM
        )
        return encoded_jwt
