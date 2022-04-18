from typing import List, Optional
from fastapi import Security

# from app.domain.auth.authUtils import auth_check
from domain.userManagment.userConstants import UserRoles
from domain.auth.authUtils import get_current_user_from_service

from fastapi import APIRouter, HTTPException, Depends, status

from api.utils import get_user_services
from domain.userManagment.userSchema import (
    UserCreateSchema,
    UserDBSchema,
    UserUpdateSchema,
)
from domain.userManagment.userService import UserService
from domain.auth.authSchema import AuthSchema

router = APIRouter()


@router.post("/", response_model=UserDBSchema)
def create_user(
    user: UserCreateSchema,
    user_service: UserService = Depends(get_user_services),
    token: str = Depends(AuthSchema),
    # current_user: UserDBSchema = Security(
    #     get_current_user_from_service, scopes=[UserRoles.admin.value]
    # ),
) -> UserDBSchema:
    return user_service.create_user(user)


@router.get("/{user_id}", response_model=UserDBSchema)
def get_user_by_id(
    user_id: int,
    user_service: UserService = Depends(get_user_services),
    token: str = Depends(AuthSchema),
    current_user: UserDBSchema = Security(
        get_current_user_from_service, scopes=[UserRoles.admin.value]
    ),
) -> Optional[UserDBSchema]:
    user = user_service.get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id:{user_id} not found",
    )


@router.put("/{user_id}", response_model=UserDBSchema)
def update_user(
    user_id: int,
    new_user: UserUpdateSchema,
    user_service: UserService = Depends(get_user_services),
    token: str = Depends(AuthSchema),
    current_user: UserDBSchema = Security(
        get_current_user_from_service, scopes=[UserRoles.admin.value]
    ),
) -> UserDBSchema:
    user_updated: UserDBSchema = user_service.update_user(user_id, new_user)
    return user_updated


@router.delete("/{user_id}", response_model=UserDBSchema)
def remove_user(
    user_id: int,
    user_service: UserService = Depends(get_user_services),
    token: str = Depends(AuthSchema),
    current_user: UserDBSchema = Security(
        get_current_user_from_service, scopes=[UserRoles.admin.value]
    ),
) -> UserDBSchema:
    user_removed: UserDBSchema = user_service.remove_user(user_id)
    return user_removed
