from typing import Any, List, Optional
from fastapi.security import SecurityScopes
from  domain.userManagment.userSchema import UserCreateSchema, UserDBSchema, UserUpdateSchema

class UserService:
    def __init__(self, user_queries: Any, auth_service: Any):
        self.__user_queries = user_queries
        self.__auth_service = auth_service

    def create_user(self, user: UserCreateSchema) -> UserDBSchema:
        encrypt_pass = self.__auth_service.bcrypt(user.password)
        user.password = encrypt_pass
        new_user = self.__user_queries.create_user(user)
        return UserDBSchema.from_orm(new_user)

    def get_user_by_id(self, user_id: int) -> Optional[UserDBSchema]:
        user = self.__user_queries.get_user_byid(user_id)
        if user:
            return UserDBSchema.from_orm(user)
        else:
            return None

    def update_user(self, user_id: int, new_user: UserUpdateSchema) -> UserDBSchema:
        old_user = self.__user_queries.get_user_byid(user_id)
        if 'password' in new_user.dict(exclude_unset=True):
            encrypt_pass = self.__auth_service.bcrypt(new_user.password)
            new_user.password = encrypt_pass
        user_updated = self.__user_queries.update_user(old_user, new_user)
        return UserDBSchema.from_orm(user_updated)

    def remove_user(self, user_id: int) -> UserDBSchema:
        user_removed = self.__user_queries.delete_user(user_id)
        return UserDBSchema.from_orm(user_removed)

    def get_user_by_email(self, user_email: str) -> Optional[UserDBSchema]:
        user = self.__user_queries.get_user_byemail(user_email)
        if user:
            return UserDBSchema.from_orm(user)
        else:
            return None

    def login(self, email: str, req_pass: str) -> str:
        user = self.__user_queries.get_user_byemail(email)
        if not user:
            return False
        if not self.__auth_service.verify(user.password, req_pass):
            return False
        access_token = self.__auth_service.create_access_token(
            data={'sub': user.email, 'scopes': user.rol.value})
        return access_token
    
    def get_current_user(self, security_scopes: SecurityScopes, token: str) -> Optional[UserDBSchema]:
        payload = self.__auth_service.decode(token)
        if 'sub' not in payload:
            return False
        user_email = payload['sub']
        user_scope = payload['scopes']
        user = self.__user_queries.get_user_byemail(user_email)
        for scope in security_scopes.scopes:
            if scope not in user_scope:
                return False
        return user
