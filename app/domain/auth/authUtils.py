from fastapi import HTTPException, status, Depends
from fastapi.security import SecurityScopes
from api.utils import get_user_services
from domain.auth.authSchema import AuthSchema


def get_current_user_from_service(
    security_scopes: SecurityScopes,
    token: str = Depends(AuthSchema), 
    user_service=Depends(get_user_services),
    ):
    current_user = user_service.get_current_user(security_scopes=security_scopes, token=token)
    if not current_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized", headers={"WWW-Authenticate": "Bearer"})
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
