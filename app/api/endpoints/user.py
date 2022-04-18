from typing import List, Optional

from fastapi import APIRouter, HTTPException, Depends, status

from  api.utils import get_user_services
from  domain.userManagment.userSchema import UserCreateSchema, UserDBSchema, UserUpdateSchema
from  domain.userManagment.userService import UserService
from domain.auth.authSchema import AuthSchema

router = APIRouter()


@router.post("/", response_model=UserDBSchema)
def create_user(user: UserCreateSchema, user_service: UserService = Depends(get_user_services)) -> UserDBSchema:
    return user_service.create_user(user)


@router.get("/{user_id}", response_model=UserDBSchema)
def get_user_by_id(user_id: int, user_service: UserService = Depends(get_user_services), token: str = Depends(AuthSchema)) -> Optional[UserDBSchema]:
    user = user_service.get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(
        status_code=404, detail=f"User with id:{user_id} not found",
    )


@router.put("/{user_id}", response_model=UserDBSchema)
def update_user(user_id: int, new_user: UserUpdateSchema, user_service: UserService = Depends(get_user_services)) -> UserDBSchema:
    user_updated: UserDBSchema = user_service.update_user(user_id, new_user)
    return user_updated


@router.delete("/{user_id}", response_model=UserDBSchema)
def remove_user(user_id: int, user_service: UserService = Depends(get_user_services)) -> UserDBSchema:
    user_removed: UserDBSchema = user_service.remove_user(user_id)
    return user_removed