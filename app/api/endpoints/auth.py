from typing import List, Optional

from fastapi import APIRouter, HTTPException, Depends

from  api.utils import get_user_services
from  domain.userManagment.userSchema import UserCreateSchema, UserDBSchema, UserUpdateSchema
from  domain.userManagment.userService import UserService

router = APIRouter(
    tags=['authentication']
)

@router.post('/token')
def generate_token():
    pass