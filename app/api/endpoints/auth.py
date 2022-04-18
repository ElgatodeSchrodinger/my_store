from typing import List, Optional

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from  api.utils import get_user_services
from  domain.userManagment.userSchema import UserCreateSchema, UserDBSchema, UserUpdateSchema
from  domain.userManagment.userService import UserService

router = APIRouter(
    tags=['authentication']
)

@router.post('/token')
def generate_token(request: OAuth2PasswordRequestForm = Depends(), user_service: UserService = Depends(get_user_services)):
    access_token = user_service.login(request.username, request.password)
    if not access_token:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    return {
        'access_token': access_token,
        'token_type': 'bearer',
    }